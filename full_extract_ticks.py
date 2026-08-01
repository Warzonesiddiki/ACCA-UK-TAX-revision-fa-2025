#!/usr/bin/env python3
"""
FULL VERSION UPGRADE — STEP 2b: EXTRACT TICK-BOX ANSWER GRIDS
For questions whose answers are tables of ✓ marks (Wingdings \uf050), re-read the
answer pages with text coordinates and reconstruct (row, column) answer grids.
Writes full_tick_answers.json
"""
import json
import re
from pypdf import PdfReader
import full_extract_answers as fea

PDF = 'TX_Exam_Kit_FA25.pdf'
OUT = 'full_tick_answers.json'

# Which questions are tick-style (answer is a table of ticks)
# Detected from questions JSON + answer keys that are empty/table-like
TICK_PAIRS = [('taxable', 'exempt'), ('true', 'false'), ('satisfies', 'does not satisfy'),
              ('qualifying', 'not qualifying'), ('deductible', 'not deductible'),
              ('allowable', 'not allowable'), ('chargeable', 'exempt'), ('correct', 'incorrect'),
              ('yes', 'no'), ('capital', 'revenue'), ('exempt', 'not exempt'),
              ('taxable', 'not taxable'), ('ordinary', 'additional'),
              ('treated as taxable', 'not treated as taxable')]


def is_tick_question(q):
    low = (q.get('text') or '').lower()
    if q.get('tick'):
        return True
    if any(a in low and b in low for a, b in TICK_PAIRS):
        return True
    return False


def collect_spans(page):
    """Return list of (text, x, y) spans using visitor."""
    spans = []
    def visitor(text, cm, tm, font_dict, font_size):
        if text.strip():
            spans.append((text, tm[4], tm[5]))
    try:
        page.extract_text(visitor_text=visitor)
    except Exception:
        pass
    return spans


def group_rows(spans, y_tol=3.5):
    """Group spans into rows by y proximity; keep x order."""
    rows = []
    for text, x, y in spans:
        placed = False
        for r in rows:
            if abs(r['y'] - y) < y_tol:
                r['spans'].append((text, x, y))
                placed = True
                break
        if not placed:
            rows.append({'y': y, 'spans': [(text, x, y)]})
    rows.sort(key=lambda r: r['y'])
    for r in rows:
        r['spans'].sort(key=lambda s: s[1])
        r['text'] = ' '.join(s[0] for s in r['spans']).strip()
    return rows


def split_words_with_x(text, x0, char_w=4.5):
    """Approximate x positions of words inside a single text span."""
    out = []
    cx = x0
    for word in re.findall(r'\S+', text):
        out.append((word, cx))
        cx += len(word) * char_w + 2.0
    return out


JUNK_WORDS = {'The', 'This', 'Which', 'What', 'For', 'How', 'When', 'Where', 'Why',
              'Tick', 'Select', 'Identify', 'Indicate', 'Mark', 'Choose', 'Section',
              'KAPLAN', 'PUBLISHING', 'PRACTICE', 'ANSWERS', 'QUESTIONS', 'TAXATION',
              'INCOME', 'NATIONAL', 'INSURANCE', 'CHARGEABLE', 'INHERITANCE',
              'CORPORATION', 'VALUE', 'ADDED', 'TAX', 'AND', 'TO', 'OF', 'IN', 'THE',
              'WITH', 'NOT', 'IS', 'ARE', 'A', 'AN', 'THAT', 'THIS', 'FOR', 'YOUR',
              'YEAR', 'YEARS', 'FROM', 'ON', 'AT', 'BY', 'BE'}

CHECK_CHARS = ('\uf050', '\uf0fc', '\uf04a', '✓', '✗', '☑', '☐', '✔', '✘')


def norm(s):
    return re.sub(r'\s+', ' ', s.lower()).strip()


def extract_grid(page, qtext=''):
    """Best-effort: return {'headers': [..], 'checks': [(row_text, col_idx)]}."""
    spans = collect_spans(page)
    rows = group_rows(spans)
    # find check marks
    checks = []
    for r in rows:
        for text, x, y in r['spans']:
            if any(c in text for c in CHECK_CHARS):
                checks.append({'y': y, 'x': x + 2})
    if not checks:
        return None
    # split spans into word-level entries with x
    word_spans = []
    for r in rows:
        for text, x, y in r['spans']:
            for w, wx in split_words_with_x(text, x):
                word_spans.append((w, wx, y))

    # Build candidate (row_label, check) pairs
    candidates = []
    for c in checks:
        same_row = [(w, wx) for w, wx, y in word_spans if abs(y - c['y']) < 3.5 and not any(ch in w for ch in CHECK_CHARS)]
        label = ' '.join(w for w, wx in sorted(same_row, key=lambda t: t[1]) if wx < c['x'] - 5).strip()
        if not label:
            continue
        candidates.append({'row': label, 'x': c['x'], 'y': c['y']})

    qn = norm(qtext) if qtext else ''
    if qn:
        candidates = [c for c in candidates
                      if norm(c['row'])[:35] in qn or qn[:35] in norm(c['row'])
                      or any(norm(c['row'])[i:i+18] in qn for i in range(0, max(1, len(norm(c['row'])) - 18), 9))]
    if not candidates:
        return None

    first_check_y = min(c['y'] for c in candidates)
    xmin = min(c['x'] for c in candidates)
    xmax = max(c['x'] for c in candidates)

    # header: row above (higher y in PDF coords) the checks, with 2+ caps words
    # whose x-range overlaps the check x-range; pick the closest row above the table.
    # Additionally, header words should appear in the question text (they are the
    # column labels like "Taxable Exempt" / "True False").
    header_row = None
    header_words = []
    for r in rows:
        if r['y'] <= first_check_y + 4:
            continue
        words = [(w.strip(':,;.'), wx) for w, wx, y in word_spans if abs(y - r['y']) < 3.5
                 and w[:1].isupper() and len(w.strip(':,;.')) > 2 and w.strip(':,;.') not in JUNK_WORDS]
        if len(words) < 2:
            continue
        if qn and not any(norm(w)[:12] in qn for w, _ in words):
            continue
        wx_min = min(wx for _, wx in words)
        wx_max = max(wx + len(w) * 4.5 for w, wx in words)
        if wx_max < xmin - 40 or wx_min > xmax + 40:
            continue
        if header_row is None or r['y'] < header_row:
            header_row = r['y']
            header_words = words
    if header_row is None or len(header_words) < 2:
        return None

    col_centers = [wx + len(w) * 4.5 for w, wx in header_words]
    headers = [w for w, wx in header_words]

    def col_for(x):
        best, bestd = 0, 1e9
        for i, cx in enumerate(col_centers):
            d = abs(x - cx)
            if d < bestd:
                bestd, best = d, i
        return best

    grid = []
    for c in candidates:
        grid.append({'row': c['row'], 'col': col_for(c['x'])})
    return {'headers': headers, 'grid': grid}


# answer page ranges per section (0-indexed)
ANS_PAGE_RANGES = {
    1: (256, 418), 2: (418, 482), 3: (482, 522), 4: (522, 616), 5: (616, 684),
}


def main():
    reader = PdfReader(PDF)
    with open('full_questions.json', encoding='utf-8') as f:
        questions = json.load(f)
    with open('full_answers.json', encoding='utf-8') as f:
        answers = json.load(f)

    # Re-derive exact answer start (page, line) with the same logic as the answers extractor
    fea.SECTION_OF_Q = {q['num']: q['section'] for q in questions}
    pages = fea.load_pages(reader)
    starts = fea.find_answer_starts(pages)
    page_of = {n: pages[pi][0] for n, (pi, li) in starts.items()}

    out = {}
    for q in questions:
        if not is_tick_question(q):
            continue
        n = q['num']
        if n not in page_of:
            print(f"Q{n}: no answer start located")
            continue
        found_page = page_of[n] - 1  # 0-indexed
        grid = extract_grid(reader.pages[found_page], qtext=q['text'])
        if (not grid or not grid['grid']) and found_page + 1 < 684:
            grid2 = extract_grid(reader.pages[found_page + 1], qtext=q['text'])
            if grid2 and grid2['grid']:
                grid = grid2
        if grid and grid['grid']:
            out[n] = grid
            print(f"Q{n}: headers={grid['headers']} rows={len(grid['grid'])} page={found_page+1}")
        else:
            print(f"Q{n}: no grid found (page {found_page+1})")

    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print(f"Saved {len(out)} tick grids to {OUT}")


if __name__ == '__main__':
    main()
