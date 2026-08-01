# ACCA TX-UK (FA2025) — Full Revision Platform

Single-file HTML revision platform for the ACCA **Taxation (TX-UK)** exam, built from the
official **Kaplan TX-UK Exam Kit (Finance Act 2025, 684 pages)** — for the
**June 2026 – June 2027** examination sittings.

## 📦 The two HTML packs

| File | What it is |
|---|---|
| **`TX-UK_Full_Revision_Pack_FA2025.html`** ⭐ | **THE FULL VERSION** — all **306 official exam-kit questions** (Sections A, B & C across Income Tax, CGT, IHT, CT and VAT), interactive marking, worked solutions, examiner reports & tutor tips. |
| `TX-UK_Revision_Pack.html` | Original 100-part tutorial pack (rules summaries + selected drills). Kept for reference. |

## ✨ What the full version includes

- **All 306 questions** extracted from the PDF exam kit, organised by syllabus area and exam section:
  - 🟢 Income Tax & NIC (Q1–127) · 🔵 CGT (Q128–179) · 🟣 IHT (Q180–212) · 🟠 CT (Q213–270) · 🔴 VAT (Q271–306)
  - **Section A** OTQs · **Section B** OT cases (scenario + sub-questions) · **Section C** constructed-response
- **Interactive question types**
  - A–F multiple choice with instant green/red feedback (multi-answer questions use checkboxes)
  - Clickable **tick-box tables** with a "Check My Ticks" button
  - Type-in numeric answers with smart checking (accepts `£5,510` or `5510`)
- **Every question has a worked solution** (official computations in ledger style) plus
  - 72 **Examiner's reports** · 216 **Tutor's top tips** · 96 **Key answer tips** · tutorial notes
- **Study tools**: ⚡ 20-question Quick Fire quiz · ⏱ timed 25-question mock · 📇 spaced-repetition flashcards ·
  🌙 dark mode · ⌨️ keyboard shortcuts (`D`, `Q`, `M`, `F`, `/`, `Ctrl+/`, `Esc`) · 🔎 instant search ·
  📊 progress dashboard · XP / rank gamification · 🖨 print-to-PDF · progress saved in your browser
- FA2025 **rates & allowances quick-reference** table
- Fully offline-capable single file (fonts degrade gracefully without internet)

## 🔁 Rebuilding from the PDF

```bash
./full_build_all.sh        # runs the whole pipeline in one go
```

| Step | Script | Output |
|---|---|---|
| 1 | `full_extract_questions.py` | `full_questions.json` — all 306 questions, classified & parsed |
| 2 | `full_extract_answers.py` | `full_answers.json` — answers, workings, examiner/tutor callouts |
| 3 | `full_extract_ticks.py` | `full_tick_answers.json` — tick-box answer grids (PDF coordinates) |
| 4 | `build_full_version.py` | `TX-UK_Full_Revision_Pack_FA2025.html` |

Requires Python 3 + `pypdf` (`pip install pypdf`).

## 📋 Exam facts (FA2025)

- Personal Allowance **£12,570** · Basic rate band **£37,700** · CT main rate **25%** / small profits **19%**
- VAT registration threshold **£90,000** · IHT nil-rate band **£325,000** · CGT AEA **£3,000**
