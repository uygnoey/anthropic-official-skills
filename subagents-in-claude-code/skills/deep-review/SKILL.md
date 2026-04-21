---
name: deep-review
description: Comprehensive code review that runs security, performance, and style reviews in parallel as subagents and synthesizes findings. Use when reviewing staged changes before a commit or PR.
---

# Deep Review

Run three parallel subagent reviews on the staged changes and merge their findings into one prioritized summary.

## Instructions

1. Security review — check for vulnerabilities, injection risks, authentication issues, and sensitive data exposure.
2. Performance review — check for N+1 queries, unnecessary iterations, memory leaks, and blocking operations.
3. Style review — check for consistency with project patterns documented in `/docs/style-guide.md`.

Run all three in parallel (not sequentially). Each reviewer should use read-only tools only.

## Output format

Synthesize findings into a single summary with priority-ranked issues. Each issue must include:

- File and line number (`path/to/file.ext:123`)
- Category (security / performance / style)
- Severity (high / medium / low)
- Recommended fix

If a reviewer finds nothing, it must say so explicitly rather than inventing issues.

## Examples

Invocation in a Claude Code session:

```
/deep-review
```

Expected synthesized output shape:

```
High severity
- src/api/payments.ts:142 (security) — User input flows into a raw SQL string. Parameterize.
- src/db/pool.ts:37 (performance) — N+1 inside a loop over orders. Batch-fetch once.

Medium severity
- src/components/Cart.tsx:88 (style) — Diverges from the list-rendering pattern in /docs/style-guide.md.

No findings
- Style reviewer reports no additional style deviations.
```

## Source

Distilled verbatim from [How and when to use subagents in Claude Code](https://claude.com/blog/subagents-in-claude-code) (published 2026-04-07).
