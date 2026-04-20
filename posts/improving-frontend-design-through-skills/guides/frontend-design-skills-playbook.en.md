**English** · [한국어](./frontend-design-skills-playbook.ko.md) · [Español](./frontend-design-skills-playbook.es.md) · [日本語](./frontend-design-skills-playbook.ja.md)

# Frontend design through Skills: a practical playbook

This guide summarizes the concrete prompting and reuse patterns described in the source post, oriented toward turning them into a reusable Skill you can load on demand.

## Problem: “distributional convergence” in AI UI output
The post describes how UI generations often converge on a generic look (common font stacks and predictable gradients), which can dilute brand identity.

## Approach: keep design guidance reusable with Skills
- Store design guidance as a Skill file (often markdown) so Claude can load it only when the task calls for it.
- This prevents permanent context overhead in your default prompt setup.

## Give guidance at the “right altitude”
- Too high-level: vague aesthetic requests don’t reliably change outputs.
- Too low-level: brittle, overly specific prescriptions (e.g., fixed hex codes and pixel-perfect micromanagement) can reduce flexibility.
- Better: specify coherent direction (typography, theme references, motion, background treatment) with room for implementation.

## Concrete guidance areas from the post
### Typography
- Avoid default fonts (the post explicitly calls out common defaults to avoid).
- Choose more distinctive type families and pairings.
- Use contrast: extreme weights and noticeable scale jumps.

### Themes
The post provides an RPG-themed example:
- Fantasy-inspired palettes
- Ornate borders
- Parchment-like textures
- Dramatic lighting
- Medieval serif typography

### Motion
- Use CSS animations and staggered reveals where appropriate.
- For React, use a motion library when useful.

### Backgrounds
- Use gradients and patterns intentionally to support the theme.
- Prefer geometric patterns or textured treatments over predictable defaults.

## Artifact generation note (from the post)
The post references using an additional skill to create richer web artifacts using modern tooling (e.g., React + Tailwind and component libraries), bundled into a single HTML artifact.

## Source
Distilled from [Improving frontend design through Skills](https://claude.com/blog/improving-frontend-design-through-skills) (published 2025-11-12).
