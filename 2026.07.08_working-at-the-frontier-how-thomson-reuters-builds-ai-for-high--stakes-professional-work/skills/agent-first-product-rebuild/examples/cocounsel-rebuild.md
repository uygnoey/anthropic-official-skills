# The CoCounsel Legal rebuild

## What CoCounsel Legal is

A professional-grade legal AI platform designed to make legal professionals more effective with
defensible answers. It sits alongside Thomson Reuters' reference tools — Westlaw and Practical Law for
legal research.

## Before and after

| | Before | After |
| --- | --- | --- |
| Structure | Separate skills, run sequentially | Rebuilt on the Claude Agent SDK |
| Who sequences the work | The product / the user | The agent, planning in real time |
| Tool access | Per-skill | A single agent accessing hundreds of company tools simultaneously |

The rebuild is part of a broader decision: instead of creating smarter chatbots, Thomson Reuters
rebuilt its products as agent-based systems.

## What the rebuild demands of the model

> "Our big test for Claude is to assess how good it is at making plans and using tools effectively."
> — Joel Hron

And alongside it, the requirement that models maintain thread continuity across extended tool-use
chains — which is what a single agent working across hundreds of tools generates constantly.

## What is held constant through the rebuild

- **Customer data remains protected** and is not used for third-party model training.
- **The human professional remains accountable** for the end work product.
- **Citations are validated before findings reach human review** — legal research was rebuilt around
  agents tuned for citation validation and verification rather than just search and retrieval.

## Why Anthropic

Thomson Reuters chose Anthropic based on its approaches to transparency, safety, and responsible AI
development. Early proof came through deep research capabilities built collaboratively.

Hron joined Thomson Reuters four years ago when his startup was acquired, and notes that AI has
fundamentally reshaped software development — which is what makes technology partner selection
critically important.

## What comes next

Hron's team prioritizes longer-horizon work, better context management, and dependable tool-calling
across agent task chains. He personally uses Claude Code to rapidly onboard codebases and Claude Cowork
for strategic analysis.

For work that "ultimately has to hold up in court," he sees pushing model capabilities as "the frontier
worth pushing on next. After all, professional AI has to work in environments where being almost right
is not good enough."

## Source

[Working at the Frontier: How Thomson Reuters Builds AI for High-Stakes Professional Work](https://claude.com/blog/working-at-the-frontier-how-thomson-reuters-builds-ai-for-high--stakes-professional-work) — Claude blog, July 8, 2026.
