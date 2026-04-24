# Time-anchored extraction prompt template

Use this template when you need a value that must satisfy a strict time boundary (e.g., “most recent X before procedure start”).

## Template

### Task
You are a domain abstractor extracting **{FIELD_NAME}** from the provided documentation.

### Time anchor
- Procedure/event start time (boundary): **{BOUNDARY_TIMESTAMP}**
- Interpret “pre‑procedure/pre‑event” as: timestamps **strictly earlier** than {BOUNDARY_TIMESTAMP}.

### Evidence
You will be given documentation snippets (notes, vitals, labs, flowsheets). Each snippet includes its timestamp.

### Instructions
1. Find candidate values for {FIELD_NAME} with timestamps.
2. Exclude any candidate with a timestamp on/after {BOUNDARY_TIMESTAMP}.
3. Select the most recent remaining candidate.
4. Output the value and timestamp.
5. Provide supporting evidence:
   - Quote the exact source snippet(s)
   - Explain briefly why the chosen value qualifies as “pre‑procedure/pre‑event”

### Output format
- Value: ...
- Timestamp: ...
- Evidence:
  - “...”
- Rationale: ...

## Notes
If no qualifying candidate exists, return “Not found” and explain what evidence was searched.
