#!/usr/bin/env python3
"""
FULL VERSION UPGRADE — STEP 3: BUILD TX-UK_Full_Revision_Pack_FA2025.html
Assembles the complete single-file revision pack from:
  • full_questions.json   (all 306 questions)
  • full_answers.json     (all 306 answers + examiner/tutor callouts)
  • full_tick_answers.json (tick-grid answer keys)
  • design CSS + JS engine (fresh, self-contained)
"""
import json
import re
import html as htmlmod

QJSON = 'full_questions.json'
AJSON = 'full_answers.json'
TJSON = 'full_tick_answers.json'
OUT = 'TX-UK_Full_Revision_Pack_FA2025.html'

SECTIONS = [
    {'num': 1, 'name': 'Income Tax & National Insurance', 'short': 'IT',
     'emoji': '🟢', 'a': (1, 92), 'b': (93, 97), 'c': (98, 127),
     'weight': '40%', 'desc': 'Employment income, benefits, trading income, property, savings & dividends, losses, partnerships, NIC, pensions, admin & ethics'},
    {'num': 2, 'name': 'Chargeable Gains (CGT)', 'short': 'CGT',
     'emoji': '🔵', 'a': (128, 161), 'b': (162, 170), 'c': (171, 179),
     'weight': '10-15%', 'desc': 'Basic computation, chattels, shares & securities, reliefs, corporate gains'},
    {'num': 3, 'name': 'Inheritance Tax (IHT)', 'short': 'IHT',
     'emoji': '🟣', 'a': (180, 201), 'b': (202, 209), 'c': (210, 212),
     'weight': '10-15%', 'desc': 'Lifetime transfers, exemptions, death estate, taper relief, administration'},
    {'num': 4, 'name': 'Corporation Tax (CT)', 'short': 'CT',
     'emoji': '🟠', 'a': (213, 251), 'b': (252, 255), 'c': (256, 270),
     'weight': '25-30%', 'desc': 'Rates, adjusted trading profits, capital allowances, losses, groups, overseas, administration'},
    {'num': 5, 'name': 'Value Added Tax (VAT)', 'short': 'VAT',
     'emoji': '🔴', 'a': (271, 292), 'b': (293, 303), 'c': (304, 306),
     'weight': '10%', 'desc': 'Registration, output & input tax, special schemes, partial exemption, administration'},
]

PART_NAMES = {'A': 'Section A · Objective Test Questions', 'B': 'Section B · Objective Test Cases', 'C': 'Section C · Constructed Response'}


# PDF text-extraction artifacts (split words) seen across the 684-page kit
SPLIT_WORD_FIXES = [
    ('ta x ', 'tax '), ('thro ugh', 'through'), ('trea ted', 'treated'),
    ('po tentially', 'potentially'), ('st ill', 'still'), ('wast ing', 'wasting'),
    ('reim bursed', 'reimbursed'), ('treat ed', 'treated'), ('consid er', 'consider'),
    ('receive d', 'received'), ('prepar ed', 'prepared'), ('incurr ed', 'incurred'),
    ('computa tion', 'computation'), ('individ ual', 'individual'), ('liab ility', 'liability'),
    ('emplo yee', 'employee'), ('busi ness', 'business'), ('expen diture', 'expenditure'),
    ('allow ance', 'allowance'), ('contri bution', 'contribution'), ('resid ent', 'resident'),
    ('tempor ary', 'temporary'), ('perman ent', 'permanent'), ('secur ities', 'securities'),
    ('deduc tion', 'deduction'), ('calcula tion', 'calculation'), ('rela ted', 'related'),
    ('requir ed', 'required'), ('retur n', 'return'), ('includ ed', 'included'),
    ('purchas ed', 'purchased'), ('provid ed', 'provided'), ('amount s', 'amounts'),
]


def clean_pdf_text(t):
    """Normalise PDF-extracted text into readable HTML-safe text."""
    t = t.replace('\uf050', '✓').replace('\uf0fc', '✗').replace('\uf04a', '✓')
    t = re.sub(r'CO\s*2', 'CO₂', t)
    t = t.replace('–', '–').replace('—', '—')
    for a, b in SPLIT_WORD_FIXES:
        t = t.replace(a, b)
    t = re.sub(r'[ \t]+$', '', t)           # trailing spaces
    t = re.sub(r'^\s+', '', t)              # leading spaces
    return t


def esc(t):
    return htmlmod.escape(t, quote=False)


def fmt_text(t):
    """Convert plain text (with newlines) to HTML paragraphs preserving layout."""
    t = clean_pdf_text(t)
    lines = [ln.rstrip() for ln in t.split('\n')]
    # collapse 3+ blank lines
    out = []
    blank = 0
    for ln in lines:
        if not ln.strip():
            blank += 1
            if blank <= 1:
                out.append('')
        else:
            blank = 0
            out.append(ln)
    body = '<br>'.join(esc(ln) for ln in out)
    return f'<div class="pdf-text">{body}</div>'


def fmt_working(t):
    t = clean_pdf_text(t)
    lines = [ln.rstrip() for ln in t.split('\n')]
    out = []
    blank = 0
    for ln in lines:
        if not ln.strip():
            blank += 1
            if blank <= 1:
                out.append('')
        else:
            blank = 0
            out.append(ln)
    body = '<br>'.join(esc(ln) for ln in out)
    return f'<div class="pdf-text mono">{body}</div>'


CALLOUT_STYLE = {'examiner': 'examiner', 'tutor': 'tip', 'tutorial': 'tip', 'keytips': 'tip'}
CALLOUT_TITLE = {'examiner': '📋 Examiner’s Report', 'tutor': '💡 Tutor’s Top Tips',
                 'tutorial': '📘 Tutorial Note', 'keytips': '🔑 Key Answer Tips'}


def fmt_callout(t, kind):
    t = clean_pdf_text(t).strip()
    if not t:
        return ''
    title = CALLOUT_TITLE[kind]
    style = CALLOUT_STYLE[kind]
    body = '<br>'.join(esc(ln) for ln in t.split('\n'))
    return (f'<div class="callout callout-{style}">'
            f'<div class="callout-title">{title}</div>'
            f'<p>{body}</p></div>')


def letters_to_list(key):
    """'B and F' / 'A, D' / 'C' -> ['B','F']"""
    m = re.findall(r'[A-F]', key or '')
    return m


def parse_fill_expected(key):
    """Extract expected numeric value(s) from an answer key like '£5,510'."""
    nums = re.findall(r'£?\s?([\d,]+(?:\.\d+)?)', key or '')
    return [n.replace(',', '') for n in nums]


def split_case(text, sub_count):
    """Split a Section B case into (scenario, [sub_question_texts])."""
    lines = text.split('\n')
    starts = []
    for i, ln in enumerate(lines):
        m = re.match(r'^(\d{1,2})\s', ln)
        if m and 1 <= int(m.group(1)) <= sub_count:
            starts.append((int(m.group(1)), i))
    # keep only a strictly increasing run at the end
    run = []
    for num, i in starts:
        if run and num != run[-1][0] + 1:
            run = []
        run.append((num, i))
    if len(run) < 2:
        return text, []
    first_i = run[0][1]
    scenario = '\n'.join(lines[:first_i]).strip()
    subs = []
    for idx in range(len(run)):
        start = run[idx][1]
        end = run[idx + 1][1] if idx + 1 < len(run) else len(lines)
        subs.append('\n'.join(lines[start:end]).strip())
    return scenario, subs


def parse_sub_options(sub_text):
    """Parse A-D options within a sub-question block."""
    lines = sub_text.split('\n')
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


def render_options(name, opts, multi=False):
    """Render interactive options (radio or checkbox)."""
    tag = 'checkbox' if multi else 'radio'
    items = []
    for letter, text in opts:
        items.append(
            f'<label class="option-item"><input type="{tag}" name="{name}" value="{letter}"> '
            f'<span class="opt-letter">{letter})</span> {esc(text)}</label>')
    return '<div class="options-group" data-multi="1" data-name="' + name + '">' + '\n'.join(items) + '</div>'


def render_tick_table(q, name, tick_grid=None):
    """Render a tick table (clickable cells). Uses grid data when available."""
    headers = None
    rows = []
    if tick_grid:
        headers = [''] + tick_grid.get('headers', ['✓', '✗'])
        seen = []
        for g in tick_grid.get('grid', []):
            if g['row'] not in seen:
                seen.append(g['row'])
        rows = seen
    if not rows:
        tick = q.get('tick') or {}
        headers = [''] + (tick.get('header') or ['✓', '✗'])
        rows = tick.get('rows') or []
    if not rows:
        return ''
    head_html = ''.join(f'<th>{esc(h)}</th>' for h in headers)
    ncols = len(headers) - 1
    row_html = []
    for r in rows:
        cells = ''.join(f'<td class="tick-cell" data-q="{name}" data-row="{esc(r)}" data-col="{ci}" onclick="TICK.toggle(this)"></td>'
                        for ci in range(ncols))
        row_html.append(f'<tr><td class="tick-row-label">{esc(r)}</td>{cells}</tr>')
    return (f'<table class="fiscal-table tick-table" data-q="{name}" id="tick-{name}">'
            f'<thead><tr>{head_html}</tr></thead><tbody>{"".join(row_html)}</tbody></table>'
            f'<button class="solution-toggle-btn" onclick="TICK.check(\'{name}\')">✓ Check My Ticks</button>')


def render_fill_input(name):
    return (f'<div class="fill-row"><label>Your answer:</label> '
            f'<input type="text" class="fill-input" id="fill-{name}" data-q="{name}" '
            f'placeholder="Type your answer (e.g. £5,510 or 5510)" '
            f'onkeydown="if(event.key===\'Enter\')FILL.check(\'{name}\')"></input> '
            f'<button class="solution-toggle-btn" onclick="FILL.check(\'{name}\')">✓ Check Answer</button></div>')


def answer_map_for(q, a):
    """Build the JS answer entries for a question card."""
    key = (a or {}).get('key', '')
    subtype = q.get('subtype')
    if subtype == 'mcq':
        letters = letters_to_list(key)
        return {'type': 'mcq', 'letters': letters}
    if subtype == 'tick':
        return {'type': 'tick'}
    if subtype in ('fill', 'text'):
        nums = parse_fill_expected(key)
        # phrase answers like "60, 31 JANUARY THAT FOLLOWS..." -> keep full key for substring check
        is_pure_num = bool(re.match(r'^£?[\d,]+(\.\d+)?$', key.strip())) if key else False
        if nums and (is_pure_num or subtype == 'fill'):
            return {'type': 'fill', 'nums': nums, 'key': key}
        if not is_pure_num and key:
            return {'type': 'fill', 'nums': nums, 'key': key, 'phrase': clean_pdf_text(key)}
        return {'type': 'fill', 'nums': nums, 'key': key}
    if q.get('part') == 'B':
        # sub-keys "1: A; 2: B; ..."
        subs = {}
        for part in (key or '').split(';'):
            m = re.match(r'^(\d+)\s*:\s*(.+)$', part.strip())
            if m:
                subs[int(m.group(1))] = m.group(2).strip()
        return {'type': 'case', 'subs': subs}
    return {'type': 'none', 'key': key}


def build_question_card(q, a, tick_grid, idx):
    n = q['num']
    name = f'q{n}'
    part = q['part']
    subtype = q['subtype']

    chips = f'<span class="chip chip-xp">+10 XP</span><span class="chip chip-type">{part} · {subtype.upper()}</span>'
    title = q.get('title') or f'Question {n}'
    title_html = f'Q{n} · {esc(title)}'

    body_parts = []

    if part == 'B' and subtype == 'case':
        qtext = re.sub(r'^\s*\d{1,3}\s+.*?(?:Walk in the footsteps of a top tutor\s*)?', '', q['text'], count=1)
        scenario, subs = split_case(qtext, 5)
        body_parts.append('<div class="case-scenario"><div class="case-scenario-title">📄 Scenario</div>'
                          + fmt_text(scenario) + '</div>')
        ansmap = answer_map_for(q, a)
        for si, sub in enumerate(subs, start=1):
            sub_opts = parse_sub_options(sub)
            # strip the leading number and any option lines from the displayed text
            sub_text = re.sub(r'^\d{1,2}\s', '', sub, count=1).strip()
            if sub_opts:
                opt_lines = [ln for ln in sub_text.split('\n') if not re.match(r'^[A-F][.)\s]', ln.strip())]
                sub_text = '\n'.join(opt_lines).strip()
            sname = f'{name}_s{si}'
            sub_ans = ansmap['subs'].get(si, '')
            sub_letters = letters_to_list(sub_ans)
            body_parts.append(f'<div class="sub-question" data-sub="{si}" data-ans="{esc(sub_ans)}">'
                              f'<div class="sub-q-label">Sub-question {si}</div>{fmt_text(sub_text)}')
            if sub_opts:
                multi = len(sub_letters) > 1
                body_parts.append(render_options(sname, sub_opts, multi=multi))
            elif '____' in sub or '__' in sub:
                body_parts.append(render_fill_input(sname))
            elif sub_ans and re.match(r'^£?[\d,]', sub_ans):
                body_parts.append(render_fill_input(sname))
            body_parts.append('</div>')
    elif part == 'C':
        body_parts.append(fmt_text(q['text']))
        body_parts.append('<div class="constructed-note">✍️ Constructed response — attempt the full computation in your answer book, then compare with the official solution below.</div>')
    elif subtype == 'mcq':
        # strip the A-F option lines from the displayed text (options rendered interactively)
        qtext = '\n'.join(ln for ln in q['text'].split('\n')
                          if not re.match(r'^[A-F][.)\s]', ln.strip()))
        body_parts.append(fmt_text(qtext))
        am = answer_map_for(q, a)
        letters = am['letters']
        multi = len(letters) > 1
        if multi:
            body_parts.append('<div class="multi-hint">⚡ Select ALL correct options ({})</div>'.format(', '.join(letters)))
        body_parts.append(render_options(name, q['options'], multi=multi))
    elif subtype == 'tick' or (tick_grid and tick_grid.get('grid')):
        body_parts.append(fmt_text(q['text']))
        body_parts.append(render_tick_table(q, name, tick_grid))
    elif subtype == 'fill':
        body_parts.append(fmt_text(q['text']))
        body_parts.append(render_fill_input(name))
    else:
        body_parts.append(fmt_text(q['text']))
        if a and a.get('key') and re.match(r'^£?[\d,]+(\.\d+)?$', a['key'].strip()):
            body_parts.append(render_fill_input(name))

    # Solution block
    sol_parts = []
    if a:
        if a.get('key'):
            sol_parts.append(f'<div class="answer-key-line">✅ <strong>Answer:</strong> {esc(clean_pdf_text(a["key"]))}</div>')
        if a.get('working') and len(a['working']) > 5:
            sol_parts.append(fmt_working(a['working']))
        for kind in ('keytips', 'tutor', 'examiner', 'tutorial'):
            c = fmt_callout(a.get(kind, ''), kind)
            if c:
                sol_parts.append(c)
    if not sol_parts:
        sol_parts.append('<p>See the official Kaplan Exam Kit for the full worked solution.</p>')
    solution = ('<button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>'
                + '<div class="solution-content">' + ''.join(sol_parts) + '</div>')

    tick_data = ''

    marks = ('<div style="margin-top:1rem;">'
             '<label class="mark-done-check"><input type="checkbox" data-task-id="' + name
             + '" onchange="GAMIFICATION.toggleTask(\'' + name + '\', 10, this.checked)"> Mark Done (+10 XP)</label></div>')

    return (f'<div class="drill-card" id="{name}" data-num="{n}" data-section="{q["section"]}" data-part="{part}" data-subtype="{subtype}">'
            f'<div class="drill-header"><span class="drill-title">{title_html}</span><div>{chips}</div></div>'
            + ''.join(body_parts) + solution + tick_data + marks + '</div>')


def build_sidebar():
    links = []
    links.append('<a class="sidebar-link" href="#cover" data-part="cover">🏠 Cover</a>')
    links.append('<a class="sidebar-link" href="#dashboard" data-part="dashboard">📊 Dashboard</a>')
    links.append('<a class="sidebar-link" href="#rates" data-part="rates">🧾 FA2025 Rates</a>')
    links.append('<a class="sidebar-link" href="#howto" data-part="howto">🎯 How to Use</a>')
    for sec in SECTIONS:
        links.append(f'<div class="sidebar-section">{sec["emoji"]} {sec["short"]} · {sec["name"]}</div>')
        for part, label in (('A', 'Section A · OTQs'), ('B', 'Section B · Cases'), ('C', 'Section C · CR')):
            lo, hi = sec[part.lower()]
            links.append(f'<a class="sidebar-link" href="#sec-{sec["num"]}-{part}" data-part="sec-{sec["num"]}-{part}">'
                         f'&nbsp;&nbsp;{label} · Q{lo}–Q{hi}</a>')
    links.append('<div class="sidebar-section">⚡ Tools</div>')
    links.append('<a class="sidebar-link" href="#" onclick="QUICK_FIRE.start();return false;">⚡ Quick Fire Quiz</a>')
    links.append('<a class="sidebar-link" href="#" onclick="EXAM_SIM.start();return false;">⏱ Exam Simulator</a>')
    links.append('<a class="sidebar-link" href="#" onclick="window.print();return false;">🖨 Print / PDF</a>')
    return '\n'.join(links)


def build_dashboard(q_by_num):
    total = len(q_by_num)
    stats = []
    for sec in SECTIONS:
        lo, hi = sec['a'][0], sec['c'][1]
        cnt = hi - lo + 1
        stats.append(f'<div class="dash-sec"><span>{sec["emoji"]} {sec["short"]}</span>'
                     f'<strong>{cnt}</strong><small>Q{lo}–Q{hi} · {sec["weight"]} of exam</small></div>')
    return (f'<section class="part-section" id="dashboard">'
            f'<div class="part-header"><div class="part-kicker">FULL EXAM KIT · FA2025</div>'
            f'<h2 class="part-title">📊 Question Bank Dashboard — All {total} Official Questions</h2>'
            f'<p class="part-subtitle">Every question from the Kaplan TX-UK Exam Kit (FA2025, June 2026 – June 2027 sittings), '
            f'with interactive marking, worked solutions, examiner reports and tutor tips.</p></div>'
            f'<div class="dash-grid">{"".join(stats)}</div>'
            f'<div class="dash-progress"><div class="progress-container"><div class="progress-bar-bg">'
            f'<div class="progress-bar-fill" id="dash-fill" style="width:0%"></div></div>'
            f'<span id="dash-label" class="dash-label">0 / {total} questions completed</span></div></div>'
            f'<div class="search-row"><input id="search-input" class="search-input" placeholder="🔎 Search questions… (e.g. 128, lease premium, child benefit)">'
            f'<button class="quickfire-btn" onclick="doSearch()">Search</button>'
            f'<button class="solution-toggle-btn" onclick="clearSearch()">Clear</button></div>'
            f'</section>')


def build_rates_table():
    rows = [
        ('Personal Allowance', '£12,570', 'Income Tax'),
        ('PA taper', '£1 for every £2 over adjusted net income of £100,000 (nil above £125,140)', 'Income Tax'),
        ('Basic rate band', '£37,700 (20%)', 'Income Tax'),
        ('Higher rate', '£37,701 – £125,140 (40%)', 'Income Tax'),
        ('Additional rate', 'over £125,140 (45%)', 'Income Tax'),
        ('Savings starting rate', '£5,000 @ 0% (above PA)', 'Income Tax'),
        ('Savings nil-rate band', '£1,000 basic / £500 higher / £0 additional', 'Income Tax'),
        ('Dividend nil-rate band', '£500', 'Income Tax'),
        ('Dividend rates', '8.75% basic / 33.75% higher / 39.35% additional', 'Income Tax'),
        ('Marriage allowance transfer', '£1,260 (20% relief)', 'Income Tax'),
        ('Child benefit charge', '1% per £200 of ANI between £60,000–£80,000', 'Income Tax'),
        ('Employment allowance', '£10,500 per year', 'NIC'),
        ('Class 1 employee NIC', '8% on £12,571–£50,270; 2% above', 'NIC'),
        ('Class 1 employer NIC', '13.8% above £9,100', 'NIC'),
        ('Class 4 NIC', '6% on £12,571–£50,270; 2% above', 'NIC'),
        ('Class 2 NIC', '£3.50/week', 'NIC'),
        ('Annual Investment Allowance', '£1,000,000', 'Capital Allowances'),
        ('Writing Down Allowance (main pool)', '18%', 'Capital Allowances'),
        ('Special rate pool', '6%', 'Capital Allowances'),
        ('CGT Annual Exempt Amount', '£3,000', 'CGT'),
        ('CGT basic rate (non-residential)', '18%', 'CGT'),
        ('CGT higher rate (non-residential)', '24%', 'CGT'),
        ('CGT residential property rates', '18% / 24%', 'CGT'),
        ('BADR / Investors’ Relief', '10% · £1,000,000 lifetime limit', 'CGT'),
        ('IHT Nil Rate Band', '£325,000', 'IHT'),
        ('Residence NRB', '£175,000 (max, with taper)', 'IHT'),
        ('IHT lifetime rates', '20% (chargeable transfers) / 0% PETs', 'IHT'),
        ('IHT death rates', '40% (excess over NRB); 36% if 10%+ left to charity', 'IHT'),
        ('IHT annual exemption', '£3,000 per donor', 'IHT'),
        ('Corporation tax main rate', '25% (profits over £250,000)', 'CT'),
        ('CT small profits rate', '19% (profits up to £50,000)', 'CT'),
        ('CT marginal relief fraction', '3/200 (lower limit £50,000, upper £250,000)', 'CT'),
        ('VAT registration threshold', '£90,000 (12-month test)', 'VAT'),
        ('VAT deregistration threshold', '£88,000 (30-day test)', 'VAT'),
        ('VAT standard rate', '20%', 'VAT'),
        ('VAT flat rate scheme', 'based on trade sector (e.g. 13.5% limited cost trader)', 'VAT'),
        ('VAT return filing', 'quarterly, due 1 month + 7 days', 'VAT'),
    ]
    trs = ''.join(f'<tr><td>{esc(a)}</td><td>{esc(b)}</td><td><span class="chip chip-type">{esc(c)}</span></td></tr>'
                  for a, b, c in rows)
    return (f'<section class="part-section" id="rates">'
            f'<div class="part-header"><div class="part-kicker">REFERENCE · EXAMINABLE</div>'
            f'<h2 class="part-title">🧾 FA2025 Rates & Allowances Quick-Reference</h2>'
            f'<p class="part-subtitle">Key figures for the June 2026 – June 2027 exam sittings (Finance Act 2025). '
            f'Always cross-check with the rates & allowances given in your exam.</p></div>'
            f'<table class="fiscal-table"><thead><tr><th>Item</th><th>FA2025 Value</th><th>Area</th></tr></thead>'
            f'<tbody>{trs}</tbody></table></section>')


def build_js(q_by_num, a_by_num, tick_grids):
    # Build QUIZ answers map: name -> letters or expected fill
    mcq_map = {}
    fill_map = {}
    case_map = {}
    tick_names = set()
    for n, q in q_by_num.items():
        a = a_by_num.get(n, {})
        name = f'q{n}'
        am = answer_map_for(q, a)
        if am['type'] == 'mcq' and am['letters']:
            mcq_map[name] = ''.join(am['letters'])
        if am['type'] == 'fill' and am.get('nums'):
            fill_map[name] = am['nums'][0]
        if am['type'] == 'fill' and am.get('phrase'):
            fill_map[name + '_phrase'] = clean_pdf_text(am['phrase']).lower().strip()
        if q.get('part') == 'B':
            subs = am.get('subs', {})
            for si in range(1, 6):
                if si in subs:
                    key = subs[si]
                    letters = letters_to_list(key)
                    if letters:
                        mcq_map[f'{name}_s{si}'] = ''.join(letters)
                    nums = parse_fill_expected(key)
                    if nums:
                        fill_map[f'{name}_s{si}'] = nums[0]
                    if re.search(r'[A-Za-z]', key or ''):
                        fill_map[f'{name}_s{si}_phrase'] = clean_pdf_text(key).lower().strip()
        if am['type'] == 'tick' or q.get('subtype') == 'tick':
            tick_names.add(name)

    js = r"""

/* ═══════════════ TX-UK FULL PACK ENGINE (auto-generated) ═══════════════ */
const ANSWERS = __ANSWERS__;
const FILLS = __FILLS__;
const TICK_Q = __TICK_Q__;
const TICK_GRIDS = __TICK_GRIDS__;
const TOTAL_Q = __TOTALQ__;

function $(id){ return document.getElementById(id); }
function qs(sel){ return document.querySelectorAll(sel); }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }

const GAMIFICATION = {
  completedTasks: new Set(),
  xp: 0,
  init() {
    try {
      const s = JSON.parse(localStorage.getItem('TXFULL_STATE') || '{}');
      this.completedTasks = new Set(s.done || []);
      this.xp = s.xp || 0;
    } catch(e) {}
    this.refresh();
  },
  toggleSolution(btn) {
    const card = btn.closest('.drill-card');
    const sol = card ? card.querySelector('.solution-content') : null;
    if (!sol) return;
    sol.classList.toggle('open');
    btn.innerHTML = sol.classList.contains('open') ? '▲ Hide Working & Solution' : '▼ Show Working & Solution';
  },
  toggleTask(id, xp, checked) {
    if (checked) { this.completedTasks.add(id); this.xp += xp; }
    else { this.completedTasks.delete(id); this.xp = Math.max(0, this.xp - xp); }
    this.refresh();
    this.save();
    const card = $(id);
    if (card) card.classList.toggle('completed', checked);
  },
  save() { localStorage.setItem('TXFULL_STATE', JSON.stringify({done: Array.from(this.completedTasks), xp: this.xp})); },
  refresh() {
    const done = this.completedTasks.size;
    const pct = Math.round(done / TOTAL_Q * 100);
    const fill = $('hud-fill'); if (fill) fill.style.width = pct + '%';
    const lbl = $('hud-pct'); if (lbl) lbl.textContent = pct + '%';
    const xpEl = $('hud-xp'); if (xpEl) xpEl.textContent = this.xp + ' XP';
    const dfill = $('dash-fill'); if (dfill) dfill.style.width = pct + '%';
    const dlbl = $('dash-label'); if (dlbl) dlbl.textContent = done + ' / ' + TOTAL_Q + ' questions completed · ' + pct + '%';
    const rank = $('hud-rank');
    if (rank) {
      const r = pct>=90?'🏆 TX Master':pct>=70?'🥇 Gold':pct>=50?'🥈 Silver':pct>=25?'🥉 Bronze':'🎓 Cadet';
      rank.textContent = r;
    }
    qs('.sidebar-link').forEach(l=>{
      const p = l.getAttribute('data-part');
      if (p && p.startsWith('sec-')) {
        const key = 'sec-' + p.split('-')[1] + '-' + p.split('-')[2];
      }
    });
  }
};

const QUIZ = {
  init() {
    qs('.options-group').forEach(group => {
      const name = group.getAttribute('data-name') || (group.querySelector('input')||{}).name;
      if (!name) return;
      group.querySelectorAll('input').forEach((inp, idx) => {
        if (!inp.getAttribute('value')) inp.value = String.fromCharCode(65 + idx);
      });
      group.querySelectorAll('input').forEach(inp => {
        inp.addEventListener('change', () => this.check(name));
      });
    });
    qs('.fill-input').forEach(inp => {
      inp.addEventListener('input', () => { inp.classList.remove('correct','incorrect'); });
    });
  },
  correctSet(name) {
    const key = ANSWERS[name];
    if (!key) return null;
    return key.split('');
  },
  check(name) {
    const group = qs('input[name="'+name+'"]');
    if (!group.length) return;
    const correct = ANSWERS[name];
    if (!correct) { reveal(name); return; }
    const correctSet = correct.split('');
    const isMulti = group[0].type === 'checkbox';
    if (isMulti) {
      const chosen = Array.from(group).filter(i => i.checked).map(i => i.value).sort().join('');
      const right = correctSet.slice().sort().join('');
      group.forEach(i => {
        const lab = i.closest('.option-item');
        if (correctSet.includes(i.value)) lab.classList.add('reveal-correct');
        if (i.checked && !correctSet.includes(i.value)) lab.classList.add('incorrect');
        i.disabled = true;
      });
      if (chosen === right) {
        streak(true); group.forEach(i=>{ const lab=i.closest('.option-item'); if(correctSet.includes(i.value)) lab.classList.add('correct'); });
      } else {
        streak(false);
        group.forEach(i=>{ const lab=i.closest('.option-item'); if(i.checked && correctSet.includes(i.value)) lab.classList.add('correct'); });
      }
    } else {
      const sel = Array.from(group).find(i => i.checked);
      if (!sel) return;
      const ok = sel.value === correct;
      group.forEach(i => {
        const lab = i.closest('.option-item');
        if (i.value === correct) lab.classList.add('reveal-correct');
        if (i.checked && !ok) lab.classList.add('incorrect');
        if (i.checked && ok) lab.classList.add('correct');
        i.disabled = true;
      });
      streak(ok);
    }
    reveal(name);
  }
};

function reveal(name) {
  const card = qs('input[name="'+name+'"]')[0]?.closest('.drill-card')
    || qs('.fill-input[data-q="'+name+'"]')[0]?.closest('.drill-card')
    || $(name);
  if (!card) return;
  const btn = card.querySelector('.solution-toggle-btn');
  const sol = card.querySelector('.solution-content');
  if (btn && sol && !sol.classList.contains('open')) {
    setTimeout(() => { sol.classList.add('open'); btn.innerHTML = '▲ Hide Working & Solution'; }, 500);
  }
  const mk = card.querySelector('.mark-done-check input');
  if (mk && !mk.checked) { mk.checked = true; mk.dispatchEvent(new Event('change')); }
}

let streakCount = 0, bestStreak = 0;
function streak(ok) {
  streakCount = ok ? streakCount + 1 : 0;
  if (ok && streakCount > bestStreak) bestStreak = streakCount;
  const b = $('streak-badge');
  if (b) {
    if (streakCount > 0) { b.textContent = '🔥 ' + streakCount + ' Streak'; b.style.display = 'flex'; }
    else b.style.display = 'none';
  }
}

const TICK = {
  toggle(cell) {
    cell.classList.toggle('marked');
    cell.textContent = cell.classList.contains('marked') ? '✓' : '';
  },
  check(name) {
    const table = $('tick-' + name);
    if (!table) return;
    const grid = TICK_GRIDS[name] || null;
    const cells = table.querySelectorAll('.tick-cell');
    if (grid && grid.grid) {
      cells.forEach(c => { c.onclick = null; c.style.pointerEvents = 'none'; });
      // build expected map
      const expected = {};
      grid.grid.forEach(g => { expected[g.row + '|' + g.col] = true; });
      const rows = table.querySelectorAll('tbody tr');
      let allRight = true, any = false;
      rows.forEach(tr => {
        const label = tr.querySelector('.tick-row-label').textContent.trim();
        tr.querySelectorAll('.tick-cell').forEach(cell => {
          const col = parseInt(cell.getAttribute('data-col'), 10);
          const should = !!expected[label + '|' + col];
          const marked = cell.classList.contains('marked');
          any = any || marked;
          if (should) {
            cell.classList.add('reveal-correct');
            if (marked) cell.classList.add('correct');
            else cell.textContent = '✓';
          } else if (marked) {
            cell.classList.add('incorrect'); cell.textContent = '✗';
            allRight = false;
          }
        });
      });
      if (any && allRight) streak(true); else if (any) streak(false);
    } else {
      cells.forEach(c => { c.onclick = null; c.style.pointerEvents = 'none'; });
    }
    reveal(name);
  }
};

const FILL = {
  normalize(v) {
    v = (v || '').toLowerCase().replace(/[£,]/g, '').trim();
    return v;
  },
  check(name) {
    const inp = $('fill-' + name);
    if (!inp) return;
    const expected = FILLS[name];
    const phrase = FILLS[name + '_phrase'];
    if (expected === undefined && !phrase) { reveal(name); return; }
    const val = this.normalize(inp.value);
    let ok = false;
    if (expected !== undefined) ok = val === String(expected);
    if (!ok && phrase) ok = phrase.split(/[;,]\s*/).every(p => p && val.includes(p));
    inp.classList.remove('correct','incorrect');
    if (ok) { inp.classList.add('correct'); streak(true); }
    else { inp.classList.add('incorrect'); streak(false); }
    reveal(name);
  }
};

const QUICK_FIRE = {
  pool: [],
  qs: [],
  current: 0,
  score: 0,
  start() {
    if (!this.pool.length) {
      qs('.drill-card[data-subtype="mcq"]').forEach(card => {
        const group = card.querySelector('.options-group');
        if (!group) return;
        const opts = Array.from(group.querySelectorAll('.option-item'));
        const qtext = card.querySelector('.pdf-text') ? card.querySelector('.pdf-text').textContent.trim() : '';
        const name = group.getAttribute('data-name');
        if (!name || !ANSWERS[name] || ANSWERS[name].length > 1) return;
        if (qtext.length < 20 || qtext.length > 700) return;
        this.pool.push({name, qtext, opts: opts.map(o=>o.textContent.trim().replace(/^[A-F]\)\s*/, '')), ans: ANSWERS[name]});
      });
    }
    const shuffled = this.pool.slice().sort(() => Math.random() - 0.5).slice(0, 20);
    this.qs = shuffled;
    this.current = 0; this.score = 0;
    const modal = $('qf-modal'); if (modal) modal.classList.add('show');
    this.show();
  },
  show() {
    if (this.current >= this.qs.length) { this.results(); return; }
    const q = this.qs[this.current];
    const opts = q.opts.map((o, i) =>
      '<button class="quickfire-btn qf-opt" style="display:block;margin:.4rem 0;text-align:left" onclick="QUICK_FIRE.answer(' + i + ')">' +
      String.fromCharCode(65+i) + ') ' + esc(o) + '</button>').join('');
    $('qf-content').innerHTML =
      '<div class="qf-progress">Question ' + (this.current+1) + ' / ' + this.qs.length + ' · Score ' + this.score + '</div>' +
      '<h3 class="qf-q">' + esc(q.qtext) + '</h3><div class="options-group">' + opts + '</div>';
  },
  answer(i) {
    const q = this.qs[this.current];
    const correct = q.ans;
    const btns = qs('#qf-content .qf-opt');
    btns.forEach((b, idx) => {
      b.disabled = true;
      if (idx === q.ans.charCodeAt(0) - 65) b.classList.add('correct');
      if (idx === i && idx !== q.ans.charCodeAt(0) - 65) b.classList.add('incorrect');
    });
    if (i === q.ans.charCodeAt(0) - 65) { this.score++; streak(true); } else streak(false);
    setTimeout(() => { this.current++; this.show(); }, 900);
  },
  results() {
    const pct = Math.round(this.score / this.qs.length * 100);
    const msg = pct >= 80 ? '🏆 Outstanding — exam ready!' : pct >= 60 ? '👍 Good — keep practising!' : pct >= 40 ? '📖 Getting there — review the solutions.' : '💪 Keep going — review the workings.';
    $('qf-content').innerHTML =
      '<div style="text-align:center;padding:2rem 0"><div class="qf-score">' + this.score + ' / ' + this.qs.length + '</div>' +
      '<p style="font-size:1.1rem;color:var(--ink-soft);margin:1rem 0">' + pct + '% — ' + msg + '</p>' +
      '<div style="display:flex;gap:1rem;justify-content:center"><button class="quickfire-btn" onclick="QUICK_FIRE.start()">🔄 Try Again</button>' +
      '<button class="solution-toggle-btn" onclick="QUICK_FIRE.close()">✓ Done</button></div></div>';
  },
  close() { const m = $('qf-modal'); if (m) m.classList.remove('show'); }
};

const EXAM_SIM = {
  qs: [],
  current: 0,
  score: 0,
  timer: null,
  seconds: 0,
  start() {
    const pool = [];
    qs('.drill-card[data-subtype="mcq"]').forEach(card => {
      const group = card.querySelector('.options-group');
      const name = group && group.getAttribute('data-name');
      if (name && ANSWERS[name] && ANSWERS[name].length === 1) pool.push(name);
    });
    this.qs = pool.sort(() => Math.random() - 0.5).slice(0, 25);
    this.current = 0; this.score = 0; this.seconds = 25 * 120;
    const modal = $('sim-modal'); if (modal) modal.classList.add('show');
    this.tick(); this.show();
  },
  tick() {
    clearInterval(this.timer);
    this.timer = setInterval(() => {
      if (this.seconds > 0) this.seconds--;
      const d = $('sim-timer');
      if (d) d.textContent = Math.floor(this.seconds/60) + ':' + String(this.seconds%60).padStart(2,'0');
      if (this.seconds <= 0) this.finish();
    }, 1000);
  },
  show() {
    if (this.current >= this.qs.length) return this.finish();
    const name = this.qs[this.current];
    const card = $(name);
    const group = card.querySelector('.options-group');
    const opts = Array.from(group.querySelectorAll('.option-item'));
    const qtext = card.querySelector('.pdf-text').textContent.trim();
    const html = '<div class="qf-progress">Mock Q' + (this.current+1) + ' / ' + this.qs.length + ' · Score ' + this.score + ' · ⏱ <span id="sim-timer">25:00</span></div>' +
      '<h3 class="qf-q">' + esc(qtext) + '</h3><div class="options-group">' +
      opts.map((o, i) => '<button class="quickfire-btn qf-opt" style="display:block;margin:.4rem 0;text-align:left" onclick="EXAM_SIM.answer(' + i + ')">' +
        String.fromCharCode(65+i) + ') ' + esc(o.textContent.trim().replace(/^[A-F]\)\s*/, '')) + '</button>').join('') + '</div>';
    $('sim-content').innerHTML = html;
  },
  answer(i) {
    const name = this.qs[this.current];
    const correct = ANSWERS[name];
    const btns = qs('#sim-content .qf-opt');
    btns.forEach((b, idx) => {
      b.disabled = true;
      if (idx === correct.charCodeAt(0) - 65) b.classList.add('correct');
      if (idx === i && idx !== correct.charCodeAt(0) - 65) b.classList.add('incorrect');
    });
    if (i === correct.charCodeAt(0) - 65) this.score++;
    setTimeout(() => { this.current++; this.show(); }, 800);
  },
  finish() {
    clearInterval(this.timer);
    const pct = Math.round(this.score / Math.max(1,this.qs.length) * 100);
    $('sim-content').innerHTML = '<div style="text-align:center;padding:2rem 0"><div class="qf-score">' + this.score + ' / ' + this.qs.length + '</div>' +
      '<p style="font-size:1.1rem;color:var(--ink-soft);margin:1rem 0">Mock score: ' + pct + '%</p>' +
      '<button class="quickfire-btn" onclick="EXAM_SIM.close()">✓ Close</button></div>';
  },
  close() { const m = $('sim-modal'); if (m) m.classList.remove('show'); }
};

function doSearch() {
  const q = $('search-input').value.toLowerCase().trim();
  qs('.drill-card').forEach(card => {
    const txt = card.textContent.toLowerCase();
    const n = card.getAttribute('data-num');
    let show = !q || txt.includes(q) || (n && n.includes(q.replace(/^q/,'')));
    card.style.display = show ? '' : 'none';
  });
}
function clearSearch() {
  const si = $('search-input'); if (si) si.value = '';
  qs('.drill-card').forEach(c => c.style.display = '');
}

/* ── Dark mode ── */
const DARK = {
  init() {
    try {
      const d = JSON.parse(localStorage.getItem('TXFULL_THEME') || '{}');
      if (d.dark) this.on();
    } catch(e) {}
  },
  on() { document.documentElement.setAttribute('data-theme', 'dark');
         const b = $('dark-btn'); if (b) b.textContent = '☀️';
         localStorage.setItem('TXFULL_THEME', JSON.stringify({dark: true})); },
  off() { document.documentElement.removeAttribute('data-theme');
          const b = $('dark-btn'); if (b) b.textContent = '🌙';
          localStorage.setItem('TXFULL_THEME', JSON.stringify({dark: false})); },
  toggle() { document.documentElement.getAttribute('data-theme') === 'dark' ? this.off() : this.on(); }
};

/* ── Flashcards (spaced repetition lite) ── */
const FLASHCARDS = {
  deck: [], pos: 0, known: new Set(),
  build() {
    const pool = [];
    qs('.drill-card[data-subtype="mcq"]').forEach(card => {
      const group = card.querySelector('.options-group');
      if (!group) return;
      const name = group.getAttribute('data-name');
      if (!name || !ANSWERS[name] || ANSWERS[name].length > 1) return;
      const qtext = card.querySelector('.pdf-text') ? card.querySelector('.pdf-text').textContent.trim() : '';
      if (qtext.length < 20 || qtext.length > 700) return;
      const correct = ANSWERS[name];
      const opts = Array.from(group.querySelectorAll('.option-item')).map(o =>
        o.textContent.trim().replace(/^[A-F]\)\s*/, ''));
      pool.push({name, qtext, correct, opts});
    });
    const shuffled = pool.slice().sort(() => Math.random() - 0.5).slice(0, 40);
    this.deck = shuffled;
    this.pos = 0;
    try { this.known = new Set(JSON.parse(localStorage.getItem('TXFULL_KNOWN') || '[]')); } catch(e) {}
  },
  open() {
    this.build();
    const m = $('fc-modal'); if (m) m.classList.add('show');
    this.render();
  },
  close() { const m = $('fc-modal'); if (m) m.classList.remove('show'); },
  render() {
    if (this.pos >= this.deck.length) {
      $('fc-content').innerHTML = '<div style="text-align:center;padding:2rem 0"><div class="qf-score">Deck complete! 🎉</div><p style="color:var(--ink-soft);margin-top:.6rem">You reviewed ' + this.deck.length + ' cards (' + this.known.size + ' known).</p></div>';
      $('fc-actions').innerHTML = '<button class="quickfire-btn" onclick="FLASHCARDS.open()">🔄 Restart</button><button class="solution-toggle-btn" onclick="FLASHCARDS.close()">✓ Done</button>';
      return;
    }
    const c = this.deck[this.pos];
    const isKnown = this.known.has(c.name);
    const optsHtml = c.opts.map(o => '<div class="flashcard-opt">• ' + esc(o) + '</div>').join('');
    $('fc-counter').textContent = 'Card ' + (this.pos + 1) + ' / ' + this.deck.length + ' · Known: ' + this.known.size;
    $('fc-content').innerHTML =
      '<div class="flashcard-wrapper" id="fc-card" onclick="FLASHCARDS.flip()">' +
      '<div class="flashcard-inner"><div class="flashcard-front">' + esc(c.qtext) + '</div>' +
      '<div class="flashcard-back"><strong>Answer: ' + esc(c.correct) + '</strong><br>' + optsHtml + '</div></div></div>';
    $('fc-actions').innerHTML =
      (isKnown ? '<span style="align-self:center;font-size:.8rem;color:var(--green-bright)">✓ Already known</span>' : '') +
      '<button class="quickfire-btn" onclick="FLASHCARDS.know()">✓ Got it</button>' +
      '<button class="solution-toggle-btn" onclick="FLASHCARDS.retry()">🔁 Review again</button>' +
      '<button class="solution-toggle-btn" onclick="FLASHCARDS.jump()">Open in pack</button>';
  },
  flip() { const w = $('fc-card'); if (w) w.classList.toggle('flipped'); },
  know() {
    this.known.add(this.deck[this.pos].name);
    try { localStorage.setItem('TXFULL_KNOWN', JSON.stringify(Array.from(this.known))); } catch(e) {}
    this.deck.splice(this.pos, 1);
    this.render();
  },
  retry() { const c = this.deck[this.pos]; this.deck.splice(this.pos, 1); this.deck.splice(Math.min(this.pos + 3, this.deck.length), 0, c); this.render(); },
  jump() { const n = this.deck[this.pos].name; FLASHCARDS.close(); const el = $(n); if (el) { el.scrollIntoView({behavior:'smooth'}); } }
};

/* ── Keyboard shortcuts ── */
const KEYS = {
  open() { const m = $('keys-modal'); if (m) m.classList.add('show'); },
  close() { const m = $('keys-modal'); if (m) m.classList.remove('show'); }
};

document.addEventListener('keydown', (e) => {
  const tag = (e.target.tagName || '').toLowerCase();
  const typing = tag === 'input' || tag === 'textarea' || e.target.isContentEditable;
  if ((e.ctrlKey || e.metaKey) && e.key === '/') { e.preventDefault(); KEYS.open(); return; }
  if (e.key === '?' && !typing) { KEYS.open(); return; }
  if (e.key === 'Escape') { QUICK_FIRE.close(); EXAM_SIM.close(); FLASHCARDS.close(); KEYS.close(); return; }
  if (typing) return;
  const k = e.key.toLowerCase();
  if (k === 'd') DARK.toggle();
  else if (k === 'q') QUICK_FIRE.start();
  else if (k === 'm') EXAM_SIM.start();
  else if (k === 'f') FLASHCARDS.open();
  else if (k === '/') { const si = $('search-input'); if (si) { si.focus(); e.preventDefault(); } }
  else if ((e.ctrlKey || e.metaKey) && k === 'p') { /* allow native print */ }
});

document.addEventListener('DOMContentLoaded', () => {
  GAMIFICATION.init(); QUIZ.init(); DARK.init();
  qs('.drill-card').forEach(card => {
    const mk = card.querySelector('.mark-done-check input');
    if (mk && GAMIFICATION.completedTasks.has(card.id)) { mk.checked = true; card.classList.add('completed'); }
  });
  const saved = JSON.parse(localStorage.getItem('TXFULL_STATE') || '{}');
  if (saved.done) saved.done.forEach(id => { const c = $(id); if (c) c.classList.add('completed'); });
});
"""
    js = (js
          .replace('__ANSWERS__', json.dumps(mcq_map, ensure_ascii=False))
          .replace('__FILLS__', json.dumps(fill_map, ensure_ascii=False))
          .replace('__TICK_Q__', json.dumps(sorted(tick_names), ensure_ascii=False))
          .replace('__TICK_GRIDS__', json.dumps({'q' + k: v for k, v in tick_grids.items()}, ensure_ascii=False))
          .replace('__TOTALQ__', str(len(q_by_num))))
    return js



def main():
    with open(QJSON, encoding='utf-8') as f:
        questions = json.load(f)
    with open(AJSON, encoding='utf-8') as f:
        answers = json.load(f)
    with open(TJSON, encoding='utf-8') as f:
        tick_grids = json.load(f)

    q_by_num = {q['num']: q for q in questions}
    a_by_num = {a['num']: a for a in answers}

    # inject tick parse into questions that failed grid parsing but have tables
    # (keep whatever the question extractor found)

    cards = []
    idx = 0
    for n in range(1, 307):
        q = q_by_num[n]
        a = a_by_num.get(n, {})
        tg = tick_grids.get(str(n))
        cards.append(build_question_card(q, a, tg, idx))
        idx += 1

    # Assemble per-section HTML
    sec_html = []
    for sec in SECTIONS:
        inner = []
        for part in ('A', 'B', 'C'):
            lo, hi = sec[part.lower()]
            nums = [n for n in range(lo, hi + 1)]
            part_cards = '\n'.join(cards[n - 1] for n in nums)
            inner.append(f'<section class="part-section" id="sec-{sec["num"]}-{part}">'
                         f'<div class="part-header"><div class="part-kicker">{sec["emoji"]} {sec["name"]}</div>'
                         f'<h2 class="part-title">{sec["emoji"]} {PART_NAMES[part]} · Q{lo}–Q{hi}</h2>'
                         f'<p class="part-subtitle">{sec["desc"]}</p></div>{part_cards}</section>')
        sec_html.append(f'<div class="syllabus-block" id="syllabus-{sec["num"]}">'
                        f'<div class="syllabus-banner"><span>{sec["emoji"]}</span>'
                        f'<h2>{sec["name"]}</h2><span class="pill">{sec["weight"]} of exam</span></div>'
                        + ''.join(inner) + '</div>')

    body = f"""
<body>
<button class="sidebar-toggle" id="sidebar-toggle" onclick="document.getElementById('topic-sidebar').classList.toggle('open');this.classList.toggle('shifted')" title="Topic Navigation">☰</button>
<nav class="topic-sidebar" id="topic-sidebar">
  {build_sidebar()}
</nav>

<div class="sticky-command-bar"><div class="command-bar-inner">
  <div class="brand-badge"><span>ACCA TX-UK</span><span class="pill">FA2025 FULL</span></div>
  <div class="progress-container">
    <div style="display:flex;justify-content:space-between;font-family:var(--font-mono);font-size:.7rem;color:var(--ink-soft)"><span>PROGRESS</span><span id="hud-pct">0%</span></div>
    <div class="progress-bar-bg"><div class="progress-bar-fill" id="hud-fill"></div></div>
  </div>
  <div class="hud-metrics">
    <div class="hud-item"><span class="hud-label">RANK</span><span class="hud-value" id="hud-rank">🎓 Cadet</span></div>
    <div class="hud-item"><span class="hud-label">XP</span><span class="hud-value" id="hud-xp">0 XP</span></div>
    <div style="display:flex;gap:.5rem;align-items:center">
      <button class="quickfire-btn" onclick="QUICK_FIRE.start()">⚡ Quick Fire</button>
      <button class="hud-btn-sm" onclick="EXAM_SIM.start()">⏱ Mock 25</button>
      <button class="hud-btn-sm" onclick="FLASHCARDS.open()" title="Spaced-repetition flashcards (F)">📇 Cards</button>
      <button class="hud-btn-sm" onclick="DARK.toggle()" id="dark-btn" title="Toggle dark mode (D)">🌙</button>
      <button class="hud-btn-sm" onclick="KEYS.open()" title="Keyboard shortcuts (Ctrl+/)">⌨️</button>
      <button class="hud-btn-sm" onclick="window.print()">🖨</button>
    </div>
  </div>
</div></div>

<div class="container">
<section class="part-section" id="cover" style="text-align:center;padding:3rem 0">
  <div class="part-kicker" style="margin:0 auto">OFFICIAL EXAM KIT · COMPLETE QUESTION BANK</div>
  <h1 style="font-size:3rem;color:var(--green-deep);margin:1rem 0">ACCA TX-UK (FA2025)<br><span style="font-size:1.8rem">Full Revision Pack — All {len(questions)} Questions</span></h1>
  <p class="part-subtitle">Finance Act 2025 · June 2026 – June 2027 sittings · Source: Kaplan TX-UK Exam Kit (684 pages)</p>
  <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;margin-top:1.5rem">
    <span class="chip chip-xp">{sum(1 for q in questions if q['subtype']=='mcq')} Interactive MCQs</span>
    <span class="chip chip-type">{sum(1 for q in questions if q['part']=='B')} Section B Cases</span>
    <span class="chip chip-xp">{sum(1 for q in questions if q['part']=='C')} Section C Questions</span>
    <span class="chip chip-type">✓ Instant feedback</span>
  </div>
</section>

{build_dashboard(q_by_num)}
{build_rates_table()}

<section class="part-section" id="howto">
  <div class="part-header"><div class="part-kicker">GUIDE</div><h2 class="part-title">🎯 How to Use This Full Pack</h2></div>
  <div class="card" style="padding:1.2rem">
    <p>• <strong>Work through the sections</strong> in exam order (Income Tax → CGT → IHT → CT → VAT) or jump straight to a topic via the ☰ sidebar.</p>
    <p>• <strong>Answer each question</strong> — select an option (or type a number, or click the ✓ cells for tick-box tables). You get instant green/red feedback and the worked solution auto-reveals.</p>
    <p>• <strong>Multi-answer questions</strong> ("Which TWO...") use checkboxes — select all correct options.</p>
    <p>• <strong>Examiner's reports & tutor tips</strong> appear inside each solution — these are exactly what ACCA markers look for.</p>
    <p>• Use <strong>⚡ Quick Fire</strong> for a 20-question random warm-up, or <strong>⏱ Mock 25</strong> for a timed 25-question Section A simulation.</p>
    <p>• Progress is saved automatically in your browser (localStorage). Use 🖨 to print or save as PDF.</p>
  </div>
</section>

{''.join(sec_html)}

<section class="part-section" id="finale" style="text-align:center;padding:3rem 0">
  <h2 class="part-title">🏆 You've reached the end of the full question bank</h2>
  <p class="part-subtitle">All {len(questions)} questions from the TX-UK FA2025 Exam Kit · Worked solutions · Examiner reports · Tutor tips</p>
  <button class="quickfire-btn" onclick="QUICK_FIRE.start()" style="margin-top:1rem">⚡ Final Quick Fire Challenge</button>
</section>
</div>

<div class="streak-badge" id="streak-badge" style="display:none"></div>
<div class="qf-modal-overlay" id="qf-modal"><div class="qf-modal">
  <button class="qf-close" onclick="QUICK_FIRE.close()">✕</button>
  <h2 style="color:var(--green-deep);margin-bottom:1rem">⚡ Quick Fire Quiz</h2>
  <div id="qf-content"></div>
</div></div>
<div class="qf-modal-overlay" id="sim-modal"><div class="qf-modal">
  <button class="qf-close" onclick="EXAM_SIM.close()">✕</button>
  <h2 style="color:var(--green-deep);margin-bottom:1rem">⏱ Timed Mock — Section A (25 questions)</h2>
  <div id="sim-content"></div>
</div></div>
<div class="qf-modal-overlay" id="fc-modal"><div class="qf-modal">
  <button class="qf-close" onclick="FLASHCARDS.close()">✕</button>
  <h2 style="color:var(--green-deep);margin-bottom:1rem">📇 Flashcards — spaced repetition</h2>
  <div class="fc-counter" id="fc-counter"></div>
  <div id="fc-content"></div>
  <div class="fc-actions" id="fc-actions"></div>
</div></div>
<div class="qf-modal-overlay" id="keys-modal"><div class="qf-modal" style="max-width:520px">
  <button class="qf-close" onclick="KEYS.close()">✕</button>
  <h2 style="color:var(--green-deep);margin-bottom:.4rem">⌨️ Keyboard Shortcuts</h2>
  <div class="sc-grid">
    <div><kbd>Ctrl</kbd>+<kbd>/</kbd> or <kbd>?</kbd><span>This help</span></div>
    <div><kbd>Ctrl</kbd>+<kbd>F</kbd> or <kbd>/</kbd><span>Search questions</span></div>
    <div><kbd>D</kbd><span>Toggle dark mode</span></div>
    <div><kbd>Q</kbd><span>Quick Fire quiz</span></div>
    <div><kbd>M</kbd><span>Timed mock</span></div>
    <div><kbd>F</kbd><span>Flashcards</span></div>
    <div><kbd>Esc</kbd><span>Close overlays</span></div>
    <div><kbd>Ctrl</kbd>+<kbd>P</kbd><span>Print / PDF</span></div>
  </div>
</div></div>
</body>
"""

    # Reuse the original pack's design system (extracted from its <style> block)
    with open('TX-UK_Revision_Pack.html', encoding='utf-8') as _f:
        _old = _f.read()
    _s0 = _old.find('<style>')
    _s1 = _old.find('</style>')
    css = _old[_s0 + 7:_s1] if _s0 != -1 and _s1 != -1 else ''
    if not css.strip():
        raise RuntimeError('Could not extract design CSS from TX-UK_Revision_Pack.html')

    # extra CSS for the new components
    extra_css = """
.pdf-text { white-space: pre-wrap; line-height: 1.65; }
.pdf-text.mono { font-family: var(--font-mono); font-size: 0.88rem; white-space: pre-wrap; }
.option-item { display: flex; gap: .5rem; align-items: flex-start; padding: .45rem .6rem; border: 1px solid var(--line); border-radius: 8px; margin: .3rem 0; cursor: pointer; transition: background .15s; }
.option-item:hover { background: var(--paper-deep); }
.option-item.correct { background: var(--green-pale); border-color: var(--green-bright); }
.option-item.incorrect { background: var(--red-pale); border-color: var(--red); }
.option-item.reveal-correct { outline: 2px solid var(--green-bright); }
.opt-letter { font-family: var(--font-mono); font-weight: 700; color: var(--green-deep); }
.multi-hint { font-size: .85rem; color: var(--gold); margin: .6rem 0; }
.tick-table td, .tick-table th { text-align: center; }
.tick-row-label { text-align: left !important; font-size: .85rem; }
.tick-cell { min-width: 3.2rem; height: 2rem; cursor: pointer; font-weight: 700; color: var(--green-bright); user-select: none; }
.tick-cell:hover { background: var(--green-pale); }
.tick-cell.marked { background: var(--green-pale); }
.tick-cell.correct { background: var(--green-pale); color: var(--green-bright); }
.tick-cell.incorrect { background: var(--red-pale); color: var(--red); }
.tick-cell.reveal-correct { outline: 2px solid var(--green-bright); }
.fill-row { display: flex; gap: .6rem; align-items: center; margin: .8rem 0; flex-wrap: wrap; }
.fill-input { font-family: var(--font-mono); padding: .45rem .7rem; border: 1px solid var(--line-strong); border-radius: 8px; font-size: 1rem; min-width: 240px; background: var(--card); }
.fill-input.correct { border-color: var(--green-bright); background: var(--green-pale); }
.fill-input.incorrect { border-color: var(--red); background: var(--red-pale); }
.answer-key-line { background: var(--green-pale); border-left: 4px solid var(--green-bright); padding: .6rem .9rem; border-radius: 0 8px 8px 0; margin-bottom: .8rem; font-size: 1.02rem; }
.case-scenario { background: var(--blue-pale); border: 1px solid #b9cde6; border-left: 4px solid var(--blue); border-radius: 8px; padding: .9rem 1.1rem; margin-bottom: 1rem; }
.case-scenario-title { font-weight: 700; color: var(--blue); margin-bottom: .4rem; letter-spacing: .03em; }
.sub-question { border-top: 1px dashed var(--line-strong); margin-top: .8rem; padding-top: .8rem; }
.sub-q-label { display: inline-block; font-family: var(--font-mono); font-size: .72rem; font-weight: 700; color: var(--blue); background: var(--blue-pale); border-radius: 20px; padding: .15rem .6rem; margin-bottom: .4rem; }
.constructed-note { background: var(--gold-pale); border-left: 4px solid var(--gold); border-radius: 0 8px 8px 0; padding: .7rem 1rem; margin: .8rem 0; font-size: .92rem; }
.dash-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: .8rem; margin: 1rem 0; }
.dash-sec { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: .9rem; text-align: center; }
.dash-sec span { display: block; font-weight: 700; }
.dash-sec strong { font-size: 1.6rem; color: var(--green-deep); display: block; }
.dash-sec small { color: var(--ink-faint); }
.dash-progress { margin: .6rem 0 1rem; }
.dash-label { font-family: var(--font-mono); font-size: .8rem; color: var(--ink-soft); }
.search-row { display: flex; gap: .6rem; margin: 1rem 0 .4rem; flex-wrap: wrap; }
.search-input { flex: 1; min-width: 220px; font-family: var(--font-body); padding: .5rem .8rem; border: 1px solid var(--line-strong); border-radius: 8px; font-size: 1rem; }
.syllabus-banner { display: flex; align-items: center; gap: .8rem; background: linear-gradient(90deg, var(--green-deep), var(--green)); color: #fff; border-radius: 12px; padding: 1rem 1.3rem; margin: 2.2rem 0 1.2rem; }
.syllabus-banner h2 { font-size: 1.35rem; margin: 0; }
.syllabus-banner .pill { background: rgba(255,255,255,.18); color: #fff; }
.qf-q { font-size: 1.05rem; color: var(--ink); margin: .8rem 0; line-height: 1.5; }
.qf-opt.correct { background: var(--green-pale) !important; border: 1px solid var(--green-bright) !important; color: var(--green-deep) !important; }
.qf-opt.incorrect { background: var(--red-pale) !important; border: 1px solid var(--red) !important; color: var(--red) !important; }
/* modal visibility (JS uses .show) */
.qf-modal-overlay.show { display: flex; }

/* ── Dark mode (token remap) ── */
html[data-theme="dark"] {
  --ink: #e6efe9;
  --ink-soft: #b9c9c0;
  --ink-faint: #8aa296;
  --paper: #0e1a15;
  --paper-deep: #15241d;
  --card: #17261f;
  --line: #2c4036;
  --line-strong: #3d574b;
  --green: #4cd08a;
  --green-deep: #7fe3ad;
  --green-bright: #34b875;
  --green-pale: #143427;
  --gold: #e0b04a;
  --gold-bright: #eec257;
  --gold-pale: #3a2f15;
  --red: #ef6b60;
  --red-pale: #3d1f1c;
  --blue: #7fb0e8;
  --blue-pale: #1c2f47;
  --violet: #b49ce0;
  --violet-pale: #2f2644;
  --shadow-sm: 0 1px 3px rgba(0,0,0,.45);
  --shadow-md: 0 4px 12px rgba(0,0,0,.45);
  --shadow-lg: 0 12px 28px rgba(0,0,0,.55);
}
html[data-theme="dark"] .case-scenario { border-color: #2c4568; }
html[data-theme="dark"] .answer-key-line { background: #143427; }
html[data-theme="dark"] .syllabus-banner { background: linear-gradient(90deg, #0b2a20, #145236); }

/* ── Flashcards ── */
.flashcard-wrapper { perspective: 1000px; min-height: 260px; margin-bottom: 1rem; }
.flashcard-inner { position: relative; width: 100%; height: 100%; min-height: 260px; transition: transform .5s cubic-bezier(.4,0,.2,1); transform-style: preserve-3d; }
.flashcard-wrapper.flipped .flashcard-inner { transform: rotateY(180deg); }
.flashcard-front, .flashcard-back { position: absolute; inset: 0; backface-visibility: hidden; border-radius: 12px; padding: 1.3rem; display: flex; flex-direction: column; justify-content: center; align-items: center; border: 2px solid var(--green-bright); box-sizing: border-box; overflow: auto; text-align: left; }
.flashcard-front { background: var(--card); color: var(--ink); font-size: .95rem; }
.flashcard-back { background: var(--green-pale); color: var(--green-deep); transform: rotateY(180deg); font-family: var(--font-mono); font-size: .88rem; }
.flashcard-opt { font-size: .85rem; margin: .15rem 0; }
.fc-actions { display: flex; gap: .6rem; justify-content: center; margin-top: .8rem; flex-wrap: wrap; }
.fc-counter { font-family: var(--font-mono); font-size: .75rem; color: var(--ink-faint); text-align: center; margin-bottom: .5rem; }

/* ── Shortcuts overlay ── */
.sc-grid { display: grid; grid-template-columns: 1fr 1fr; gap: .5rem 1.5rem; margin-top: .8rem; }
.sc-grid kbd { font-family: var(--font-mono); background: var(--paper-deep); border: 1px solid var(--line-strong); border-radius: 4px; padding: .1rem .4rem; font-size: .78rem; }
.sc-grid div { display: flex; justify-content: space-between; gap: .8rem; font-size: .88rem; }

@media print { .sidebar-toggle, .topic-sidebar, .sticky-command-bar, .solution-toggle-btn, .mark-done-check, .quickfire-btn, .search-row { display: none !important; } .solution-content { display: block !important; } .drill-card { break-inside: avoid; } }
"""
    full_css = css + extra_css

    js = build_js(q_by_num, a_by_num, tick_grids)

    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ACCA TX-UK (FA2025) — FULL Revision Pack · All 306 Questions</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,300..800&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
{full_css}
</style>
<script>
{js}
</script>
</head>
{body}
</html>
"""
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(doc)
    print(f"Wrote {OUT}: {len(doc):,} chars")


if __name__ == '__main__':
    main()
