---
name: browser-based-code-delegation
description: Enables delegating well-defined coding tasks to a cloud sandbox from a web browser (useful for bug backlogs, routine fixes, and parallel coding work). Trigger when the user asks to connect a GitHub repo and have Claude implement changes without using a local terminal.
---

# Browser-Based Code Delegation

Use this skill when the user wants to hand off small-to-medium coding tasks from a browser UI, connected to a GitHub repository, with progress tracking and PR creation.

## Instructions
1. Ask which GitHub repository (and branch, if relevant) the user wants to work on, and what success criteria they want (tests passing, lint clean, specific behavior).
2. Restate the task as a set of clear, checkable subtasks (e.g., reproduce issue, implement fix, run tests, open PR).
3. Keep the task well-scoped: prefer bugfixes, routine changes, and well-defined tickets over ambiguous greenfield work.
4. While working, provide progress updates and ask for steering if requirements are unclear.
5. Verify changes with tests or other validation steps before proposing a PR.
6. Summarize what changed and what remains (if anything), then create or request a PR.

## Examples
- “Connect my GitHub repo and fix the failing CI job on the main branch.”
- “Please handle my backlog: update deprecated dependencies and open separate PRs per package.”
- “Implement this routine change across multiple repos in parallel and give me a short change summary for each PR.”

## Tips
- Prefer isolated, well-defined tasks (bug backlogs, routine fixes, backend changes you can validate with tests).
- Remember cloud sessions can be rate-limited alongside other usage, and may require allowing specific network domains for dependencies.

## Human-readable descriptions
This skill is summarized for humans in [../../description.en.md](../../description.en.md) and [../../description.ko.md](../../description.ko.md).

## Source
Distilled from [Claude Code on the web](https://claude.com/blog/claude-code-on-the-web) (published 2025-10-20).
