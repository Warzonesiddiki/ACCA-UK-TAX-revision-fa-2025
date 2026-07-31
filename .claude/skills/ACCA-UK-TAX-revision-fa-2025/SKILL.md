```markdown
# ACCA-UK-TAX-revision-fa-2025 Development Patterns

> Auto-generated skill from repository analysis

## Overview
This codebase provides scripts and utilities for generating, expanding, and maintaining the ACCA TX-UK FA2025 Revision Pack. It focuses on automating the creation and enhancement of revision materials, applying audit-driven fixes, and ensuring high-quality, up-to-date content for ACCA UK Tax exam revision. The repository is Python-based and does not rely on external frameworks.

## Coding Conventions

- **File Naming:**  
  All files use `snake_case` for readability and consistency.  
  **Example:**  
  ```
  generate_session_1.py
  build_polished_master_pack.py
  apply_fix_patches.py
  ```

- **Import Style:**  
  Relative imports are preferred within the package.  
  **Example:**  
  ```python
  from .utils import expand_content
  ```

- **Export Style:**  
  Named exports are used for clarity.  
  **Example:**  
  ```python
  def generate_revision_pack():
      ...
  ```

- **Commit Messages:**  
  Freeform style, typically around 82 characters in length.

## Workflows

### Revision Pack Generation and Polishing
**Trigger:** When you want to build or update the full revision pack with new or improved content.  
**Command:** `/build-revision-pack`

1. Run the relevant Python scripts to generate or expand revision pack sessions or parts:
   ```bash
   python generate_session_1.py
   python expand_section_a.py
   ```
2. Polish and enhance the generated pack using dedicated scripts (e.g., add JS search, enrich content):
   ```bash
   python build_polished_master_pack.py
   ```
3. Update the main HTML output file (`TX-UK_Revision_Pack.html`) with the new or improved content.

**Files Involved:**
- `TX-UK_Revision_Pack.html`
- `generate_session_*.py`
- `expand_*.py`
- `build_polished_master_pack.py`

**Frequency:** ~2x/month

---

### Audit and Fix Application
**Trigger:** When you need to address audit findings or apply targeted fixes to the revision pack.  
**Command:** `/apply-audit-fixes`

1. Run audit or verification scripts to identify issues:
   ```bash
   python full_audit.py
   python run_forensic_audit.py
   python verify_all_passes.py
   ```
2. Apply fixes using dedicated scripts (e.g., patch application, formula fixes, content additions):
   ```bash
   python apply_fix_patches.py
   python fix_formula_errors.py
   python add_new_questions.py
   ```
3. Update the main HTML output file (`TX-UK_Revision_Pack.html`) to reflect the applied fixes.

**Files Involved:**
- `TX-UK_Revision_Pack.html`
- `apply_fix_patches.py`
- `fix_*.py`
- `add_*.py`
- `full_audit.py`
- `run_forensic_audit.py`
- `verify_all_passes.py`

**Frequency:** ~2x/month

---

## Testing Patterns

- **Framework:** Unknown (no explicit framework detected).
- **File Pattern:** Test files follow the `*.test.*` naming convention.
  - **Example:** `session_generator.test.py`
- **General Approach:**  
  Tests are likely written as standalone scripts or modules. To run a test:
  ```bash
  python session_generator.test.py
  ```

## Commands

| Command              | Purpose                                                      |
|----------------------|--------------------------------------------------------------|
| /build-revision-pack | Generate and polish the full ACCA TX-UK FA2025 Revision Pack |
| /apply-audit-fixes   | Apply audit-driven fixes and update the revision pack        |
```
