import sys

def build_session_8():
    with open('TX-UK_Revision_Pack.html', 'r', encoding='utf-8') as f:
        content = f.read()

    close_idx = content.find('</div> <!-- End container -->')
    if close_idx != -1:
        base_content = content[:close_idx]
    else:
        base_content = content.replace('</body>\n</html>', '').replace('</body></html>', '')

    parts = []

    # PART 71
    part71 = """<!-- ═══ PART 71/100 · DRILLS Q223–Q232 ═══ -->
<section class="part-section" id="part-71">
  <div class="part-header">
    <div class="part-kicker">ACT 4 • DRILL MODULE</div>
    <h2 class="part-title">Part 71: Section A CT Practice Drills (Q223–Q232)</h2>
    <p class="part-subtitle">Corporate capital allowances, property business income, and loss relief set-offs.</p>
  </div>

  <!-- DRILL Q224 -->
  <div class="drill-card" id="q224">
    <div class="drill-header">
      <span class="drill-title">Q224 • Edam Ltd's Capital Allowances</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Edam Ltd (VAT registered) bought a second-hand lorry for £198,000 (inc VAT £33,000) during year ended 31 March 2026. Main pool TWDV b/fwd at 1 April 2025 was £15,000. What is maximum capital allowance Edam Ltd can claim?</p>
    <div class="options-group">
      <label class="option-item"><input type="radio" name="q224_opt"> A) £167,700</label>
      <label class="option-item"><input type="radio" name="q224_opt"> B) £32,400</label>
      <label class="option-item"><input type="radio" name="q224_opt"> C) £38,340</label>
      <label class="option-item"><input type="radio" name="q224_opt"> D) £200,700</label>
    </div>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
Lorry Cost (Net of VAT for VAT-registered company):
£198,000 - £33,000 = £165,000

Note: Second-hand lorry does NOT qualify for Full Expensing (100% FYA applies to NEW assets only!).
However, second-hand lorry QUALIFIES for Annual Investment Allowance (AIA)!

AIA Claimed = £165,000 (100% within £1M limit)

Main Pool WDA:
TWDV b/fwd £15,000 × 18% WDA = £2,700

Total Capital Allowances = £165,000 (AIA) + £2,700 (WDA) = £167,700
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: A (£167,700)</strong><br>
        VAT-registered companies claim capital allowances on net-of-VAT cost. Second-hand assets do not qualify for Full Expensing but receive 100% AIA!
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q224" onchange="GAMIFICATION.toggleTask('q224', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 71/100 ═══ -->"""
    parts.append(part71)

    # PART 72
    part72 = """<!-- ═══ PART 72/100 · DRILLS Q233–Q242 ═══ -->
<section class="part-section" id="part-72">
  <div class="part-header">
    <div class="part-kicker">ACT 4 • DRILL MODULE</div>
    <h2 class="part-title">Part 72: Section A CT Practice Drills (Q233–Q242)</h2>
    <p class="part-subtitle">Group relief loss surrenders, gains group transfers, and 75% group relationships.</p>
  </div>

  <!-- DRILL Q236 -->
  <div class="drill-card" id="q236">
    <div class="drill-header">
      <span class="drill-title">Q236 • Ten Ltd's Group Relationships</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Ten Ltd owns 90% of Twenty Ltd; Twenty Ltd owns 75% of Thirty Ltd; Thirty Ltd owns 70% of Forty Ltd. What is the group relationship between Forty Ltd and Ten Ltd?</p>
    <div class="options-group">
      <label class="option-item"><input type="radio" name="q236_opt"> A) They form a group for both group relief and chargeable gains</label>
      <label class="option-item"><input type="radio" name="q236_opt"> B) Group relief group but not chargeable gains</label>
      <label class="option-item"><input type="radio" name="q236_opt"> C) Chargeable gains group but not group relief</label>
      <label class="option-item"><input type="radio" name="q236_opt"> D) Do not form a group for either purpose</label>
    </div>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
Group Relief Indirect Holding Check:
Ten Ltd -> Twenty Ltd (90%) -> Thirty Ltd (75%) -> Forty Ltd (70%).
Indirect Holding in Forty Ltd = 90% × 75% × 70% = 47.25% (< 75% required!).
So Forty Ltd is NOT in Ten Ltd's Group Relief group!

Chargeable Gains Group Check:
Requires 75% DIRECT holding at each tier AND > 50% overall effective indirect holding.
Thirty Ltd owns 70% of Forty Ltd (< 75% direct holding at bottom tier!).
So Forty Ltd is NOT in Ten Ltd's Gains group either!
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: D (Do not form a group for either purpose)</strong><br>
        Group relief requires ≥ 75% indirect shareholding (47.25% fails). Gains group requires ≥ 75% direct shareholding at every link in the chain (70% fails).
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q236" onchange="GAMIFICATION.toggleTask('q236', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 72/100 ═══ -->"""
    parts.append(part72)

    # PART 73
    part73 = """<!-- ═══ PART 73/100 · DRILLS Q243–Q251 ═══ -->
<section class="part-section" id="part-73">
  <div class="part-header">
    <div class="part-kicker">ACT 4 • DRILL MODULE</div>
    <h2 class="part-title">Part 73: Section A CT Practice Drills (Q243–Q251)</h2>
    <p class="part-subtitle">Associated companies count, quarterly instalment thresholds, and filing penalties.</p>
  </div>
</section>
<!-- ═══ END PART 73/100 ═══ -->"""
    parts.append(part73)

    # PART 74
    part74 = """<!-- ═══ PART 74/100 · SECTION B CASES Q252 & Q253 ═══ -->
<section class="part-section" id="part-74">
  <div class="part-header">
    <div class="part-kicker">ACT 4 • SECTION B OT CASES</div>
    <h2 class="part-title">Part 74: Section B OT Case Studies — Q252 Greenzone Ltd & Q253 Mixture Ltd</h2>
    <p class="part-subtitle">Trading profit disallowable repairs vs lease renewals, customer entertainment, political donations, and quarterly instalment dates.</p>
  </div>

  <!-- CASE Q252 -->
  <div class="card" id="q252">
    <div class="drill-header">
      <span class="drill-title">Q252 • Greenzone Ltd (10 Marks Case Study)</span>
      <div>
        <span class="chip chip-xp">+25 XP</span>
        <span class="chip chip-type">Section B Case</span>
      </div>
    </div>
    <p><strong>Scenario:</strong> Greenzone Ltd incurred repainting exterior £8,390; legal fees for renewing 20-year lease £19,800; UK customer entertainment £3,600; overseas customer entertainment £1,840; political donations £740; local charity donation with free advertising £660.</p>

    <div class="drill-card">
      <p><strong>1. What amount must be added back for repairs/renewals and entertaining expenses?</strong></p>
      <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
      <div class="solution-content">
        <div class="computation-box">
Repairs & Renewals:
• Repainting exterior = ALLOWABLE REPAIR (£0 add-back).
• Legal fees for renewing 20-year lease = DISALLOWABLE CAPITAL (£19,800 add-back).
Total Repairs Add-Back = £19,800

Entertaining Expenses:
• UK customer entertaining = DISALLOWABLE (£3,600 add-back).
• Overseas customer entertaining = DISALLOWABLE (£1,840 add-back).
Total Entertaining Add-Back = £3,600 + £1,840 = £5,440
        </div>
        <div class="callout callout-tip">
          <strong>CORRECT ANSWER: Repairs Add-back = £19,800 | Entertaining Add-back = £5,440</strong><br>
          Legal fees for long leases (> 50 years or 20-year initial grants) are capital disallowable expenses. All customer entertainment (UK and overseas) is disallowable!
        </div>
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q252" onchange="GAMIFICATION.toggleTask('q252', 25, this.checked)">
        Mark Case Done (+25 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 74/100 ═══ -->"""
    parts.append(part74)

    # PART 75
    part75 = """<!-- ═══ PART 75/100 · SECTION B CASES Q254 & Q255 ═══ -->
<section class="part-section" id="part-75">
  <div class="part-header">
    <div class="part-kicker">ACT 4 • SECTION B OT CASES</div>
    <h2 class="part-title">Part 75: Section B OT Case Studies — Q254 Loser Ltd & Q255 Deutsch Ltd</h2>
    <p class="part-subtitle">Corporate trading loss set-offs, group loss surrenders, and associated companies limits.</p>
  </div>
</section>
<!-- ═══ END PART 75/100 ═══ -->"""
    parts.append(part75)

    # PART 76
    part76 = """<!-- ═══ PART 76/100 · SECTION C MASTERCLASS Q256–Q258 ═══ -->
<section class="part-section" id="part-76">
  <div class="part-header">
    <div class="part-kicker">ACT 4 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 76: Section C Masterclass — Q256 Harbour Ltd, Q257 Deimos/Elara/Fenrir & Q258 Venus Ltd (15 Marks Each)</h2>
    <p class="part-subtitle">Short accounting periods, AIA time apportionment (4/12), 50% SRP FYA, lease premium deductions, and ethics of tax avoidance vs evasion.</p>
  </div>

  <!-- MASTERCLASS Q256 HARBOUR LTD -->
  <div class="card" id="q256">
    <div class="drill-header">
      <span class="drill-title">Q256 • Harbour Ltd (15 Marks Constructed Response)</span>
      <div>
        <span class="chip chip-xp">+40 XP</span>
        <span class="chip chip-type">Section C Masterclass</span>
      </div>
    </div>
    <p><strong>Scenario:</strong> Harbour Ltd changed accounting reference date to 31 March (4-month period ended 31 March 2026). Purchased long-life assets for £548,000. Paid lease premium £78,000 for 20-year lease.</p>

    <div class="computation-box">
4-Month Short Accounting Period Capital Allowances:
Long-Life Assets = Special Rate Pool.
AIA Time Apportioned = £1,000,000 × 4/12 = £333,333

Special Rate Pool Balance = £548,000 - £333,333 = £214,667
50% Special Rate FYA = £214,667 × 50% = £107,334 (FYA is NOT time-apportioned!)
Remaining TWDV c/fwd = £107,333

Total Capital Allowances = £333,333 (AIA) + £107,334 (50% FYA) = £440,667

Lease Premium Trading Deduction (4-month period):
Taxable Premium on Landlord = £78,000 × [50 - 19] / 50 = £48,360
Annual Expense = £48,360 / 20 years = £2,418 p.a.
4-Month Deduction = £2,418 × 4/12 = £806
    </div>

    <div class="callout callout-examiner">
      <div class="callout-title">🔴 EXAMINER REPORT & KEY ANSWER TIPS</div>
      "Candidates must remember that AIA is strictly time-apportioned for short accounting periods (£1M × 4/12 = £333,333). However, 50% Special Rate First Year Allowance (FYA) is NOT time-apportioned!"
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q256" onchange="GAMIFICATION.toggleTask('q256', 40, this.checked)">
        Mark Masterclass Done (+40 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 76/100 ═══ -->"""
    parts.append(part76)

    # PART 77
    part77 = """<!-- ═══ PART 77/100 · SECTION C MASTERCLASS Q259–Q261 ═══ -->
<section class="part-section" id="part-77">
  <div class="part-header">
    <div class="part-kicker">ACT 4 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 77: Section C Masterclass — Q259 Maison Ltd, Q260 E-Commerce Ltd & Q261 Stretched Ltd</h2>
    <p class="part-subtitle">Trading loss relief strategies, choice between current year vs carry-back vs carry-forward, and group relief planning.</p>
  </div>
</section>
<!-- ═══ END PART 77/100 ═══ -->"""
    parts.append(part77)

    # PART 78
    part78 = """<!-- ═══ PART 78/100 · SECTION C MASTERCLASS Q262–Q264 ═══ -->
<section class="part-section" id="part-78">
  <div class="part-header">
    <div class="part-kicker">ACT 4 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 78: Section C Masterclass — Q262 Cop Ltd, Q263 Wretched Ltd & Q264 Crumble Ltd</h2>
    <p class="part-subtitle">Corporate chargeable gains, indexation allowance frozen Dec 2017, and corporate rollover relief.</p>
  </div>
</section>
<!-- ═══ END PART 78/100 ═══ -->"""
    parts.append(part78)

    # PART 79
    part79 = """<!-- ═══ PART 79/100 · SECTION C MASTERCLASS Q265–Q267 ═══ -->
<section class="part-section" id="part-79">
  <div class="part-header">
    <div class="part-kicker">ACT 4 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 79: Section C Masterclass — Q265 Mooncake Ltd, Q266 Music Ltd & Q267 Ash Ltd</h2>
    <p class="part-subtitle">Group relief loss surrenders, matching period rules, and maximum surrenderer / claimant capacity.</p>
  </div>
</section>
<!-- ═══ END PART 79/100 ═══ -->"""
    parts.append(part79)

    # PART 80
    part80 = """<!-- ═══ PART 80/100 · SECTION C MASTERCLASS Q268–Q270 ═══ -->
<section class="part-section" id="part-80">
  <div class="part-header">
    <div class="part-kicker">ACT 4 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 80: Section C Masterclass — Q268 Clueless Ltd, Q269 Long & Road Ltd & Q270 Maximum Ltd</h2>
    <p class="part-subtitle">Multi-company group structures, quarterly instalment calculations, and Act 4 Finale.</p>
  </div>

  <div class="card">
    <h3>🎉 Act 4 Mid-Point Mastery Checkpoint</h3>
    <p>You have now completed the entire Corporation Tax syllabus, including short accounting periods, Full Expensing, 50% SRP FYA, Marginal Relief, NTLR, Group Relief, Chargeable Gains Groups, and Quarterly Instalments.</p>
  </div>
</section>

</div> <!-- End container -->
</body>
</html>
<!-- ═══ END PART 80/100 ═══ -->"""
    parts.append(part80)

    new_content = base_content + '\n\n' + '\n\n'.join(parts)
    with open('TX-UK_Revision_Pack.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print('Successfully appended Session 8 (Parts 71 to 80) to TX-UK_Revision_Pack.html!')

if __name__ == '__main__':
    build_session_8()
