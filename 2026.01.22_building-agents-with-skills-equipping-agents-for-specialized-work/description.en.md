**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Building agents with Skills: Equipping agents for specialized work

## What is this post?
This post explains what Agent Skills are, how they package domain expertise for agents, and why progressive disclosure (metadata → SKILL.md → references) helps scale to many skills.

## When is it useful?
- When you want agents to reliably apply domain rules, standards, or workflows without re-explaining them in every conversation.
- When you need many skills but must keep context usage manageable.

## Key points
- A skill’s YAML frontmatter (name + description) is shown first; the full SKILL.md and deeper reference files are loaded only when needed.
- The post emphasizes a three-tier structure: metadata (~50 tokens), SKILL.md (~500 tokens), and reference files (2,000+ tokens) loaded on demand.
- Skills can bundle supporting files (e.g., docs, slide guidance, and scripts) and reference them from within SKILL.md.

## Bundled resources
- Skill: `skills-packaging-principles` (structure guidance + templates)
- Guide: `skills-packaging-guide` (overview, recommended layout)

## Source
- https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work
