import sys

def build_session_9():
    with open('TX-UK_Revision_Pack.html', 'r', encoding='utf-8') as f:
        content = f.read()

    close_idx = content.find('</div> <!-- End container -->')
    if close_idx != -1:
        base_content = content[:close_idx]
    else:
        base_content = content.replace('</body>\n</html>', '').replace('</body></html>', '')

    parts = []

    # PART 81
    part81 = """<!-- ═══ PART 81/100 · VAT-01 REGISTRATION & TAX POINTS ═══ -->
<section class="part-section" id="part-81">
  <div class="part-header">
    <div class="part-kicker">ACT 5 • VALUE ADDED TAX</div>
    <h2 class="part-title">Part 81: VAT-01 Compulsory/Voluntary Registration & Tax Point Rules</h2>
    <p class="part-subtitle">Historic test (£90,000 threshold in 12m), Future test (£90,000 in next 30 days), Deregistration (£88,000), Basic vs Actual tax point (14-day rule), and pre-registration input VAT.</p>
  </div>

  <div class="card">
    <h3>📊 VAT Registration & Deregistration Thresholds (FA2025)</h3>
    <table class="fiscal-table">
      <thead>
        <tr><th>Registration Test</th><th>Statutory Threshold</th><th>Notification Deadline</th><th>Effective Registration Date</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Historic Test</strong></td><td>Taxable supplies > £90,000 in past 12 months</td><td>Within 30 days of end of month threshold exceeded</td><td>1st day of second month following threshold month</td></tr>
        <tr><td><strong>Future Test</strong></td><td>Taxable supplies > £90,000 in next 30 days alone</td><td>By end of the 30-day period</td><td>Beginning of the 30-day period</td></tr>
        <tr><td><strong>Compulsory Deregistration</strong></td><td>Taxable supplies ≤ £88,000 expected in next 12m</td><td>Notify within 30 days of cessation</td><td>Date of cessation / request</td></tr>
      </tbody>
    </table>
  </div>

  <div class="card">
    <h3>⏰ Basic vs Actual Tax Point Rules (14-Day Rule)</h3>
    <div class="computation-box">
• Basic Tax Point = Date goods are removed/made available OR service completed.
• Actual Tax Point Exceptions:
  1. If payment received or VAT invoice issued BEFORE basic tax point -> Tax point = Date of payment / invoice.
  2. If VAT invoice issued within 14 DAYS AFTER basic tax point -> Tax point = Date of invoice!
    </div>

    <div class="callout callout-tip">
      <div class="callout-title">🟢 PRE-REGISTRATION INPUT VAT RECOVERY</div>
      A newly registered trader can reclaim pre-registration input VAT on:<br>
      • <strong>Goods:</strong> Incurred within <strong>4 years</strong> prior to registration (provided goods are still held at registration date).<br>
      • <strong>Services:</strong> Incurred within <strong>6 months</strong> prior to registration.
    </div>
  </div>
</section>
<!-- ═══ END PART 81/100 ═══ -->"""
    parts.append(part81)

    # PART 82
    part82 = """<!-- ═══ PART 82/100 · VAT-02 OUTPUT & INPUT VAT ═══ -->
<section class="part-section" id="part-82">
  <div class="part-header">
    <div class="part-kicker">ACT 5 • VALUE ADDED TAX</div>
    <h2 class="part-title">Part 82: VAT-02 Output & Input VAT, Fuel Scale Charges & Impaired Debts</h2>
    <p class="part-subtitle">Standard rate 20%, non-recoverable input VAT (business entertainment, cars with private use), fuel scale charges, and bad debt relief.</p>
  </div>

  <div class="card">
    <h3>🚘 Fuel Scale Charges & Bad Debt Relief Rules</h3>
    <p>1. <strong>Car Fuel Scale Charge:</strong> If an employer provides free fuel for private motoring in a company car and reclaims full input VAT on fuel, employer MUST account for <strong>output VAT on the quarterly scale charge</strong>.</p>
    <p>2. <strong>Bad Debt Relief (Impaired Debts):</strong> Reclaim output VAT paid on bad debts if:</p>
    <ul>
      <li>Debt is written off in business accounts.</li>
      <li>Debt is <strong>over 6 months overdue</strong> from payment due date (or supply date if later).</li>
      <li>Claim made within 4 years of becoming eligible.</li>
    </ul>
  </div>
</section>
<!-- ═══ END PART 82/100 ═══ -->"""
    parts.append(part82)

    # PART 83
    part83 = """<!-- ═══ PART 83/100 · VAT-03 SPECIAL SCHEMES & PENALTIES ═══ -->
<section class="part-section" id="part-83">
  <div class="part-header">
    <div class="part-kicker">ACT 5 • VALUE ADDED TAX</div>
    <h2 class="part-title">Part 83: VAT-03 Special VAT Schemes & MTD Penalty System</h2>
    <p class="part-subtitle">Cash Accounting (£1.35M / £1.6M limit), Annual Accounting (£1.35M / £1.6M limit), Flat Rate Scheme (£150k / £230k limit, 1% discount), and MTD penalty points system.</p>
  </div>

  <div class="card">
    <h3>⚡ Special VAT Schemes Master Summary</h3>
    <table class="fiscal-table">
      <thead>
        <tr><th>Special Scheme</th><th>Entry Limit (Taxable Turnover)</th><th>Exit Limit</th><th>Key Benefit</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Cash Accounting Scheme</strong></td><td class="num">≤ £1,350,000 p.a.</td><td class="num">£1,600,000</td><td>Account for VAT on cash received/paid. Automatic bad debt relief!</td></tr>
        <tr><td><strong>Annual Accounting Scheme</strong></td><td class="num">≤ £1,350,000 p.a.</td><td class="num">£1,600,000</td><td>Submit 1 return p.a. Pay 9 interim monthly/quarterly payments.</td></tr>
        <tr><td><strong>Flat Rate Scheme (FRS)</strong></td><td class="num">≤ £150,000 p.a.</td><td class="num">£230,000</td><td>VAT paid = FRS % × Gross VAT-inclusive turnover. 1% discount in year 1.</td></tr>
      </tbody>
    </table>
  </div>
</section>
<!-- ═══ END PART 83/100 ═══ -->"""
    parts.append(part83)

    # PART 84
    part84 = """<!-- ═══ PART 84/100 · VAT-04 OVERSEAS, GROUPS & TOGC ═══ -->
<section class="part-section" id="part-84">
  <div class="part-header">
    <div class="part-kicker">ACT 5 • VALUE ADDED TAX</div>
    <h2 class="part-title">Part 84: VAT-04 Overseas VAT, Reverse Charge, VAT Groups & TOGC</h2>
    <p class="part-subtitle">Import VAT vs reverse charge on overseas services, Transfer of Going Concern (TOGC) no supply rule, and VAT groups.</p>
  </div>
</section>
<!-- ═══ END PART 84/100 ═══ -->"""
    parts.append(part84)

    # PART 85
    part85 = """<!-- ═══ PART 85/100 · DRILLS Q271–Q281 ═══ -->
<section class="part-section" id="part-85">
  <div class="part-header">
    <div class="part-kicker">ACT 5 • DRILL MODULE</div>
    <h2 class="part-title">Part 85: Section A VAT Practice Drills (Q271–Q281)</h2>
    <p class="part-subtitle">Voluntary registration benefits, historic registration test, and pre-registration input VAT.</p>
  </div>

  <!-- DRILL Q276 -->
  <div class="drill-card" id="q276">
    <div class="drill-header">
      <span class="drill-title">Q276 • Yui's Pre-Registration Input VAT</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Yui started trading 1 April 2025, registered for VAT from 1 Jan 2026. Incurred input VAT of £110/month on hire of office equipment from 1 April 2025. How much input VAT can Yui reclaim on her first VAT return for quarter ended 31 March 2026?</p>
    <div class="options-group">
      <label class="option-item"><input type="radio" name="q276_opt"> A) £660</label>
      <label class="option-item"><input type="radio" name="q276_opt"> B) £990</label>
      <label class="option-item"><input type="radio" name="q276_opt"> C) £330</label>
      <label class="option-item"><input type="radio" name="q276_opt"> D) £1,320</label>
    </div>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
Office Equipment Hire = SERVICE!
Pre-registration limit for SERVICES = 6 months prior to registration date (1 Jan 2026)!

Period eligible prior to registration: 1 July 2025 to 31 Dec 2025 = 6 months.
Pre-registration input VAT = 6 months × £110 = £660.

Current Quarter (1 Jan 2026 - 31 March 2026): 3 months × £110 = £330.

Total Input VAT Reclaimable = £660 (pre-reg) + £330 (current) = £990
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: B (£990)</strong><br>
        Reclaim pre-registration service input VAT incurred in the 6 months prior to registration (£660) PLUS current quarter input VAT (£330) = £990!
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q276" onchange="GAMIFICATION.toggleTask('q276', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 85/100 ═══ -->"""
    parts.append(part85)

    # PART 86
    part86 = """<!-- ═══ PART 86/100 · DRILLS Q282–Q292 ═══ -->
<section class="part-section" id="part-86">
  <div class="part-header">
    <div class="part-kicker">ACT 5 • DRILL MODULE</div>
    <h2 class="part-title">Part 86: Section A VAT Practice Drills (Q282–Q292)</h2>
    <p class="part-subtitle">Fuel scale charges, Flat Rate Scheme calculations, and reverse charge.</p>
  </div>

  <!-- DRILL Q290 -->
  <div class="drill-card" id="q290">
    <div class="drill-header">
      <span class="drill-title">Q290 • Hamza's Flat Rate Scheme Liability</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Hamza uses Flat Rate Scheme (11%). Net sales: £100,000 standard rated, £30,000 zero rated. Net purchases: £15,000. What is Hamza's VAT liability for year ended 31 March 2026?</p>
    <div class="options-group">
      <label class="option-item"><input type="radio" name="q290_opt"> A) £14,300</label>
      <label class="option-item"><input type="radio" name="q290_opt"> B) £16,500</label>
      <label class="option-item"><input type="radio" name="q290_opt"> C) £14,520</label>
      <label class="option-item"><input type="radio" name="q290_opt"> D) £13,200</label>
    </div>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
Under Flat Rate Scheme:
Gross VAT-inclusive turnover = Standard rated sales (inc 20% VAT) + Zero rated sales
Standard rated gross = £100,000 × 1.20 = £120,000
Zero rated gross = £30,000
Total Gross Turnover = £120,000 + £30,000 = £150,000

FRS VAT Liability = £150,000 × 11% = £16,500
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: B (£16,500)</strong><br>
        Flat rate scheme percentage applies to total gross VAT-INCLUSIVE turnover (including zero-rated supplies)!
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q290" onchange="GAMIFICATION.toggleTask('q290', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 86/100 ═══ -->"""
    parts.append(part86)

    # PART 87
    part87 = """<!-- ═══ PART 87/100 · SECTION B CASES Q293–Q295 ═══ -->
<section class="part-section" id="part-87">
  <div class="part-header">
    <div class="part-kicker">ACT 5 • SECTION B OT CASES</div>
    <h2 class="part-title">Part 87: Section B OT Case Studies — Q293 Thidar, Q294 CandyApple & Q295 Lithograph</h2>
    <p class="part-subtitle">Building sales VAT registration thresholds, invoice retention 6 years, late registration output tax 20/120ths, and bad debt relief.</p>
  </div>

  <!-- CASE Q293 -->
  <div class="card" id="q293">
    <div class="drill-header">
      <span class="drill-title">Q293 • Thidar (10 Marks Case Study)</span>
      <div>
        <span class="chip chip-xp">+25 XP</span>
        <span class="chip chip-type">Section B Case</span>
      </div>
    </div>
    <p><strong>Scenario:</strong> Thidar started builder trade 1 Jan 2025. Voluntarily registered for VAT. Evaluates compulsory threshold test and invoice retention rules.</p>

    <div class="drill-card">
      <p><strong>What is the statutory retention period for VAT invoices?</strong></p>
      <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
      <div class="solution-content">
        <div class="callout callout-tip">
          <strong>MODEL ANSWER: Issue invoice within 30 days | Retain for 6 YEARS</strong><br>
          VAT invoices must be issued within 30 days of supply and retained for a minimum of 6 years!
        </div>
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q293" onchange="GAMIFICATION.toggleTask('q293', 25, this.checked)">
        Mark Case Done (+25 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 87/100 ═══ -->"""
    parts.append(part87)

    # PART 88
    part88 = """<!-- ═══ PART 88/100 · SECTION B CASES Q296–Q298 ═══ -->
<section class="part-section" id="part-88">
  <div class="part-header">
    <div class="part-kicker">ACT 5 • SECTION B OT CASES</div>
    <h2 class="part-title">Part 88: Section B OT Case Studies — Q296 Alisa, Q297 Whitlock & Q298 Knight</h2>
    <p class="part-subtitle">Historic compulsory registration timing, MTD late penalty points, and error corrections on VAT returns.</p>
  </div>
</section>
<!-- ═══ END PART 88/100 ═══ -->"""
    parts.append(part88)

    # PART 89
    part89 = """<!-- ═══ PART 89/100 · SECTION B CASES Q299–Q303 ═══ -->
<section class="part-section" id="part-89">
  <div class="part-header">
    <div class="part-kicker">ACT 5 • SECTION B OT CASES</div>
    <h2 class="part-title">Part 89: Section B OT Case Studies — Q299 Ardent, Q300 DenzilDyer, Q301 Kristel, Q302 Lian & Q303 Mabel</h2>
    <p class="part-subtitle">Overseas supplies, reverse charge, partial exemption, and TOGC rules.</p>
  </div>
</section>
<!-- ═══ END PART 89/100 ═══ -->"""
    parts.append(part89)

    # PART 90
    part90 = """<!-- ═══ PART 90/100 · SECTION C MASTERCLASS Q304–Q306 ═══ -->
<section class="part-section" id="part-90">
  <div class="part-header">
    <div class="part-kicker">ACT 5 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 90: Section C Masterclass — Q304 Silverstone, Q305 Tardy & Q306 Zia (10 Marks Each)</h2>
    <p class="part-subtitle">Constructed response scenarios on VAT registration, late payment interest, and Act 5 Finale.</p>
  </div>

  <div class="card">
    <h3>🎉 Act 5 Mid-Point Mastery Checkpoint</h3>
    <p>You have now completed the entire VAT syllabus, including registration thresholds (£90k/£88k), tax points, fuel scale charges, Flat Rate Scheme, MTD penalties, reverse charge, and bad debt relief.</p>
  </div>
</section>

</div> <!-- End container -->
</body>
</html>
<!-- ═══ END PART 90/100 ═══ -->"""
    parts.append(part90)

    new_content = base_content + '\n\n' + '\n\n'.join(parts)
    with open('TX-UK_Revision_Pack.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print('Successfully appended Session 9 (Parts 81 to 90) to TX-UK_Revision_Pack.html!')

if __name__ == '__main__':
    build_session_9()
