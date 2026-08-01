#!/usr/bin/env python3
"""
FULL VERSION UPGRADE — STEP 2: EXTRACT ALL ANSWERS FROM TX_Exam_Kit_FA25.pdf
Reads the five answer sections (PDF pages 257–684), splits by question number,
extracts answer keys, workings, examiner reports and tutor tips,
and writes full_answers.json.
"""
import re
import json
from pypdf import PdfReader

PDF = 'TX_Exam_Kit_FA25.pdf'
OUT = 'full_answers.json'

ANSWER_SECTIONS = [
    {'num': 6, 'pages': (256, 418)},   # answers to Q1-127
    {'num': 7, 'pages': (418, 482)},   # answers to Q128-179
    {'num': 8, 'pages': (482, 522)},   # answers to Q180-212
    {'num': 9, 'pages': (522, 616)},   # answers to Q213-270
    {'num': 10, 'pages': (616, 684)},  # answers to Q271-306
]

# question -> section map (from full_questions.json)
SECTION_OF_Q = {}


def is_noise_line(line):
    s = line.strip()
    if not s:
        return False
    if re.match(r'^\d{1,3}\s*KAPLAN PUBLISHING', s) or re.match(r'^KAPLAN PUBLISHING\s*\d{1,3}', s):
        return True
    if re.match(r'^TX[-–]?\s?UK\s*:\s*TAXATION', s, re.I):
        return True
    if re.match(r'^PRACTICE (INCOME TAX AND NATIONAL INSURANCE|CHARGEABLE GAINS|INHERITANCE TAX|CORPORATION TAX|VALUE ADDED TAX) QUESTIONS', s, re.I):
        return True
    if re.match(r'^ANSWERS TO PRACTICE', s, re.I):
        return True
    if re.match(r'^SECTION\s+\d+$', s):
        return True
    return False


def load_pages(reader):
    """Return list of (page_no, lines) for all answer pages."""
    pages = []
    for sec in ANSWER_SECTIONS:
        p0, p1 = sec['pages']
        for p in range(p0, p1):
            try:
                t = reader.pages[p].extract_text() or ''
            except Exception:
                t = ''
            lines = t.split('\n')
            pages.append((p + 1, lines))
    return pages


def find_answer_starts(pages):
    """
    Return dict: question number -> (page_idx, line_idx).
    Scans sequentially; the first line matching '^N ' where N is a question number
    and the remainder starts with A-E, £, or an uppercase word is taken as the start.
    """
    starts = {}
    known = set(SECTION_OF_Q.keys())
    MONTHS = 'January|February|March|April|May|June|July|August|September|October|November|December'

    def plausible_rest(rest):
        """Is the text after the number an answer key / title / table header?"""
        if not rest:
            return None
        if re.match(r'^[A-E](?:\s*,\s*[A-E])*$', rest):
            return 'key'
        if re.match(r'^£', rest):
            return 'numkey'
        # Pure date like "31 January 2027" (title-case month + nothing else) -> not an answer
        if re.match(r'^\d{1,2}\s+(?:' + MONTHS + r')\s+\d{4}\s*$', rest):
            return None
        # Prose date continuation "31 January 2027, making..." -> not an answer
        if re.match(r'^\d{1,2}\s+(?:' + MONTHS + r')\b', rest) and re.search(r'[a-z]', rest):
            return None
        if re.match(r'^(?:' + MONTHS + r')\s+\d{4}\s*$', rest):
            return None
        if re.match(r'^(?:KAPLAN|PRACTICE|SECTION|ANSWERS|TX)', rest, re.I):
            return None
        if rest[0].isupper() or rest[0].isdigit():
            # numeric phrase answers like "60, 31 JANUARY THAT FOLLOWS..." / "31 DECEMBER 2027 AND £1,000"
            return 'title'
        return None

    # Monotonic scan: answers appear strictly in question order.
    cursor = (0, -1)  # (page_idx, line_idx) of previous answer start
    for n in sorted(known):
        found = None
        start_pi, start_li = cursor
        for pi in range(start_pi, len(pages)):
            lines = pages[pi][1]
            li0 = start_li + 1 if pi == start_pi else 0
            for li in range(li0, len(lines)):
                s = lines[li].strip()
                m = re.match(r'^' + str(n) + r'(?![0-9,.])\s*(.*)$', s)
                if not m:
                    continue
                rest = m.group(1).strip()
                kind = plausible_rest(rest)
                if kind:
                    found = (pi, li)
                    break
                if rest == '':
                    # bare number line; look ahead for an answer/table header
                    for ahead in range(1, 5):
                        if li + ahead < len(lines):
                            nxt = lines[li + ahead].strip()
                            if plausible_rest(nxt) or re.match(r'^[A-Z][a-z]+(\s+[A-Z][a-z]+){1,3}$', nxt):
                                found = (pi, li)
                                break
                if found:
                    break
            if found:
                break
        if found:
            starts[n] = found
            cursor = found
    return starts


def split_answer_blocks(pages, starts):
    """Return dict num -> list of (page_no, line) tuples spanning the answer."""
    blocks = {}
    ordered = sorted(starts.keys())
    for idx, n in enumerate(ordered):
        pi, li = starts[n]
        if idx + 1 < len(ordered):
            end_pi, end_li = starts[ordered[idx + 1]]
        else:
            end_pi, end_li = len(pages) - 1, len(pages[-1][1])
        end_pi = min(end_pi, len(pages) - 1)
        block = []
        for p in range(pi, end_pi + 1):
            if p == pi and p == end_pi:
                chunk = pages[p][1][li:end_li]
            elif p == pi:
                chunk = pages[p][1][li:]
            elif p == end_pi:
                chunk = pages[p][1][:end_li]
            else:
                chunk = pages[p][1]
            for ln in chunk:
                if not is_noise_line(ln):
                    block.append((pages[p][0], ln.rstrip()))
        blocks[n] = block
    return blocks


CALLOUT_RE = re.compile(r'^(Tutor.?s? top tips?|Examiner.?s? report|Tutorial note|Key answer tips)\s*$', re.I)
SUBKEY_RE = re.compile(r'^(\d{1,2})\s+([A-F](?:\s*(?:,\s*|\s+and\s+)[A-F])*|\£?[\d,]+(?:\.\d+)?)\s*$')


def parse_answer_block(block, num, section_no, q_subtype, q_part='A'):
    """Extract answer key, working, callouts from raw block lines."""
    lines = [ln for _, ln in block]
    text = '\n'.join(lines)

    result = {
        'num': num, 'section': section_no, 'key': '', 'keys': [],
        'working': '', 'examiner': '', 'tutor': '', 'tutorial': '', 'keytips': '',
        'raw': text
    }

    # ---- line-based callout extraction ----
    def callout_kind(ln):
        m = CALLOUT_RE.match(ln.strip())
        if m:
            k = m.group(1).lower()
            if k.startswith('tutor'):
                return 'tutor'
            if k.startswith('examiner'):
                return 'examiner'
            if k.startswith('tutorial'):
                return 'tutorial'
            if k.startswith('key answer'):
                return 'keytips'
        return None

    def is_structural(ln):
        s = ln.strip()
        if not s:
            return False
        if callout_kind(ln):
            return True
        if SUBKEY_RE.match(s):
            return True
        if re.match(r'^\d{1,3}\s+[A-Z£]', s):
            return True
        return False

    # Scan for callout blocks: from marker line until next structural line
    callouts = {'tutor': [], 'examiner': [], 'tutorial': [], 'keytips': []}
    i = 0
    while i < len(lines):
        kind = callout_kind(lines[i])
        if kind:
            j = i + 1
            chunk = []
            while j < len(lines) and not is_structural(lines[j]):
                chunk.append(lines[j].strip())
                j += 1
            callouts[kind].append('\n'.join(chunk).strip())
            i = j
        else:
            i += 1

    result['tutor'] = '\n\n'.join(callouts['tutor'])
    result['examiner'] = '\n\n'.join(callouts['examiner'])
    result['tutorial'] = '\n\n'.join(callouts['tutorial'])
    result['keytips'] = '\n\n'.join(callouts['keytips'])

    # ---- working = raw text minus callout sections ----
    keep = []
    i = 0
    while i < len(lines):
        if callout_kind(lines[i]):
            j = i + 1
            while j < len(lines) and not is_structural(lines[j]):
                j += 1
            i = j
            continue
        keep.append(lines[i])
        i += 1
    working = '\n'.join(keep).strip()
    result['working'] = working

    # ---- parse answer key line(s) ----
    LETTERS = r'[A-F](?:\s*(?:,\s*|\s+and\s+)[A-F])*'
    keys = []
    first = lines[0].strip() if lines else ''
    second = lines[1].strip() if len(lines) > 1 else ''
    cand = first
    if not re.match(r'^' + str(num) + r'\s+', cand) and re.match(r'^' + str(num) + r'$', cand):
        cand = str(num) + ' ' + second
    m = re.match(r'^' + str(num) + r'\s+(' + LETTERS + r'|\£?[\d,]+(?:\.\d+)?)\s*$', cand)
    if not m and q_part == 'A':
        # phrase answers like "80 60, 31 JANUARY THAT FOLLOWS..." or "235 31 DECEMBER 2027 AND £1,000"
        m = re.match(r'^' + str(num) + r'\s+([A-Z0-9£].{2,90})\s*$', cand)
        if m and not re.match(r'^' + str(num) + r'\s+(?:Tutor|Examiner|Tutorial|Key answer)', cand, re.I):
            result['key'] = m.group(1).strip()
            keys.append(result['key'])
    if m and not keys:
        keys.append(m.group(1))
        result['key'] = m.group(1)
    # Section B/C: sub-answer keys "1 A", "2 B", ... "5 C" at line starts
    if not keys or result['key'] in ('', ' '):
        for ln in lines:
            m2 = re.match(r'^(\d{1,2})\s+(' + LETTERS + r'|\£?[\d,]+(?:\.\d+)?)\s*$', ln.strip())
            if m2:
                keys.append(f"{m2.group(1)}: {m2.group(2)}")
        result['keys'] = keys
        if keys:
            result['key'] = '; '.join(keys)
    else:
        result['keys'] = [result['key']]

    return result


def main():
    global SECTION_OF_Q
    with open('full_questions.json', encoding='utf-8') as f:
        questions = json.load(f)
    SECTION_OF_Q = {q['num']: q['section'] for q in questions}

    reader = PdfReader(PDF)
    pages = load_pages(reader)
    starts = find_answer_starts(pages)

    print(f"Found answer starts: {len(starts)} (expected 306)")
    missing = [n for n in range(1, 307) if n not in starts]
    if missing:
        print("MISSING answer keys:", missing)

    blocks = split_answer_blocks(pages, starts)

    q_by_num = {q['num']: q for q in questions}
    answers = []
    for n in range(1, 307):
        if n not in blocks:
            continue
        q = q_by_num.get(n, {})
        result = parse_answer_block(blocks[n], n, q.get('section', 0), q.get('subtype', ''), q.get('part', 'A'))
        answers.append(result)

    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(answers, f, indent=1, ensure_ascii=False)
    print(f"Saved {len(answers)} answers to {OUT}")

    # sample
    for n in [1, 11, 16, 93, 98]:
        a = next((x for x in answers if x['num'] == n), None)
        if a:
            print(f"\nQ{n}: key={a['key'][:60]!r} tutor={bool(a['tutor'])} examiner={bool(a['examiner'])} tutorial={bool(a['tutorial'])}")
            print("  working:", a['working'][:200].replace('\n', ' | '))


if __name__ == '__main__':
    main()
