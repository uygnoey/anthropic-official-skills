**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Using Claude Code: session management and 1M context

## What is this post?

A practical walkthrough from the Claude Code team on how to manage sessions and the context window — now up to 1 million tokens — to get better results. The post introduces the `/usage` slash command, explains context rot and compaction, and frames every turn as a branching point between five options: continue, `/rewind`, `/clear`, `/compact`, or delegate to a subagent.

## When useful

- You run long Claude Code sessions and notice output quality degrades over time.
- You are unsure whether to `/compact`, `/clear`, rewind, or spawn a subagent.
- You want a mental model for when context is still "load-bearing" vs. when it should be shed.
- You hit bad autocompacts and want to understand why.
- You want concrete prompts for delegating work to subagents.

## Key points

- The context window includes system prompt, full conversation, every tool call and output, and every file read. It is a hard cutoff.
- **Context rot**: model performance degrades as context grows because attention spreads thin and older content distracts from the current task.
- **Compaction** replaces history with a model-written summary when the window fills up. You can also trigger it yourself with `/compact <hint>`.
- Every turn is a branching point: Continue, `/rewind` (double-Esc), `/clear`, `/compact`, or Subagent.
- Rule of thumb: **new task ⇒ new session**. But related follow-ups (e.g., docs for what you just built) benefit from keeping context.
- **Rewind over correction**: when Claude goes down a wrong path, `/rewind` to just after the useful file reads and re-prompt with what you learned, rather than telling Claude "that didn't work."
- **Compact vs Clear**: compact is lossy but low-effort; clear is more work but you control what carries forward.
- **Bad autocompacts** happen when the model can't predict your next direction — compact proactively with a hint before the window fills.
- **Subagents**: best when the next chunk produces intermediate output you will not need again. Mental test: *do I need this tool output again, or just the conclusion?*

## Bundled resources

- `skills/context-window-management/SKILL.md` — decision framework for picking continue / rewind / compact / clear / subagent.
- `skills/context-window-management/references/decision-table.md` — the situation → tool table from the post.
- `skills/context-window-management/examples/subagent-prompts.md` — the subagent delegation prompts quoted in the post.
- `guides/session-management-1m-context.{en,ko,es,ja}.md` — four-language narrative walkthrough of the post.

## Source

- [Using Claude Code: session management and 1M context](https://claude.com/blog/using-claude-code-session-management-and-1m-context) — published April 15, 2026.
