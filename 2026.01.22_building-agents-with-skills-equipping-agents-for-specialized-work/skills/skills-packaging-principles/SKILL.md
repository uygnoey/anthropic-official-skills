---
name: skills-packaging-principles
description: Package domain expertise into scalable Agent Skills using progressive disclosure (metadata, SKILL.md, and on-demand references).
---

# Skills Packaging Principles

## Instructions
Use this skill when creating or refactoring Agent Skills so they remain discoverable and scalable as the skill library grows.

1) **Use progressive disclosure**
- Put only `name` and a short `description` in YAML frontmatter.
- Keep `SKILL.md` focused on actionable instructions.
- Move long documentation into `references/` so it’s only read when needed.

2) **Bundle supporting files**
- Include any documents or scripts the skill needs in the same folder and reference them with relative links.
- Prefer a clear, navigable structure (e.g., `templates/`, `examples/`, `references/`, `scripts/`).

3) **Write cross-file pointers intentionally**
- Put short “what to read next” links in `SKILL.md` rather than pasting everything inline.

## Examples
- Frontmatter pattern: [templates/frontmatter.yml](./templates/frontmatter.yml)
- Example bundle layout: [examples/bundle-tree.md](./examples/bundle-tree.md)
- Notes on progressive disclosure: [references/progressive-disclosure.md](./references/progressive-disclosure.md)

## Source
- https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work
