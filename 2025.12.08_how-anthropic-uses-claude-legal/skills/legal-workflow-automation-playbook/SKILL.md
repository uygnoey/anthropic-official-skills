---
name: legal-workflow-automation-playbook
description: Package recurring in-house legal workflows (marketing review, contract redlining, outside business activity checks, and PIAs) into repeatable AI-assisted processes with human oversight, using Skills for consistency and MCP for contextual retrieval.
---

## Instructions
Use this skill to design and run AI-assisted legal workflows that:
1) start from high-friction legal tasks,
2) create self-serve intake and first-pass analysis,
3) keep humans as final decision-makers, and
4) capture institutional guidance in reusable files (“Skills”), optionally enriched with MCP connections.

### Workflow design principles
- Start with pain points, not technology: pick the busiest, most repetitive, energy-draining work.
- Build in human oversight: verify citations and outputs; treat AI as a first pass (triage/drafting), not final judgment.
- Use Skills for consistency:
  - **Workflow consistency**: embed the team’s review framework and issue taxonomy.
  - **Voice/style consistency**: encode formatting preferences and typical content (e.g., for briefs or memos).
- Use MCP to connect relevant sources when available (e.g., Drive folders, Jira tickets, Slack messages, Calendar).

### Four workflow patterns from the post
1) **Marketing content review triage**
   - Intake: marketer pastes content into a self-serve tool.
   - Analysis: use a review framework to flag issues (low/medium/high risk) and suggest fixes.
   - Routing: if submitted for formal review, send to the right lawyer with pre-flagged issues.
   - Template: see [templates/marketing-review-framework.md](./templates/marketing-review-framework.md).

2) **Contract redlining assistant**
   - Compare versions in a doc editor, highlight changes, and recommend fallback language.
   - Support “ask in the doc” interactions (prompt in-line).
   - Reference: see [references/contract-redlining-interaction.md](./references/contract-redlining-interaction.md).

3) **Outside business activity (conflict-of-interest) review**
   - Intake: employee form (department, manager, activity description).
   - Analysis: evaluate against a COI policy framework; ask clarifying questions if needed.
   - Routing: send recommendation to lawyers for approval.
   - Template: see [templates/outside-activity-intake-form.md](./templates/outside-activity-intake-form.md).

4) **Privacy impact assessment (PIA) drafting with prior examples**
   - Connect to a folder of prior PIAs (e.g., via MCP) and use a formatting/concerns guide.
   - Produce a draft aligned to prior launches.
   - Template: see [templates/pia-drafting-prompt.md](./templates/pia-drafting-prompt.md).

## Examples
### Example: In-document contract question
See [examples/in-doc-contract-question.md](./examples/in-doc-contract-question.md).

### Example: PIA drafting request referencing prior launches
See [examples/pia-request-example.md](./examples/pia-request-example.md).
