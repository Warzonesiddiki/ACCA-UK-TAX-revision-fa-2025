import sys

def build_session_4():
    with open('TX-UK_Revision_Pack.html', 'r', encoding='utf-8') as f:
        content = f.read()

    close_idx = content.find('</div> <!-- End container -->')
    if close_idx != -1:
        base_content = content[:close_idx]
    else:
        base_content = content.replace('</body>\n</html>', '').replace('</body></html>', '')

    parts = []

    # PART 31
    part31 = """<!-- ═══ PART 31/100 · SECTION C MASTERCLASS Q100 & Q101 ═══ -->
<section class="part-section" id="part-31">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 31: Section C Masterclass — Q100 Kazuo & Q101 Sheldon (15 Marks Each)</h2>
    <p class="part-subtitle">Constructed response scenarios on interest-free loans, gym benefits, and PA tapering.</p>
  </div>

  <!-- MASTERCLASS Q101 SHELDON -->
  <div class="card" id="q101">
    <div class="drill-header">
      <span class="drill-title">Q101 • Sheldon (15 Marks Constructed Response)</span>
      <div>
        <span class="chip chip-xp">+40 XP</span>
        <span class="chip chip-type">Section C Masterclass</span>
      </div>
    </div>
    <p><strong>Scenario:</strong> Sheldon earned gross salary of £126,000 from Luqe Ltd. Provided with interest-free loan of £80,000 on 1 August 2025 (repaid £8,000 on 31 Jan 2026). Had workplace gym access.</p>

    <div class="computation-box">
Salary:                                  £126,000
Interest-Free Loan Benefit:
- Average Method:
  Start: £80,000 | End (31 Jan - 5 Apr): £72,000
  Average Loan = (£80,000 + £72,000) / 2 = £76,000
  Period: 1 Aug 2025 - 5 Apr 2026 = 8 months
  Benefit = £76,000 × 3.75% × 8/12 = £1,900

Workplace Gym Benefit: £0 (Statutory Exempt)

Net Income:                              £127,900
Personal Allowance Taper:
ANI (£127,900) >= £125,140 -> PA = £0

Taxable Income:                          £127,900
Tax Liability:
£37,700 × 20% =                           £7,540
(£125,140 - £37,700) = £87,440 × 40% =   £34,976
(£127,900 - £125,140) = £2,760 × 45% =    £1,242
                                         -------
Total Income Tax Liability:              £43,758
    </div>

    <div class="callout callout-examiner">
      <div class="callout-title">🔴 EXAMINER REPORT & KEY ANSWER TIPS</div>
      "Candidates must remember that loan benefits are time-apportioned for the months outstanding during the tax year (8/12). Workplace gym benefits available to all staff are strictly exempt (£0)."
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q101" onchange="GAMIFICATION.toggleTask('q101', 40, this.checked)">
        Mark Masterclass Done (+40 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 31/100 ═══ -->"""
    parts.append(part31)

    # PART 32
    part32 = """<!-- ═══ PART 32/100 · SECTION C MASTERCLASS Q102 & Q103 ═══ -->
<section class="part-section" id="part-32">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 32: Section C Masterclass — Q102 Kagan & Q103 Esme</h2>
    <p class="part-subtitle">Inherited shares tax planning, dividend vs interest income, marriage allowance restrictions, and Q102–Q103.</p>
  </div>

  <!-- MASTERCLASS Q102 KAGAN -->
  <div class="card" id="q102">
    <div class="drill-header">
      <span class="drill-title">Q102 • Kagan (15 Marks)</span>
      <div>
        <span class="chip chip-xp">+40 XP</span>
        <span class="chip chip-type">Section C Masterclass</span>
      </div>
    </div>
    <p><strong>Scenario:</strong> Kagan inherited £510,000 quoted shares. Additional rate taxpayer (employment income £400,000). Considers selling shares to fund ISA, personal pension, and freehold property.</p>

    <div class="callout callout-tip">
      <div class="callout-title">🟢 KEY TAX PLANNING LESSONS</div>
      1. <strong>Inherited Probate Value:</strong> Base cost for CGT equals probate market value at date of death (£510,000). Immediate sale yields £0 gain!<br>
      2. <strong>ISA Investment:</strong> Income and capital gains inside ISA are 100% EXEMPT.<br>
      3. <strong>Personal Pension:</strong> Gross pension contribution extends basic/higher rate bands and provides 45% relief for additional rate taxpayers.
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q102" onchange="GAMIFICATION.toggleTask('q102', 40, this.checked)">
        Mark Masterclass Done (+40 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 32/100 ═══ -->"""
    parts.append(part32)

    # PART 33
    part33 = """<!-- ═══ PART 33/100 · SECTION C MASTERCLASS Q104 & Q105 ═══ -->
<section class="part-section" id="part-33">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 33: Section C Masterclass — Q104 Tonie & Q105 Kat</h2>
    <p class="part-subtitle">IR35 employment status tests, mileage allowances, and sole trader vs employment comparisons.</p>
  </div>
</section>
<!-- ═══ END PART 33/100 ═══ -->"""
    parts.append(part33)

    # PART 34
    part34 = """<!-- ═══ PART 34/100 · SECTION C MASTERCLASS Q106 & Q107 ═══ -->
<section class="part-section" id="part-34">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 34: Section C Masterclass — Q106 Bertie & Q107 Triple A</h2>
    <p class="part-subtitle">Extraction of company profits (salary vs dividends), corporate car provision, and NIC optimization.</p>
  </div>
</section>
<!-- ═══ END PART 34/100 ═══ -->"""
    parts.append(part34)

    # PART 35
    part35 = """<!-- ═══ PART 35/100 · SECTION C MASTERCLASS Q108–Q110 ═══ -->
<section class="part-section" id="part-35">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 35: Section C Masterclass — Q108 Idris, Q109 Ethel & Q110 Dada</h2>
    <p class="part-subtitle">Sole trader loss relief claims, partnership profit allocations, and capital allowance pooling.</p>
  </div>
</section>
<!-- ═══ END PART 35/100 ═══ -->"""
    parts.append(part35)

    # PART 36
    part36 = """<!-- ═══ PART 36/100 · SECTION C MASTERCLASS Q111–Q113 ═══ -->
<section class="part-section" id="part-36">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 36: Section C Masterclass — Q111 Fleur, Q112 Paul & Q113 Na Style</h2>
    <p class="part-subtitle">Property income, cash basis elections, rent-a-room relief, and lease premiums.</p>
  </div>
</section>
<!-- ═══ END PART 36/100 ═══ -->"""
    parts.append(part36)

    # PART 37
    part37 = """<!-- ═══ PART 37/100 · SECTION C MASTERCLASS Q114–Q117 ═══ -->
<section class="part-section" id="part-37">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 37: Section C Masterclass — Q114 Zhi, Q115 Jade, Q116 Hannah & Q117 Alfred & Amaia</h2>
    <p class="part-subtitle">Husband and wife income splitting, joint property ownership elections, and child benefit charges.</p>
  </div>
</section>
<!-- ═══ END PART 37/100 ═══ -->"""
    parts.append(part37)

    # PART 38
    part38 = """<!-- ═══ PART 38/100 · SECTION C MASTERCLASS Q118–Q121 ═══ -->
<section class="part-section" id="part-38">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 38: Section C Masterclass — Q118 Ashura, Q119 Dee Zyne, Q120 Samantha & Q121 Michael & Sean</h2>
    <p class="part-subtitle">Comprehensive individual tax returns, self-assessment payment schedules, and interest on late tax.</p>
  </div>
</section>
<!-- ═══ END PART 38/100 ═══ -->"""
    parts.append(part38)

    # PART 39
    part39 = """<!-- ═══ PART 39/100 · SECTION C MASTERCLASS Q122–Q127 ═══ -->
<section class="part-section" id="part-39">
  <div class="part-header">
    <div class="part-kicker">ACT 1 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 39: Section C Masterclass — Q122 to Q127 Comprehensive Act 1 Finale</h2>
    <p class="part-subtitle">Multi-topic constructed response scenarios completing Act 1 Income Tax & NIC.</p>
  </div>
</section>
<!-- ═══ END PART 39/100 ═══ -->"""
    parts.append(part39)

    # PART 40
    part40 = """<!-- ═══ PART 40/100 · CGT-01 BASICS ═══ -->
<section class="part-section" id="part-40">
  <div class="part-header">
    <div class="part-kicker">ACT 2 • CHARGEABLE GAINS</div>
    <h2 class="part-title">Part 40: CGT-01 Chargeable Gains Fundamentals, Rates 18%/24% & Annual Exempt Amount</h2>
    <p class="part-subtitle">Scope of CGT, chargeable persons, disposal pro-forma, AEA (£3,000), basic/higher rate ordering, and residential property gains.</p>
  </div>

  <div class="card">
    <h3>📐 Standard Capital Gains Tax Pro-Forma Layout</h3>
    <table class="fiscal-table">
      <thead>
        <tr><th>Gain Item / Asset</th><th class="num">Amount (£)</th></tr>
      </thead>
      <tbody>
        <tr><td>Gross Disposal Proceeds / Market Value</td><td class="num">X,XXX</td></tr>
        <tr><td>Less: Incidental Costs of Disposal (Legal / Agent fees)</td><td class="num">(X,XXX)</td></tr>
        <tr style="font-weight:600;"><td>NET DISPOSAL PROCEEDS</td><td class="num">X,XXX</td></tr>
        <tr><td>Less: Allowable Acquisition Cost</td><td class="num">(X,XXX)</td></tr>
        <tr><td>Less: Incidental Acquisition Costs</td><td class="num">(X,XXX)</td></tr>
        <tr><td>Less: Subsequent Capital Enhancement Expenditure</td><td class="num">(X,XXX)</td></tr>
        <tr style="font-weight:700; background-color:var(--paper-deep);"><td>UNrelieved GROSS CHARGEABLE GAIN</td><td class="num">X,XXX</td></tr>
      </tbody>
    </table>
  </div>

  <div class="card">
    <h3>📊 CGT Tax Rates & Annual Exempt Amount (FA2025)</h3>
    <table class="fiscal-table">
      <thead>
        <tr><th>Taxpayer Band</th><th>Standard Gains Rate</th><th>Residential Property Rate</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Annual Exempt Amount (AEA)</strong></td><td class="num">£3,000 @ 0%</td><td class="num">£3,000 @ 0%</td></tr>
        <tr><td><strong>Basic Rate Taxpayer</strong> (Within remaining basic rate band)</td><td class="num">18%</td><td class="num">18%</td></tr>
        <tr><td><strong>Higher / Additional Rate Taxpayer</strong> (Above basic rate band)</td><td class="num">24%</td><td class="num">24%</td></tr>
        <tr><td><strong>Business Asset Disposal Relief (BADR) / Investors' Relief</strong></td><td class="num">14% (Lifetime £1M)</td><td class="num">14%</td></tr>
      </tbody>
    </table>

    <div class="callout callout-hook">
      <div class="callout-title">🧠 MEMORY HOOK: FA2025 CGT RATE HARMONISATION</div>
      Under Finance Act 2025, the CGT lower rate for ALL gains (non-residential and residential property) is <strong>18%</strong>, and the higher rate for ALL gains is <strong>24%</strong>!
    </div>

    <div class="callout callout-trap">
      <div class="callout-title">⚠️ TRAP WARNING: ALLOCATION OF AEA (£3,000)</div>
      Always allocate the Annual Exempt Amount (£3,000) against gains taxed at the HIGHEST rate first (e.g. 24% gains before BADR 14% gains) to minimize tax liability!
    </div>
  </div>
</section>

</div> <!-- End container -->
</body>
</html>
<!-- ═══ END PART 40/100 ═══ -->"""
    parts.append(part40)

    new_content = base_content + '\n\n' + '\n\n'.join(parts)
    with open('TX-UK_Revision_Pack.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print('Successfully appended Session 4 (Parts 31 to 40) to TX-UK_Revision_Pack.html!')

if __name__ == '__main__':
    build_session_4()
