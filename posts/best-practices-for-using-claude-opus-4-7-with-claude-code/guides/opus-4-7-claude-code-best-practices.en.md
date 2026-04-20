[English](./opus-4-7-claude-code-best-practices.en.md) · [한국어](./opus-4-7-claude-code-best-practices.ko.md) · [Español](./opus-4-7-claude-code-best-practices.es.md) · [日本語](./opus-4-7-claude-code-best-practices.ja.md)

# Guide: Best practices for Opus 4.7 in Claude Code

This guide restates the post’s recommendations as a checklist you can apply when configuring prompts and sessions in Claude Code.

## Structuring interactive sessions
- Treat Claude like a capable engineer you delegate to, not a pair programmer you guide line-by-line.
- In the first turn, include intent, constraints, acceptance criteria, and relevant file locations.
- Reduce the number of user turns by batching questions and providing context up front.
- Use auto mode when you trust the model to execute safely with fewer check-ins, especially for long-running tasks.

## Effort level guidance
- `xhigh` is the new default between `high` and `max` and is recommended for most agentic coding work.
- Use `high` to balance intelligence and cost when you are running concurrent sessions or want to reduce spend.
- Use `max` deliberately for genuinely hard problems and expect diminishing returns and more overthinking.

## Adaptive thinking prompts
- Opus 4.7 does not support Extended Thinking with a fixed thinking budget; it uses adaptive thinking.
- To encourage more thinking: ask for careful, step-by-step reasoning before responding.
- To encourage less thinking: ask the model to prioritize responding quickly and directly when in doubt.

## Behavior changes to account for
- Response length is calibrated to task complexity; specify a target voice/length if your workflow needs it.
- The model calls tools less often and reasons more; explicitly say when and why tools should be used if you want more tool use.
- The model spawns fewer subagents by default; explicitly request parallel subagents when fanning out across files/items.

## Source
- Best practices for using Claude Opus 4.7 with Claude Code (2026-04-16): https://claude.com/blog/best-practices-for-using-claude-opus-4-7-with-claude-code
