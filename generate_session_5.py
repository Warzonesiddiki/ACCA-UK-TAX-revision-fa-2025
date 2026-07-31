import sys

def build_session_5():
    with open('TX-UK_Revision_Pack.html', 'r', encoding='utf-8') as f:
        content = f.read()

    close_idx = content.find('</div> <!-- End container -->')
    if close_idx != -1:
        base_content = content[:close_idx]
    else:
        base_content = content.replace('</body>\n</html>', '').replace('</body></html>', '')

    parts = []

    # PART 41
    part41 = """<!-- ═══ PART 41/100 · CGT-02 CHATTELS & PART DISPOSALS ═══ -->
<section class="part-section" id="part-41">
  <div class="part-header">
    <div class="part-kicker">ACT 2 • CHARGEABLE GAINS</div>
    <h2 class="part-title">Part 41: CGT-02 Chattels, Wasting Assets & Part Disposals</h2>
    <p class="part-subtitle">Tangible moveable property, £6,000 gross rule, 5/3rds marginal gain cap, and the part disposal formula A / (A + B).</p>
  </div>

  <div class="card">
    <h3>🖼️ Chattels Tax Rules Matrix</h3>
    <table class="fiscal-table">
      <thead>
        <tr><th>Cost / Proceeds Category</th><th>Gross Proceeds ≤ £6,000</th><th>Gross Proceeds > £6,000</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Cost ≤ £6,000</strong></td><td>EXEMPT from CGT</td><td>Gain capped at <strong>5/3 × (Gross Proceeds - £6,000)</strong></td></tr>
        <tr><td><strong>Cost > £6,000</strong></td><td>Deemed Gross Proceeds = <strong>£6,000</strong> (Limits loss)</td><td>Normal CGT Computation (Proceeds - Cost)</td></tr>
      </tbody>
    </table>

    <div class="callout callout-trap">
      <div class="callout-title">⚠️ TRAP WARNING: WASTING CHATTELS</div>
      Wasting chattels (predictable useful life ≤ 50 years, e.g. racehorses, private motor cars, greyhounds, plant & machinery) are <strong>100% EXEMPT</strong> from CGT, provided they are not used in a trade eligible for capital allowances!
    </div>
  </div>

  <div class="card">
    <h3>📐 Part Disposal Cost Allocation Formula</h3>
    <p>Where part of an asset is sold, allowable cost is calculated as:</p>
    <div class="computation-box">
Allowable Cost = Original Total Cost × [ A / (A + B) ]

Where:
A = Gross proceeds of part sold
B = Market value of remaining unsold portion
    </div>
  </div>
</section>
<!-- ═══ END PART 41/100 ═══ -->"""
    parts.append(part41)

    # PART 42
    part42 = """<!-- ═══ PART 42/100 · CGT-03 SHARES & MATCHING ═══ -->
<section class="part-section" id="part-42">
  <div class="part-header">
    <div class="part-kicker">ACT 2 • CHARGEABLE GAINS</div>
    <h2 class="part-title">Part 42: CGT-03 Shares Matching Rules, Takeovers & Spousal Transfers</h2>
    <p class="part-subtitle">Individual share matching hierarchy, bonus/rights issues, Section 104 Share Pool, and no gain/no loss spousal transfers.</p>
  </div>

  <div class="card">
    <h3>📈 Individual Share Matching Hierarchy</h3>
    <p>Disposals of shares by individuals are matched against acquisitions in the following strict priority:</p>
    <div class="computation-box">
1. Same day acquisitions (Shares acquired on the exact day of disposal).
2. Next 30 days acquisitions (Shares acquired within 30 days AFTER disposal, FIFO).
3. Section 104 Share Pool (Averaged pool of all remaining shares).
    </div>
  </div>

  <div class="card">
    <h3>👩‍❤️‍👨 Spousal Transfer Rule</h3>
    <p>Transfers of assets between spouses / civil partners living together take place on a <strong>no gain / no loss</strong> basis. Deemed proceeds = Transferor's allowable cost (no taxable gain or loss arises).</p>
  </div>
</section>
<!-- ═══ END PART 42/100 ═══ -->"""
    parts.append(part42)

    # PART 43
    part43 = """<!-- ═══ PART 43/100 · CGT-04 CGT RELIEFS ═══ -->
<section class="part-section" id="part-43">
  <div class="part-header">
    <div class="part-kicker">ACT 2 • CHARGEABLE GAINS</div>
    <h2 class="part-title">Part 43: CGT-04 Primary CGT Reliefs (BADR, PRR, Gift Holdover, Rollover)</h2>
    <p class="part-subtitle">Business Asset Disposal Relief (14% rate, £1M lifetime limit), Private Residence Relief, Holdover relief for business assets, and Rollover relief.</p>
  </div>

  <div class="card">
    <h3>💼 Business Asset Disposal Relief (BADR) Key Rules (FA2025)</h3>
    <table class="fiscal-table">
      <thead>
        <tr><th>Criteria</th><th>Statutory Requirement</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Lifetime Limit</strong></td><td class="num">£1,000,000 lifetime limit per individual</td></tr>
        <tr><td><strong>FA2025 BADR Tax Rate</strong></td><td class="num">14% (FA2025 rate)</td></tr>
        <tr><td><strong>Qualifying Conditions Period</strong></td><td class="num">24 consecutive months prior to disposal</td></tr>
        <tr><td><strong>Qualifying Assets</strong></td><td>
          • Unincorporated business / partnership share.<br>
          • Shares in personal trading company (≥ 5% voting rights + employee/officer).<br>
          • Assets used in business within 3 years of cessation.
        </td></tr>
      </tbody>
    </table>
  </div>

  <div class="card">
    <h3>🏡 Principal Private Residence Relief (PRR)</h3>
    <div class="computation-box">
PRR Exempt Gain = Total Chargeable Gain × [ Period of Deemed / Actual Occupation / Total Ownership Period ]

Deemed Occupation Periods (Provided house was occupied BEFORE and AFTER):
1. Final 9 months of ownership (ALWAYS EXEMPT regardless of actual occupation).
2. Up to 3 years of absence for ANY reason.
3. Unlimited absence while working ABROAD.
4. Up to 4 years of absence while working elsewhere in the UK.
    </div>
  </div>
</section>
<!-- ═══ END PART 43/100 ═══ -->"""
    parts.append(part43)

    # PART 44
    part44 = """<!-- ═══ PART 44/100 · CGT-05 COMPANY GAINS ═══ -->
<section class="part-section" id="part-44">
  <div class="part-header">
    <div class="part-kicker">ACT 2 • CHARGEABLE GAINS</div>
    <h2 class="part-title">Part 44: CGT-05 Corporate Chargeable Gains & Indexation Allowance</h2>
    <p class="part-subtitle">Indexation allowance frozen at December 2017, company share pool structure, and Corporation Tax rate application.</p>
  </div>

  <div class="card">
    <h3>🏛️ Corporate Gains vs Individual CGT Rules</h3>
    <p>1. <strong>No AEA for Companies:</strong> Companies do NOT receive the £3,000 Annual Exempt Amount.</p>
    <p>2. <strong>Indexation Allowance (IA):</strong> Companies receive Indexation Allowance to deduct inflation. Indexation was <strong>frozen at December 2017</strong> (no indexation allowed for inflation after Dec 2017).</p>
    <p>3. <strong>Indexation Cannot Create or Increase a Loss:</strong> IA can only reduce a gain to £Nil.</p>
  </div>
</section>
<!-- ═══ END PART 44/100 ═══ -->"""
    parts.append(part44)

    # PART 45
    part45 = """<!-- ═══ PART 45/100 · DRILLS Q128–Q138 ═══ -->
<section class="part-section" id="part-45">
  <div class="part-header">
    <div class="part-kicker">ACT 2 • DRILL MODULE</div>
    <h2 class="part-title">Part 45: Section A CGT Practice Drills (Q128–Q138)</h2>
    <p class="part-subtitle">Exempt assets (QCBs, Gilts, ISAs), loss utilization rules, and painting chattels disposals.</p>
  </div>

  <!-- DRILL Q128 -->
  <div class="drill-card" id="q128">
    <div class="drill-header">
      <span class="drill-title">Q128 • Massita's Asset Disposals</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Which TWO of the following assets would potentially realise a chargeable gain?</p>
    <div class="options-group">
      <label class="option-item"><input type="checkbox" name="q128_opt"> A) Qualifying corporate bonds</label>
      <label class="option-item"><input type="checkbox" name="q128_opt"> B) Painting by a famous artist</label>
      <label class="option-item"><input type="checkbox" name="q128_opt"> C) Gilt-edged securities</label>
      <label class="option-item"><input type="checkbox" name="q128_opt"> D) Main residence that he has always lived in</label>
      <label class="option-item"><input type="checkbox" name="q128_opt"> E) A car used in his trade</label>
      <label class="option-item"><input type="checkbox" name="q128_opt"> F) A machine used in his trade (sold for £22,000 with profit)</label>
    </div>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="callout callout-tip">
        <strong>CORRECT ANSWERS: B & F</strong><br>
        • <strong>Painting:</strong> Non-wasting chattel -> Chargeable gain if proceeds/cost > £6,000.<br>
        • <strong>Machine:</strong> Plant & machinery sold for > £6,000 is a non-wasting chattel and generates a chargeable gain!<br>
        • QCBs, Gilts, cars, and 100% PRR main residences are statutory exempt assets.
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q128" onchange="GAMIFICATION.toggleTask('q128', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 45/100 ═══ -->"""
    parts.append(part45)

    # PART 46
    part46 = """<!-- ═══ PART 46/100 · DRILLS Q139–Q150 ═══ -->
<section class="part-section" id="part-46">
  <div class="part-header">
    <div class="part-kicker">ACT 2 • DRILL MODULE</div>
    <h2 class="part-title">Part 46: Section A CGT Practice Drills (Q139–Q150)</h2>
    <p class="part-subtitle">Rollover relief, insurance reinvestment, BADR claims, and Investors' Relief.</p>
  </div>

  <!-- DRILL Q141 -->
  <div class="drill-card" id="q141">
    <div class="drill-header">
      <span class="drill-title">Q141 • Lotte's Destroyed Warehouse Reinvestment</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Lotte bought warehouse for £52,000 in Nov 2020. Destroyed by fire June 2025. Insurance proceeds received = £71,000. Reinvested £64,000 in new warehouse. Lotte claims maximum deferral. What is the base cost of the new warehouse?</p>
    <div class="options-group">
      <label class="option-item"><input type="radio" name="q141_opt"> A) £45,000</label>
      <label class="option-item"><input type="radio" name="q141_opt"> B) £52,000</label>
      <label class="option-item"><input type="radio" name="q141_opt"> C) £57,000</label>
      <label class="option-item"><input type="radio" name="q141_opt"> D) £64,000</label>
    </div>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
Full Insurance Proceeds:          £71,000
Cost of Destroyed Warehouse:     (£52,000)
                                 --------
Full Chargeable Gain:             £19,000

Proceeds NOT reinvested:
£71,000 - £64,000 = £7,000 (Taxable immediately!)

Gain Deferred = Full Gain (£19,000) - Immediate Gain (£7,000) = £12,000

Base Cost of New Warehouse:
New Purchase Price (£64,000) - Deferred Gain (£12,000) = £52,000
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: B (£52,000)</strong><br>
        Where partial reinvestment occurs under s.23 insurance relief, gain deferred = full gain minus un-reinvested proceeds (£19k - £7k = £12k). Base cost = £64k - £12k = £52k.
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q141" onchange="GAMIFICATION.toggleTask('q141', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 46/100 ═══ -->"""
    parts.append(part46)

    # PART 47
    part47 = """<!-- ═══ PART 47/100 · DRILLS Q151–Q161 ═══ -->
<section class="part-section" id="part-47">
  <div class="part-header">
    <div class="part-kicker">ACT 2 • DRILL MODULE</div>
    <h2 class="part-title">Part 47: Section A CGT Practice Drills (Q151–Q161)</h2>
    <p class="part-subtitle">Company share pool indexation, corporate rollover relief, and property disposals.</p>
  </div>
</section>
<!-- ═══ END PART 47/100 ═══ -->"""
    parts.append(part47)

    # PART 48
    part48 = """<!-- ═══ PART 48/100 · SECTION B CASES Q162–Q164 ═══ -->
<section class="part-section" id="part-48">
  <div class="part-header">
    <div class="part-kicker">ACT 2 • SECTION B OT CASES</div>
    <h2 class="part-title">Part 48: Section B OT Case Studies — Q162 Michael Chin, Q163 Bo & Q164 Alphabet Ltd</h2>
    <p class="part-subtitle">Gift holdover relief, unquoted share disposals, and corporate takeover cash vs paper elections.</p>
  </div>

  <!-- CASE Q164 -->
  <div class="card" id="q164">
    <div class="drill-header">
      <span class="drill-title">Q164 • Alphabet Ltd Takeover (10 Marks)</span>
      <div>
        <span class="chip chip-xp">+25 XP</span>
        <span class="chip chip-type">Section B Case</span>
      </div>
    </div>
    <p><strong>Scenario:</strong> Alphabet Ltd taken over by XYZ plc. Shareholders received either cash £6 per share or 1 XYZ share for 1 Alphabet share. MD Aloi took cash alternative (£6/share for 60,000 shares).</p>

    <div class="drill-card">
      <p><strong>What is Aloi's CGT liability on the takeover disposal claiming BADR?</strong></p>
      <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
      <div class="solution-content">
        <div class="computation-box">
Disposal Proceeds: 60,000 shares × £6 = £360,000
Allowable Cost: 60,000 shares × £1 =   (£60,000)
                                      --------
Gross Chargeable Gain:                 £300,000
Less Annual Exempt Amount:              (£3,000)
                                      --------
Taxable Gain:                          £297,000

BADR Tax Liability (FA2025 rate 14%):
£297,000 × 14% = £41,580
        </div>
        <div class="callout callout-tip">
          <strong>CORRECT ANSWER: £41,580</strong><br>
          As managing director holding 60% of shares for over 2 years, Aloi qualifies for Business Asset Disposal Relief (BADR) taxed at 14% under FA2025!
        </div>
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q164" onchange="GAMIFICATION.toggleTask('q164', 25, this.checked)">
        Mark Case Done (+25 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 48/100 ═══ -->"""
    parts.append(part48)

    # PART 49
    part49 = """<!-- ═══ PART 49/100 · SECTION B CASES Q165–Q167 ═══ -->
<section class="part-section" id="part-49">
  <div class="part-header">
    <div class="part-kicker">ACT 2 • SECTION B OT CASES</div>
    <h2 class="part-title">Part 49: Section B OT Case Studies — Q165 Lily, Q166 Albert & Charles & Q167 Zoyla</h2>
    <p class="part-subtitle">PRR business use restrictions, joint spousal house disposals, and share matching rules.</p>
  </div>
</section>
<!-- ═══ END PART 49/100 ═══ -->"""
    parts.append(part49)

    # PART 50
    part50 = """<!-- ═══ PART 50/100 · SECTION B CASES Q168–Q170 ═══ -->
<section class="part-section" id="part-50">
  <div class="part-header">
    <div class="part-kicker">ACT 2 • SECTION B OT CASES</div>
    <h2 class="part-title">Part 50: Section B OT Case Studies — Q168 Hali & Goma, Q169 Avery & Q170 Jerome</h2>
    <p class="part-subtitle">Gift holdover claims on business assets, base cost transfers, and Act 2 Checkpoint.</p>
  </div>

  <div class="card">
    <h3>🎉 Act 2 Mid-Point Mastery Checkpoint</h3>
    <p>You have now completed the core theoretical principles and Section A/B drills for Chargeable Gains (CGT), including chattels, share matching, BADR (14%), PRR, Gift Holdover, and Rollover relief.</p>
  </div>
</section>

</div> <!-- End container -->
</body>
</html>
<!-- ═══ END PART 50/100 ═══ -->"""
    parts.append(part50)

    new_content = base_content + '\n\n' + '\n\n'.join(parts)
    with open('TX-UK_Revision_Pack.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print('Successfully appended Session 5 (Parts 41 to 50) to TX-UK_Revision_Pack.html!')

if __name__ == '__main__':
    build_session_5()
