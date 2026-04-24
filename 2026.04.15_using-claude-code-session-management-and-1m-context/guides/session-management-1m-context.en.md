**English** · [한국어](./session-management-1m-context.ko.md) · [Español](./session-management-1m-context.es.md) · [日本語](./session-management-1m-context.ja.md)

# Session Management and the 1M Context Window

A narrative walkthrough of the guidance in *Using Claude Code: session management and 1M context* (April 15, 2026).

## Why this matters

The Claude Code team rolled out the `/usage` slash command and heard a consistent theme in customer conversations: usage patterns vary enormously. Some developers keep one or two terminals open for days; others start a new session per prompt. With the new 1M-token context window in Claude Code, these choices matter more, not less.

Almost all the variance in outcomes comes down to **how you manage your context window**.

## A quick primer

The context window is everything the model can see at once when generating its next response: system prompt, the conversation so far, every tool call and its output, and every file that has been read. Claude Code's window holds one million tokens.

Context has a cost, though — a phenomenon called **context rot**. As the context grows, attention spreads across more tokens, and older, irrelevant content starts to distract from the current task. Model performance degrades.

When the window nears its limit, Claude Code automatically summarizes the task into a shorter description and continues in a new window. This is **compaction**. You can also trigger it yourself.

## Every turn is a branching point

After Claude finishes responding, you have five options:

- **Continue** — send another message in the same session.
- **`/rewind`** (or double-Esc) — jump back to a previous message and try again. Messages after that point are dropped.
- **`/clear`** — start a new session, usually with a brief distilled from what you just learned.
- **`/compact`** — summarize the session so far and keep going on top of the summary.
- **Subagents** — delegate the next chunk of work to an agent with its own clean context, and only pull its result back in.

Continuing is the default, but the other four are how you manage context deliberately.

## When to start a new session

Rule of thumb: **new task ⇒ new session**. The 1M window means you can do longer tasks more reliably — full-stack apps from scratch, for instance — but context rot still happens.

Exceptions exist. Writing documentation for a feature you just implemented is technically a new task, but you probably do not want to pay to reread all those files. Keep the session.

## Rewinding instead of correcting

`/rewind` (double-Esc) jumps back to any previous message and re-prompts from there, dropping everything after.

When Claude reads five files, tries an approach, and it fails, the instinctive reply is "that didn't work, try X instead." The better move is often to rewind to just after the file reads and re-prompt with what you learned: *"Don't use approach A, the foo module doesn't expose that — go straight to B."*

You can also use "summarize from here" or `/rewind` to have Claude write a handoff note — a message from the future self that tried something and found it didn't work — before rewinding.

## Compacting vs. clearing

`/compact` asks the model to summarize the conversation and replaces history with that summary. It is lossy, but it requires no effort from you, and Claude may be thorough about capturing learnings. You can steer it: `/compact focus on the auth refactor, drop the test debugging`.

`/clear` starts fresh, but *you* write down what matters: *"we're refactoring the auth middleware, the constraint is X, the files that matter are A and B, we've ruled out approach Y."* More work, but the resulting context is exactly what you decided.

## Why autocompacts sometimes fail

A bad autocompact usually means the model could not predict your next direction. A long debugging session compacts, then your next message is "now fix the other warning we saw in `bar.ts`." But because the session was focused on debugging, that warning may not have made it into the summary.

This is particularly hard because the model is at its least capable point when compacting — context rot is already in effect. With 1M context, you have more time to `/compact` proactively with a hint describing where you are going.

## Subagents and fresh context

Subagents shine when a chunk of work will produce lots of intermediate output you will never need again.

When Claude spawns a subagent via the Agent tool, the subagent gets a clean context window, does whatever work it needs, synthesizes the result, and returns only the final report. The parent never sees the intermediate noise.

The mental test from Anthropic: *will I need this tool output again, or just the conclusion?*

Example prompts for explicitly invoking subagents:

- "Spin up a subagent to verify the result of this work based on the following spec file."
- "Spin off a subagent to read through this other codebase and summarize how it implemented the auth flow, then implement it yourself in the same way."
- "Spin off a subagent to write the docs on this feature based on my git changes."

## Putting it together

| Situation | Consider reaching for | Why |
|---|---|---|
| Same task, context is still relevant | Continue | Everything in the window is still load-bearing; don't pay to rebuild it. |
| Claude went down a wrong path | Rewind (double-Esc) | Keep the useful file reads, drop the failed attempt, re-prompt with what you learned. |
| Mid-task but the session is bloated with stale debugging/exploration | `/compact <hint>` | Low effort; Claude decides what mattered. Steer it with instructions if needed. |
| Starting a genuinely new task | `/clear` | Zero rot; you control exactly what carries forward. |
| Next step will generate lots of output you'll only need the conclusion from | Subagent | Intermediate tool noise stays in the child's context; only the result comes back. |

## Source

- [Using Claude Code: session management and 1M context](https://claude.com/blog/using-claude-code-session-management-and-1m-context) — Thariq Shihipar, April 15, 2026.
