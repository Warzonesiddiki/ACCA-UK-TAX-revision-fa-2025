with open('TX-UK_Revision_Pack.html', 'r', encoding='utf-8') as f:
    text = f.read()

q16_card = """
  <!-- DRILL Q16 -->
  <div class="drill-card" id="q16-card">
    <div class="drill-header">
      <span class="drill-title">Q16 • Harrison's Dividend Income Tax Liability</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Harrison's only income in the tax year 2025/26 was dividend income of £56,950. What is Harrison's income tax liability for the tax year 2025/26?</p>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
Gross Dividend Income:            £56,950
Less Personal Allowance:         (£12,570)
                                  -------
Taxable Dividend Income:          £44,380

Income Tax Liability:
Dividend Nil Rate Band (£500 × 0%):                     £0
Basic Rate Band (£37,200 × 8.75%):                  £3,255
Higher Rate Band ((£44,380 - £37,700) = £6,680 × 33.75%): £2,255
                                                    ------
Total Income Tax Liability:                         £5,510
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: £5,510</strong><br>
        The dividend nil rate band is £500. It uses up part of the basic rate band (£37,700), leaving £37,200 taxed at basic rate (8.75%) and the remaining £6,680 taxed at higher rate (33.75%).
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q16-chk" onchange="GAMIFICATION.toggleTask('q16', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
"""

# Insert Q16 right after Q15 in Part 8
target = "<!-- ═══ END PART 8/100 ═══ -->"
new_part8_end = q16_card + "\n</section>\n" + target

text = text.replace("</section>\n<!-- ═══ END PART 8/100 ═══ -->", new_part8_end)

with open('TX-UK_Revision_Pack.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Added Q16 Harrison to Part 8 successfully.")
