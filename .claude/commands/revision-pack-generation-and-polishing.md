---
name: revision-pack-generation-and-polishing
description: Workflow command scaffold for revision-pack-generation-and-polishing in ACCA-UK-TAX-revision-fa-2025.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /revision-pack-generation-and-polishing

Use this workflow when working on **revision-pack-generation-and-polishing** in `ACCA-UK-TAX-revision-fa-2025`.

## Goal

Generate and polish the ACCA TX-UK FA2025 Revision Pack, including content expansion and enhancements.

## Common Files

- `TX-UK_Revision_Pack.html`
- `generate_session_*.py`
- `expand_*.py`
- `build_polished_master_pack.py`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Run Python scripts to generate or expand revision pack sessions or parts.
- Polish and enhance the generated pack (e.g., add JS search, rich content) using dedicated Python scripts.
- Update the main HTML output file with the new or improved content.

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.