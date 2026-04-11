---
name: xlsx
description: "Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved."
license: Proprietary. LICENSE.txt has complete terms
---

# XLSX Skills

## Requirements

### General
- **Professional Font**: Use Arial or Times New Roman.
- **Zero Errors**: No `#REF!`, `#DIV/0!`, etc.
- **Formula First**: ALWAYS use Excel formulas for calculations; do not hardcode values computed in Python.

### Financial Models
- **Blue Text**: Hardcoded inputs.
- **Black Text**: Formulas.
- **Green Text**: Links within the same workbook.
- **Negative Numbers**: Use parentheses: `(123)`.
- **Zeros**: Format as `-`.
- **Assumptions**: Keep all assumptions in a dedicated section/sheet.

## Tools
- **pandas**: Best for bulk data analysis and processing.
- **openpyxl**: Best for formatting, complex formulas, and workbook structure.

## Code Pattern
```python
import pandas as pd
from openpyxl import load_workbook

# ❌ WRONG: sheet['B10'] = 5000
# ✅ RIGHT: sheet['B10'] = "=SUM(B2:B9)"
```

## Recalculation
Modifying files with `openpyxl` does not evaluate formulas. Use `recalc.py` (LibreOffice) to update the cached values before delivering to the user.

## Checklist
- [ ] No hardcoded numbers in calculation cells.
- [ ] All cell references are correctly mapped (1-indexed).
- [ ] Denominators checked for zero to avoid `#DIV/0!`.
- [ ] Column widths adjusted for readability.
- [ ] Data sources documented in cell comments.
