---
name: time-bounded-extraction-context-engineering
description: Build reliable, reviewable extraction prompts by assembling the right domain evidence and explicit time anchors (e.g., “most recent value before procedure start time”), and by using granular evaluation to locate failures in prompts vs context vs retrieval.
---

# Time-bounded extraction context engineering

## Instructions
You are helping build or refine an AI workflow that extracts a specific clinical (or similarly regulated) data point from messy domain documents.

Follow these principles:

1) Define the decision precisely
- State the field to extract and the exact temporal constraint (e.g., “most recent glucose before procedure start time”).
- Provide the temporal anchor explicitly as a concrete timestamp when possible.

2) Engineer the context, not just the prompt
- Choose what evidence to include and exclude.
- Order evidence so the model sees the most relevant, time-adjacent documentation first.
- Assemble patient-/case-specific context at runtime rather than trying to write a single static prompt for all cases.

3) Make temporal logic unavoidable
- When asking for “pre‑procedure”, include the procedure start time boundary and instruct the model to ignore post-procedure values.
- Ask for the supporting evidence (date/time, source snippet) so a human reviewer can validate.

4) Evaluate early, evaluate granularly
- Build an evaluation harness that can isolate failures to (a) prompt wording, (b) missing/incorrect context, or (c) retrieval gaps.
- When a case fails, trace back to which of those three caused the error and fix that specific layer.

5) Close the loop with domain experts
- Collect expert feedback on edge cases and documentation patterns.
- Incorporate that feedback into prompt/context changes quickly.

6) Design for transparency
- Return both the extracted value and the rationale plus citations/evidence, so reviewers can apply judgment.

## Bundled resources
- Prompt templates: [templates/time-anchored-extraction-prompt.md](./templates/time-anchored-extraction-prompt.md)
- Evaluation checklist: [references/evaluation-checklist.md](./references/evaluation-checklist.md)
- Worked examples: [examples/pre-procedure-glucose.md](./examples/pre-procedure-glucose.md)

## Examples
### Example 1: Pre-procedure extraction (template-based)
Use the template in [templates/time-anchored-extraction-prompt.md](./templates/time-anchored-extraction-prompt.md) and fill in:
- The procedure start time
- The target field definition
- The evidence bundle

Return:
- Extracted value
- Timestamp (and why it qualifies)
- Evidence snippet(s)
- Short rationale suitable for a human abstractor/reviewer

## Source
This skill is derived from: https://claude.com/blog/carta-healthcare-clinical-abstractor
