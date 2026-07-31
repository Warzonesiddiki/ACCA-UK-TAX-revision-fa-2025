import sys, re

def expand_final():
    with open('TX-UK_Revision_Pack.html', 'r', encoding='utf-8') as f:
        text = f.read()

    p59 = """<!-- ═══ PART 59/100 · DRILLS Q191–Q201 ═══ -->
<section class="part-section" id="part-59">
  <div class="part-header">
    <div class="part-kicker">ACT 3 • DRILL MODULE</div>
    <h2 class="part-title">Part 59: Section A IHT Practice Drills (Q191–Q201)</h2>
    <p class="part-subtitle">Loss on sale of shares/property, valuation of unquoted shares (related settlements), and liabilities deductible from estate.</p>
  </div>

  <!-- DRILL Q195 -->
  <div class="drill-card" id="q195">
    <div class="drill-header">
      <span class="drill-title">Q195 • Dominic's Unquoted Share Valuation</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Dominic owned 7,500 shares (75%) in Halder Ltd. On 1 July 2025 gave 3,000 shares to his son (retaining 4,500 shares = 45%). Share values: up to 25% @ £5/sh, 26-50% @ £8/sh, 51-74% @ £13/sh, 75%+ @ £20/sh. What is the transfer of value for IHT?</p>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
Loss to Donor Principle:
Value of holding BEFORE gift (7,500 shares = 75% holding):
7,500 shares × £20 per share =                    £150,000

Value of holding AFTER gift (4,500 shares = 45% holding):
4,500 shares × £8 per share =                     (£36,000)
                                                  ---------
Transfer of Value (Loss to Donor) =               £114,000
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: £114,000</strong><br>
        Lifetime IHT value is calculated strictly on the "Loss to Donor" principle (Value before gift minus Value after gift), NOT on the value received by the donee!
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q195" onchange="GAMIFICATION.toggleTask('q195', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 59/100 ═══ -->"""

    p61 = """<!-- ═══ PART 61/100 · IHT CASES Q205–Q207 ═══ -->
<section class="part-section" id="part-61">
  <div class="part-header">
    <div class="part-kicker">ACT 3 • SECTION B OT CASES</div>
    <h2 class="part-title">Part 61: Section B OT Case Studies — Q205 Roman, Q206 Adana & Q207 Tony & Anita</h2>
    <p class="part-subtitle">Transferred unused spouse NRB (up to 100%), interest-only mortgage deductions, and lifetime gift tax.</p>
  </div>

  <!-- CASE Q205 -->
  <div class="card" id="q205">
    <div class="drill-header">
      <span class="drill-title">Q205 • Roman and Paris (10 Marks Case Study)</span>
      <div>
        <span class="chip chip-xp">+25 XP</span>
        <span class="chip chip-type">Section B Case</span>
      </div>
    </div>
    <p><strong>Scenario:</strong> Roman died 7 Aug 2025. Made CLT £325,000 into trust in 2023. Paid 20% lifetime tax (£0, covered by NRB). On death, CLT becomes chargeable to death tax at 40%.</p>

    <div class="computation-box">
CLT Death Tax on Roman's Death:
Gift Amount: £325,000
NRB Available on Death = £325,000 (No prior gifts in 7 years).
Taxable Excess = £325,000 - £325,000 = £0
Additional Death Tax Due = £0
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q205" onchange="GAMIFICATION.toggleTask('q205', 25, this.checked)">
        Mark Case Done (+25 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 61/100 ═══ -->"""

    p62 = """<!-- ═══ PART 62/100 · IHT CASES Q208–Q209 ═══ -->
<section class="part-section" id="part-62">
  <div class="part-header">
    <div class="part-kicker">ACT 3 • SECTION B OT CASES</div>
    <h2 class="part-title">Part 62: Section B OT Case Studies — Q208 Nagina & Rishi & Q209 Dianne</h2>
    <p class="part-subtitle">Related settlements, unquoted share valuation loss to donor, and PET taper relief timing.</p>
  </div>

  <!-- CASE Q208 -->
  <div class="card" id="q208">
    <div class="drill-header">
      <span class="drill-title">Q208 • Nagina & Rishi (10 Marks Case Study)</span>
      <div>
        <span class="chip chip-xp">+25 XP</span>
        <span class="chip chip-type">Section B Case</span>
      </div>
    </div>
    <p><strong>Scenario:</strong> Rishi made CLT £355,000 to trust on 16 April 2019 (Rishi paid lifetime tax). Gifted 2,000 shares in Altion Ltd on 10 Jan 2025 (owned 8,000 / 10,000 shares before gift).</p>

    <div class="computation-box">
Rishi Share Gift Loss to Donor:
Holding before gift: 8,000 shares (80% holding @ £30/sh) = £240,000
Holding after gift:  6,000 shares (60% holding @ £20/sh) = (£120,000)
                                                           --------
Transfer of Value (PET) =                                  £120,000
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q208" onchange="GAMIFICATION.toggleTask('q208', 25, this.checked)">
        Mark Case Done (+25 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 62/100 ═══ -->"""

    p73 = """<!-- ═══ PART 73/100 · DRILLS Q243–Q251 ═══ -->
<section class="part-section" id="part-73">
  <div class="part-header">
    <div class="part-kicker">ACT 4 • DRILL MODULE</div>
    <h2 class="part-title">Part 73: Section A CT Practice Drills (Q243–Q251)</h2>
    <p class="part-subtitle">Associated companies count, quarterly instalment thresholds, and filing penalties.</p>
  </div>

  <!-- DRILL Q249 -->
  <div class="drill-card" id="q249">
    <div class="drill-header">
      <span class="drill-title">Q249 • Asher, Barton & Chelfry Quarterly Instalments</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Which of the three companies (Asher Ltd: TTP £700k, 3 associated; Barton Ltd: TTP £600k 4m AP, 0 associated; Chelfry Ltd: TTP £1.6M, 0 associated) will NOT have to pay CT by quarterly instalments?</p>
    <div class="options-group">
      <label class="option-item"><input type="radio" name="q249_opt"> A) Asher Ltd</label>
      <label class="option-item"><input type="radio" name="q249_opt"> B) Barton Ltd</label>
      <label class="option-item"><input type="radio" name="q249_opt"> C) Chelfry Ltd</label>
    </div>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
Large Company Threshold = £1,500,000 / N

Asher Ltd: N = 1 + 3 = 4. Threshold = £1,500,000 / 4 = £375,000.
TTP £700,000 > £375,000 -> Asher Ltd IS Large (Pays Instalments!).

Barton Ltd: 4-month AP. Threshold = £1,500,000 × 4/12 = £500,000.
TTP £600,000 > £500,000 -> Barton Ltd IS Large (Pays Instalments!).

Chelfry Ltd: N = 1. Threshold = £1,500,000.
Previous TTP = £1,400,000 (< £1,500,000).
Grace Period Exception: A company is NOT large if TTP < £10M AND it was NOT large in the preceding 12 months!
Chelfry Ltd qualifies for the grace period exception!
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: C (Chelfry Ltd)</strong><br>
        Chelfry Ltd does NOT have to pay by instalments due to the 1-year grace period exception (it was not large in the preceding year and TTP < £10M)!
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q249" onchange="GAMIFICATION.toggleTask('q249', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 73/100 ═══ -->"""

    p79 = """<!-- ═══ PART 79/100 · SECTION C MASTERCLASS Q265–Q267 ═══ -->
<section class="part-section" id="part-79">
  <div class="part-header">
    <div class="part-kicker">ACT 4 • SECTION C MASTERCLASSES</div>
    <h2 class="part-title">Part 79: Section C Masterclass — Q265 Mooncake Ltd, Q266 Music Ltd & Q267 Ash Ltd (15 Marks Each)</h2>
    <p class="part-subtitle">Group relief loss surrenders, matching period rules, and maximum surrenderer / claimant capacity.</p>
  </div>

  <div class="card" id="q265">
    <div class="drill-header">
      <span class="drill-title">Q265 • Mooncake Ltd & Group (15 Marks)</span>
      <div>
        <span class="chip chip-xp">+40 XP</span>
        <span class="chip chip-type">Section C Masterclass</span>
      </div>
    </div>
    <p><strong>Scenario:</strong> Mooncake Ltd owns 80% of Pastry Ltd. Mooncake Ltd incurred trading loss £150,000 (12m AP to 31 March 2026). Pastry Ltd has TTP £200,000 (6m AP to 31 March 2026).</p>

    <div class="computation-box">
Group Relief Time Apportionment Rule:
Overlapping Period = 6 months (1 Oct 2025 - 31 March 2026).

Surrenderer (Mooncake Ltd) Maximum Surrender = £150,000 × 6/12 = £75,000
Claimant (Pastry Ltd) Maximum Claim = £200,000 (for 6m period)

Max Group Relief Surrendered = Lower of £75,000 and £200,000 = £75,000
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q265" onchange="GAMIFICATION.toggleTask('q265', 40, this.checked)">
        Mark Masterclass Done (+40 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 79/100 ═══ -->"""

    p89 = """<!-- ═══ PART 89/100 · SECTION B CASES Q299–Q303 ═══ -->
<section class="part-section" id="part-89">
  <div class="part-header">
    <div class="part-kicker">ACT 5 • SECTION B OT CASES</div>
    <h2 class="part-title">Part 89: Section B OT Case Studies — Q299 Ardent, Q300 DenzilDyer, Q301 Kristel, Q302 Lian & Q303 Mabel</h2>
    <p class="part-subtitle">Overseas supplies, reverse charge, partial exemption, and TOGC rules.</p>
  </div>

  <div class="card" id="q299">
    <div class="drill-header">
      <span class="drill-title">Q299 • Ardent (10 Marks Case Study)</span>
      <div>
        <span class="chip chip-xp">+25 XP</span>
        <span class="chip chip-type">Section B Case</span>
      </div>
    </div>
    <p><strong>Scenario:</strong> Ardent transferred trade as a going concern (TOGC) to a VAT-registered buyer carrying on the same business.</p>

    <div class="computation-box">
TOGC VAT Treatment:
Transfer of a Going Concern (TOGC) is treated as NEITHER a supply of goods NOR a supply of services.
Output VAT Charged = £0 (Outside scope of VAT).
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q299" onchange="GAMIFICATION.toggleTask('q299', 25, this.checked)">
        Mark Case Done (+25 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 89/100 ═══ -->"""

    replacements = {
        r'<!-- ═══ PART 59/100 .*?<!-- ═══ END PART 59/100 ═══ -->': p59,
        r'<!-- ═══ PART 61/100 .*?<!-- ═══ END PART 61/100 ═══ -->': p61,
        r'<!-- ═══ PART 62/100 .*?<!-- ═══ END PART 62/100 ═══ -->': p62,
        r'<!-- ═══ PART 73/100 .*?<!-- ═══ END PART 73/100 ═══ -->': p73,
        r'<!-- ═══ PART 79/100 .*?<!-- ═══ END PART 79/100 ═══ -->': p79,
        r'<!-- ═══ PART 89/100 .*?<!-- ═══ END PART 89/100 ═══ -->': p89,
    }

    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text, flags=re.DOTALL)

    with open('TX-UK_Revision_Pack.html', 'w', encoding='utf-8') as f:
        f.write(text)

    print("Final batch expanded successfully!")

if __name__ == '__main__':
    expand_final()
