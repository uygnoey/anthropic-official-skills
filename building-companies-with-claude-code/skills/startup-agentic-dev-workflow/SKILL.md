---
name: startup-agentic-dev-workflow
description: A repeatable session-based workflow for startups using Claude Code: research, planning, implementation, plus context distillation and parallel sub-agent investigation.
---

## Instructions
Use this workflow to ship reliably with Claude Code while keeping context clean.

1) Research session
- Use a dedicated session for background research on the feature.
- When needed, use subagents to investigate different parts of the codebase in parallel.
- Produce a single research document that captures what matters.

2) Planning session
- Create an implementation plan with discrete phases.
- Iterate on the plan until it’s coherent and testable.
- Write the plan into a Markdown file you can follow during implementation.

3) Implementation session
- Execute phases systematically.
- If the agent starts producing contradictory or low-quality output, stop early and re-start with a distilled context summary.

4) Context management
- Prefer new sessions for major phases.
- Pass only distilled conclusions forward.

## Examples
- Template for the three-phase workflow: `templates/research-plan-implement.md`
- Template for context distillation between sessions: `templates/context-distillation.md`
- Best practices summary: `references/session-best-practices.md`
