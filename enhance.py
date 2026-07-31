#!/usr/bin/env python3
"""Enhance the TX-UK Revision Pack HTML with interactive features."""

import re

with open('TX-UK_Revision_Pack.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. ADD NEW CSS
new_css = """
/* SIDEBAR, QUIZ ENGINE, CONFETTI, STREAKS */
.topic-sidebar{position:fixed;top:60px;left:0;width:260px;height:calc(100vh - 60px);background:rgba(253,253,250,0.97);border-right:2px solid var(--green);overflow-y:auto;z-index:999;padding:1rem 0;transform:translateX(-260px);transition:transform 0.3s ease;box-shadow:4px 0 12px rgba(0,0,0,0.1);font-size:0.85rem}
.topic-sidebar.open{transform:translateX(0)}
.sidebar-toggle{position:fixed;top:70px;left:8px;z-index:1001;background:var(--green);color:var(--paper);border:none;border-radius:6px;padding:0.5rem 0.7rem;cursor:pointer;font-size:1.2rem;transition:all 0.2s;box-shadow:var(--shadow-md)}
.sidebar-toggle:hover{background:var(--green-bright);transform:scale(1.1)}
.sidebar-toggle.shifted{left:268px}
.sidebar-section{padding:0.5rem 1rem;font-family:var(--font-mono);font-weight:700;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.08em;color:var(--gold);border-bottom:1px solid var(--line);margin-top:0.5rem}
.sidebar-link{display:block;padding:0.4rem 1rem 0.4rem 1.5rem;color:var(--ink-soft);text-decoration:none;transition:all 0.15s;border-left:3px solid transparent}
.sidebar-link:hover{background:var(--paper-deep);color:var(--green-deep);border-left-color:var(--green-bright)}
.sidebar-link.completed{color:var(--green-bright);border-left-color:var(--green)}
.sidebar-link.completed::before{content:"✓ ";font-weight:700}
.option-item.correct{background-color:#d4edda!important;border-color:#28a745!important;color:#155724}
.option-item.incorrect{background-color:#f8d7da!important;border-color:#dc3545!important;color:#721c24}
.option-item.reveal-correct{background-color:#d4edda!important;border-color:#28a745!important;border-width:2px}
.streak-badge{position:fixed;top:70px;right:20px;z-index:1001;background:linear-gradient(135deg,#ff6b35,#f7931e);color:white;padding:0.5rem 1rem;border-radius:50px;font-family:var(--font-mono);font-weight:700;font-size:0.9rem;box-shadow:0 4px 15px rgba(255,107,53,0.4);display:flex;align-items:center;gap:0.4rem;animation:streakPulse 2s infinite}
@keyframes streakPulse{0%,100%{transform:scale(1)}50%{transform:scale(1.05)}}
.streak-badge.fire{animation:streakFire 0.5s infinite;background:linear-gradient(135deg,#ff0000,#ff6b35,#ffcc00)}
@keyframes streakFire{0%,100%{transform:scale(1)}50%{transform:scale(1.1)}}
#confetti-canvas{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:9999}
.exam-timer-panel{position:fixed;bottom:20px;right:20px;z-index:1001;background:rgba(8,53,39,0.95);color:white;padding:1.2rem 1.5rem;border-radius:12px;box-shadow:0 8px 25px rgba(0,0,0,0.3);font-family:var(--font-mono);display:none;min-width:220px}
.exam-timer-panel.active{display:block}
.timer-display{font-size:2.2rem;font-weight:700;text-align:center;letter-spacing:0.05em}
.timer-section{font-size:0.75rem;color:rgba(255,255,255,0.7);text-align:center;margin-top:0.3rem}
.timer-controls{display:flex;gap:0.5rem;margin-top:0.8rem}
.timer-controls button{flex:1;padding:0.4rem;border:1px solid rgba(255,255,255,0.3);border-radius:4px;background:transparent;color:white;cursor:pointer;font-family:var(--font-mono);font-size:0.75rem;transition:all 0.2s}
.timer-controls button:hover{background:rgba(255,255,255,0.15)}
.timer-warning{color:#ff6b35;animation:timerBlink 1s infinite}
.timer-critical{color:#ff0000;animation:timerBlink 0.5s infinite}
@keyframes timerBlink{0%,100%{opacity:1}50%{opacity:0.5}}
.qf-modal-overlay{position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.7);z-index:10000;display:none;align-items:center;justify-content:center}
.qf-modal-overlay.active{display:flex}
.qf-modal{background:var(--card);border-radius:12px;padding:2.5rem;max-width:700px;width:90%;max-height:85vh;overflow-y:auto;box-shadow:0 20px 60px rgba(0,0,0,0.4);position:relative}
.qf-close{position:absolute;top:1rem;right:1rem;background:none;border:none;font-size:1.5rem;cursor:pointer;color:var(--ink-soft)}
.qf-progress{display:flex;gap:4px;margin-bottom:1.5rem}
.qf-dot{width:24px;height:6px;border-radius:3px;background:var(--line);transition:background 0.3s}
.qf-dot.correct{background:#28a745}
.qf-dot.incorrect{background:#dc3545}
.qf-dot.current{background:var(--gold-bright)}
.qf-score{font-family:var(--font-display);font-size:3rem;font-weight:800;text-align:center;color:var(--green-deep)}
.badge-notification{position:fixed;top:50%;left:50%;transform:translate(-50%,-50%) scale(0);z-index:10001;background:linear-gradient(135deg,var(--gold-bright),var(--gold));color:white;padding:2rem 3rem;border-radius:16px;text-align:center;font-family:var(--font-display);font-size:1.5rem;font-weight:800;box-shadow:0 20px 50px rgba(168,121,15,0.5);transition:transform 0.5s cubic-bezier(0.175,0.885,0.32,1.275)}
.badge-notification.show{transform:translate(-50%,-50%) scale(1)}
.callout-examiner.real{background:linear-gradient(135deg,#fff5f5,#f7e4e1);border-left-color:#c0392b}
.callout-examiner.real .callout-title{color:#c0392b}
.quickfire-btn{background:linear-gradient(135deg,#ff6b35,#f7931e);color:white;border:none;padding:0.6rem 1.2rem;border-radius:6px;font-family:var(--font-mono);font-weight:700;font-size:0.85rem;cursor:pointer;transition:all 0.2s;box-shadow:0 4px 12px rgba(255,107,53,0.3)}
.quickfire-btn:hover{transform:translateY(-2px);box-shadow:0 6px 18px rgba(255,107,53,0.4)}
.dark-mode-toggle{background:none;border:1px solid var(--line-strong);border-radius:4px;padding:0.3rem 0.5rem;cursor:pointer;font-size:1rem;transition:all 0.2s}
.dark-mode-toggle:hover{background:var(--paper-deep)}
.trap-card{transition:transform 0.15s}
.trap-card:hover{transform:translateY(-1px)}
@media(max-width:768px){.topic-sidebar{width:220px;transform:translateX(-220px)}.sidebar-toggle.shifted{left:228px}.streak-badge{top:auto;bottom:80px;right:10px;font-size:0.8rem}.exam-timer-panel{bottom:10px;right:10px;min-width:180px}.timer-display{font-size:1.6rem}}
"""

html = html.replace('</style>', new_css + '\n</style>')

# 2. ADD ENHANCED JS — read from separate file
with open('enhance_js.js', 'r', encoding='utf-8') as f:
    new_js = f.read()

# Add timer panel and modal to body
html = html.replace('</head>', """
<canvas id="confetti-canvas"></canvas>
<div class="exam-timer-panel" id="exam-timer-panel">
  <div class="timer-section" id="timer-section">Section A</div>
  <div class="timer-display" id="timer-display">54:00</div>
  <div class="timer-controls">
    <button onclick="EXAM_TIMER.pause()">⏸ Pause</button>
    <button onclick="EXAM_TIMER.resume()">▶ Resume</button>
    <button onclick="EXAM_TIMER.stop();document.getElementById('exam-timer-panel').classList.remove('active')">✕ Stop</button>
  </div>
</div>
<div class="qf-modal-overlay" id="qf-modal">
  <div class="qf-modal">
    <button class="qf-close" onclick="QUICK_FIRE.close()">✕</button>
    <h2 style="color:var(--green-deep);margin-bottom:1rem">⚡ Quick Fire Quiz</h2>
    <div id="qf-content"></div>
  </div>
</div>
</head>""")

# Add new script after existing GAMIFICATION script
old_script_end = "GAMIFICATION.init();\n});\n</script>"
new_script_with_enhancements = old_script_end + "\n<script>\n" + new_js + "\n</script>"
html = html.replace(old_script_end, new_script_with_enhancements, 1)

# 3. ADD SIDEBAR
sidebar_html = """
<button class="sidebar-toggle" id="sidebar-toggle" onclick="SIDEBAR.toggle()" title="Topic Navigation (Ctrl+[)">☰</button>
<nav class="topic-sidebar" id="topic-sidebar">
  <div class="sidebar-section">📋 Command Center</div>
  <a class="sidebar-link" href="#cover" data-part="cover">Cover Page</a>
  <a class="sidebar-link" href="#part-4" data-part="part-4">Part 4: Mission Briefing</a>
  <a class="sidebar-link" href="#part-5" data-part="part-5">Part 5: Exam Blueprint</a>
  <a class="sidebar-link" href="#part-6" data-part="part-6">Part 6: Tax Rates Master</a>
  <div class="sidebar-section">🟢 Act 1 — Income Tax & NIC</div>
  <a class="sidebar-link" href="#part-7" data-part="part-7">IT-01 Computation Skeleton</a>
  <a class="sidebar-link" href="#part-8" data-part="part-8">IT-02 Savings & Dividends</a>
  <a class="sidebar-link" href="#part-9" data-part="part-9">IT-03 PA Restriction</a>
  <a class="sidebar-link" href="#part-10" data-part="part-10">IT-04 HICBC & SRT</a>
  <a class="sidebar-link" href="#part-11" data-part="part-11">IT-05 Employment Income</a>
  <a class="sidebar-link" href="#part-12" data-part="part-12">IT-06 Benefits in Kind</a>
  <a class="sidebar-link" href="#part-13" data-part="part-13">IT-07 Trading Adjustments</a>
  <a class="sidebar-link" href="#part-14" data-part="part-14">IT-08 Capital Allowances</a>
  <a class="sidebar-link" href="#part-15" data-part="part-15">IT-09 Trading Losses</a>
  <a class="sidebar-link" href="#part-16" data-part="part-16">IT-10 Partnerships</a>
  <a class="sidebar-link" href="#part-17" data-part="part-17">IT-11 National Insurance</a>
  <a class="sidebar-link" href="#part-18" data-part="part-18">IT-12 Pensions</a>
  <a class="sidebar-link" href="#part-19" data-part="part-19">IT-13 Admin & Ethics</a>
  <div class="sidebar-section">🔵 Act 2 — Chargeable Gains</div>
  <a class="sidebar-link" href="#part-40" data-part="part-40">CGT-01 Basics</a>
  <a class="sidebar-link" href="#part-45" data-part="part-45">CGT Drills Q128+</a>
  <a class="sidebar-link" href="#part-48" data-part="part-48">CGT Section B Cases</a>
  <a class="sidebar-link" href="#part-52" data-part="part-52">CGT Section C</a>
  <div class="sidebar-section">🟣 Act 3 — Inheritance Tax</div>
  <a class="sidebar-link" href="#part-54" data-part="part-54">IHT-01 Transfers</a>
  <a class="sidebar-link" href="#part-55" data-part="part-55">IHT-02 Lifetime Tax</a>
  <a class="sidebar-link" href="#part-56" data-part="part-56">IHT-03 Death Estate</a>
  <a class="sidebar-link" href="#part-58" data-part="part-58">IHT Drills</a>
  <div class="sidebar-section">🟠 Act 4 — Corporation Tax</div>
  <a class="sidebar-link" href="#part-64" data-part="part-64">CT-01 Rates</a>
  <a class="sidebar-link" href="#part-65" data-part="part-65">CT-02 Adjustments</a>
  <a class="sidebar-link" href="#part-66" data-part="part-66">CT-03 Capital Allowances</a>
  <a class="sidebar-link" href="#part-68" data-part="part-68">CT-05 Groups</a>
  <a class="sidebar-link" href="#part-76" data-part="part-76">CT Section C</a>
  <div class="sidebar-section">🔴 Act 5 — VAT</div>
  <a class="sidebar-link" href="#part-81" data-part="part-81">VAT-01 Registration</a>
  <a class="sidebar-link" href="#part-82" data-part="part-82">VAT-02 Output & Input</a>
  <a class="sidebar-link" href="#part-83" data-part="part-83">VAT-03 Special Schemes</a>
  <a class="sidebar-link" href="#part-85" data-part="part-85">VAT Drills</a>
  <div class="sidebar-section">⚫ Finale</div>
  <a class="sidebar-link" href="#part-93" data-part="part-93">Specimen Section A</a>
  <a class="sidebar-link" href="#part-99" data-part="part-99">50 Deadly Traps</a>
  <a class="sidebar-link" href="#part-100" data-part="part-100">🏆 Completion</a>
</nav>
"""
html = html.replace('<body>', '<body>\n' + sidebar_html)

# 4. ADD QUICK FIRE BUTTON TO COMMAND BAR
html = html.replace(
    '</div>\n  </div>\n</div>\n\n<div class="container">',
    """<div style="display:flex;gap:0.5rem;align-items:center">
        <button class="quickfire-btn" onclick="QUICK_FIRE.start()">⚡ Quick Fire</button>
      </div>
    </div>
  </div>
</div>

<div class="container">"""
)

# 5. REPLACE EXAM SIMULATOR
old_exam = '<section id="exam-simulator" class="part-section">'
if old_exam in html:
    # Find and replace the entire exam simulator section
    start = html.index(old_exam)
    end = html.index('</section>', start) + len('</section>')
    # Also remove the old script
    script_start = html.find('<script>window.examTimer', end)
    script_end = html.find('</script>', script_start) + len('</script>')
    html = html[:start] + """<section id="exam-simulator" class="part-section">
  <div class="part-header">
    <div class="part-kicker">ACT 7 • EXAM SIMULATOR</div>
    <h2 class="part-title">⏱ Exam Simulator — 3 Hours / 100 Marks</h2>
    <p class="part-subtitle">Real countdown timer with section warnings. Time management is the #1 predictor of exam success.</p>
  </div>
  <div class="card">
    <h3>🎯 Start Your Timed Practice Session</h3>
    <table class="fiscal-table">
      <thead><tr><th>Section</th><th>Questions</th><th>Marks</th><th>Time</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td><strong>Section A</strong></td><td>15 OTQs × 2</td><td class="num">30</td><td class="num">54 min</td>
          <td><button class="solution-toggle-btn" onclick="EXAM_TIMER.start(54, 'Section A — 15 OTQs')">▶ Start A</button></td></tr>
        <tr><td><strong>Section B</strong></td><td>3 Cases × 5</td><td class="num">30</td><td class="num">54 min</td>
          <td><button class="solution-toggle-btn" onclick="EXAM_TIMER.start(54, 'Section B — 3 Cases')">▶ Start B</button></td></tr>
        <tr><td><strong>Section C</strong></td><td>Q1(10)+Q2(15)+Q3(15)</td><td class="num">40</td><td class="num">72 min</td>
          <td><button class="solution-toggle-btn" onclick="EXAM_TIMER.start(72, 'Section C — Constructed Response')">▶ Start C</button></td></tr>
        <tr style="font-weight:700;background:var(--paper-deep)"><td><strong>FULL EXAM</strong></td><td>All</td><td class="num">100</td><td class="num">180 min</td>
          <td><button class="quickfire-btn" onclick="EXAM_TIMER.start(180, 'Full Exam — 3 Hours')">▶ Start Full Exam</button></td></tr>
      </tbody>
    </table>
    <div class="callout callout-trap">
      <div class="callout-title">⚠️ TIME MANAGEMENT RULES</div>
      <p>• <strong>1.8 minutes per mark</strong> — never spend more than 3.6 min on a 2-mark OTQ.</p>
      <p>• <strong>Section C:</strong> Max 18 min on 10-mark Q, 27 min on 15-mark Q.</p>
    </div>
    <div class="callout callout-examiner real">
      <div class="callout-title">🔴 EXAMINER REPORT — Time Management (PDF p.321)</div>
      <p>"Quite a few candidates failed to achieve fairly easy marks due to poor examination technique and/or not reading the question carefully enough. Many candidates had a lot more workings than necessary, which would have taken more time."</p>
    </div>
  </div>
</section>""" + html[script_end:]

# 6. REPLACE REPETITIVE EXAMINER CALLOUTS
examiner_map = {
    'BATCH EXAMINER FEEDBACK — Part 11': ('Employment Income (PDF p.309)',
     '<p><strong>Examiner (p.309):</strong> "The income tax question involved Jason, employed by Initial plc but considering taking up an offer with Subsequent plc. Part (a) required candidates to state one advantage and one disadvantage for an employee if their employer payrolled the taxable benefits. This section was not particularly well answered."</p><p><strong>Common trap:</strong> Not comparing total employment income between two employers — include ALL benefits (car, fuel, loan, gym) and check PA taper for each option!</p>'),
    'BATCH EXAMINER FEEDBACK — Part 12': ('Car & Accommodation Benefits (PDF p.268)',
     '<p><strong>Examiner (p.268):</strong> "Note that regardless of the market value, an additional benefit for expensive accommodation is only charged if the original cost plus improvements exceeds £75,000."</p><p><strong>Common trap:</strong> Forgetting to time-apportion car benefits when provided part-way through the tax year, and incorrectly applying the 4% diesel surcharge to RDE2-compliant cars.</p>'),
    'BATCH EXAMINER FEEDBACK — Part 13': ('Lease Premiums (PDF p.266)',
     '<p><strong>Examiner (p.266):</strong> "The premium received is on a short lease therefore a proportion of it is treated as income. Option (D) — This does not deduct one year from n, the number of years on the lease."</p><p><strong>Common trap:</strong> Using N instead of (N-1) in the lease premium formula Premium × [51-(N-1)]/50!</p>'),
    'BATCH EXAMINER FEEDBACK — Part 14': ('Capital Allowances on Cars (PDF p.273)',
     '<p><strong>Examiner (p.273):</strong> "This question required students to demonstrate their knowledge of capital allowances on cars, where there was a disposal of a car during the year which was also used for private use. Candidates need to recognise that a balancing allowance arose on its disposal, restricted to the business use element (60%)."</p><p><strong>Common trap:</strong> Cars with private use go into their own single asset pool — on disposal a balancing charge/allowance arises!</p>'),
    'BATCH EXAMINER FEEDBACK — Part 15': ('Loss Relief Deadlines (PDF p.280)',
     '<p><strong>Examiner (p.280):</strong> "This question examines knowledge of the deadline for an individual taxpayer to claim relief for a trading loss. The correct answer is 31 January 2028 — a claim must be made within one year of 31 January following the end of the tax year in which the loss arose."</p><p><strong>Common trap:</strong> Confusing the loss relief claim deadline with the SA return filing deadline!</p>'),
    'BATCH EXAMINER FEEDBACK — Part 16': ('Partnerships (PDF p.276)',
     '<p><strong>Examiner (p.276):</strong> Partnership profit allocation must be time-apportioned when the PSR changes during the accounting period. Split the year into sub-periods, calculate each partner\'s share separately for each sub-period.</p><p><strong>Common trap:</strong> Not splitting the year into sub-periods when salaries or PSR change!</p>'),
    'BATCH EXAMINER FEEDBACK — Part 17': ('NIC (PDF p.281)',
     '<p><strong>Examiner (p.281):</strong> Class 1 employee NIC at 8% applies between £12,571 and £50,270. Class 4 NIC at 6% applies on the same band for trading profits. Remember: pension contributions do NOT reduce trading profit for Class 4 NIC!</p><p><strong>Common trap:</strong> Deducting pension contributions from trading profit before calculating Class 4 NIC!</p>'),
    'BATCH EXAMINER FEEDBACK — Part 18': ('Pension Annual Allowance (PDF p.287)',
     '<p><strong>Examiner (p.287):</strong> "The annual allowance of £60,000 is reduced by £1 for every £2 by which the individual\'s adjusted income exceeds £260,000, subject to a minimum of £10,000. A number of candidates selected £25,000, which is the annual allowance, rather than the annual allowance charge."</p><p><strong>Common trap:</strong> Confusing the tapered AA with the AA charge!</p>'),
    'BATCH EXAMINER FEEDBACK — Part 19': ('SA Deadlines (PDF p.291)',
     '<p><strong>Examiner (p.291):</strong> "The correct answer is B — 30 April 2027, because the return was filed late and this is the first quarter day after the anniversary of the submission. Taxpayers with a business must keep their records until 5 years after the 31 January filing date."</p><p><strong>Common trap:</strong> Confusing the SA amendment deadline with the HMRC enquiry window!</p>'),
    'BATCH EXAMINER FEEDBACK — Part 20': ('PA & Transferable Allowance (PDF p.260)',
     '<p><strong>Examiner (p.260):</strong> "Statement B is incorrect. It is not possible for Zara to claim the transferable personal allowance from Dane, as she is a higher rate taxpayer. Neither spouse/civil partner can be a higher or additional rate taxpayer. Statement C is also incorrect — a joint property election would INCREASE Zara\'s tax liability."</p><p><strong>Common trap:</strong> Transferable PA requires BOTH spouses to be basic rate taxpayers!</p>'),
    'BATCH EXAMINER FEEDBACK — Part 21': ('Qualifying Interest (PDF p.262)',
     '<p><strong>Examiner (p.262):</strong> Relief is given for interest paid on loans for qualifying purposes: acquisition of plant/machinery by an employed person for use in employment; purchase of shares in an employee-controlled trading company; purchase of a share in a partnership.</p><p><strong>Common trap:</strong> Mortgage interest on main residence is NOT qualifying. Interest on shares in QUOTED companies is NOT qualifying!</p>'),
    'BATCH EXAMINER FEEDBACK — Part 22': ('Car & Accommodation Benefits (PDF p.268)',
     '<p><strong>Examiner (p.268):</strong> For living accommodation, the property is not considered expensive if the original cost did not exceed £75,000. If the employee contributes more than the annual value, the taxable benefit is £0.</p><p><strong>Common trap:</strong> Forgetting the £75,000 threshold for expensive accommodation!</p>'),
    'BATCH EXAMINER FEEDBACK — Part 23': ('Capital Allowances on Cars (PDF p.273)',
     '<p><strong>Examiner (p.273):</strong> "Candidates are reminded that cars which are used partly for private use by a sole trader are put into their own pool and on disposal a balancing charge or allowance may arise."</p><p><strong>Common trap:</strong> AIA on motor cars? NO — cars are EXCLUDED from AIA!</p>'),
    'BATCH EXAMINER FEEDBACK — Part 24': ('Loss Relief Claims (PDF p.280)',
     '<p><strong>Examiner (p.280):</strong> "A significant number of candidates chose each of the other answer options, suggesting that many candidates were not well prepared for a question on this topic."</p><p><strong>Common trap:</strong> Not knowing the loss relief claim deadline — 1 year from 31 Jan following the tax year of the loss!</p>'),
    'BATCH EXAMINER FEEDBACK — Part 25': ('Tapered Annual Allowance (PDF p.287)',
     '<p><strong>Examiner (p.287):</strong> "The annual allowance of £60,000 is reduced by £1 for every £2 by which the individual\'s adjusted income exceeds £260,000, subject to a minimum annual allowance of £10,000."</p><p><strong>Common trap:</strong> Confusing the ANNUAL ALLOWANCE with the ANNUAL ALLOWANCE CHARGE!</p>'),
    'BATCH EXAMINER FEEDBACK — Part 26': ('SA Penalties (PDF p.293)',
     '<p><strong>Examiner (p.293):</strong> "The incorrect options: A — £100 being the initial penalty only. B — £1,000 being the initial penalty of £100 plus maximum daily penalties of £10 × 90. D — £1,300 being the initial penalty plus daily penalties plus minimum tax-geared penalty."</p><p><strong>Common trap:</strong> Not knowing the penalty structure: initial £100, then daily £10 for up to 90 days, then tax-geared 5%/10%/100%.</p>'),
    'BATCH EXAMINER FEEDBACK — Part 45': ('CGT Chattels (PDF p.419)',
     '<p><strong>Examiner (p.419):</strong> "A chattel is tangible, moveable property. A wasting chattel has a predictable life of 50 years or less and is generally exempt from CGT. The motor boat is a wasting chattel — exempt. Shares in an unquoted company are not exempt. Antique jewellery is a non-wasting chattel — only exempt if both proceeds and cost are less than £6,000."</p><p><strong>Common trap:</strong> Only WASTING chattels (life ≤50 years) are exempt. Non-wasting chattels are chargeable if proceeds exceed £6,000.</p>'),
    'BATCH EXAMINER FEEDBACK — Part 46': ('Rollover & Insurance Relief (PDF p.425)',
     '<p><strong>Examiner (p.425):</strong> "The incorrect answers are: A — £64,000 being the reinvested amount less the whole gain. C — £57,000 being the amount reinvested less the gain immediately chargeable. D — £64,000 being the purchase price of the replacement warehouse."</p><p><strong>Common trap:</strong> Rollover relief is restricted by the amount of proceeds NOT reinvested!</p>'),
    'BATCH EXAMINER FEEDBACK — Part 47': ('CGT BADR (PDF p.441)',
     '<p><strong>Examiner (p.441):</strong> To qualify for BADR, the company must be trading and the individual must own 5%+ of the shares, work for the company, and satisfy the 2-year ownership period. Lifetime limit is £1,000,000.</p><p><strong>Common trap:</strong> Apply AEA (£3,000) against higher-rate gains (24%) first, NOT against BADR gains (14%)!</p>'),
    'BATCH EXAMINER FEEDBACK — Part 48': ('CGT Section B Cases (PDF p.469)',
     '<p><strong>Examiner (p.469):</strong> "Although there were some very good answers, it caused problems for many and was often the reason they failed to achieve a pass mark. The jointly owned property caused particular difficulty. Only a few candidates correctly calculated the private residence relief."</p><p><strong>Common trap:</strong> Not allocating the chargeable gain between joint owners before applying AEA!</p>'),
    'BATCH EXAMINER FEEDBACK — Part 50': ('CGT & IHT Cross-topic (PDF p.514)',
     '<p><strong>Examiner (p.514):</strong> "As is typical for the 10-mark question, different taxes were covered — IHT and CGT. The question revolved around three residential properties. It was important for candidates to sort out which information related to which requirement."</p><p><strong>Common trap:</strong> PRR applies to CGT, not IHT. Spouse exemption applies to IHT, not CGT!</p>'),
    'BATCH EXAMINER FEEDBACK — Part 52': ('CGT & VAT (PDF p.558)',
     '<p><strong>Examiner (p.558):</strong> "Harbour Ltd is going to prepare accounts for a four-month period. Candidates should take a note that this is going to impact on the lease premium deduction, capital allowances and property business income."</p><p><strong>Common trap:</strong> Time-apportion AIA for short accounting periods, but 50% Special Rate FYA is NOT time-apportioned!</p>'),
}

for old_prefix, (new_title, new_content) in examiner_map.items():
    pattern = r'(callout-title[^>]*>' + re.escape(old_prefix) + r'[^<]*</div>\s*<p><strong>Examiner reports.*?</p>\s*<p><strong>Common.*?</p>)'
    match = re.search(pattern, html, re.DOTALL)
    if match:
        replacement = f'callout-title">{new_title}</div>\n    {new_content}'
        html = html[:match.start()] + replacement + html[match.end():]

# 7. REPLACE STATIC GAMIFICATION HUB
old_gam_start = '<section class="part-section" id="gamification-hub">'
if old_gam_start in html:
    start = html.index(old_gam_start)
    end = html.index('</section>', start) + len('</section>')
    # Read the new gamification hub from file
    with open('enhance_gamification.html', 'r', encoding='utf-8') as f:
        new_gam = f.read()
    html = html[:start] + new_gam + html[end:]

# WRITE
with open('TX-UK_Revision_Pack.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Enhanced HTML written. Size: {len(html)} chars")
