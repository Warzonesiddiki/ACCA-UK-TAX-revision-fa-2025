---
name: audit-and-fix-application
description: Workflow command scaffold for audit-and-fix-application in ACCA-UK-TAX-revision-fa-2025.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /audit-and-fix-application

Use this workflow when working on **audit-and-fix-application** in `ACCA-UK-TAX-revision-fa-2025`.

## Goal

Apply audit-driven fixes and patches to the revision pack, including formula corrections, deduplication, and content updates.

## Common Files

- `TX-UK_Revision_Pack.html`
- `apply_fix_patches.py`
- `fix_*.py`
- `add_*.py`
- `full_audit.py`
- `run_forensic_audit.py`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Run audit or verification scripts to identify issues.
- Apply fixes via dedicated Python scripts (e.g., patch application, formula fixes, content additions).
- Update the main HTML output file to reflect the applied fixes.

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.