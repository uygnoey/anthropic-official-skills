# Context + documentation hygiene checklist

## Structured context (CLAUDE.md)
- [ ] A `CLAUDE.md` exists for each major domain directory.
- [ ] Each `CLAUDE.md` includes domain overview, constraints, conventions, dependencies, doc pointers, and gotchas.
- [ ] Context is written so that a new team member can orient without “tribal knowledge.”

## Documentation hygiene in CI/CD
- [ ] CI/CD has a step that flags doc-risky changes (e.g., API surface changes, schema changes).
- [ ] The check prompts a documentation update when changes likely invalidate docs.
- [ ] Ownership is defined: who approves doc updates and what counts as complete.

## Context-aware commands
- [ ] Custom commands load relevant context before executing.
- [ ] Commands gather the minimum repo state needed to avoid mistakes (git status, recent changes, etc.).

## Source
- https://claude.com/blog/how-brex-improves-code-quality-and-productivity-with-claude-code
