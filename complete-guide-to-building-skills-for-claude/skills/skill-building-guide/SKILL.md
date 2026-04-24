---
name: skill-building-guide
description: Helps plan, structure, test, and distribute Claude Agent Skills. Use when drafting SKILL.md frontmatter, organizing companion files (scripts/references/assets), or setting up a testing and iteration plan for a skill.
---

# Building Claude skills (practical guide)

## Instructions

### 1) Define a narrow first target
- Identify 2–3 concrete use cases.
- Start with one challenging task and iterate until it works, then extract the winning approach into a skill.

### 2) Structure your skill for progressive disclosure
- Keep SKILL.md focused on actionable instructions.
- Move long references, checklists, and templates into separate bundled files and link to them.

### 3) Write frontmatter that triggers correctly
- Use kebab-case for the folder and `name`.
- Ensure `description` includes both **what it does** and **when to use it** (trigger conditions).
- Avoid XML tags (`<` and `>`).

See [references/frontmatter-reference.md](references/frontmatter-reference.md).

### 4) Test triggering and behavior
Use the checklist in [references/testing-checklist.md](references/testing-checklist.md).

### 5) Distribute
- Users can zip and upload a skill folder, or place it in the Claude Code skills directory.

## Examples

### Example: validating a new skill
Before sharing a skill, confirm naming, frontmatter, triggers, and that bundled references are linked.

## Source
- https://claude.com/blog/complete-guide-to-building-skills-for-claude
- https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf
