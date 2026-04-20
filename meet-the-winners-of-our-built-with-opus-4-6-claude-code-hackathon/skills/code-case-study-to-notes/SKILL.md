---
name: code-case-study-to-notes
description: Turn a Claude Code project case study into reusable implementation notes (problem, approach, agents, tests, constraints, and takeaways) without inventing details.
---

## Instructions
You are converting a short “what someone built” story into reusable Claude Code notes.

1) Capture the case study facts (only what the post states).
- Project name
- Creator background
- What it does (inputs/outputs)
- Any build notes (time, tests, agents, tools)
- Any measurable claims (numbers, adoption, performance)

2) Identify reusable implementation patterns mentioned explicitly.
- Parallel sub-agents for decomposition/analysis
- A meta-planner that turns a spec into a task graph
- Prompt → tests workflow

3) Produce a concise “Implementation Notes” artifact.
- Problem
- Approach
- Agent architecture (if mentioned)
- Testing/verification (if mentioned)
- Constraints/risks
- Open questions (when the post omits details)

4) Do not invent missing technical details.
- If the post doesn’t specify prompts, hooks, or code, say “Not specified in the post.”

## Examples
### Example: Pattern extraction
User: Summarize the reusable engineering patterns from these hackathon winners.
Assistant:
- Parallel sub-agents can split a document analysis pipeline into focused tasks.
- A meta-planner can decompose a spec into a task graph for execution by other agents.
- A prompt-first workflow can be paired with automatically generated tests.
