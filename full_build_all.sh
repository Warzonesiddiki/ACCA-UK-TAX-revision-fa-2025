#!/usr/bin/env bash
# ============================================================
# ACCA TX-UK (FA2025) — FULL VERSION BUILD PIPELINE
# Rebuilds TX-UK_Full_Revision_Pack_FA2025.html from the PDF exam kit.
#
#   Step 1  full_extract_questions.py  → full_questions.json    (306 questions)
#   Step 2  full_extract_answers.py    → full_answers.json      (306 answers + callouts)
#   Step 3  full_extract_ticks.py      → full_tick_answers.json (tick-box grids)
#   Step 4  build_full_version.py      → TX-UK_Full_Revision_Pack_FA2025.html
# ============================================================
set -euo pipefail
cd "$(dirname "$0")"

echo "═══ STEP 1/4 · Extracting all 306 questions from PDF ═══"
python3 full_extract_questions.py

echo "═══ STEP 2/4 · Extracting all 306 answers from PDF ═══"
python3 full_extract_answers.py

echo "═══ STEP 3/4 · Extracting tick-box answer grids ═══"
python3 full_extract_ticks.py

echo "═══ STEP 4/4 · Building the full HTML pack ═══"
python3 build_full_version.py

echo "✓ FULL VERSION BUILD COMPLETE → TX-UK_Full_Revision_Pack_FA2025.html"
ls -la TX-UK_Full_Revision_Pack_FA2025.html
