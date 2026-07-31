import sys

def build_session_6():
    with open('TX-UK_Revision_Pack.html', 'r', encoding='utf-8') as f:
        content = f.read()

    close_idx = content.find('</div> <!-- End container -->')
    if close_idx != -1:
        base_content = content[:close_idx]
    else:
        base_content = content.replace('</body>\n</html>', '').replace('</body></html>', '')

    parts = []

    # PART 51
    part51 = """<!-- ═══ PART 51/100 · CGT CASES Q171–Q174 ═══ -->
<section class="part-section" id="part-51">
  <div class="part-header">
    <div class="part-kicker">ACT 2 • SECTION B OT CASES</div>
    <h2 class="part-title">Part 51: Section B OT Case Studies — Q171 Mick Stone, Q172 Expansion, Q173 Kat & Q174 Fogo & Netta</h2>
    <p class="part-subtitle">CGT losses set-off, unquoted share disposals, and spousal transfers.</p>
  </div>
</section>
<!-- ═══ END PART 51/100 ═══ -->"""
    parts.append(part51)

    # PART 52
    part52 = """<!-- ═══ PART 52/100 · CGT MASTERCLASS Q175–Q177 ═══ -->
<section class="part-section" id="part-52">
  <div class="part-header">
    <div class="part-kicker">ACT 2 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 52: Section C Masterclass — Q175 David & Angela, Q176 Bill Ding & Q177 Ginger & Nigel</h2>
    <p class="part-subtitle">10-mark constructed response scenarios on BADR, Gift Holdover relief, and corporate share disposals.</p>
  </div>
</section>
<!-- ═══ END PART 52/100 ═══ -->"""
    parts.append(part52)

    # PART 53
    part53 = """<!-- ═══ PART 53/100 · CGT MASTERCLASS Q178–Q179 ═══ -->
<section class="part-section" id="part-53">
  <div class="part-header">
    <div class="part-kicker">ACT 2 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 53: Section C Masterclass — Q178 Daljeet & Q179 Luna Ltd</h2>
    <p class="part-subtitle">Investors' Relief, corporate share pool disposals, and indexation allowance calculations.</p>
  </div>
</section>
<!-- ═══ END PART 53/100 ═══ -->"""
    parts.append(part53)

    # PART 54
    part54 = """<!-- ═══ PART 54/100 · IHT-01 TRANSFERS & EXEMPTIONS ═══ -->
<section class="part-section" id="part-54">
  <div class="part-header">
    <div class="part-kicker">ACT 3 • INHERITANCE TAX</div>
    <h2 class="part-title">Part 54: IHT-01 Lifetime Transfers, Exemptions & PET vs CLT Classification</h2>
    <p class="part-subtitle">Potentially Exempt Transfers (PETs), Chargeable Lifetime Transfers (CLTs), Annual Exemption (£3,000), Small Gifts (£250), Marriage gifts, and spouse transfers.</p>
  </div>

  <div class="card">
    <h3>🏛️ Classification of Lifetime Gifts Matrix</h3>
    <table class="fiscal-table">
      <thead>
        <tr><th>Recipient / Gift Type</th><th>IHT Classification</th><th>Immediate Lifetime Tax?</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Spouse / Civil Partner</strong></td><td>100% EXEMPT Transfer</td><td>NO (0% tax)</td></tr>
        <tr><td><strong>Individual (e.g. Son / Daughter / Friend)</strong></td><td>Potentially Exempt Transfer (PET)</td><td>NO (Taxable ONLY if donor dies within 7 years)</td></tr>
        <tr><td><strong>Discretionary Trust / Company</strong></td><td>Chargeable Lifetime Transfer (CLT)</td><td>YES (Immediate lifetime tax @ 20% or 25%)</td></tr>
      </tbody>
    </table>
  </div>

  <div class="card">
    <h3>🎁 Master List of Statutory IHT Exemptions</h3>
    <p>1. <strong>Spouse Exemption:</strong> Unlimited transfers between UK-domiciled spouses.</p>
    <p>2. <strong>Annual Exemption (AE):</strong> <strong>£3,000 per tax year</strong>. Unused AE can be carried forward 1 tax year only (used AFTER current year AE).</p>
    <p>3. <strong>Small Gifts Exemption:</strong> Up to <strong>£250 per recipient per tax year</strong> (cannot be combined with AE on same person).</p>
    <p>4. <strong>Marriage / Civil Partnership Exemption:</strong> Parent = <strong>£5,000</strong> | Grandparent / Remote ancestor = <strong>£2,500</strong> | Bride / Groom to each other = <strong>£2,500</strong> | Any other person = <strong>£1,000</strong>.</p>
    <p>5. <strong>Normal Expenditure Out of Income:</strong> Exempt if paid regularly out of surplus net income without reducing standard of living.</p>
  </div>
</section>
<!-- ═══ END PART 54/100 ═══ -->"""
    parts.append(part54)

    # PART 55
    part55 = """<!-- ═══ PART 55/100 · IHT-02 LIFETIME TAX & TAPER RELIEF ═══ -->
<section class="part-section" id="part-55">
  <div class="part-header">
    <div class="part-kicker">ACT 3 • INHERITANCE TAX</div>
    <h2 class="part-title">Part 55: IHT-02 Lifetime Tax Computations, Cumulation & Death Taper Relief</h2>
    <p class="part-subtitle">Grossing up rules (20% donee vs 25% donor), 7-year cumulation window, Nil Rate Band (£325k), and Taper Relief table.</p>
  </div>

  <div class="card">
    <h3>📊 Death Taper Relief Table (Gifts Made 3–7 Years Prior to Death)</h3>
    <table class="fiscal-table">
      <thead>
        <tr><th>Years Between Gift and Death</th><th>Percentage Reduction in Tax</th><th>Effective Tax Rate on Excess</th></tr>
      </thead>
      <tbody>
        <tr><td>0 to 3 years</td><td class="num">0% (No reduction)</td><td class="num">40.0%</td></tr>
        <tr><td>More than 3 but less than 4 years</td><td class="num">20% reduction</td><td class="num">32.0%</td></tr>
        <tr><td>More than 4 but less than 5 years</td><td class="num">40% reduction</td><td class="num">24.0%</td></tr>
        <tr><td>More than 5 but less than 6 years</td><td class="num">60% reduction</td><td class="num">16.0%</td></tr>
        <tr><td>More than 6 but less than 7 years</td><td class="num">80% reduction</td><td class="num">8.0%</td></tr>
        <tr><td>7 years or more</td><td class="num">100% EXEMPT</td><td class="num">0.0%</td></tr>
      </tbody>
    </table>

    <div class="callout callout-trap">
      <div class="callout-title">⚠️ TRAP WARNING: TAPER RELIEF APPLIES TO TAX, NOT GIFT VALUE</div>
      Taper relief reduces the <strong>INHERITANCE TAX PAYABLE</strong>, NOT the value of the gift! Always calculate full tax at 40% on excess over NRB first, then apply the taper % reduction!
    </div>
  </div>
</section>
<!-- ═══ END PART 55/100 ═══ -->"""
    parts.append(part55)

    # PART 56
    part56 = """<!-- ═══ PART 56/100 · IHT-03 DEATH ESTATE ═══ -->
<section class="part-section" id="part-56">
  <div class="part-header">
    <div class="part-kicker">ACT 3 • INHERITANCE TAX</div>
    <h2 class="part-title">Part 56: IHT-03 Death Estate Computation, NRB, RNRB & Spouse Transfers</h2>
    <p class="part-subtitle">Nil Rate Band (£325,000), Residence Nil Rate Band (£175,000), unutilised spouse NRB/RNRB transfer (up to 100%), and 40% death tax rate.</p>
  </div>

  <div class="card">
    <h3>🏠 Residence Nil Rate Band (RNRB) Rules</h3>
    <p>1. <strong>RNRB Maximum:</strong> <strong>£175,000</strong> per individual (FA2025).</p>
    <p>2. <strong>Qualifying Criteria:</strong> Applies when a <strong>main residence</strong> is left to <strong>direct descendants</strong> (children, step-children, grandchildren).</p>
    <p>3. <strong>Unused RNRB Spouse Transfer:</strong> Up to <strong>100%</strong> of unused RNRB can be transferred to a surviving spouse (providing a total potential combined tax-free threshold of <strong>£1,000,000</strong> = £325k + £325k NRB + £175k + £175k RNRB!).</p>
    <p>4. <strong>RNRB Taper Threshold:</strong> Tapered by £1 for every £2 that the gross death estate exceeds <strong>£2,000,000</strong>.</p>
  </div>
</section>
<!-- ═══ END PART 56/100 ═══ -->"""
    parts.append(part56)

    # PART 57
    part57 = """<!-- ═══ PART 57/100 · IHT-04 ADMIN & PLANNING ═══ -->
<section class="part-section" id="part-57">
  <div class="part-header">
    <div class="part-kicker">ACT 3 • INHERITANCE TAX</div>
    <h2 class="part-title">Part 57: IHT-04 Administration, Payment Dates & Tax Planning</h2>
    <p class="part-subtitle">Due dates for lifetime tax vs death tax, liability for tax (donors, donees, trustees, personal representatives), and IHT mitigation strategies.</p>
  </div>

  <div class="card">
    <h3>📅 IHT Payment Deadlines Matrix</h3>
    <table class="fiscal-table">
      <thead>
        <tr><th>IHT Transfer Event</th><th>Due Date for Payment</th><th>Person Liable</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Lifetime CLT (Made 6 April – 30 Sept)</strong></td><td>30 April in following calendar year</td><td>Donor (or Trustees if agreed)</td></tr>
        <tr><td><strong>Lifetime CLT (Made 1 Oct – 5 April)</strong></td><td>6 months after end of month of gift</td><td>Donor (or Trustees)</td></tr>
        <tr><td><strong>Death Tax on Lifetime PETs / CLTs</strong></td><td>6 months after end of month of death</td><td>Donee / Recipient of gift</td></tr>
        <tr><td><strong>Death Tax on Death Estate</strong></td><td>6 months after end of month of death</td><td>Personal Representatives (Executors)</td></tr>
      </tbody>
    </table>
  </div>
</section>
<!-- ═══ END PART 57/100 ═══ -->"""
    parts.append(part57)

    # PART 58
    part58 = """<!-- ═══ PART 58/100 · DRILLS Q180–Q190 ═══ -->
<section class="part-section" id="part-58">
  <div class="part-header">
    <div class="part-kicker">ACT 3 • DRILL MODULE</div>
    <h2 class="part-title">Part 58: Section A IHT Practice Drills (Q180–Q190)</h2>
    <p class="part-subtitle">Lifetime exemptions, PET death tax, taper relief, and grossing up.</p>
  </div>

  <!-- DRILL Q181 -->
  <div class="drill-card" id="q181">
    <div class="drill-header">
      <span class="drill-title">Q181 • Cora's Death Tax on PET</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Cora gave cash £300,000 to niece on 30 April 2020. Made cash gift £500,000 to nephew on 31 May 2021 (after deducting exemptions). Cora died on 31 October 2025. What IHT was payable on death in respect of the £500,000 gift to her nephew?</p>
    <div class="options-group">
      <label class="option-item"><input type="radio" name="q181_opt"> A) £190,000</label>
      <label class="option-item"><input type="radio" name="q181_opt"> B) £110,000</label>
      <label class="option-item"><input type="radio" name="q181_opt"> C) £114,000</label>
      <label class="option-item"><input type="radio" name="q181_opt"> D) £76,000</label>
    </div>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
Gift 1 (30 April 2020): £300,000 PET -> Uses £300,000 of NRB (£325,000).
Remaining NRB available for Gift 2 = £325,000 - £300,000 = £25,000.

Gift 2 (31 May 2021): £500,000 PET to nephew.
Less Remaining NRB:                       (£25,000)
                                          --------
Excess Taxable Amount:                    £475,000

Full Death Tax @ 40%: £475,000 × 40% = £190,000

Taper Relief Check:
Gift date 31 May 2021 -> Death 31 Oct 2025.
Time elapsed = 4 years and 5 months (More than 4 but less than 5 years).
Taper Relief = 40% reduction!

Tax Payable = £190,000 × (100% - 40%) = £190,000 × 60% = £114,000
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: C (£114,000)</strong><br>
        Remember 7-year cumulation absorbs NRB in order of gifts made, and taper relief reduces full 40% tax by 40% for gifts made 4-5 years prior to death!
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q181" onchange="GAMIFICATION.toggleTask('q181', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 58/100 ═══ -->"""
    parts.append(part58)

    # PART 59
    part59 = """<!-- ═══ PART 59/100 · DRILLS Q191–Q201 ═══ -->
<section class="part-section" id="part-59">
  <div class="part-header">
    <div class="part-kicker">ACT 3 • DRILL MODULE</div>
    <h2 class="part-title">Part 59: Section A IHT Practice Drills (Q191–Q201)</h2>
    <p class="part-subtitle">Loss on sale of shares/property, valuation of unquoted shares (related settlements), and liabilities deductible from estate.</p>
  </div>
</section>
<!-- ═══ END PART 59/100 ═══ -->"""
    parts.append(part59)

    # PART 60
    part60 = """<!-- ═══ PART 60/100 · SECTION B CASES Q202–Q204 ═══ -->
<section class="part-section" id="part-60">
  <div class="part-header">
    <div class="part-kicker">ACT 3 • SECTION B OT CASES</div>
    <h2 class="part-title">Part 60: Section B OT Case Studies — Q202 Lebna & Lulu, Q203 Tom & Q204 Afiya</h2>
    <p class="part-subtitle">Transferred spouse NRB/RNRB, mortgage deductions, and Act 3 Checkpoint.</p>
  </div>

  <!-- CASE Q203 -->
  <div class="card" id="q203">
    <div class="drill-header">
      <span class="drill-title">Q203 • Tom (10 Marks Case Study)</span>
      <div>
        <span class="chip chip-xp">+25 XP</span>
        <span class="chip chip-type">Section B Case</span>
      </div>
    </div>
    <p><strong>Scenario:</strong> Tom died 1 May 2025. Made CLT of £450,000 on 20 Feb 2019 (Tom paid lifetime tax). Death estate = £2,000,000 (including £875k main residence with £500k repayment mortgage).</p>

    <div class="drill-card">
      <p><strong>What is the net value of main residence included in Tom's death estate?</strong></p>
      <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
      <div class="solution-content">
        <div class="computation-box">
Main Residence Value:               £875,000
Less Repayment Mortgage:           (£500,000)
                                   ---------
Net Residence Estate Value:         £375,000
        </div>
        <div class="callout callout-tip">
          <strong>CORRECT ANSWER: £375,000</strong><br>
          Repayment mortgages secured on a main residence are directly deductible from the residence value!
        </div>
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q203" onchange="GAMIFICATION.toggleTask('q203', 25, this.checked)">
        Mark Case Done (+25 XP)
      </label>
    </div>
  </div>
</section>

</div> <!-- End container -->
</body>
</html>
<!-- ═══ END PART 60/100 ═══ -->"""
    parts.append(part60)

    new_content = base_content + '\n\n' + '\n\n'.join(parts)
    with open('TX-UK_Revision_Pack.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print('Successfully appended Session 6 (Parts 51 to 60) to TX-UK_Revision_Pack.html!')

if __name__ == '__main__':
    build_session_6()
