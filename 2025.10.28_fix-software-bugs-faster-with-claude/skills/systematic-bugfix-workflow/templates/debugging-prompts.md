# Debugging prompt pack

Use these templates as starting points. Replace bracketed placeholders.

## Fast triage (Claude.ai)

**Input**
- Error/trace:
  ```
  [paste stack trace]
  ```
- Context: [what changed recently? environment?]

**Prompt**
1) Summarize what is failing in 2–3 sentences.
2) List probable root causes ranked by likelihood.
3) For each, name the specific file/function/config to inspect.

## Failure mode exploration

**Prompt**
What could cause [symptom] in [component]? List realistic failure modes and what evidence would confirm each one.

## Safe refactor reasoning

**Prompt**
Help me reason through a safe refactor for [module].
- Invariants that must hold:
- Risks (races, state, backward compatibility):
- Step-by-step plan with validation steps:

## Reproduction test request

**Prompt**
Write a test that reproduces this bug. Assume we use [test framework].
- The test should fail before the fix and pass after.
- Explain why it reproduces the bug.
