---
name: context-window-management
description: Decision framework for managing Claude Code sessions and the 1M-token context window. Covers when to continue, rewind, /clear, /compact, or delegate to a subagent, plus how to avoid bad autocompacts and steer compaction with hints.
---

# Context Window Management

A skill for making deliberate choices about session and context management in Claude Code. Based on guidance from the Claude Code team in *Using Claude Code: session management and 1M context* (April 15, 2026).

## When to use

Use this skill whenever you are about to take your next turn in a Claude Code session and the context is non-trivial: you have read several files, run many tool calls, tried an approach that didn't work, or the session has been running long enough that you suspect context rot.

## Instructions

Treat every turn as a branching point with five options. Pick deliberately rather than defaulting to "continue."

1. **Inventory what is in context.** Before choosing, recall: system prompt + full conversation + every tool call/output + every file read. The window is a hard cutoff at 1M tokens, but performance drops well before that because of context rot.
2. **Ask: is my next task the same task, or a new task?**
   - Same task, context still load-bearing → **Continue**.
   - New task → prefer **`/clear`** and write a brief of what actually matters.
   - Related follow-up where rereading would be expensive (e.g. docs for what you just built) → Continue despite the "new task" heuristic.
3. **Did the last attempt go the wrong way?** Use **`/rewind`** (double-Esc) to jump back to just after the useful file reads, then re-prompt with what you learned. Do not just say "that didn't work, try X" — rewinding keeps useful context and drops the failed attempt. Optionally use "summarize from here" to leave a handoff note for the rewound self.
4. **Is the session bloated with stale debugging or exploration?** Run **`/compact <hint>`** with steering instructions (e.g. `/compact focus on the auth refactor, drop the test debugging`). Compact is low-effort and lossy; steering the hint is how you protect what matters.
5. **Will the next chunk generate lots of output you only need the conclusion from?** Delegate to a **subagent**. Mental test: *do I need this tool output again, or just the conclusion?*
6. **Avoid bad autocompacts.** Autocompact fires when the window is almost full, which is also when the model is least sharp (context rot). Compact proactively before that, with a hint describing where you are going next.
7. **Prefer `/clear` over `/compact` for genuinely new tasks.** Compact preserves history approximately; clear lets you control exactly what carries forward.

See [`references/decision-table.md`](./references/decision-table.md) for the situation-to-tool table from the post, and [`examples/subagent-prompts.md`](./examples/subagent-prompts.md) for the exact subagent delegation prompts quoted in the source.

## Examples

### Example 1 — Wrong path after file reads

Claude read five files, tried approach A, it failed. Rather than typing "that didn't work, try B":

- `/rewind` to just after the file reads.
- Re-prompt: "Don't use approach A, the foo module doesn't expose that — go straight to B."

This keeps the file-read context (which was expensive) and drops the dead-end reasoning.

### Example 2 — Long debugging session, pivoting to a new warning

After a long debugging session, you want to tackle a different warning in `bar.ts`. If you let autocompact fire, it may summarize the debugging and drop the mention of the other warning entirely.

Instead, proactively: `/compact focus on what we learned about the auth flow; we still need to fix the warning in bar.ts next.`

### Example 3 — Codebase exploration you only need a summary from

You want Claude to understand how another codebase implemented an auth flow, but you do not want all those file reads in your main context:

> Spin off a subagent to read through this other codebase and summarize how it implemented the auth flow, then implement it yourself in the same way.

Only the subagent's synthesis returns to the parent context.

### Example 4 — Starting a genuinely new task

You finished an auth refactor and now want to work on pagination. Do not continue; run `/clear` and write: "We're adding cursor-based pagination to the /items endpoint. Relevant files: api/items.ts, db/queries.ts. Constraints: must stay backward-compatible with `limit`/`offset` query params."

### Example 5 — Verification you want kept out of main context

> Spin up a subagent to verify the result of this work based on the following spec file.

The subagent runs checks, writes a verdict back, and you keep moving without the verification tool output cluttering the parent window.

## Source

- [Using Claude Code: session management and 1M context](https://claude.com/blog/using-claude-code-session-management-and-1m-context)
