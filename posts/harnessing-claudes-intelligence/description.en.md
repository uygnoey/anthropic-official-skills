**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Harnessing Claude's Intelligence | 3 Key Patterns for Building Apps

## What is this post?
This post presents three patterns for building applications on the Claude Platform that keep pace with model capability improvements while balancing latency and cost.

## When is it useful?
Use it when you are designing an agent harness (prompt/tooling/context/memory boundaries) and want principles for what to delegate to Claude versus what to harden in infrastructure.

## Key points
- Prefer tools Claude already understands well (e.g., bash and text editor) and let higher-level patterns emerge from them.
- Re-evaluate your harness assumptions continuously by asking “what can I stop doing?” as Claude becomes more capable.
- Set boundaries carefully: design prompts for cache efficiency and promote high-stakes actions into declarative tools for security, UX, and observability.

## Bundled resources
- 1 skill: `skills/building-on-evolving-models/SKILL.md` — the three patterns and cache-hit principles packaged in Agent Skills format
- 1 guide (en/ko): `guides/three-patterns-app-harness.en.md`, `guides/three-patterns-app-harness.ko.md`

## Source
Distilled from [Harnessing Claude's Intelligence | 3 Key Patterns for Building Apps](https://claude.com/blog/harnessing-claudes-intelligence) (published 2026-04-02).
