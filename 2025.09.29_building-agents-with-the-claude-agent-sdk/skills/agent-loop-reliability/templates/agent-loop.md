# Agent loop (template)

Use this template to keep an agent run structured and auditable.

## Objective
- What is the exact outcome?
- What would count as “done”?

## Gather context
- What files, logs, docs, or systems do we need to inspect?
- What tool actions will we run to collect evidence?

## Take action
- What is the smallest safe change?
- What tool calls or scripts will implement it?

## Verify
- Deterministic checks (tests, lint, schema validation):
- Visual checks (render/screenshot) if applicable:
- LLM-as-judge rubric (tone/format/correctness) if applicable:

## Iterate
- If verification fails, list hypotheses and collect new evidence before changing code.
