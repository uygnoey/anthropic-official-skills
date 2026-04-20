---
name: opus-4-7-code-best-practices
description: Applies the Opus 4.7 prompting and session-tuning guidance from "Best practices for using Claude Opus 4.7 with Claude Code". Use when opening a Claude Code session with Opus 4.7, choosing an effort level (high / xhigh / max), batching questions, or deciding whether to nudge toward more tool use and parallel subagents.
---

# Opus 4.7 prompting and session tuning for Claude Code

## Instructions
1. Start with a complete first-turn brief: include intent, constraints, acceptance criteria, and where in the codebase the work should happen.
2. Minimize back-and-forth in interactive sessions by batching questions and supplying needed context up front.
3. Use effort levels deliberately. Treat `xhigh` as the default for most agentic coding, use `high` when you need to reduce spend or run concurrent sessions, and use `max` selectively for extremely hard or eval-style problems.
4. Remember Opus 4.7 uses adaptive thinking; prompt explicitly if you want faster, more direct replies or more careful step-by-step reasoning.
5. If your workflow benefits from tool use or parallel subagents, say so explicitly, since Opus 4.7 tends to call tools and spawn subagents less often by default.

## Examples
```
User: "Migrate the auth module to the new middleware. Constraints: keep public API stable; update tests; files: src/auth/**. Acceptance: all tests pass."
Assistant: "I will keep the brief from the first turn and run at xhigh effort for the migration, batching questions to reduce extra turns."
```
```
User: "Do a code review of these three packages. Be aggressive about reading files and fanning out."
Assistant: "I will spawn multiple subagents in the same turn to review packages in parallel, and I will read files proactively since Opus 4.7 calls tools less often by default."
```

## Human-readable descriptions
Summarized in [../../description.en.md](../../description.en.md), [../../description.ko.md](../../description.ko.md), [../../description.es.md](../../description.es.md), [../../description.ja.md](../../description.ja.md).

## Companion resources
- Guide: [../../guides/opus-4-7-code-best-practices.en.md](../../guides/opus-4-7-code-best-practices.en.md), [../../guides/opus-4-7-code-best-practices.ko.md](../../guides/opus-4-7-code-best-practices.ko.md), [../../guides/opus-4-7-code-best-practices.es.md](../../guides/opus-4-7-code-best-practices.es.md), [../../guides/opus-4-7-code-best-practices.ja.md](../../guides/opus-4-7-code-best-practices.ja.md)

## Source
Distilled from [Best practices for using Claude Opus 4.7 with Claude Code](https://claude.com/blog/best-practices-for-using-claude-opus-4-7-with-claude-code) (published 2026-04-16).
