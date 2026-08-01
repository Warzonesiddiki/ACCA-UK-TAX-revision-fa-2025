#!/usr/bin/env python3
"""
FULL VERSION UPGRADE — STEP 1: EXTRACT ALL 306 QUESTIONS FROM TX_Exam_Kit_FA25.pdf
Reads the five question sections (PDF pages 47–256), splits by question number
(page-scoped detection), classifies each question, parses options/tick tables,
and writes full_questions.json.
"""
import re
import json
from pypdf import PdfReader

PDF = 'TX_Exam_Kit_FA25.pdf'
OUT = 'full_questions.json'

# Verified against the actual PDF layout (manual audit of section banners):
#   Section 1 IT&NIC  Q1-127  (pp47-118)
#   Section 2 CGT     Q128-179 (pp119-154; Section C incl. Q175-179)
#   Section 3 IHT     Q180-212 (pp155-178)
#   Section 4 CT      Q213-270 (pp179-226)
#   Section 5 VAT     Q271-306 (pp227-256)
SECTIONS = [
    {'num': 1, 'name': 'Income Tax & National Insurance', 'short': 'IT',
     'pages': (46, 118),   'q_range': (1, 127),   'a': (1, 92),   'b': (93, 97),   'c': (98, 127)},
    {'num': 2, 'name': 'Chargeable Gains (CGT)', 'short': 'CGT',
     'pages': (118, 154),  'q_range': (128, 179), 'a': (128, 161), 'b': (162, 170), 'c': (171, 179)},
    {'num': 3, 'name': 'Inheritance Tax (IHT)', 'short': 'IHT',
     'pages': (154, 178),  'q_range': (180, 212), 'a': (180, 201), 'b': (202, 209), 'c': (210, 212)},
    {'num': 4, 'name': 'Corporation Tax (CT)', 'short': 'CT',
     'pages': (178, 226),  'q_range': (213, 270), 'a': (213, 251), 'b': (252, 255), 'c': (256, 270)},
    {'num': 5, 'name': 'Value Added Tax (VAT)', 'short': 'VAT',
     'pages': (226, 256),  'q_range': (271, 306), 'a': (271, 292), 'b': (293, 303), 'c': (304, 306)},
]

def build_page_map(reader):
    """question number -> start page (1-indexed), validated by '^N ' at line start."""
    qnum_pages = {}
    for p in range(46, 256):
        try:
            t = reader.pages[p].extract_text() or ''
        except Exception:
            t = ''
        for m in re.finditer(r'(?m)^(\d{1,3})\s+(?=[A-Z"£0-9(])', t):
            n = int(m.group(1))
            if 1 <= n <= 306:
                qnum_pages.setdefault(n, []).append(p + 1)
    return {n: v[0] for n, v in qnum_pages.items()}


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


def extract_question_blocks(reader, page_map):
    """Return dict num -> block_text (raw, cleaned)."""
    blocks = {}
    for n in range(1, 307):
        pg = page_map[n]
        t = reader.pages[pg - 1].extract_text() or ''
        lines = t.split('\n')
        start_line = None
        for i, ln in enumerate(lines):
            s = ln.strip()
            if re.match(rf'^{n}\s', s) or s == str(n):
                start_line = i
                break
        if start_line is None:
            blocks[n] = ''
            continue
        # Question spans from its start line, across subsequent pages, until the
        # next question's start line (or next section's title) is found.
        collected = lines[start_line:]
        nxt = n + 1
        while True:
            # Look at current page remainder for next question
            nxt_start = None
            if nxt <= 306:
                nxt_pg = page_map[nxt]
                if nxt_pg == pg:
                    # next question on same page: find its line
                    for j, ln in enumerate(collected):
                        s = ln.strip()
                        if re.match(rf'^{nxt}\s', s) or s == str(nxt):
                            nxt_start = j
                            break
            if nxt_start is not None:
                collected = collected[:nxt_start]
                break
            if nxt > 306:
                break
            nxt_pg = page_map[nxt]
            if nxt_pg != pg + 1:
                # gap pages (section break pages): include them but stop at next q start
                for q in range(nxt, 307):
                    if page_map[q] == pg + 1:
                        nxt = q
                        break
            pg += 1
            if pg > 256:
                break
            t2 = reader.pages[pg - 1].extract_text() or ''
            lines2 = t2.split('\n')
            # stop if next question starts on this page
            stop_at = None
            if nxt <= 306 and page_map[nxt] == pg:
                for j, ln in enumerate(lines2):
                    s = ln.strip()
                    if re.match(rf'^{nxt}\s', s) or s == str(nxt):
                        stop_at = j
                        break
            collected += lines2[:stop_at] if stop_at is not None else lines2
            if stop_at is not None:
                break
            if nxt <= 306 and page_map[nxt] == pg:
                break
        # clean
        cleaned = []
        for ln in collected:
            if is_noise_line(ln):
                continue
            if re.match(r'^===== PDF PAGE', ln.strip()):
                continue
            cleaned.append(ln.rstrip())
        blocks[n] = '\n'.join(cleaned).strip()
    return blocks


def parse_options(block_text):
    lines = block_text.split('\n')
    opts = []
    for ln in lines:
        m = re.match(r'^([A-F])[.)\s]+\s*(.*)$', ln.strip())
        if m:
            opts.append((m.group(1), m.group(2).strip()))
    if not opts or opts[0][0] != 'A':
        return []
    got = ''.join(o[0] for o in opts)
    if not 'ABCDEFGH'.startswith(got):
        return []
    return opts


def parse_tick_table(block_text):
    """Best effort: returns {'header': [...], 'rows': [...]} or None."""
    lines = [ln.strip() for ln in block_text.split('\n')]
    header = None
    header_idx = None
    for i, ln in enumerate(lines):
        words = ln.split()
        if len(words) == 2 and words[0][0].isupper() and words[1][0].isupper() and len(words[0]) > 3 and len(words[1]) > 3:
            header = words
            header_idx = i
            break
    if not header:
        return None
    rows = []
    for ln in lines[header_idx + 1:]:
        if not ln:
            break
        if re.match(r'^[A-E][.)]', ln):
            break
        rows.append(ln)
    if not rows:
        return None
    return {'header': header, 'rows': rows}


def part_for(num):
    """Section part (A/B/C) from verified question-number ranges."""
    for sec in SECTIONS:
        if sec['q_range'][0] <= num <= sec['q_range'][1]:
            if sec['b'][0] <= num <= sec['b'][1]:
                return sec['num'], 'B'
            if sec['c'][0] <= num <= sec['c'][1]:
                return sec['num'], 'C'
            return sec['num'], 'A'
    return 0, 'A'


def classify(block, num, section_no, part):
    info = {'num': num, 'section': section_no, 'part': part, 'subtype': 'mcq',
            'title': '', 'text': block, 'options': [], 'tick': None, 'raw': block}
    first_line = block.split('\n')[0] if block else ''
    # Case / constructed-response titles: "93 PHILIP AND CHARLES (ADAPTED) Walk in the footsteps..."
    title = ''
    m = re.match(r'^\s*\d{1,3}\s+([A-Z][A-Za-z\'&()\- ]*?)(?:\s+Walk in the footsteps of a top tutor|$)', first_line)
    if m and len(m.group(1).strip()) > 2:
        title = m.group(1).strip()
    if part in ('B', 'C'):
        info['subtype'] = 'case' if part == 'B' else 'constructed'
        info['title'] = title
        # strip the leading number + title from the text
        body = re.sub(r'^\s*\d{1,3}\s+.*?(?:Walk in the footsteps of a top tutor\s*)?', '', block, count=1)
        info['text'] = body.strip()
        return info
    # Tick-box questions
    low = block.lower()
    tick_headers = [('taxable', 'exempt'), ('true', 'false'), ('satisfies', 'does not satisfy'),
                    ('qualifying', 'not qualifying'), ('deductible', 'not deductible'),
                    ('allowable', 'not allowable'), ('chargeable', 'exempt'),
                    ('correct', 'incorrect'), ('yes', 'no'), ('capital', 'revenue')]
    if any((a in low and b in low) for a, b in tick_headers) and re.search(r'(?i)\b(tick|identify|indicate|select)\b', low):
        tick = parse_tick_table(block)
        if tick:
            info['subtype'] = 'tick'
            info['tick'] = tick
            return info
    # Fill-blank
    if re.search(r'_{2,}|£\s*_{2,}', block):
        info['subtype'] = 'fill'
        return info
    # MCQ
    opts = parse_options(block)
    if opts:
        info['subtype'] = 'mcq'
        info['options'] = opts
        return info
    info['subtype'] = 'text'
    return info


def main():
    reader = PdfReader(PDF)
    page_map = build_page_map(reader)
    missing = [n for n in range(1, 307) if n not in page_map]
    print("missing from page map:", missing)
    blocks = extract_question_blocks(reader, page_map)

    questions = []
    for n in range(1, 307):
        block = blocks.get(n, '')
        if not block:
            print(f"WARN: empty block for Q{n}")
            continue
        section_no, part = part_for(n)
        info = classify(block, n, section_no, part)
        questions.append(info)

    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=1, ensure_ascii=False)
    print(f"Saved {len(questions)} questions to {OUT}")
    from collections import Counter
    print("By section:", dict(sorted(Counter(q['section'] for q in questions).items())))
    print("By subtype:", dict(Counter(q['subtype'] for q in questions)))
    print("By part:", dict(sorted(Counter(q['part'] for q in questions).items())))
    # spot check
    for n in [1, 27, 93, 98, 128, 175, 213, 271, 284, 306]:
        q = next((x for x in questions if x['num'] == n), None)
        if q:
            print(f"Q{n}: part={q['part']} subtype={q['subtype']} title={q['title'][:40]!r} opts={len(q['options'])} textlen={len(q['text'])}")


if __name__ == '__main__':
    main()
