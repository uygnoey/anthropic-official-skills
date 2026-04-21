# Worked example: pre-procedure glucose (time-bounded)

## Scenario
You need the **most recent glucose** documented **before** the procedure start time.

- Procedure start time: 2026-04-08 10:15

## Evidence bundle (snippets)
1) 2026-04-08 08:40 — “Glucose 118 mg/dL”
2) 2026-04-08 10:30 — “Glucose 132 mg/dL”
3) 2026-04-10 09:00 — “Glucose 125 mg/dL”

## Expected selection
Select #1 because it is the most recent value strictly before 10:15.

## Example output
- Value: 118 mg/dL
- Timestamp: 2026-04-08 08:40
- Evidence:
  - “Glucose 118 mg/dL”
- Rationale: This measurement occurs before the procedure start time (2026-04-08 10:15); later values are post-procedure.

## Source
This example follows the time-anchor pattern described in: https://claude.com/blog/carta-healthcare-clinical-abstractor
