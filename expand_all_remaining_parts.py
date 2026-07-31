import sys, re

def expand_all():
    with open('TX-UK_Revision_Pack.html', 'r', encoding='utf-8') as f:
        text = f.read()

    # Define rich expansions for all remaining short parts

    p35 = """<!-- ═══ PART 35/100 · SECTION C MASTERCLASS Q108–Q110 ═══ -->
<section class="part-section" id="part-35">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 35: Section C Masterclass — Q108 Idris, Q109 Ethel & Q110 Dada (15 Marks Each)</h2>
    <p class="part-subtitle">Sole trader loss relief claims, partnership profit allocations, capital allowance pooling, and terminal loss relief.</p>
  </div>

  <div class="card" id="q108">
    <div class="drill-header">
      <span class="drill-title">Q108 • Idris (15 Marks Constructed Response)</span>
      <div>
        <span class="chip chip-xp">+40 XP</span>
        <span class="chip chip-type">Section C Masterclass</span>
      </div>
    </div>
    <p><strong>Scenario:</strong> Idris incurred a trading loss of £84,000 in year ended 5 April 2026. Prior year profits: 2024/25 £32,000 trading profit, £45,000 employment income. Evaluates current year vs carry-back set-off under s.64.</p>

    <div class="computation-box">
Trading Loss 2025/26:                       (£84,000)

Relief Against Total Income 2024/25:
• Trading Profit 2024/25:                    £32,000 (Relieved 100% cap-free!)
• Employment Income 2024/25:                 £45,000
• Statutory Cap on Non-Trading Income:       Higher of £50,000 or 25% × Total Income (£77,000 × 25% = £19,250) -> Cap = £50,000
• Max Relief Against Non-Trading Income:    (£45,000) (Fully absorbed up to employment income)

Total Loss Relieved in 2024/25 = £32,000 + £45,000 = £77,000
Remaining Unrelieved Loss carried forward = £84,000 - £77,000 = £7,000
    </div>

    <div class="callout callout-examiner">
      <div class="callout-title">🔴 EXAMINER REPORT</div>
      "Candidates frequently forget that trading profits included in total income are exempt from the £50,000 non-trading income cap. Always relieve trading income first before applying the £50k cap to employment/property income!"
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q108" onchange="GAMIFICATION.toggleTask('q108', 40, this.checked)">
        Mark Masterclass Done (+40 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 35/100 ═══ -->"""

    p36 = """<!-- ═══ PART 36/100 · SECTION C MASTERCLASS Q111–Q113 ═══ -->
<section class="part-section" id="part-36">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 36: Section C Masterclass — Q111 Fleur, Q112 Paul & Q113 Na Style (15 Marks Each)</h2>
    <p class="part-subtitle">Property income computations, cash basis vs accruals basis, rent-a-room relief (£7,500 threshold), and lease premium relief.</p>
  </div>

  <div class="card" id="q111">
    <div class="drill-header">
      <span class="drill-title">Q111 • Fleur (15 Marks Constructed Response)</span>
      <div>
        <span class="chip chip-xp">+40 XP</span>
        <span class="chip chip-type">Section C Masterclass</span>
      </div>
    </div>
    <p><strong>Scenario:</strong> Fleur lets out furnished residential property and a spare room in her main residence (Rent-a-room gross rent £9,200, expenses £2,400).</p>

    <div class="computation-box">
Rent-a-Room Relief Options Comparison:

Option 1: Standard Calculation
Gross Rent: £9,200 - Actual Expenses: £2,400 = Taxable Property Income £6,800

Option 2: Rent-a-Room Relief Claim
Gross Rent: £9,200 - Statutory Threshold: (£7,500) = Taxable Property Income £1,700

Fleur should claim Rent-a-Room Relief (saves £5,100 of taxable income)!
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q111" onchange="GAMIFICATION.toggleTask('q111', 40, this.checked)">
        Mark Masterclass Done (+40 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 36/100 ═══ -->"""

    p37 = """<!-- ═══ PART 37/100 · SECTION C MASTERCLASS Q114–Q117 ═══ -->
<section class="part-section" id="part-37">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 37: Section C Masterclass — Q114 Zhi, Q115 Jade, Q116 Hannah & Q117 Alfred & Amaia (15 Marks Each)</h2>
    <p class="part-subtitle">Spousal income splitting, joint property elections (Form 17), marriage allowance transfer (£1,260), and child benefit tax charge.</p>
  </div>

  <div class="card" id="q114">
    <div class="drill-header">
      <span class="drill-title">Q114 • Zhi & Spouse (15 Marks)</span>
      <div>
        <span class="chip chip-xp">+40 XP</span>
        <span class="chip chip-type">Section C Masterclass</span>
      </div>
    </div>
    <p><strong>Scenario:</strong> Jointly owned rental property (actual ownership 80% / 20%). Without election, income is split 50:50 for tax purposes. Evaluates Form 17 election to split based on actual beneficial ownership.</p>

    <div class="computation-box">
Joint Property Income Rules:
• Default Rule: 50:50 income split between married couple / civil partners regardless of legal ownership.
• Form 17 Election: Allows income to be split in accordance with actual beneficial ownership (80:20).
• Beneficial if lower-earning spouse holds 80% share (utilizes PA / basic rate band!).
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q114" onchange="GAMIFICATION.toggleTask('q114', 40, this.checked)">
        Mark Masterclass Done (+40 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 37/100 ═══ -->"""

    p39 = """<!-- ═══ PART 39/100 · SECTION C MASTERCLASS Q122–Q127 ═══ -->
<section class="part-section" id="part-39">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 39: Section C Masterclass — Q122 to Q127 Comprehensive Act 1 Finale</h2>
    <p class="part-subtitle">Multi-topic constructed response scenarios covering employment benefits, trading adjustments, loss set-offs, and complete tax return computations.</p>
  </div>

  <div class="card" id="q122">
    <div class="drill-header">
      <span class="drill-title">Q122 • Sam, Tam & Uma (15 Marks)</span>
      <div>
        <span class="chip chip-xp">+40 XP</span>
        <span class="chip chip-type">Section C Masterclass</span>
      </div>
    </div>
    <div class="computation-box">
Comprehensive Income Tax Pro-Forma Summary:
Non-Savings Income + Savings Income + Dividend Income
Less Personal Allowance Taper (if ANI > £100,000)
Tax at BR (20% / 8.75%), HR (40% / 33.75%), AR (45% / 39.35%)
Add Child Benefit Tax Charge (£60k - £80k)
Less Marriage Allowance Credit (£252)
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q122" onchange="GAMIFICATION.toggleTask('q122', 40, this.checked)">
        Mark Masterclass Done (+40 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 39/100 ═══ -->"""

    p47 = """<!-- ═══ PART 47/100 · DRILLS Q151–Q161 ═══ -->
<section class="part-section" id="part-47">
  <div class="part-header">
    <div class="part-kicker">ACT 2 • DRILL MODULE</div>
    <h2 class="part-title">Part 47: Section A CGT Practice Drills (Q151–Q161)</h2>
    <p class="part-subtitle">Company share pool indexation, corporate rollover relief, and property disposals.</p>
  </div>

  <!-- DRILL Q151 -->
  <div class="drill-card" id="q151">
    <div class="drill-header">
      <span class="drill-title">Q151 • Corporate Rollover Relief</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>A company sold a freehold factory for £400,000 (gain £90,000). Reinvested £380,000 in a new factory within 12 months. What amount of gain can be rolled over?</p>
    <div class="computation-box">
Gross Proceeds: £400,000 | Reinvested: £380,000
Un-reinvested Proceeds = £400,000 - £380,000 = £20,000 (Taxable immediately!)
Gain Rolled Over = Full Gain (£90,000) - Immediate Gain (£20,000) = £70,000
    </div>
    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q151" onchange="GAMIFICATION.toggleTask('q151', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 47/100 ═══ -->"""

    p49 = """<!-- ═══ PART 49/100 · SECTION B CASES Q165–Q167 ═══ -->
<section class="part-section" id="part-49">
  <div class="part-header">
    <div class="part-kicker">ACT 2 • SECTION B OT CASES</div>
    <h2 class="part-title">Part 49: Section B OT Case Studies — Q165 Lily, Q166 Albert & Charles & Q167 Zoyla</h2>
    <p class="part-subtitle">PRR business use restrictions, joint spousal house disposals, and share matching rules.</p>
  </div>

  <!-- CASE Q166 -->
  <div class="card" id="q166">
    <div class="drill-header">
      <span class="drill-title">Q166 • Albert and Victoria (10 Marks Case Study)</span>
      <div>
        <span class="chip chip-xp">+25 XP</span>
        <span class="chip chip-type">Section B Case</span>
      </div>
    </div>
    <p><strong>Scenario:</strong> Albert sold main residence for £840,000 (cost £222,900 in 2010). One-quarter (25%) was used exclusively for business purposes throughout ownership.</p>

    <div class="computation-box">
Gross Gain = £840,000 - £222,900 = £617,100

PRR Relief Analysis:
• 75% Residential Use -> 100% PRR Exempt (£617,100 × 75% = £462,825 Exempt).
• 25% Exclusive Business Use -> NO PRR RELIEF (£617,100 × 25% = £154,275 Chargeable).

Taxable Gain = £154,275 - £3,000 AEA = £151,275
CGT Payable @ 24% (FA2025 rate) = £151,275 × 24% = £36,306
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q166" onchange="GAMIFICATION.toggleTask('q166', 25, this.checked)">
        Mark Case Done (+25 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 49/100 ═══ -->"""

    p51 = """<!-- ═══ PART 51/100 · CGT CASES Q171–Q174 ═══ -->
<section class="part-section" id="part-51">
  <div class="part-header">
    <div class="part-kicker">ACT 2 • SECTION B OT CASES</div>
    <h2 class="part-title">Part 51: Section B OT Case Studies — Q171 Mick Stone, Q172 Expansion, Q173 Kat & Q174 Fogo & Netta</h2>
    <p class="part-subtitle">CGT losses set-off, unquoted share disposals, and spousal transfers.</p>
  </div>

  <div class="card" id="q171">
    <div class="drill-header">
      <span class="drill-title">Q171 • Mick Stone (10 Marks)</span>
      <div>
        <span class="chip chip-xp">+25 XP</span>
        <span class="chip chip-type">Section B Case</span>
      </div>
    </div>
    <p><strong>Scenario:</strong> Mick realized gains £45,000 and current year losses £12,000. Brought forward losses £20,000.</p>
    <div class="computation-box">
Current Year Gains:                             £45,000
Less Current Year Losses (Must use FULLY):     (£12,000)
                                               --------
Net Current Year Gains:                         £33,000
Less Annual Exempt Amount:                      (£3,000)
                                               --------
Gain Needing B/Fwd Loss Relief:                £30,000
Less B/Fwd Losses (Only use £30,000 of £20k? B/fwd loss = £20k -> fully used = £20k!)
Taxable Gain = £30,000 - £20,000 = £10,000
    </div>
    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q171" onchange="GAMIFICATION.toggleTask('q171', 25, this.checked)">
        Mark Case Done (+25 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 51/100 ═══ -->"""

    p53 = """<!-- ═══ PART 53/100 · CGT MASTERCLASS Q178–Q179 ═══ -->
<section class="part-section" id="part-53">
  <div class="part-header">
    <div class="part-kicker">ACT 2 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 53: Section C Masterclass — Q178 Daljeet & Q179 Luna Ltd (10 Marks Each)</h2>
    <p class="part-subtitle">Investors' Relief, corporate share pool disposals, and indexation allowance calculations.</p>
  </div>

  <div class="card" id="q179">
    <div class="drill-header">
      <span class="drill-title">Q179 • Luna Ltd (10 Marks)</span>
      <div>
        <span class="chip chip-xp">+40 XP</span>
        <span class="chip chip-type">Section C Masterclass</span>
      </div>
    </div>
    <div class="computation-box">
Luna Ltd Corporate Share Disposal:
16,000 Pluto plc shares acquired June 2011 for £36,800.
Sold 10,000 shares in May 2013 for £46,200. Indexation factor 0.063.
Sold remaining 6,000 shares in Nov 2025 for £53,400. Indexation factor 0.112 (to Dec 2017).

Indexed Pool Working:
June 2011: 16,000 shares | Cost £36,800 | Indexed Cost £36,800
May 2013 IA (£36,800 × 0.063) = £2,318 -> Total Indexed £39,118
Disposal 10,000 shares (10/16):
- Cost £23,000 | Indexed Cost £24,449 -> Gain = £46,200 - £24,449 = £21,751
Remaining 6,000 shares:
- Cost £13,800 | Indexed Cost £14,669
Dec 2017 IA (£14,669 × 0.112) = £1,643 -> Total Indexed £16,312
Nov 2025 Disposal: Proceeds £53,400 - £16,312 = Chargeable Gain £37,088
    </div>
    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q179" onchange="GAMIFICATION.toggleTask('q179', 40, this.checked)">
        Mark Masterclass Done (+40 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 53/100 ═══ -->"""

    p67 = """<!-- ═══ PART 67/100 · DRILLS Q191–Q201 ═══ -->
<section class="part-section" id="part-67">
  <div class="part-header">
    <div class="part-kicker">ACT 3 • DRILL MODULE</div>
    <h2 class="part-title">Part 67: Section A IHT Practice Drills (Q191–Q201)</h2>
    <p class="part-subtitle">Loss on sale of shares/property, valuation of unquoted shares (related settlements), and liabilities deductible from estate.</p>
  </div>

  <!-- DRILL Q192 -->
  <div class="drill-card" id="q192">
    <div class="drill-header">
      <span class="drill-title">Q192 • Gita's Chargeable Estate</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Gita died 17 May 2025. Assets: House £390k, Chattels £70k, ISA shares £60k. Owed IT £25k. Left £100k to husband, remainder to daughter. What is Gita's chargeable estate?</p>
    <div class="options-group">
      <label class="option-item"><input type="radio" name="q192_opt"> A) £335,000</label>
      <label class="option-item"><input type="radio" name="q192_opt"> B) £395,000</label>
      <label class="option-item"><input type="radio" name="q192_opt"> C) £495,000</label>
      <label class="option-item"><input type="radio" name="q192_opt"> D) £420,000</label>
    </div>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
Gross Assets (House £390k + Chattels £70k + ISA £60k):  £520,000
Less Income Tax Owed:                                   (£25,000)
                                                       ---------
Net Estate Value:                                       £495,000
Less Exempt Legacy to Husband:                         (£100,000)
                                                       ---------
Chargeable Estate (Left to Daughter):                   £395,000
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: B (£395,000)</strong><br>
        ISA shares are included in the death estate (ISAs are exempt from income tax/CGT, but NOT IHT!). Deduct debts owed (£25k) and exempt spouse legacies (£100k).
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q192" onchange="GAMIFICATION.toggleTask('q192', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 67/100 ═══ -->"""

    p75 = """<!-- ═══ PART 75/100 · SECTION B CASES Q254 & Q255 ═══ -->
<section class="part-section" id="part-75">
  <div class="part-header">
    <div class="part-kicker">ACT 4 • SECTION B OT CASES</div>
    <h2 class="part-title">Part 75: Section B OT Case Studies — Q254 Loser Ltd & Q255 Deutsch Ltd</h2>
    <p class="part-subtitle">Corporate trading loss set-offs, group loss surrenders, and associated companies limits.</p>
  </div>

  <!-- CASE Q254 -->
  <div class="card" id="q254">
    <div class="drill-header">
      <span class="drill-title">Q254 • Loser Ltd (10 Marks Case Study)</span>
      <div>
        <span class="chip chip-xp">+25 XP</span>
        <span class="chip chip-type">Section B Case</span>
      </div>
    </div>
    <p><strong>Scenario:</strong> Loser Ltd incurred trading loss £120,000. Profits in preceding AP £80,000. Evaluates s.37 current year vs carry-back set-off.</p>
    <div class="computation-box">
s.37 Loss Relief Set-Off:
Current Year Total Profits:                 £0
12-Month Carry-Back Total Profits:     £80,000
Relieved in Preceding AP:              (£80,000)
                                       --------
Loss Carried Forward (s.45A):           £40,000
    </div>
    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q254" onchange="GAMIFICATION.toggleTask('q254', 25, this.checked)">
        Mark Case Done (+25 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 75/100 ═══ -->"""

    p78 = """<!-- ═══ PART 78/100 · SECTION C MASTERCLASS Q262–Q264 ═══ -->
<section class="part-section" id="part-78">
  <div class="part-header">
    <div class="part-kicker">ACT 4 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 78: Section C Masterclass — Q262 Cop Ltd, Q263 Wretched Ltd & Q264 Crumble Ltd (15 Marks Each)</h2>
    <p class="part-subtitle">Corporate chargeable gains, indexation allowance frozen Dec 2017, and corporate rollover relief.</p>
  </div>

  <div class="card" id="q262">
    <div class="drill-header">
      <span class="drill-title">Q262 • Cop Ltd (15 Marks)</span>
      <div>
        <span class="chip chip-xp">+40 XP</span>
        <span class="chip chip-type">Section C Masterclass</span>
      </div>
    </div>
    <div class="computation-box">
Cop Ltd Chargeable Gain Working:
Freehold Factory Sold: £500,000 | Cost: £200,000 | Indexation to Dec 2017: £40,000
Indexed Gain = £500,000 - (£200,000 + £40,000) = £260,000
Reinvested in new Factory: £480,000 -> Un-reinvested Proceeds = £500k - £480k = £20,000
Rolled Over Gain = £260,000 - £20,000 = £240,000
Immediate Gain Taxed = £20,000
    </div>
    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q262" onchange="GAMIFICATION.toggleTask('q262', 40, this.checked)">
        Mark Masterclass Done (+40 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 78/100 ═══ -->"""

    p84 = """<!-- ═══ PART 84/100 · VAT-04 OVERSEAS, GROUPS & TOGC ═══ -->
<section class="part-section" id="part-84">
  <div class="part-header">
    <div class="part-kicker">ACT 5 • VALUE ADDED TAX</div>
    <h2 class="part-title">Part 84: VAT-04 Overseas VAT, Reverse Charge, VAT Groups & TOGC</h2>
    <p class="part-subtitle">Import VAT vs reverse charge on overseas services, Transfer of Going Concern (TOGC) no supply rule, and VAT groups.</p>
  </div>

  <div class="card">
    <h3>🌐 Overseas Services & Reverse Charge Mechanism</h3>
    <p>1. <strong>Reverse Charge on Imported Services:</strong> When a UK business receives services from an overseas supplier, the UK business accounts for BOTH output VAT and input VAT on its own VAT return (net £0 effect for fully taxable business!).</p>
    <p>2. <strong>Transfer of Going Concern (TOGC):</strong> The sale of a business as a going concern is treated as <strong>NEITHER a supply of goods NOR a supply of services</strong> (0% VAT charged), provided the buyer carries on the same trade and is VAT registered.</p>
  </div>
</section>
<!-- ═══ END PART 84/100 ═══ -->"""

    p88 = """<!-- ═══ PART 88/100 · SECTION B CASES Q296–Q298 ═══ -->
<section class="part-section" id="part-88">
  <div class="part-header">
    <div class="part-kicker">ACT 5 • SECTION B OT CASES</div>
    <h2 class="part-title">Part 88: Section B OT Case Studies — Q296 Alisa, Q297 Whitlock & Q298 Knight</h2>
    <p class="part-subtitle">Historic compulsory registration timing, MTD late penalty points, and error corrections on VAT returns.</p>
  </div>

  <!-- CASE Q296 -->
  <div class="card" id="q296">
    <div class="drill-header">
      <span class="drill-title">Q296 • Alisa (10 Marks Case Study)</span>
      <div>
        <span class="chip chip-xp">+25 XP</span>
        <span class="chip chip-type">Section B Case</span>
      </div>
    </div>
    <p><strong>Scenario:</strong> Alisa started trading 1 Jan 2025. Sales: Jan-Apr £8k/m (£32k), May-Aug £10.5k/m (£42k), Sep-Dec £12k/m (£48k). Evaluates compulsory historic registration test.</p>

    <div class="computation-box">
Rolling 12-Month Sales Threshold (£90,000):
• Jan - Aug (8 months): £32k + £42k = £74,000 (< £90,000)
• Jan - Oct (10 months): £74k + £24k = £98,000 (> £90,000 threshold exceeded in October 2025!).

Notification Deadline = 30 November 2025 (Within 30 days of end of October).
Effective Registration Date = 1 December 2025 (1st day of second month following October).
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q296" onchange="GAMIFICATION.toggleTask('q296', 25, this.checked)">
        Mark Case Done (+25 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 88/100 ═══ -->"""

    # Apply all replacements
    replacements = {
        r'<!-- ═══ PART 35/100 .*?<!-- ═══ END PART 35/100 ═══ -->': p35,
        r'<!-- ═══ PART 36/100 .*?<!-- ═══ END PART 36/100 ═══ -->': p36,
        r'<!-- ═══ PART 37/100 .*?<!-- ═══ END PART 37/100 ═══ -->': p37,
        r'<!-- ═══ PART 39/100 .*?<!-- ═══ END PART 39/100 ═══ -->': p39,
        r'<!-- ═══ PART 47/100 .*?<!-- ═══ END PART 47/100 ═══ -->': p47,
        r'<!-- ═══ PART 49/100 .*?<!-- ═══ END PART 49/100 ═══ -->': p49,
        r'<!-- ═══ PART 51/100 .*?<!-- ═══ END PART 51/100 ═══ -->': p51,
        r'<!-- ═══ PART 53/100 .*?<!-- ═══ END PART 53/100 ═══ -->': p53,
        r'<!-- ═══ PART 67/100 .*?<!-- ═══ END PART 67/100 ═══ -->': p67,
        r'<!-- ═══ PART 75/100 .*?<!-- ═══ END PART 75/100 ═══ -->': p75,
        r'<!-- ═══ PART 78/100 .*?<!-- ═══ END PART 78/100 ═══ -->': p78,
        r'<!-- ═══ PART 84/100 .*?<!-- ═══ END PART 84/100 ═══ -->': p84,
        r'<!-- ═══ PART 88/100 .*?<!-- ═══ END PART 88/100 ═══ -->': p88,
    }

    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text, flags=re.DOTALL)

    with open('TX-UK_Revision_Pack.html', 'w', encoding='utf-8') as f:
        f.write(text)

    print("Expanded all remaining short parts successfully!")

if __name__ == '__main__':
    expand_all()
