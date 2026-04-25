---
name: systematic-bugfix-workflow
description: A systematic workflow to debug faster with Claude.ai for rapid hypothesis generation and Claude Code for autonomous investigation, fixes, and verification.
---

## Instructions

Follow this workflow to go from symptoms to a verified fix.

1. Gather evidence
   - Capture stack traces, logs, reproduction steps, and the expected vs actual behavior.

2. Triage with Claude.ai (fast)
   - Ask for a ranked list of probable root causes and what to inspect.
   - Use the templates in [templates/debugging-prompts.md](./templates/debugging-prompts.md).

3. Escalate to Claude Code (deep)
   - In your repo, start Claude Code and describe the bug and evidence.
   - Ask it to search for the relevant code paths, propose a fix, and request permission before edits.

4. Validate
   - Ask for a reproduction test.
   - Run the test suite and confirm what changed.
   - Request an explanation of the changes.

5. Ship safely
   - If appropriate, ask Claude Code to commit changes and open a PR.
   - Monitor for regressions and add coverage for the failure mode.

## Examples

- "Here's a test failure from CI. What could be causing it?" (triage)
- "probable root causes ranked by likelihood" (log analysis)
- "Write a test that reproduces this bug" (validation)
- "Commit these changes and open a PR" (shipping)
