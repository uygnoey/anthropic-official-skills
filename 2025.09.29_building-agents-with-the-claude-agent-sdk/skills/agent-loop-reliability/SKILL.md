---
name: agent-loop-reliability
description: Design and improve agents using a repeatable loop (context → action → verification) with practical verification patterns.
---

This skill is derived from: https://claude.com/blog/building-agents-with-the-claude-agent-sdk (published 2025-09-29).

## Instructions
- Start every run by writing down the current objective and success criteria.
- Gather context with explicit actions (file search, logs, docs) before making changes.
- Take action in small, reversible steps; prefer tool calls or scripts over manual reasoning for deterministic work.
- Verify each step using one or more of: deterministic rules, visual validation, or an LLM-as-judge rubric.
- If the agent is stuck, change the environment (better tools, better search, stricter rules) rather than repeating the same attempt.
- After completion, capture failures as test cases and add them to an eval set.

## Examples
### Example: turn an unreliable task into an agent loop

1) Gather context: search logs for the failing module, open relevant files.

2) Take action: apply the smallest patch.

3) Verify: run unit tests and lint.

4) Repeat until clean.


### Example: verification checklist

Use `references/verification-checklist.md` as a standard review rubric for UI or content output.

## Templates
See:
- templates/agent-loop.md
- templates/verification-plan.md

## References
See:
- references/verification-checklist.md
- references/testing-improvement-questions.md
