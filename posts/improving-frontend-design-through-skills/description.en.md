# Improving frontend design through Skills

## What is this post?
This post explains how to use Claude **Skills** as reusable, on-demand design guidance so frontend/UI generations don’t converge on generic “AI defaults” (e.g., common fonts and predictable gradients).

## When is it useful?
- When you need brand-distinct UI output for customer-facing experiences (landing pages, dashboards, apps) rather than generic layouts.
- When you want to keep design rules reusable without permanently bloating your base prompts.
- When generating web artifacts that benefit from modern stacks (React + Tailwind + component libraries) rather than single-file toy examples.

## Key points
- Skills are stored as files Claude can load only when needed, letting you keep specialized design constraints separate from general prompting.
- Give guidance at the “right altitude”: avoid overly vague directives, but also avoid fragile pixel/hex micromanagement.
- Push typography, theme, motion, and background choices away from common defaults by providing concrete alternatives.
- The post provides prompt blocks for typography choices, an RPG theme, and a more comprehensive `frontend_aesthetics` block.

## Bundled resources
- Skill: `skills/frontend-design-aesthetics/SKILL.md`
- Guide (en/ko): `guides/frontend-design-skills-playbook.*.md`

## Source
Distilled from Claude’s official blog post: https://claude.com/blog/improving-frontend-design-through-skills (published 2025-11-12).
