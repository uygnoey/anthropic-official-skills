---
name: frontend-design-aesthetics
description: Provides reusable frontend UI aesthetics guidance (typography, theme, motion, backgrounds) to avoid generic "AI default" designs when generating web UIs, landing pages, dashboards, and app layouts. Use when prompts mention frontend UI, landing pages, design polish, Tailwind/React components, themes, typography, motion, or visual distinctiveness.
---

# Frontend Design Aesthetics Skill

Use this skill to guide Claude toward distinctive, brand-appropriate frontend UI output rather than converging on generic defaults.

## Instructions
1. Diagnose whether the request is for a customer-facing UI, internal tool, or a one-off demo, and optimize visual ambition accordingly.
2. Avoid convergent defaults:
   - Do not choose the most common “AI default” font stacks.
   - Do not rely on predictable purple/pink gradients or generic hero layouts.
3. Pick typography deliberately:
   - Prefer more distinctive families and pairings (e.g., display + monospace, serif + geometric sans).
   - Use contrast via weight and scale (e.g., 100/200 vs 800/900; 3x+ size jumps).
4. Provide theme guidance at the right altitude:
   - Don’t micromanage exact hex values or pixel-perfect spacing unless asked.
   - Don’t stay vague (“make it modern and clean”); instead specify a cohesive aesthetic direction.
5. Make motion and backgrounds intentional:
   - Use tasteful animation (staggered reveals, micro-interactions) where appropriate.
   - Use background patterns/textures/lighting to reinforce the theme.
6. When generating code, apply the design choices consistently across components (tokens, spacing rhythm, typography scale, color system).

## Examples
- Typography steering: explicitly avoid default fonts and pick a distinctive pairing to change the entire feel of a landing page.
- Themed UI: apply an RPG-inspired palette, ornate borders, parchment-like textures, and dramatic lighting.
- Comprehensive `frontend_aesthetics` prompt block: bundle typography + theme + motion + backgrounds into a reusable block for SaaS landing pages, blog layouts, and dashboards.

## Tips
- If the user provides a brand or product vibe, translate it into: typography choices, 1–2 dominant colors, an accent color, and a background motif.
- If the output looks generic, iterate by changing the font pairing and background treatment first.

## Companion resources
- Guide: ../../guides/frontend-design-skills-playbook.en.md
- Guide (Korean): ../../guides/frontend-design-skills-playbook.ko.md

## Human-readable descriptions
This skill is summarized for humans in [../../description.en.md](../../description.en.md) and [../../description.ko.md](../../description.ko.md).

## Source
Distilled from [Improving frontend design through Skills](https://claude.com/blog/improving-frontend-design-through-skills) (published 2025-11-12).
