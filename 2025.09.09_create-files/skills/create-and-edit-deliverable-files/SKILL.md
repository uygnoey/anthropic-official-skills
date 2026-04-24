---
name: create-and-edit-deliverable-files
description: Create and iteratively refine ready-to-use deliverable files (spreadsheets, documents, slide decks, PDFs) from user instructions and uploaded source materials.
---

## Instructions
You produce a finished file (or a small set of files) as the primary output, not just text.

When the user requests a deliverable:
1. Confirm the intended output format(s) (spreadsheet, document, slide deck, PDF) and the destination (download vs. save to Drive when available).
2. Ask for or request uploads of any relevant source data (tables, CSVs, PDFs, notes) if it is missing.
3. Plan the file structure before generating (worksheets and key formulas; document sections; slide outline).
4. Generate the file, then offer an iteration loop: “Review and tell me what to adjust.”

Supported work patterns (as described in the post):
- Turn raw data into cleaned datasets, analysis, charts, and written insights.
- Build spreadsheets with multiple sheets and working formulas.
- Convert work across formats (e.g., a PDF report to a slide deck).

Safety and privacy note (from the post): treat file creation features as potentially network-enabled; encourage the user to avoid sensitive data and to review outputs carefully.

## Examples
### Example 1: Data → report
User: “Clean this dataset and create a PDF report with charts and key insights.”
Assistant: Confirm inputs, clean data, generate charts, and deliver a PDF report.

### Example 2: Spreadsheet model
User: “Create a budget template with variance calculations and a dashboard sheet.”
Assistant: Create a multi-sheet spreadsheet with formulas and a simple dashboard.

### Example 3: Cross-format conversion
User: “Turn this PDF report into a 10-slide deck with an executive summary.”
Assistant: Extract key points and visuals, then generate a slide deck.
