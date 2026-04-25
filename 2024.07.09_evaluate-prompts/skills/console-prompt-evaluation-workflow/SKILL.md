---
name: console-prompt-evaluation-workflow
description: A workflow for generating prompts, building test suites, running batch evaluations, and iterating based on side-by-side comparisons and SME scoring in the Anthropic Console.
---

## Instructions

Use this skill when you are iterating on an LLM prompt and want a structured evaluation loop in the Anthropic Console.

1. Draft an initial prompt using the Console prompt generator by describing the task.
2. Define your prompt variables and their generation requirements.
3. Build a test suite:
   - Import real-world test cases from a CSV, and/or
   - Use the Console's test case generation to auto-generate inputs per variable.
4. Run the full test suite and review responses.
5. Create a new prompt version and re-run the same test suite.
6. Compare outputs side-by-side across prompt versions.
7. If available, ask subject matter experts to score response quality on a 5-point scale and use the scores to decide whether the new version is better.

Constraints:
- Do not invent test cases. Prefer importing representative real inputs.
- Keep evaluation criteria consistent across prompt versions.

## Examples

### Example: Customer support triage prompt

- Task description: "Triage inbound customer support requests"
- Approach:
  1. Generate a first prompt in the Console.
  2. Generate or import a set of inbound messages as test cases.
  3. Iterate on the prompt while keeping the same test suite.
  4. Compare outputs and optionally collect SME 1–5 quality scores.
