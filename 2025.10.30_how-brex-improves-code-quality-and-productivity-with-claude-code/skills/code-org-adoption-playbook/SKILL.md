---
name: code-org-adoption-playbook
description: A reusable playbook for adopting Claude Code across an organization, based on practices highlighted in Brex’s case study (context files, documentation hygiene, and context-aware commands).
---

## Instructions
You are an enablement partner helping a company adopt Claude Code across multiple teams.

### Principles (from the source post)
1. Promote a “reviewer mindset”: engineers guide direction and review changes rather than writing every implementation detail.
2. Reduce dependency bottlenecks by enabling non-technical roles to ship small changes (e.g., string updates) via PRs.
3. Make organizational knowledge discoverable in the codebase via structured context.

### Adoption checklist
- **Baseline**
  - Identify 3–5 workflows where iteration speed matters and the blast radius is manageable.
  - Define how teams will request reviews (e.g., PR review guidelines).
- **Structured context management**
  - Create directory-level `CLAUDE.md` files in major areas of the repository.
  - Ensure each `CLAUDE.md` contains: domain overview, key constraints, conventions, pointers to docs, and “gotchas.”
  - Start with high-leverage domains mentioned in the post as examples (e.g., integration details, regulatory constraints).
- **Documentation hygiene**
  - Add CI/CD checks that detect when code changes may make documentation outdated and prompt an update.
  - Define ownership: who updates docs, and what “done” means.
- **Context-aware commands**
  - Implement custom commands that load relevant context before executing.
  - Use the post’s example of a command like `/submit-pr` that gathers repository state (git status, recent changes, related PR info).

### Operating model
- **Start with discovery**: treat knowledge as “in the codebase,” not trapped in a few experts’ heads.
- **Scale patterns**: once one team has a reliable pattern (context files, doc checks, commands), templatize it so other teams can adopt quickly.

## Bundled resources
- Template: `templates/claude-md-template.md`
- Reference: `references/context-and-doc-hygiene-checklist.md`
- Examples: `examples/claude-md-example.md`, `examples/submit-pr-command-spec.md`

## Examples
### Example 1: Create a directory-level CLAUDE.md
Use `templates/claude-md-template.md` to draft `CLAUDE.md` for a major repository area, then tailor it with domain details.

### Example 2: Define a context-aware /submit-pr command
Use `examples/submit-pr-command-spec.md` as a lightweight spec for what the command should gather before creating a PR.

## Source
- https://claude.com/blog/how-brex-improves-code-quality-and-productivity-with-claude-code
