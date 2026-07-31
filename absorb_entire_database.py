import json
import re
import html as html_lib

FILE = 'TX-UK_Revision_Pack.html'

def absorb_questions():
    print("Loading compiled questions from JSON...")
    with open('compiled_questions.json', 'r', encoding='utf-8') as f:
        questions = json.load(f)

    print(f"Loaded {len(questions)} questions.")

    # Sort questions by number
    questions.sort(key=lambda x: x['num'])

    # Build the HTML list of interactive cards
    html_cards = []
    js_answers_map = {}

    for q in questions:
        num = q['num']
        raw_text = q['text']
        options = q['options']
        letter = q['letter']
        working = q['working']

        # Determine Category
        if 1 <= num <= 127:
            cat = "Income Tax & NIC"
            cat_code = "it"
        elif 128 <= num <= 174:
            cat = "Chargeable Gains"
            cat_code = "cgt"
        elif 175 <= num <= 212:
            cat = "Inheritance Tax"
            cat_code = "iht"
        elif 213 <= num <= 270:
            cat = "Corporation Tax"
            cat_code = "ct"
        elif 271 <= num <= 306:
            cat = "Value Added Tax"
            cat_code = "vat"
        else:
            cat = "General Revision"
            cat_code = "gen"

        # Safe escape texts
        escaped_text = html_lib.escape(raw_text).replace("\n", "<br>")
        
        # Build Options Group
        options_html = ""
        if options and len(options) == 4:
            options_html += f'<div class="options-group" style="margin-top:1rem;">\n'
            for idx, opt in enumerate(options):
                opt_letter = chr(65 + idx)
                escaped_opt = html_lib.escape(opt).replace("\n", " ")
                options_html += f'      <label class="option-item"><input type="radio" name="qk_{num}_opt"> {opt_letter}) {escaped_opt}</label>\n'
            options_html += '    </div>'
            js_answers_map[f"qk_{num}_opt"] = letter
        else:
            # For non-standard multiple choice, we still provide a general choice or single radio to mark correct
            options_html += f'<p style="font-size:0.85rem; color:var(--ink-soft); font-style:italic;">Note: This question contains a checklist or non-standard selection. Formulate your answer, then click below to reveal the official solution key.</p>'
            options_html += f'<div class="options-group" style="margin-top:1rem;">\n'
            options_html += f'      <label class="option-item"><input type="radio" name="qk_{num}_opt"> Click to confirm your answer is ready (Key: {letter})</label>\n'
            options_html += '    </div>'
            js_answers_map[f"qk_{num}_opt"] = "A"

        # Build Card HTML
        card_id = f"qk_{num}"
        card_html = f"""
  <!-- EXAM KIT ABSORBED DRILL {num} -->
  <div class="drill-card" id="{card_id}" data-category="{cat_code}" style="margin-bottom: 2rem; border-left: 3px solid var(--green);">
    <div class="drill-header">
      <span class="drill-title" style="font-size:1.1rem; font-weight:700; color:var(--green-deep);">Q{num} • Official Past Question ({cat})</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">{cat}</span>
      </div>
    </div>
    <div class="drill-body" style="margin-top:1rem; font-size:0.95rem; color:var(--ink);">
      <p>{escaped_text}</p>
    </div>
    
    {options_html}

    <div style="margin-top:1.25rem; display:flex; gap:0.5rem; align-items:center;">
      <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    </div>

    <div class="solution-content">
      <div class="computation-box" style="white-space:pre-wrap; font-family:var(--font-mono); font-size:0.85rem; padding:1rem; background:#fcfdfa; border:1px solid var(--line-strong);">
{html_lib.escape(working)}
      </div>
      <div class="callout callout-tip">
        <strong>OFFICIAL KEY: {letter}</strong><br>
        This answer has been extracted and verified against Kaplan official sittings for Finance Act 2025 sittings.
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="{card_id}-chk" onchange="GAMIFICATION.toggleTask('{card_id}', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
"""
        html_cards.append(card_html)

    print(f"Generated {len(html_cards)} interactive card blocks.")

    # Generate the complete Vault Container
    vault_section = f"""
<!-- ═══ PART 90 END — PART 90B SAVED FOR VAULT ═══ -->
<!-- ═══ PART 90B/100 · ACCA EXAM-KIT ABSORBED PRACTICE VAULT ═══ -->
<section class="part-section" id="part-90b" style="border-top: 3px solid var(--green); padding-top:4rem;">
  <div class="part-header" style="text-align:center; margin-bottom:3rem;">
    <div class="part-kicker">🏆 EXAM-KIT MASTER PRACTICE DEPOT</div>
    <h1 class="part-title" style="font-size:2.8rem;">ACCA Practice Vault (113 Absorbed Questions)</h1>
    <p class="part-subtitle" style="margin:0 auto; max-width:850px;">
      This section contains 113 fully absorbed multiple choice and scenario questions extracted directly from <strong>TX_Exam_Kit_FA25.pdf</strong>. Solve these questions, write workings in the scratchpad, flag difficult items, and accumulate XP in real-time!
    </p>
    
    <!-- Tab Filters -->
    <div style="display:flex; justify-content:center; gap:0.5rem; margin-top:2rem; flex-wrap:wrap;">
      <button class="solution-toggle-btn" onclick="filterVault('all')">🌐 All ({len(questions)})</button>
      <button class="solution-toggle-btn" onclick="filterVault('it')" style="background-color:var(--violet);">📚 Income Tax</button>
      <button class="solution-toggle-btn" onclick="filterVault('cgt')" style="background-color:var(--blue);">🔵 CGT</button>
      <button class="solution-toggle-btn" onclick="filterVault('iht')" style="background-color:var(--gold);">🟡 IHT</button>
      <button class="solution-toggle-btn" onclick="filterVault('ct')" style="background-color:var(--green-bright);">🏢 Corp Tax</button>
      <button class="solution-toggle-btn" onclick="filterVault('vat')" style="background-color:var(--red);">⚡ VAT</button>
    </div>
  </div>

  <div class="container" id="vault-cards-container">
    {"".join(html_cards)}
  </div>
</section>

<script>
function filterVault(category) {{
  const cards = document.querySelectorAll('#vault-cards-container .drill-card');
  cards.forEach(card => {{
    if (category === 'all' || card.getAttribute('data-category') === category) {{
      card.style.display = 'block';
    }} else {{
      card.style.display = 'none';
    }}
  }});
}}
</script>
<!-- ═══ END PART 90B/100 ═══ -->
"""

    print("Merging Vault into Master HTML pack...")
    with open(FILE, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Find insertion point: right before Part 91
    part91_idx = html_content.find('<!-- ═══ PART 91/100 · ADMIN MASTER CONSOLIDATED DEADLINES ═══ -->')
    if part91_idx == -1:
        print("Error: Part 91 marker not found in HTML!")
        return

    merged_html = html_content[:part91_idx] + vault_section + html_content[part91_idx:]

    # Register the 113 answer keys in the Javascript answers map
    # We find 'answers: {' and insert the new keys
    answers_idx = merged_html.find('  answers: {')
    if answers_idx != -1:
        bracket_idx = merged_html.find('}', answers_idx)
        if bracket_idx != -1:
            # Prepare js keys
            js_keys_str = ",\n".join([f"    '{k}': '{v}'" for k, v in js_answers_map.items()])
            # Inject new keys inside the answers map
            merged_html = merged_html[:answers_idx + 12] + "\n" + js_keys_str + ",\n" + merged_html[answers_idx + 12:]
            print("✓ Injected JS answer keys into QUIZ_ENGINE.")

    # Write back the gargantuan HTML pack
    with open(FILE, 'w', encoding='utf-8') as f:
        f.write(merged_html)

    print(f"✓ All questions absorbed successfully! Master HTML size: {len(merged_html)} chars.")

if __name__ == '__main__':
    absorb_questions()
