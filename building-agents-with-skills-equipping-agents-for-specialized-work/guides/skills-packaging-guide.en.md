**English** · [한국어](./skills-packaging-guide.ko.md) · [Español](./skills-packaging-guide.es.md) · [日本語](./skills-packaging-guide.ja.md)

# Skills packaging guide

## Overview
This guide summarizes the post’s recommended approach to structuring Agent Skills using progressive disclosure.

## Recommended structure
- Keep YAML frontmatter minimal (name + description).
- Put core, actionable instructions in `SKILL.md`.
- Put long-form material in `references/` and link to it from `SKILL.md`.

## Why this helps
Progressive disclosure keeps large skill libraries usable: models can see many skill “titles” cheaply and only load full details when needed.

## Source
- https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work
