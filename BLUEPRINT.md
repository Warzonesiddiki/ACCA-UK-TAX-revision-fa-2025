╔══════════════════════════════════════════════════════════════════════════════╗
║        ACCA TX-UK (FA2025) PRACTICE PLATFORM — BLUEPRINT                    ║
║        Source: TX_Exam_Kit_FA25.pdf  |  Master HTML: TX-UK_Revision_Pack.html  ║
╚══════════════════════════════════════════════════════════════════════════════╝

DATE: 2026-08-01
BRANCH: arena/019fba0a-acca-uk-tax-revision-fa-2025
STATUS: BLUEPRINT — WAITING FOR CONFIRMATION BEFORE EXECUTION

──────────────────────────────────────────────────────────────────────────────
1. CURRENT STATE (VERIFIED)
──────────────────────────────────────────────────────────────────────────────
• TX-UK_Revision_Pack.html        5273 lines | 100 parts | Audits PASS (8/8)
• TX_Exam_Kit_FA25.pdf             684 pages | Official ACCA Exam Kit (Jun 2026–Jun 2027)
• Build script                    build_polished_master_pack.py BROKEN (truncated at Part 5)
• Session generators               generate_session_1.py → 10.py (appends parts 1–100)
• Patches applied                  CT 3/200 | Fuel £769 | Lease 51-(N-1) ✓
• Gamification engine              GAMIFICATION.toggleSolution / toggleTask / XP chips ✓
• Examiner callouts                8 instances (needs 84 PDF pages of examiner reports)
• Tutor tips                       45 instances (needs expansion)
• Interactive drills               drill-card + solution-toggle present in HTML

──────────────────────────────────────────────────────────────────────────────
2. WHAT YOU WANT (CLARIFIED)
──────────────────────────────────────────────────────────────────────────────
A) ALL QUESTIONS FROM PDF → IN HTML (Section A OTQs, Section B OT Cases, Section C)
B) EXAMINER COMMENTS FROM PDF → IN HTML CALL-OUTS (84 pages of examiner reports)
C) SECTION C STUDENTS → EXCEL WORKBOOK (constructed-response practice + mark schemes)
D) MAKE IT INTERESTING / USEFUL → Gamification + interactivity + exam simulation

──────────────────────────────────────────────────────────────────────────────
3. BLUEPRINT — PHASES
──────────────────────────────────────────────────────────────────────────────

PHASE 1 — DATA EXTRACTION FROM PDF (684 pages)
──────────────────────────────────────────────────────────────────────────────
Task 1.1  Extract Section A OTQs (15 questions × 2 marks)              → HTML drill cards
Task 1.2  Extract Section B OT Cases (3 cases × 5 OTQs = 15 questions)  → HTML case cards
Task 1.3  Extract Section C Questions (3 questions: 10 + 15 + 15)       → HTML + EXCEL
Task 1.4  Extract Answer Keys / Working from PDF answer sections         → Hidden solution divs
Task 1.5  Extract Examiner Reports (84 pages with examiner comments)    → callout-examiner
Task 1.6  Extract Tutor Top Tips / Study Text guidance                  → callout-tip
Task 1.7  Extract Tax Rate Tables / Allowances / Calendar                 → Reference cards

Key PDF pages to target (verified):
  • p.260 — Examiner’s report (Income Tax / transferable allowance)
  • p.266, 273, 280–284 — Examiner reports + tutor guidance
  • p.258 — Tutor’s top tips
  • Answer sections: traverse pages 350–684 for practice answers

PHASE 2 — HTML INTEGRATION (100-part master pack)
──────────────────────────────────────────────────────────────────────────────
Task 2.1  Insert all Section A/B questions into interactive drill-card elements
         • Each card: Question | Options (A–D) | Correct Answer | Working | Examiner note
         • Toggle button: “▼ Show Working & Solution” (existing JS: GAMIFICATION.toggleSolution)
Task 2.2  Insert examiner reports into callout-examiner blocks beside relevant questions
         • Format: “Examiner said…” + “Common mistake: …” + “Correct approach: …”
Task 2.3  Insert tutor tips into callout-tip blocks (green styling)
Task 2.4  Add “Exam Simulator” mode (timer + score tracker) for full 100-mark practice
Task 2.5  Add embedded tax calculators (JS) for CT marginal relief, CGT, VAT, NIC

PHASE 3 — SECTION C EXCEL WORKBOOK
──────────────────────────────────────────────────────────────────────────────
File:  TX-UK_SectionC_Practice_Pack_FA2025.xlsx
Sheets:
  • Sheet 1: “Section C Questions” — All 3 Section C prompts from PDF (Q1 10-marks, Q2 15-marks, Q3 15-marks)
  • Sheet 2: “Student Answer Template” — Blank structured template (calculation boxes, working lines, conclusion)
  • Sheet 3: “Answer Key & Mark Scheme” — Verified answers from PDF + examiner comments + mark allocation
  • Sheet 4: “Examiner Feedback” — Extracted examiner reports per Section C topic
  • Sheet 5: “Progress Tracker” — Student checklist (completed / time taken / score / weak areas)
  • Sheet 6: “Tax Rate Quick Ref” — All FA2025 rates / thresholds (copy from Part 98)

PHASE 4 — MAKE IT INTERESTING & USEFUL (GAMIFICATION + INTERACTIVITY)
──────────────────────────────────────────────────────────────────────────────
Task 4.1  XP / Badge System (enhance existing GAMIFICATION)
         • +10 XP per completed drill | +50 XP for Section C completed | Badge for 100% pass
Task 4.2  “50 Deadly Traps” Quiz (Part 99 already exists — make interactive)
         • Each trap = multiple-choice question with explanation
Task 4.3  Timer / Exam Simulator
         • 3-hour countdown with section reminders (A: 54 min | B: 54 min | C: 72 min)
Task 4.4  Progress Dashboard (visible on page load)
         • % complete per Act / Section / Part | Weak topic highlight
Task 4.5  “Examiner’s Report” Pop-up / Side-panel
         • Click any question → see examiner comment for that exact topic
Task 4.6  Printable / PDF Export
         • Print button already in Part 100 — enhance with “Export Section C to PDF”
Task 4.7  Mobile-friendly cards (CSS is responsive — verify touch targets)

──────────────────────────────────────────────────────────────────────────────
4. BUILD PIPELINE (FIX + REBUILD)
──────────────────────────────────────────────────────────────────────────────
Step A  Fix build_polished_master_pack.py (complete truncated script or replace with pipeline)
Step B  Run session generators 1→10 in sequence (or direct build from PDF + HTML template)
Step C  Apply fix patches (apply_fix_patches.py) — verify 3/200, £769, 51-(N-1)
Step D  Apply add_q16_to_part8.py (if not applied)
Step E  Apply expand_all_remaining_parts.py + expand_final_batch.py
Step F  Apply fix_lease_formula.py
Step G  Run verify_all_passes.py — must pass 8/8
Step H  Insert examiner reports + questions (Phase 2)
Step I  Generate Section C Excel (Phase 3)
Step J  Add gamification enhancements (Phase 4)
Step K  Final audit + user test

──────────────────────────────────────────────────────────────────────────────
5. WHAT I NEED FROM YOU TO START
──────────────────────────────────────────────────────────────────────────────
□ Confirm PHASE 1–4 above — YES / modify?
□ Priority order:  IT/CT first, or all at once?
□ Should I create Section C Excel now (Phase 3) or after HTML questions built?
□ Should the examiner comments be inserted for ALL 100 parts, or only exam-heavy ones (IT 40–45%, CT 25–30%, CGT 10–15%)?
□ “More interesting” — specific ideas? (Quiz mode? Leaderboard? Timer? Badges?)

──────────────────────────────────────────────────────────────────────────────
6. FIRST DELIVERABLE (IMMEDIATE — NO RISK TO CURRENT HTML)
──────────────────────────────────────────────────────────────────────────────
• This BLUEPRINT file (done)
• Fixed build script (ready to apply)
• Sample: Extract 1 examiner report (p.260) → insert into HTML Part 8 or Part 35
• Create blank Section C Excel template (ready to fill)

READY WHEN YOU ARE.
Reply with:  “Start Phase 1”  or  “Modify blueprint: _____”  or pick priorities.
