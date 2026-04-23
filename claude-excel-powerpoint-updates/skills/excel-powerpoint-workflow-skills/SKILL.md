---
name: excel-powerpoint-workflow-skills
description: Create reusable Claude workflows (“skills”) tailored for Excel and PowerPoint add-ins, with emphasis on cross-file context, repeatable financial modeling and deck workflows, and persistent instructions.
---

## Instructions
Use this skill as a repeatable workflow wrapper. Adapt the steps to the specific workbook or deck you have open.

When you run the skill:
1) Ask the user what deliverable they want (workbook changes, summary table, updated slides) and which files/tabs/slides are in scope.
2) Confirm any constraints that should be treated as persistent preferences (formatting rules, slide bullet length, assumptions policy).
3) Execute the workflow in small, checkable steps and narrate what changed.

### Workflows explicitly mentioned in the post
- Excel: audit a model for formula errors and balance-sheet integrity.
- Excel: build and populate LBO, DCF, and 3-statement model templates.
- Excel: run comparable company analyses.
- Excel: clean messy spreadsheet data.
- PowerPoint: build competitive landscape decks.
- PowerPoint: update an existing deck with new information or additional data.
- PowerPoint: review a deck for number consistency, data-narrative alignment, and language polish.

### Notes
- The post states that the Excel and PowerPoint add-ins share conversation context across open files.
- The post notes that skills and organization-wide skills configured in Claude (desktop/web) work inside the add-ins.
- The post mentions routing through Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry.

## Examples
### Example: Excel model audit
User: "Audit this workbook for formula errors and balance-sheet integrity."
Assistant:
- Clarify scope (which sheets, time periods).
- Check for common integrity issues (sign conventions, circular refs, hardcodes where formulas expected).
- Summarize findings and propose fixes.

### Example: PowerPoint consistency review
User: "Review this deck for number consistency and language polish."
Assistant:
- Identify the slides in scope.
- Cross-check repeated figures and labels.
- Suggest concrete edits slide-by-slide.

## Source
- https://claude.com/blog/claude-excel-powerpoint-updates
