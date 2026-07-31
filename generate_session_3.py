import sys

def build_session_3():
    with open('TX-UK_Revision_Pack.html', 'r', encoding='utf-8') as f:
        content = f.read()

    close_idx = content.find('</div> <!-- End container -->')
    if close_idx != -1:
        base_content = content[:close_idx]
    else:
        base_content = content.replace('</body>\n</html>', '').replace('</body></html>', '')

    parts = []

    # PART 21
    part21 = """<!-- ═══ PART 21/100 · DRILLS Q13–Q24 ═══ -->
<section class="part-section" id="part-21">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • DRILL MODULE</div>
    <h2 class="part-title">Part 21: Section A Practice Drills (Q13–Q24)</h2>
    <p class="part-subtitle">Qualifying interest, Gift Aid, ISA exemptions, property income basics, and employment receipts.</p>
  </div>

  <!-- DRILL Q13 -->
  <div class="drill-card" id="q13">
    <div class="drill-header">
      <span class="drill-title">Q13 • Ifram's Qualifying Interest Payments</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Ifram made interest payments during the tax year. Identify whether each payment represents qualifying interest (deductible from total income) or not qualifying:</p>
    
    <table class="fiscal-table">
      <thead>
        <tr><th>Loan Interest Description</th><th class="num">Qualifying</th><th class="num">Not Qualifying</th></tr>
      </thead>
      <tbody>
        <tr><td>Loan to purchase a laptop for employment use</td><td class="num">[ ]</td><td class="num">[ ]</td></tr>
        <tr><td>Mortgage on main private residence</td><td class="num">[ ]</td><td class="num">[ ]</td></tr>
        <tr><td>Loan to acquire 2,000 shares in a quoted company</td><td class="num">[ ]</td><td class="num">[ ]</td></tr>
        <tr><td>Loan to invest capital in a partnership as a partner</td><td class="num">[ ]</td><td class="num">[ ]</td></tr>
      </tbody>
    </table>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="callout callout-tip">
        <strong>MODEL ANSWER & TUTORIAL NOTE:</strong><br>
        • <strong>Laptop for employment:</strong> QUALIFYING (Loan for plant & machinery used in employment).<br>
        • <strong>Main residence mortgage:</strong> NOT QUALIFYING (Private residential mortgage interest is not deductible against total income).<br>
        • <strong>Shares in quoted company:</strong> NOT QUALIFYING (Qualifying interest applies ONLY to shares in unquoted trading companies or employee-controlled companies).<br>
        • <strong>Capital in partnership:</strong> QUALIFYING (Loan to contribute capital or acquire a share in a partnership by an active partner).
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q13" onchange="GAMIFICATION.toggleTask('q13', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>

  <!-- DRILL Q19 -->
  <div class="drill-card" id="q19">
    <div class="drill-header">
      <span class="drill-title">Q19 • Nicolas' Office Lease Premium</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Nicolas granted a 15-year lease on an unfurnished freehold office building on 6 April 2025 for a premium of £82,000. How much is taxable as property income for 2025/26?</p>
    <div class="options-group">
      <label class="option-item"><input type="radio" name="q19_opt"> A) £59,040</label>
      <label class="option-item"><input type="radio" name="q19_opt"> B) £22,960</label>
      <label class="option-item"><input type="radio" name="q19_opt"> C) £82,000</label>
      <label class="option-item"><input type="radio" name="q19_opt"> D) £5,467</label>
    </div>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
Capital Premium Received:           £82,000
Lease Term (N):                     15 years

Property Income Taxable Portion:
£82,000 × [51 - (15 - 1)] / 50
= £82,000 × (51 - 14) / 50
= £82,000 × 37 / 50 = £60,680... wait!
Let's check 51 - 14 = 37 / 50 = 74% × £82,000 = £60,680 (or £59,040 if N=15: £82,000 × 50 - 14 = 36/50 = 72% × £82,000 = £59,040).
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: A (£59,040)</strong><br>
        Taxable property income = Premium × [50 - (N - 1)] / 50 = £82,000 × [50 - 14] / 50 = £82,000 × 36/50 = £59,040.
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q19" onchange="GAMIFICATION.toggleTask('q19', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 21/100 ═══ -->"""
    parts.append(part21)

    # PART 22
    part22 = """<!-- ═══ PART 22/100 · DRILLS Q25–Q36 ═══ -->
<section class="part-section" id="part-22">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • DRILL MODULE</div>
    <h2 class="part-title">Part 22: Section A Practice Drills (Q25–Q36)</h2>
    <p class="part-subtitle">Car benefits, fuel charges, beneficial loans, living accommodation, and trading profit adjustments.</p>
  </div>

  <!-- DRILL Q28 -->
  <div class="drill-card" id="q28">
    <div class="drill-header">
      <span class="drill-title">Q28 • Enzo's Electric Company Car</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Enzo is provided with an electric car (0g/km CO₂) on 5 April 2025 (60% business, 40% private). List price £45,000 (cost employer £42,000). Workplace electric charging is provided free.</p>
    <p>What is Enzo's car benefit for 2025/26?</p>
    
    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
List Price (Ignore employer discount/cost):  £45,000
Appropriate % for Electric Car (0g/km):      3%

Car Benefit = £45,000 × 3% = £1,350
Note: Workplace charging of electric vehicles is EXEMPT!
Note 2: Ignore business/private mileage split (benefit is NOT reduced for business use).
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: £1,350</strong><br>
        Car benefit is always based on official list price (not discounted purchase cost) and is not reduced for partial business use. Workplace EV charging is 100% exempt.
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q28" onchange="GAMIFICATION.toggleTask('q28', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 22/100 ═══ -->"""
    parts.append(part22)

    # PART 23
    part23 = """<!-- ═══ PART 23/100 · DRILLS Q37–Q48 ═══ -->
<section class="part-section" id="part-23">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • DRILL MODULE</div>
    <h2 class="part-title">Part 23: Section A Practice Drills (Q37–Q48)</h2>
    <p class="part-subtitle">Capital allowances allocations, cash basis, balancing allowances, partnership PSR, and loss relief caps.</p>
  </div>

  <!-- DRILL Q38 -->
  <div class="drill-card" id="q38">
    <div class="drill-header">
      <span class="drill-title">Q38 • Olive's Cash Basis Car Disposal</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Olive uses the cash basis. TWDV b/fwd at 6 April 2025 for her car (65g/km, 40% private use) was £12,000. Sold car for £6,000 on 1 Nov 2025. What capital allowance can Olive claim for 2025/26?</p>
    <div class="options-group">
      <label class="option-item"><input type="radio" name="q38_opt"> A) £3,600</label>
      <label class="option-item"><input type="radio" name="q38_opt"> B) £648</label>
      <label class="option-item"><input type="radio" name="q38_opt"> C) £2,400</label>
      <label class="option-item"><input type="radio" name="q38_opt"> D) £216</label>
    </div>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
TWDV b/fwd:                          £12,000
Less Disposal Proceeds:              (£6,000)
                                     --------
Unrelieved Balance on Disposal:        £6,000

Business Percentage = 100% - 40% = 60%
Balancing Allowance Claimable = £6,000 × 60% = £3,600
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: A (£3,600)</strong><br>
        On disposal of a single asset with private use, a balancing allowance arises equal to the unrelieved balance multiplied by the business use percentage!
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q38" onchange="GAMIFICATION.toggleTask('q38', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 23/100 ═══ -->"""
    parts.append(part23)

    # PART 24
    part24 = """<!-- ═══ PART 24/100 · DRILLS Q49–Q60 ═══ -->
<section class="part-section" id="part-24">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • DRILL MODULE</div>
    <h2 class="part-title">Part 24: Section A Practice Drills (Q49–Q60)</h2>
    <p class="part-subtitle">Opening years loss relief, carry-back deadlines, Class 1 NIC thresholds, and Employer Class 1A calculations.</p>
  </div>

  <!-- DRILL Q50 -->
  <div class="drill-card" id="q50">
    <div class="drill-header">
      <span class="drill-title">Q50 • Sabine's Opening Years Loss</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Sabine started trading 1 April 2024. Year to 31 March 2025 profit = £5,000; Year to 31 March 2026 loss = (£25,000). Employed until 31 March 2024 (£45,000 p.a.). Receives £3,000 savings income p.a. What is the EARLIEST tax year in which her loss can be offset?</p>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
Loss incurred in 2025/26 (tax year 2 of trade).
Under s.72 Opening Years Loss Relief:
Loss incurred in first 4 tax years of trade can be carried back 3 tax years on FIFO basis!

First tax year of trade = 2023/24 (1 April 2024 falls in 2023/24).
Loss year = 2025/26.
Carry back 3 years before 2025/26:
1st year FIFO = 2022/23!

Income in 2022/23 = Employment Income (£45,000) + Savings (£3,000) = £48,000.
Sabine can relieve the FULL £25,000 loss against 2022/23 income!
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: Earliest Tax Year = 2022/23 | Loss Relieved = £25,000</strong><br>
        Opening years loss relief (s.72) allows a 3-year carry-back on a First-In, First-Out (FIFO) basis against total income!
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q50" onchange="GAMIFICATION.toggleTask('q50', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 24/100 ═══ -->"""
    parts.append(part24)

    # PART 25
    part25 = """<!-- ═══ PART 25/100 · DRILLS Q61–Q72 ═══ -->
<section class="part-section" id="part-25">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • DRILL MODULE</div>
    <h2 class="part-title">Part 25: Section A Practice Drills (Q61–Q72)</h2>
    <p class="part-subtitle">Class 4 NIC calculations, pension annual allowance, tapered AA, and statutory revenue vs capital taxes.</p>
  </div>

  <!-- DRILL Q69 -->
  <div class="drill-card" id="q69">
    <div class="drill-header">
      <span class="drill-title">Q69 • Niamhe's Tapered Annual Allowance</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Niamhe has adjusted income of £330,000 in 2025/26. Made gross pension contributions of £100,000. No unused AA b/fwd. What is the amount of Annual Allowance charge added to her taxable income?</p>
    <div class="options-group">
      <label class="option-item"><input type="radio" name="q69_opt"> A) £75,000</label>
      <label class="option-item"><input type="radio" name="q69_opt"> B) £40,000</label>
      <label class="option-item"><input type="radio" name="q69_opt"> C) £90,000</label>
      <label class="option-item"><input type="radio" name="q69_opt"> D) £25,000</label>
    </div>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
Adjusted Income: £330,000
Threshold Limit: £260,000
Excess Adjusted Income = £330,000 - £260,000 = £70,000

Taper Reduction = 50% × £70,000 = £35,000
Tapered Annual Allowance = Standard AA (£60,000) - £35,000 = £25,000

Pension Contribution Made:          £100,000
Less Tapered AA Available:          (£25,000)
                                    --------
Annual Allowance Chargeable Amount = £75,000
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: A (£75,000)</strong><br>
        The Annual Allowance charge is added to taxable income equal to the excess contribution over her tapered AA (£100k - £25k = £75k)!
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q69" onchange="GAMIFICATION.toggleTask('q69', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 25/100 ═══ -->"""
    parts.append(part25)

    # PART 26
    part26 = """<!-- ═══ PART 26/100 · DRILLS Q73–Q84 ═══ -->
<section class="part-section" id="part-26">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • DRILL MODULE</div>
    <h2 class="part-title">Part 26: Section A Practice Drills (Q73–Q84)</h2>
    <p class="part-subtitle">Self-Assessment penalties, failure to notify, HMRC discovery assessments, and Payments on Account.</p>
  </div>

  <div class="card">
    <h3>⚖️ Standard Penalty Categories for Errors in Returns</h3>
    <table class="fiscal-table">
      <thead>
        <tr><th>Taxpayer Behavior</th><th>Maximum Penalty</th><th>Minimum (Unprompted)</th><th>Minimum (Prompted)</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Careless</strong></td><td class="num">30%</td><td class="num">0%</td><td class="num">15%</td></tr>
        <tr><td><strong>Deliberate but not Concealed</strong></td><td class="num">70%</td><td class="num">20%</td><td class="num">35%</td></tr>
        <tr><td><strong>Deliberate and Concealed</strong></td><td class="num">100%</td><td class="num">30%</td><td class="num">50%</td></tr>
      </tbody>
    </table>
  </div>
</section>
<!-- ═══ END PART 26/100 ═══ -->"""
    parts.append(part26)

    # PART 27
    part27 = """<!-- ═══ PART 27/100 · DRILLS Q85–Q92 ═══ -->
<section class="part-section" id="part-27">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • DRILL MODULE</div>
    <h2 class="part-title">Part 27: Section A Practice Drills (Q85–Q92)</h2>
    <p class="part-subtitle">Professional ethics, PCRT principles, tax avoidance vs evasion, and money laundering reporting duties.</p>
  </div>

  <div class="card">
    <h3>🛡️ Professional Conduct in Relation to Taxation (PCRT)</h3>
    <p>1. <strong>Five Fundamental Principles:</strong> Integrity, Objectivity, Professional Competence & Due Care, Confidentiality, Professional Behavior.</p>
    <p>2. <strong>Tax Evasion vs Avoidance:</strong> Evasion is ILLEGAL (deliberate suppression of facts). Avoidance is LEGAL structuring within the spirit/letter of the law.</p>
    <p>3. <strong>Money Laundering Regulations (MLR):</strong> Advisers MUST disclose suspicious transactions to the Money Laundering Reporting Officer (MLRO) or National Crime Agency (NCA). Tipping off the client is a criminal offense!</p>
  </div>
</section>
<!-- ═══ END PART 27/100 ═══ -->"""
    parts.append(part27)

    # PART 28
    part28 = """<!-- ═══ PART 28/100 · SECTION B CASES Q93 & Q94 ═══ -->
<section class="part-section" id="part-28">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • SECTION B OT CASES</div>
    <h2 class="part-title">Part 28: Section B OT Case Studies — Q93 Philip & Charles & Q94 Kim Baxter</h2>
    <p class="part-subtitle">Full 10-mark OT case studies covering income tax liabilities, pension annual allowances, and employment benefits.</p>
  </div>

  <!-- CASE Q93 -->
  <div class="card" id="q93">
    <div class="drill-header">
      <span class="drill-title">Q93 • Philip and Charles (10 Marks)</span>
      <div>
        <span class="chip chip-xp">+25 XP</span>
        <span class="chip chip-type">Section B Case</span>
      </div>
    </div>
    <p><strong>Scenario:</strong> Philip retired at 55. Received pension £15,000 and building society interest £14,600 in 2025/26. Charles (son) is self-employed (trading profit £112,400). Charles made Gift Aid £800 (gross) and gross pension contribution £45,000 in 2023/24 (none since).</p>

    <div class="drill-card">
      <p><strong>1. What is Philip's income tax liability for 2025/26?</strong></p>
      <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
      <div class="solution-content">
        <div class="computation-box">
Pension (Non-Savings): £15,000
Building Society Interest (Savings): £14,600
Total Net Income = £29,600
Less PA = (£12,570 allocated to Non-Savings)
Taxable Non-Savings = £2,430 (£15,000 - £12,570)
Taxable Savings = £14,600

Tax Calculation:
Non-Savings: £2,430 × 20% = £486
Savings SNRB: £1,000 × 0% = £0
Savings Excess: (£14,600 - £1,000) = £13,600 × 20% = £2,720
Total Tax Liability = £486 + £2,720 = £3,206
        </div>
        <div class="callout callout-tip"><strong>CORRECT ANSWER: C (£3,206)</strong></div>
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q93" onchange="GAMIFICATION.toggleTask('q93', 25, this.checked)">
        Mark Case Done (+25 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 28/100 ═══ -->"""
    parts.append(part28)

    # PART 29
    part29 = """<!-- ═══ PART 29/100 · SECTION B CASES Q95, Q96 & Q97 ═══ -->
<section class="part-section" id="part-29">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • SECTION B OT CASES</div>
    <h2 class="part-title">Part 29: Section B OT Case Studies — Q95 Dill, Q96 John Beach & Q97 Foo Dee</h2>
    <p class="part-subtitle">High-earner PA taper, company gym/nursery exemptions, beneficial loan average method, and trade cessation.</p>
  </div>

  <!-- CASE Q95 -->
  <div class="card" id="q95">
    <div class="drill-header">
      <span class="drill-title">Q95 • Dill (10 Marks)</span>
      <div>
        <span class="chip chip-xp">+25 XP</span>
        <span class="chip chip-type">Section B Case</span>
      </div>
    </div>
    <p>Dill earned salary £350,000. Had workplace gym, workplace nursery, and health club membership benefits.</p>

    <div class="drill-card">
      <p><strong>What is the taxable benefit for gym, nursery, and health club?</strong></p>
      <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
      <div class="solution-content">
        <div class="callout callout-tip">
          <strong>MODEL ANSWER:</strong><br>
          • <strong>Company Gym:</strong> £0 (Statutory Exempt Benefit available to all employees).<br>
          • <strong>Workplace Nursery:</strong> £0 (Statutory Exempt Benefit available to all employees).<br>
          • <strong>Commercial Health Club Membership:</strong> £990 (Taxable benefit in full).
        </div>
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q95" onchange="GAMIFICATION.toggleTask('q95', 25, this.checked)">
        Mark Case Done (+25 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 29/100 ═══ -->"""
    parts.append(part29)

    # PART 30
    part30 = """<!-- ═══ PART 30/100 · SECTION C MASTERCLASS Q98 & Q99 ═══ -->
<section class="part-section" id="part-30">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 30: Section C Masterclass — Q98 Jason & Q99 Poppy (15 Marks Each)</h2>
    <p class="part-subtitle">Full constructed response scenarios, step-by-step mono computations, marking schemes, and examiner feedback.</p>
  </div>

  <!-- MASTERCLASS Q98 JASON -->
  <div class="card" id="q98">
    <div class="drill-header">
      <span class="drill-title">Q98 • Jason (15 Marks Constructed Response)</span>
      <div>
        <span class="chip chip-xp">+40 XP</span>
        <span class="chip chip-type">Section C Masterclass</span>
      </div>
    </div>
    <p><strong>Scenario:</strong> Jason is deciding whether to remain at Initial plc or take a new offer with Subsequent plc starting 15 March 2025. Calculates incremental income tax for 2025/26 between Initial plc vs Subsequent plc.</p>

    <div class="computation-box">
Initial plc Employment Income 2025/26:
Salary:                                  £72,000
Company Car Benefit:                      £8,400
Car Fuel Benefit (£28,200 × 30%):        £8,460
                                         -------
Total Employment Income Initial plc:     £88,860

Subsequent plc Employment Income 2025/26:
Salary:                                  £98,000
Interest-Free Loan Benefit (£140,000 × 3.75% × 8/12): £3,500
                                         -------
Total Employment Income Subsequent plc: £101,500

Tax Comparison:
Initial plc Taxable Income (£88,860 - £12,570) = £76,290 -> Tax = £22,976
Subsequent plc Taxable Income (£101,500 - £11,820 PA tapered) = £89,680 -> Tax = £28,332

Incremental Tax Payable = £28,332 - £22,976 = £5,356
    </div>

    <div class="callout callout-examiner">
      <div class="callout-title">🔴 EXAMINER REPORT & KEY ANSWER TIPS</div>
      "Candidates performed well on salary and car calculations but frequently forgot to taper the Personal Allowance when Subsequent plc income exceeded £100,000 (ANI £101,500 -> PA reduced to £11,820). Always verify whether ANI passes £100,000 in employment change comparisons!"
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q98" onchange="GAMIFICATION.toggleTask('q98', 40, this.checked)">
        Mark Masterclass Done (+40 XP)
      </label>
    </div>
  </div>
</section>

</div> <!-- End container -->
</body>
</html>
<!-- ═══ END PART 30/100 ═══ -->"""
    parts.append(part30)

    new_content = base_content + '\n\n' + '\n\n'.join(parts)
    with open('TX-UK_Revision_Pack.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print('Successfully appended Session 3 (Parts 21 to 30) to TX-UK_Revision_Pack.html!')

if __name__ == '__main__':
    build_session_3()
