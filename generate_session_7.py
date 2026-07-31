import sys

def build_session_7():
    with open('TX-UK_Revision_Pack.html', 'r', encoding='utf-8') as f:
        content = f.read()

    close_idx = content.find('</div> <!-- End container -->')
    if close_idx != -1:
        base_content = content[:close_idx]
    else:
        base_content = content.replace('</body>\n</html>', '').replace('</body></html>', '')

    parts = []

    # PART 61
    part61 = """<!-- ═══ PART 61/100 · IHT CASES Q205–Q207 ═══ -->
<section class="part-section" id="part-61">
  <div class="part-header">
    <div class="part-kicker">ACT 3 • SECTION B OT CASES</div>
    <h2 class="part-title">Part 61: Section B OT Case Studies — Q205 Roman, Q206 Adana & Q207 Tony & Anita</h2>
    <p class="part-subtitle">Transferred unused spouse NRB (up to 100%), deductible estate liabilities, and CLT death tax liability.</p>
  </div>
</section>
<!-- ═══ END PART 61/100 ═══ -->"""
    parts.append(part61)

    # PART 62
    part62 = """<!-- ═══ PART 62/100 · IHT CASES Q208–Q209 ═══ -->
<section class="part-section" id="part-62">
  <div class="part-header">
    <div class="part-kicker">ACT 3 • SECTION B OT CASES</div>
    <h2 class="part-title">Part 62: Section B OT Case Studies — Q208 Nagina & Rishi & Q209 Dianne</h2>
    <p class="part-subtitle">Related settlements, unquoted share valuation loss to donor, and PET taper relief timing.</p>
  </div>
</section>
<!-- ═══ END PART 62/100 ═══ -->"""
    parts.append(part62)

    # PART 63
    part63 = """<!-- ═══ PART 63/100 · IHT MASTERCLASS Q210–Q212 ═══ -->
<section class="part-section" id="part-63">
  <div class="part-header">
    <div class="part-kicker">ACT 3 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 63: Section C Masterclass — Q210 Aurora, Q211 James & Q212 Jessica (10 Marks Each)</h2>
    <p class="part-subtitle">Constructed response scenarios on lifetime gifts, death estate tax, and IHT planning.</p>
  </div>
</section>
<!-- ═══ END PART 63/100 ═══ -->"""
    parts.append(part63)

    # PART 64
    part64 = """<!-- ═══ PART 64/100 · CT-01 CT FUNDAMENTALS & RATES ═══ -->
<section class="part-section" id="part-64">
  <div class="part-header">
    <div class="part-kicker">ACT 4 • CORPORATION TAX</div>
    <h2 class="part-title">Part 64: CT-01 Corporation Tax Accounting Periods, FY2023–2025 Rates & Marginal Relief</h2>
    <p class="part-subtitle">Accounting periods (max 12 months), Small Profits Rate (19%), Main Rate (25%), Marginal Relief formula (3/400ths), and Associated Companies division.</p>
  </div>

  <div class="card">
    <h3>🏢 Corporation Tax Rates & Thresholds (FA2025)</h3>
    <table class="fiscal-table">
      <thead>
        <tr><th>Profits Level (Augmented Profits)</th><th>Tax Rate / Tax Treatment</th><th>Upper / Lower Threshold (Divided by N)</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Profits ≤ £50,000 / N</strong></td><td class="num">Small Profits Rate = 19%</td><td class="num">Lower Limit = £50,000 / N</td></tr>
        <tr><td><strong>£50,000 / N &lt; Profits ≤ £250,000 / N</strong></td><td class="num">Main Rate 25% LESS Marginal Relief</td><td class="num">Marginal Relief Zone</td></tr>
        <tr><td><strong>Profits > £250,000 / N</strong></td><td class="num">Main Rate = 25%</td><td class="num">Upper Limit = £250,000 / N</td></tr>
      </tbody>
    </table>

    <div class="computation-box">
Marginal Relief Formula = (3 / 400) × [ Upper Limit - Augmented Profits ] × ( Taxable Total Profits / Augmented Profits )

Where:
• N = 1 + Number of Associated Companies worldwide.
• Augmented Profits = Taxable Total Profits (TTP) + Exempt ABGH Dividends from non-group companies.
    </div>

    <div class="callout callout-trap">
      <div class="callout-title">⚠️ TRAP WARNING: ASSOCIATED COMPANIES DIVISION</div>
      Upper (£250k) and Lower (£50k) limits are divided by <strong>N</strong> (where N = the company ITSELF + all worldwide associated companies active at any point in the AP). Do NOT count dormant companies!
    </div>
  </div>
</section>
<!-- ═══ END PART 64/100 ═══ -->"""
    parts.append(part64)

    # PART 65
    part65 = """<!-- ═══ PART 65/100 · CT-02 ADJUSTMENTS & NTLR ═══ -->
<section class="part-section" id="part-65">
  <div class="part-header">
    <div class="part-kicker">ACT 4 • CORPORATION TAX</div>
    <h2 class="part-title">Part 65: CT-02 Trading Adjustments, Non-Trade Loan Relationships (NTLR) & Property Income</h2>
    <p class="part-subtitle">Disallowable items for companies, NTLR interest received vs non-trade interest paid, and Qualifying Charitable Donations (QCD).</p>
  </div>

  <div class="card">
    <h3>📖 Non-Trade Loan Relationships (NTLR) Rules</h3>
    <div class="computation-box">
NTLR Net Income = Non-Trading Interest Received (Accruals basis) - Non-Trading Interest Paid (Accruals basis)

• Interest paid on trading loans (e.g. loan to purchase delivery vans) = ALLOWABLE TRADING EXPENSE.
• Interest paid on non-trading loans (e.g. loan to buy shares / investment property) = DEDUCTED IN NTLR.
    </div>
  </div>
</section>
<!-- ═══ END PART 65/100 ═══ -->"""
    parts.append(part65)

    # PART 66
    part66 = """<!-- ═══ PART 66/100 · CT-03 CAPITAL ALLOWANCES ═══ -->
<section class="part-section" id="part-66">
  <div class="part-header">
    <div class="part-kicker">ACT 4 • CORPORATION TAX</div>
    <h2 class="part-title">Part 66: CT-03 Corporate Capital Allowances: Full Expensing & 50% Special Rate FYA</h2>
    <p class="part-subtitle">Full Expensing (100% FYA on main pool new plant & machinery), 50% Special Rate Pool FYA, AIA (£1M), and Structures & Buildings Allowance (SBA 3%).</p>
  </div>

  <div class="card">
    <h3>⚙️ Corporate Capital Allowances Matrix (FA2025)</h3>
    <table class="fiscal-table">
      <thead>
        <tr><th>Allowance Type</th><th>Rate & Pool Allocation</th><th>Qualifying Assets</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Full Expensing (100% FYA)</strong></td><td class="num">100% FYA (No cap limit!)</td><td>NEW & unused main pool plant & machinery purchased by companies.</td></tr>
        <tr><td><strong>50% Special Rate FYA</strong></td><td class="num">50% FYA (Balance to SR Pool @ 6%)</td><td>NEW & unused special rate pool assets (integral features).</td></tr>
        <tr><td><strong>Annual Investment Allowance (AIA)</strong></td><td class="num">100% FYA (Limit £1,000,000 p.a.)</td><td>Used or new assets, cars EXCLUDED.</td></tr>
        <tr><td><strong>Structures & Buildings Allowance (SBA)</strong></td><td class="num">3% Straight Line p.a.</td><td>New commercial structures/buildings.</td></tr>
      </tbody>
    </table>

    <div class="callout callout-hook">
      <div class="callout-title">🧠 MEMORY HOOK: FULL EXPENSING VS AIA ALLOCATION</div>
      Always allocate Full Expensing (100% FYA) to NEW main pool assets first. Then use AIA (£1,000,000) on SPECIAL RATE POOL assets (to get 100% immediate relief instead of 50% FYA)!
    </div>
  </div>
</section>
<!-- ═══ END PART 66/100 ═══ -->"""
    parts.append(part66)

    # PART 67
    part67 = """<!-- ═══ PART 67/100 · CT-04 TRADING LOSSES ═══ -->
<section class="part-section" id="part-67">
  <div class="part-header">
    <div class="part-kicker">ACT 4 • CORPORATION TAX</div>
    <h2 class="part-title">Part 67: CT-04 Corporate Trading Loss Reliefs</h2>
    <p class="part-subtitle">Current year set-off against total profits, 12-month carry-back, carry-forward relief against total profits (subject to £5M + 50% cap), and Terminal Loss Relief.</p>
  </div>

  <div class="card">
    <h3>📉 Corporate Trading Loss Options Summary</h3>
    <table class="fiscal-table">
      <thead>
        <tr><th>Loss Claim Type</th><th>Target Profits</th><th>Rules & Restrictions</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>s.37 Current Year Set-Off</strong></td><td>Total Profits of same accounting period (before QCDs).</td><td>Must claim ALL or NOTHING (QCDs may be lost).</td></tr>
        <tr><td><strong>s.37 Carry-Back (12 M M)</strong></td><td>Total Profits of preceding 12 months (LIFO).</td><td>Must claim current year s.37 FIRST before carry-back.</td></tr>
        <tr><td><strong>s.45A Carry-Forward</strong></td><td>Future Total Profits of subsequent APs.</td><td>Flexible amount claim. £5M deduction allowance + 50% excess cap.</td></tr>
      </tbody>
    </table>
  </div>
</section>
<!-- ═══ END PART 67/100 ═══ -->"""
    parts.append(part67)

    # PART 68
    part68 = """<!-- ═══ PART 68/100 · CT-05 GROUPS ═══ -->
<section class="part-section" id="part-68">
  <div class="part-header">
    <div class="part-kicker">ACT 4 • CORPORATION TAX</div>
    <h2 class="part-title">Part 68: CT-05 Corporate Groups: Group Relief & Chargeable Gains Groups</h2>
    <p class="part-subtitle">Group relief 75% direct/indirect trading loss surrender, gains group 75% direct / 51% overall no gain / no loss transfers, and associated companies.</p>
  </div>

  <div class="card">
    <h3>🌐 Corporate Group Structures Comparison</h3>
    <table class="fiscal-table">
      <thead>
        <tr><th>Feature</th><th>Group Relief Group (Losses)</th><th>Chargeable Gains Group</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Minimum Shareholding Requirement</strong></td><td>75% direct/indirect ordinary share capital</td><td>75% direct AND > 50% effective indirect holding</td></tr>
        <tr><td><strong>Surrenderable Items</strong></td><td>Current year trading losses, NTLR deficits, property losses</td><td>Asset transfers at No Gain / No Loss (Deemed cost transfer)</td></tr>
      </tbody>
    </table>
  </div>
</section>
<!-- ═══ END PART 68/100 ═══ -->"""
    parts.append(part68)

    # PART 69
    part69 = """<!-- ═══ PART 69/100 · CT-06 ADMIN & INSTALMENTS ═══ -->
<section class="part-section" id="part-69">
  <div class="part-header">
    <div class="part-kicker">ACT 4 • CORPORATION TAX</div>
    <h2 class="part-title">Part 69: CT-06 Administration, Filing Deadlines & Quarterly Instalments</h2>
    <p class="part-subtitle">CT600 return filing (12m post-AP), payment deadlines (9m 1d for small/medium vs quarterly instalments for large companies), iXBRL tagging, and corporate residence.</p>
  </div>

  <div class="card">
    <h3>📅 Quarterly Instalment Due Dates for Large Companies (12-Month AP)</h3>
    <p>A company is <strong>Large</strong> if Augmented Profits exceed <strong>£1,500,000 / N</strong>. Instalments are due on the 14th day of months 7, 10, 13, and 16 from start of AP:</p>
    <div class="computation-box">
For AP 1 April 2025 to 31 March 2026:
• 1st Instalment: 14 October 2025 (Month 7)
• 2nd Instalment: 14 January 2026 (Month 10)
• 3rd Instalment: 14 April 2026 (Month 13)
• 4th Instalment: 14 July 2026 (Month 16)
    </div>
  </div>
</section>
<!-- ═══ END PART 69/100 ═══ -->"""
    parts.append(part69)

    # PART 70
    part70 = """<!-- ═══ PART 70/100 · DRILLS Q213–Q222 ═══ -->
<section class="part-section" id="part-70">
  <div class="part-header">
    <div class="part-kicker">ACT 4 • DRILL MODULE</div>
    <h2 class="part-title">Part 70: Section A Corporation Tax Practice Drills (Q213–Q222)</h2>
    <p class="part-subtitle">NTLR interest calculations, marginal relief calculations, and associated companies count.</p>
  </div>

  <!-- DRILL Q218 -->
  <div class="drill-card" id="q218">
    <div class="drill-header">
      <span class="drill-title">Q218 • Flower Ltd's NTLR Income</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Flower Ltd's year ended 31 March 2026 results: Loan interest rec'd £35,000 (accrued £5,000). Loan interest paid on van fleet £10,000; Loan interest paid on loan to buy shares in trading company £8,000. What is NTLR income included in TTP?</p>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
Non-Trading Interest Receivable (Accruals basis):
Received £35,000 + Accrued £5,000 = £40,000

Non-Trading Interest Payable:
• Interest on van fleet loan (£10,000) = TRADING EXPENSE (Deductible in trade profit).
• Interest on share acquisition loan (£8,000) = NON-TRADE LOAN RELATIONSHIP DEDUCTION.

NTLR Net Income = £40,000 - £8,000 = £32,000
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: £32,000</strong><br>
        Remember trade loan interest is a trading deduction, while non-trade interest paid is offset against non-trade interest received in NTLR!
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q218" onchange="GAMIFICATION.toggleTask('q218', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>

</div> <!-- End container -->
</body>
</html>
<!-- ═══ END PART 70/100 ═══ -->"""
    parts.append(part70)

    new_content = base_content + '\n\n' + '\n\n'.join(parts)
    with open('TX-UK_Revision_Pack.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print('Successfully appended Session 7 (Parts 61 to 70) to TX-UK_Revision_Pack.html!')

if __name__ == '__main__':
    build_session_7()
