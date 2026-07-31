import sys

def build_session_2():
    # Read existing file
    with open('TX-UK_Revision_Pack.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find where container closes
    close_idx = content.find('</div> <!-- End container -->')
    if close_idx != -1:
        base_content = content[:close_idx]
    else:
        # fallback
        base_content = content.replace('</body>\n</html>', '').replace('</body></html>', '')

    parts = []

    # PART 11
    part11 = """<!-- ═══ PART 11/100 · IT-05 EMPLOYMENT INCOME BASICS ═══ -->
<section class="part-section" id="part-11">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • INCOME TAX & NIC</div>
    <h2 class="part-title">Part 11: IT-05 Employment Income: Receipts Basis, Bonuses & Exempt Benefits</h2>
    <p class="part-subtitle">Rules of taxability, receipts basis timing, statutory exempt benefits, and practice questions Q32 & Q33.</p>
  </div>

  <div class="card">
    <h3>📖 Core Rules: Receipts Basis & Timing of Bonuses</h3>
    <p>Employment income is taxed on the <strong>receipts basis</strong>. For directors and employees, earnings are treated as received on the <strong>earliest</strong> of:</p>
    <ul>
      <li>1. The date payment is actually received.</li>
      <li>2. The date the person becomes entitled to payment.</li>
      <li>3. (For directors) The date earnings are credited in the company's accounts or end of period of account.</li>
    </ul>

    <div class="callout callout-trap">
      <div class="callout-title">⚠️ TRAP WARNING: BONUS TIMING</div>
      A bonus voted in respect of a calendar year (e.g. year to 31 Dec 2024) but paid on 6 April 2025 falls into the tax year <strong>2025/26</strong> because it was received/entitled on 6 April 2025!
    </div>
  </div>

  <div class="card">
    <h3>🎁 Statutory Exempt Benefits Master List</h3>
    <p>The following employee benefits are <strong>100% exempt</strong> from Income Tax and Class 1A NIC:</p>
    <table class="fiscal-table">
      <thead>
        <tr><th>Exempt Benefit</th><th>Statutory Condition / Limits</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Workplace Parking</strong></td><td>Parking spaces at or near the employee's place of work.</td></tr>
        <tr><td><strong>Subscribed Professional Fees</strong></td><td>Subscriptions to HMRC-approved professional bodies (e.g. ACCA, CIM).</td></tr>
        <tr><td><strong>Workplace Canteen / Meals</strong></td><td>Available to ALL employees on a non-discriminatory basis.</td></tr>
        <tr><td><strong>Job-Related Relocation Expenses</strong></td><td>Up to <strong>£8,000</strong> max per move.</td></tr>
        <tr><td><strong>Work Mobile Phone</strong></td><td>One mobile phone provided per employee (including line rental and calls).</td></tr>
        <tr><td><strong>Annual Parties / Events</strong></td><td>Up to <strong>£150 per head</strong> per year (inclusive of VAT).</td></tr>
        <tr><td><strong>Trivial Benefits</strong></td><td>Cost under <strong>£50</strong> per gift, not cash or cash equivalent.</td></tr>
      </tbody>
    </table>
  </div>

  <!-- DRILL Q32 -->
  <div class="drill-card" id="q32">
    <div class="drill-header">
      <span class="drill-title">Q32 • Dong's Bonus Timing</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Dong is employed. As well as his annual salary he is also paid a bonus in April each year based upon performance to the end of the previous calendar year. Tick the appropriate box to show the tax treatment for 2025/26:</p>
    
    <table class="fiscal-table">
      <thead>
        <tr><th>Bonus Description</th><th class="num">Taxable in 2025/26</th><th class="num">Not Taxable in 2025/26</th></tr>
      </thead>
      <tbody>
        <tr><td>Bonus of £2,800 received on 6 April 2025 in respect of year to 31 Dec 2024</td><td class="num">[ ]</td><td class="num">[ ]</td></tr>
        <tr><td>Bonus of £3,300 received on 3 April 2026 in respect of year to 31 Dec 2025</td><td class="num">[ ]</td><td class="num">[ ]</td></tr>
      </tbody>
    </table>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="callout callout-tip">
        <strong>MODEL ANSWER & EXPLANATION:</strong><br>
        • <strong>£2,800 received on 6 April 2025:</strong> TAXABLE in 2025/26 (6 April 2025 is the first day of the 2025/26 tax year!).<br>
        • <strong>£3,300 received on 3 April 2026:</strong> TAXABLE in 2025/26 (3 April 2026 falls within 2025/26 tax year: 6 April 2025 to 5 April 2026).
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q32" onchange="GAMIFICATION.toggleTask('q32', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 11/100 ═══ -->"""
    parts.append(part11)

    # PART 12
    part12 = """<!-- ═══ PART 12/100 · IT-06 BENEFITS IN KIND ═══ -->
<section class="part-section" id="part-12">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • INCOME TAX & NIC</div>
    <h2 class="part-title">Part 12: IT-06 Benefits in Kind: Cars, Fuel, Vans, Accommodation, Loans & Mileage</h2>
    <p class="part-subtitle">Comprehensive calculation rules for company cars, fuel scale charges, beneficial loans, living accommodation, and Q24–Q31.</p>
  </div>

  <div class="card">
    <h3>🚗 Company Car & Fuel Benefit Formulas (FA2025)</h3>
    <div class="computation-box">
Car Benefit = List Price × Appropriate Percentage (%)
Fuel Benefit = £28,200 × Appropriate Percentage (%)
    </div>
    <table class="fiscal-table">
      <thead>
        <tr><th>Vehicle CO₂ Band</th><th>Appropriate % (Petrol & RDE2 Diesel)</th></tr>
      </thead>
      <tbody>
        <tr><td>0g/km (Pure Electric)</td><td class="num">3%</td></tr>
        <tr><td>1 – 50g/km (Hybrid 130+ electric miles)</td><td class="num">3%</td></tr>
        <tr><td>1 – 50g/km (Hybrid 70 – 129 electric miles)</td><td class="num">6%</td></tr>
        <tr><td>1 – 50g/km (Hybrid 40 – 69 electric miles)</td><td class="num">9%</td></tr>
        <tr><td>51 – 54g/km</td><td class="num">16%</td></tr>
        <tr><td>55g/km (Base Level)</td><td class="num">17%</td></tr>
        <tr><td>Every full 5g/km above 55g/km</td><td class="num">+1% (Maximum cap 37%)</td></tr>
      </tbody>
    </table>

    <div class="callout callout-trap">
      <div class="callout-title">⚠️ TRAP WARNING: DIESEL SURCHARGE</div>
      Diesel cars NOT meeting the RDE2 standard suffer a <strong>4% surcharge</strong> (capped at 37%). If the question states the diesel car <em>meets RDE2 standard</em>, do NOT add 4%!
    </div>
  </div>

  <div class="card">
    <h3>🚚 Van Benefits, Accommodation & Beneficial Loans</h3>
    <p>• <strong>Company Van Benefit:</strong> Flat charge of <strong>£4,020</strong> (Zero emission vans = £0 benefit). Fuel scale charge = <strong>£757</strong>.</p>
    <p>• <strong>Beneficial Loans:</strong> Taxable if loan exceeds <strong>£10,000</strong> at any point in the tax year. Benefit = Loan × (Official Interest Rate 3.75% - Interest Paid).</p>
    <p>• <strong>Approved Mileage Allowance Payments (AMAP):</strong> Cars/Vans: <strong>45p/mile</strong> for first 10,000 business miles; <strong>25p/mile</strong> over 10,000 miles.</p>
  </div>

  <!-- DRILL Q27 -->
  <div class="drill-card" id="q27">
    <div class="drill-header">
      <span class="drill-title">Q27 • Thiago's Company Car Benefit</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Thiago is provided with a new diesel company car on 6 May 2025 (used for business and private purposes). List price is £28,000, CO₂ emissions 152g/km, meets RDE2 standard.</p>
    <p>What is Thiago's car benefit for the tax year 2025/26?</p>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
List Price: £28,000
CO2 emissions: 152g/km
Base level 55g/km = 17%
(152 - 55) = 97g/km / 5 = 19.4 -> 19 steps of 5g/km × 1% = +19%
Base percentage: 17% + 19% = 36%
RDE2 standard diesel -> NO 4% surcharge!

Full Year Benefit: £28,000 × 36% = £10,080
Provided from 6 May 2025 -> 11 months in tax year 2025/26 (May to March + April = 11 months):
11/12 × £10,080 = £9,240
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: £9,240</strong><br>
        Remember to time-apportion benefits when provided part-way through the tax year (6 May = 11 months)!
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q27" onchange="GAMIFICATION.toggleTask('q27', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 12/100 ═══ -->"""
    parts.append(part12)

    # PART 13
    part13 = """<!-- ═══ PART 13/100 · IT-07 TRADING INCOME ADJUSTMENTS ═══ -->
<section class="part-section" id="part-13">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • INCOME TAX & NIC</div>
    <h2 class="part-title">Part 13: IT-07 Trading Income: Cash Basis vs Accruals & Profit Adjustments</h2>
    <p class="part-subtitle">Allowable vs disallowable expenditure, lease premium relief, goods for own use, and questions Q34–Q36.</p>
  </div>

  <div class="card">
    <h3>📖 Adjustment of Trading Profits Pro-Forma</h3>
    <table class="fiscal-table">
      <thead>
        <tr><th>Item</th><th class="num">Add (£)</th><th class="num">Deduct (£)</th></tr>
      </thead>
      <tbody>
        <tr><td>Net Profit per Accounts</td><td class="num">X,XXX</td><td class="num">—</td></tr>
        <tr><td>Depreciation & Amortisation (Disallowable)</td><td class="num">X,XXX</td><td class="num">—</td></tr>
        <tr><td>Business Entertainment (Disallowable)</td><td class="num">X,XXX</td><td class="num">—</td></tr>
        <tr><td>Private Proportion of Expenses (Car/Telephone)</td><td class="num">X,XXX</td><td class="num">—</td></tr>
        <tr><td>Goods for Own Use (at Selling Price / Market Value)</td><td class="num">X,XXX</td><td class="num">—</td></tr>
        <tr><td>Non-Trading Income (Property rent / Dividends / Interest)</td><td class="num">—</td><td class="num">(X,XXX)</td></tr>
        <tr><td>Lease Premium Allowable Deduction</td><td class="num">—</td><td class="num">(X,XXX)</td></tr>
        <tr><td>Capital Allowances</td><td class="num">—</td><td class="num">(X,XXX)</td></tr>
        <tr style="font-weight:700; background-color:var(--paper-deep);">
          <td>TAX ADJUSTED TRADING PROFIT</td>
          <td class="num">X,XXX</td>
          <td class="num">—</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="card">
    <h3>🏢 Lease Premium Relief Formula for Sole Traders</h3>
    <div class="computation-box">
1. Capital Premium Taxable on Landlord = P × [51 - (N - 1)] / 50
2. Annual Trading Expense Deduction = Taxable Premium / Lease Term (N)
    </div>
  </div>

  <!-- DRILL Q35 -->
  <div class="drill-card" id="q35">
    <div class="drill-header">
      <span class="drill-title">Q35 • Haniful's Goods for Own Use</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Haniful took goods from his business for personal use. Goods cost £850, selling price £1,100. No entry recorded in business accounts except original purchase. Unadjusted trading profits = £247,500.</p>
    <p>What is Haniful's tax adjusted trading profit after adjustment?</p>
    <div class="options-group">
      <label class="option-item"><input type="radio" name="q35_opt"> A) £248,350</label>
      <label class="option-item"><input type="radio" name="q35_opt"> B) £248,600</label>
      <label class="option-item"><input type="radio" name="q35_opt"> C) £246,400</label>
      <label class="option-item"><input type="radio" name="q35_opt"> D) £247,750</label>
    </div>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
Unadjusted trading profit:         £247,500
Add: Selling price of goods taken:   £1,100
                                   --------
Adjusted Trading Profit:           £248,600
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: B (£248,600)</strong><br>
        Under tax law (Sharkey v Wernher), goods taken for personal use must be credited to trading profit at full <strong>selling price</strong> (not cost).
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q35" onchange="GAMIFICATION.toggleTask('q35', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 13/100 ═══ -->"""
    parts.append(part13)

    # PART 14
    part14 = """<!-- ═══ PART 14/100 · IT-08 CAPITAL ALLOWANCES ═══ -->
<section class="part-section" id="part-14">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • INCOME TAX & NIC</div>
    <h2 class="part-title">Part 14: IT-08 Capital Allowances for Unincorporated Businesses</h2>
    <p class="part-subtitle">Main Pool (18%), Special Rate Pool (6%), AIA (£1,000,000), Private Use Assets, and Q37–Q43.</p>
  </div>

  <div class="card">
    <h3>⚙️ Capital Allowances Rates & Rules Summary</h3>
    <table class="fiscal-table">
      <thead>
        <tr><th>Plant & Machinery Pool</th><th>Writing Down Allowance (WDA)</th><th>AIA Available?</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Annual Investment Allowance (AIA)</strong></td><td class="num">100% FYA (Limit £1,000,000)</td><td class="num">YES</td></tr>
        <tr><td><strong>Main Pool</strong> (General Plant & Machinery, Cars 1-50g/km)</td><td class="num">18% p.a. WDA</td><td class="num">YES</td></tr>
        <tr><td><strong>Special Rate Pool</strong> (Integral features, Cars > 50g/km)</td><td class="num">6% p.a. WDA</td><td class="num">YES</td></tr>
        <tr><td><strong>Single Asset Pools (Private Use)</strong></td><td class="num">18% or 6% WDA (Business % only)</td><td class="num">NO</td></tr>
        <tr><td><strong>Structures & Buildings Allowance (SBA)</strong></td><td class="num">3% Straight Line</td><td class="num">NO</td></tr>
      </tbody>
    </table>

    <div class="callout callout-trap">
      <div class="callout-title">⚠️ TRAP WARNING: NO FULL EXPENSING FOR SOLE TRADERS</div>
      "Full Expensing" (100% main pool FYA) applies ONLY to companies subject to Corporation Tax. Sole traders and partnerships CANNOT claim full expensing — they use AIA!
    </div>
  </div>

  <!-- DRILL Q41 -->
  <div class="drill-card" id="q41">
    <div class="drill-header">
      <span class="drill-title">Q41 • Ronald's Cessation Capital Allowances</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Ronald ceased trading on 31 March 2026. Main pool TWDV at 1 April 2025 = £15,000. On 1 Jan 2026 bought business laptop for £4,500. On 31 March 2026 main pool items sold for £14,550. Laptop retained by Ronald (market value £4,150).</p>
    <p>What is the capital allowance / (balancing charge) for the year ended 31 March 2026?</p>
    <div class="options-group">
      <label class="option-item"><input type="radio" name="q41_opt"> A) £144</label>
      <label class="option-item"><input type="radio" name="q41_opt"> B) £450</label>
      <label class="option-item"><input type="radio" name="q41_opt"> C) (£800)</label>
      <label class="option-item"><input type="radio" name="q41_opt"> D) £800</label>
    </div>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
TWDV b/fwd 1 April 2025:            £15,000
Add: Laptop purchase:                £4,500
                                   --------
Subtotal:                           £19,500
Disposals on Cessation:
- Main pool items sold:            (£14,550)
- Laptop retained (MV):             (£4,150)
                                   --------
Remaining Unrelieved Balance:          £800

Balancing Allowance on Cessation = £800
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: D (£800 Balancing Allowance)</strong><br>
        On cessation, NO WDA or AIA is claimed. Instead, compare total pool value against total disposal proceeds/market values to arrive at a Balancing Allowance (+£800) or Balancing Charge.
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q41" onchange="GAMIFICATION.toggleTask('q41', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 14/100 ═══ -->"""
    parts.append(part14)

    # PART 15
    part15 = """<!-- ═══ PART 15/100 · IT-09 TRADING LOSSES ═══ -->
<section class="part-section" id="part-15">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • INCOME TAX & NIC</div>
    <h2 class="part-title">Part 15: IT-09 Trading Losses for Individuals</h2>
    <p class="part-subtitle">Current year, carry-back, opening years relief, terminal loss relief, statutory cap, and Q47–Q53.</p>
  </div>

  <div class="card">
    <h3>📉 Individual Trading Loss Options Summary</h3>
    <table class="fiscal-table">
      <thead>
        <tr><th>Loss Relief Claim</th><th>Target Income Stream</th><th>Statutory Cap / Restriction</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>s.64 Carry-Across / Back</strong></td><td>Total Net Income of current tax year and/or preceding tax year.</td><td>Cap: Higher of £50,000 or 25% of total income.</td></tr>
        <tr><td><strong>s.72 Opening Years Relief</strong></td><td>Loss in first 4 tax years set against total income of 3 preceding tax years (FIFO).</td><td>Cap: Higher of £50,000 or 25% of total income.</td></tr>
        <tr><td><strong>s.83 Carry-Forward</strong></td><td>Future trading profits of the SAME trade only.</td><td>NO CAP (100% relieved against future trade profits).</td></tr>
        <tr><td><strong>s.89 Terminal Loss Relief</strong></td><td>Losses in final 12 months set against trade profits of 3 preceding tax years (LIFO).</td><td>NO CAP.</td></tr>
      </tbody>
    </table>
  </div>

  <!-- DRILL Q47 -->
  <div class="drill-card" id="q47">
    <div class="drill-header">
      <span class="drill-title">Q47 • Naomi's Loss Relief Cap</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Naomi made a trading loss of £110,000 in 2025/26. In 2024/25 she had trading profit of £24,000 and employment income of £92,000 (Total income = £116,000).</p>
    <p>What is the maximum loss relief claim Naomi can make against her total income for 2024/25?</p>
    <div class="options-group">
      <label class="option-item"><input type="radio" name="q47_opt"> A) £74,000</label>
      <label class="option-item"><input type="radio" name="q47_opt"> B) £50,000</label>
      <label class="option-item"><input type="radio" name="q47_opt"> C) £110,000</label>
      <label class="option-item"><input type="radio" name="q47_opt"> D) £29,000</label>
    </div>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
Total Income 2024/25: £24,000 + £92,000 = £116,000

Statutory Cap on Non-Trading Income Set-Off:
Higher of £50,000 or 25% × Total Income (25% × £116,000 = £29,000)
Statutory Cap = £50,000

HOWEVER: Cap applies ONLY to non-trading income (£92,000)!
Trading profit (£24,000) can be FULLY relieved without cap!

Max Claim = Trading Profit (£24,000) + Cap on Non-Trading Income (£50,000)
Max Claim = £24,000 + £50,000 = £74,000
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: A (£74,000)</strong><br>
        Classic examiner trap! The £50k cap applies ONLY to non-trading income. Trading income within total income is relieved 100% cap-free!
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q47" onchange="GAMIFICATION.toggleTask('q47', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 15/100 ═══ -->"""
    parts.append(part15)

    # PART 16
    part16 = """<!-- ═══ PART 16/100 · IT-10 PARTNERSHIPS ═══ -->
<section class="part-section" id="part-16">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • INCOME TAX & NIC</div>
    <h2 class="part-title">Part 16: IT-10 Partnership Taxation</h2>
    <p class="part-subtitle">Allocation of trading profits, partner salaries, profit-sharing ratios (PSR), changes in ratios, and Q44–Q46.</p>
  </div>

  <div class="card">
    <h3>🤝 Partnership Profit Allocation Rules</h3>
    <p>1. Partnership trading profit is calculated at the partnership level using standard sole trader tax adjustment rules.</p>
    <p>2. Profits are allocated among partners in accordance with the profit-sharing agreement for that accounting period:</p>
    <div class="computation-box">
Step 1: Allocate partner salaries (pro-rata for period).
Step 2: Allocate partner interest on capital.
Step 3: Divide remaining balance in Profit Sharing Ratio (PSR).
    </div>
  </div>

  <!-- DRILL Q44 -->
  <div class="drill-card" id="q44">
    <div class="drill-header">
      <span class="drill-title">Q44 • Elizabeth & Henry Partnership Allocation</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Elizabeth and Henry share profits to 31 Dec 2025 (£120,000 total profit). Until 31 July 2025 ratio was 70:30 (no salaries). From 1 August 2025 ratio was 80:20 after Henry salary of £24,000 p.a.</p>
    <p>How much profit for year ended 31 Dec 2025 is allocated to Henry?</p>
    <div class="options-group">
      <label class="option-item"><input type="radio" name="q44_opt"> A) £41,000</label>
      <label class="option-item"><input type="radio" name="q44_opt"> B) £31,000</label>
      <label class="option-item"><input type="radio" name="q44_opt"> C) £43,200</label>
      <label class="option-item"><input type="radio" name="q44_opt"> D) £39,000</label>
    </div>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
Period 1: 1 Jan 2025 - 31 July 2025 (7 months):
Profit = 7/12 × £120,000 = £70,000
Henry's Share (30%) = £21,000

Period 2: 1 Aug 2025 - 31 Dec 2025 (5 months):
Profit = 5/12 × £120,000 = £50,000
Henry's Salary = 5/12 × £24,000 = £10,000
Remaining Profit = £50,000 - £10,000 = £40,000
Henry's Share (20%) = £8,000
Total Henry Period 2 = £10,000 + £8,000 = £18,000

Total Allocation to Henry = £21,000 + £18,000 = £39,000
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: D (£39,000)</strong><br>
        Always split the accounting year into sub-periods whenever PSR or salaries change!
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q44" onchange="GAMIFICATION.toggleTask('q44', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 16/100 ═══ -->"""
    parts.append(part16)

    # PART 17
    part17 = """<!-- ═══ PART 17/100 · IT-11 NATIONAL INSURANCE ═══ -->
<section class="part-section" id="part-17">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • INCOME TAX & NIC</div>
    <h2 class="part-title">Part 17: IT-11 National Insurance Contributions (Classes 1, 1A & 4)</h2>
    <p class="part-subtitle">Employee vs Employer Class 1, Employment Allowance (£10,500), Class 1A benefits, Class 4 trading profit thresholds, and Q54–Q63.</p>
  </div>

  <div class="card">
    <h3>💳 Master NIC Rates & Thresholds (FA2025)</h3>
    <table class="fiscal-table">
      <thead>
        <tr><th>Class</th><th>Payer / Asset Base</th><th>Earnings / Profit Threshold</th><th>FA2025 Rate</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Class 1 Employee</strong></td><td>Employee (Gross Cash Salary)</td><td>£12,571 – £50,270 p.a.<br>Over £50,270 p.a.</td><td class="num">8%<br>2%</td></tr>
        <tr><td><strong>Class 1 Employer</strong></td><td>Employer (Gross Cash Salary)</td><td>Over £5,000 p.a.</td><td class="num">15%</td></tr>
        <tr><td><strong>Employment Allowance</strong></td><td>Employer Class 1 Set-off</td><td>Max £10,500 per employer</td><td class="num">—</td></tr>
        <tr><td><strong>Class 1A Employer</strong></td><td>Employer (Non-cash Benefits)</td><td>Taxable Benefits in Kind</td><td class="num">15%</td></tr>
        <tr><td><strong>Class 4 Self-Employed</strong></td><td>Sole Trader / Partner Profit</td><td>£12,571 – £50,270 p.a.<br>Over £50,270 p.a.</td><td class="num">6%<br>2%</td></tr>
      </tbody>
    </table>
  </div>

  <!-- DRILL Q62 -->
  <div class="drill-card" id="q62">
    <div class="drill-header">
      <span class="drill-title">Q62 • Paloma's Class 4 NIC</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Paloma's tax adjusted trading profit for year ended 31 March 2026 was £58,000.</p>
    <p>What is the amount of Class 4 NIC payable by Paloma for 2025/26?</p>
    <div class="options-group">
      <label class="option-item"><input type="radio" name="q62_opt"> A) £2,678</label>
      <label class="option-item"><input type="radio" name="q62_opt"> B) £2,726</label>
      <label class="option-item"><input type="radio" name="q62_opt"> C) £2,401</label>
      <label class="option-item"><input type="radio" name="q62_opt"> D) £2,417</label>
    </div>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
Trading Profit: £58,000

Class 4 Band 1 (£12,571 to £50,270):
(£50,270 - £12,570) = £37,700 × 6% = £2,262

Class 4 Band 2 (Over £50,270):
(£58,000 - £50,270) = £7,730 × 2% = £154.60

Total Class 4 NIC = £2,262 + £154.60 = £2,416.60 -> £2,417
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: D (£2,417)</strong><br>
        Remember Class 4 NIC applies ONLY to trading profits, NOT to property or investment income!
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q62" onchange="GAMIFICATION.toggleTask('q62', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 17/100 ═══ -->"""
    parts.append(part17)

    # PART 18
    part18 = """<!-- ═══ PART 18/100 · IT-12 PENSIONS ═══ -->
<section class="part-section" id="part-18">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • INCOME TAX & NIC</div>
    <h2 class="part-title">Part 18: IT-12 Pension Reliefs & Annual Allowance Charge</h2>
    <p class="part-subtitle">Occupational vs Personal Pensions, Annual Allowance (£60,000), Tapered Annual Allowance, carry-forward rules, and Q64–Q69.</p>
  </div>

  <div class="card">
    <h3>🏦 Pension Relief & Annual Allowance Rules</h3>
    <p>1. <strong>Personal Pension Relief:</strong> Taxpayer pays 80% net; pension provider claims 20% basic rate relief at source. Basic and higher rate tax bands are extended by the GROSS contribution.</p>
    <p>2. <strong>Annual Allowance (AA):</strong> Standard Annual Allowance is <strong>£60,000</strong> per tax year.</p>
    <p>3. <strong>Carry-Forward Unused AA:</strong> Unused AA from the <strong>preceding 3 tax years</strong> can be brought forward, provided the taxpayer was a member of a registered pension scheme in those years (used on a FIFO basis).</p>
    <p>4. <strong>Tapered Annual Allowance:</strong> Applies if Adjusted Income exceeds <strong>£260,000</strong> AND Threshold Income exceeds £200,000. Reduced by £1 for every £2 over £260,000 (Minimum tapered AA = £10,000).</p>
  </div>

  <!-- DRILL Q66 -->
  <div class="drill-card" id="q66">
    <div class="drill-header">
      <span class="drill-title">Q66 • Abena's Pension Contribution</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Abena made gross personal pension contributions: 2022/23 £42k, 2023/24 £57k, 2024/25 £48k. (AA was £40k in 2022/23, £60k in 2023/24 and 2024/25).</p>
    <p>What is the maximum gross contribution Abena can make in 2025/26 without giving rise to an AA charge?</p>
    <div class="options-group">
      <label class="option-item"><input type="radio" name="q66_opt"> A) £73,000</label>
      <label class="option-item"><input type="radio" name="q66_opt"> B) £60,000</label>
      <label class="option-item"><input type="radio" name="q66_opt"> C) £75,000</label>
      <label class="option-item"><input type="radio" name="q66_opt"> D) £72,000</label>
    </div>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
2025/26 Current Year AA:                 £60,000

Brought Forward Unused AA:
- 2022/23 (£40,000 - £42,000):               £0 (Fully used)
- 2023/24 (£60,000 - £57,000):           £3,000
- 2024/25 (£60,000 - £48,000):          £12,000
                                        -------
Total Capacity 2025/26 = £60k + £3k + £12k = £75,000
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: C (£75,000)</strong><br>
        Current year AA is always used first, then brought-forward unused allowances on a First-In, First-Out (FIFO) basis.
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q66" onchange="GAMIFICATION.toggleTask('q66', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 18/100 ═══ -->"""
    parts.append(part18)

    # PART 19
    part19 = """<!-- ═══ PART 19/100 · IT-13 ADMIN & ETHICS ═══ -->
<section class="part-section" id="part-19">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • INCOME TAX & NIC</div>
    <h2 class="part-title">Part 19: IT-13 Administration & Ethics for Individuals</h2>
    <p class="part-subtitle">Self-Assessment deadlines, Payments on Account (PoA), interest on late tax, penalty categories, and Q70–Q92.</p>
  </div>

  <div class="card">
    <h3>📅 Self-Assessment Payment Timeline (Tax Year 2025/26)</h3>
    <table class="fiscal-table">
      <thead>
        <tr><th>Payment Milestone</th><th>Due Date</th><th>Calculation Basis</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>1st Payment on Account (PoA)</strong></td><td>31 January 2026 (in tax year)</td><td class="num">50% of 2024/25 Net IT & Class 4 NIC liability</td></tr>
        <tr><td><strong>2nd Payment on Account (PoA)</strong></td><td>31 July 2026 (following tax year)</td><td class="num">50% of 2024/25 Net IT & Class 4 NIC liability</td></tr>
        <tr><td><strong>Balancing Payment & Class 2/CGT</strong></td><td>31 January 2027 (following tax year)</td><td class="num">Actual 2025/26 liability less PoAs paid</td></tr>
      </tbody>
    </table>

    <div class="callout callout-tip">
      <div class="callout-title">🟢 POA DE MINIMIS EXEMPTION</div>
      Payments on account are NOT required if either:<br>
      1. Total net tax liability for prior year was under <strong>£1,000</strong>, OR<br>
      2. More than <strong>80%</strong> of prior year tax was deducted at source (e.g. PAYE).
    </div>
  </div>

  <!-- DRILL Q84 -->
  <div class="drill-card" id="q84">
    <div class="drill-header">
      <span class="drill-title">Q84 • Siena's Payments on Account</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Siena's 2024/25 IT & Class 4 NIC liability was £40,000 (£6,000 PAYE deducted). Her 2025/26 liability will total £49,000 (£8,000 PAYE deducted).</p>
    <p>What will be the amount of EACH of Siena's payments on account for 2025/26?</p>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
2024/25 Total Tax & Class 4 NIC:    £40,000
Less Tax Deducted at Source (PAYE): (£6,000)
                                    --------
2024/25 Net Self-Assessed Tax:       £34,000

Each Payment on Account for 2025/26:
50% × £34,000 = £17,000
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: £17,000</strong><br>
        Payments on account are based ALWAYS on 50% of the PRECEDING year's net tax liability after deducting PAYE/source tax!
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q84" onchange="GAMIFICATION.toggleTask('q84', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 19/100 ═══ -->"""
    parts.append(part19)

    # PART 20
    part20 = """<!-- ═══ PART 20/100 · ACT 1 CHECKPOINT & DRILL RECAP ═══ -->
<section class="part-section" id="part-20">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • INCOME TAX & NIC</div>
    <h2 class="part-title">Part 20: Act 1 Checkpoint & Section A Master Drill Recap</h2>
    <p class="part-subtitle">Summary of Act 1 core topics, XP audit, and preparation for Section B cases.</p>
  </div>

  <div class="card">
    <h3>🎉 Act 1 Mid-Point Mastery Checkpoint</h3>
    <p>You have now completed the core theoretical foundations and key OT drills for Income Tax, Employment Benefits, Trading Profits, Capital Allowances, Losses, Partnerships, NIC, Pensions, and Administration.</p>
    
    <div class="computation-box">
Current Act 1 Coverage:
• Income Tax Skeleton, PA Taper, Marriage Allowance
• Benefits in Kind (Cars, Vans, Loans, Mileage)
• Capital Allowances (AIA £1M, Main Pool 18%, Special Pool 6%)
• Loss Relief Set-offs & Statutory £50k Cap
• NIC Class 1, 1A, 4 & Employment Allowance (£10,500)
• Pension AA (£60,000) & Payments on Account
    </div>

    <div class="callout callout-hook">
      <div class="callout-title">🧠 RANK AUDIT: ARE YOU ON TRACK FOR ANALYST / STRATEGIST?</div>
      Check your HUD progress bar above! Ticking all drill checkboxes in Parts 7–20 generates over <strong>200+ XP</strong> towards your next rank upgrade.
    </div>
  </div>
</section>

</div> <!-- End container -->
</body>
</html>
<!-- ═══ END PART 20/100 ═══ -->"""
    parts.append(part20)

    # Append all parts to file
    new_content = base_content + '\n\n' + '\n\n'.join(parts)
    with open('TX-UK_Revision_Pack.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print('Successfully appended Session 2 (Parts 11 to 20) to TX-UK_Revision_Pack.html!')

if __name__ == '__main__':
    build_session_2()
