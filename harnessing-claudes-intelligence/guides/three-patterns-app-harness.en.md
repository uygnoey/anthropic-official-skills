**English** · [한국어](./three-patterns-app-harness.ko.md) · [Español](./three-patterns-app-harness.es.md) · [日本語](./three-patterns-app-harness.ja.md)

# Three patterns for building apps that keep pace with Claude

This guide summarizes three patterns from the source post for designing applications (including agents) that keep up with Claude’s evolving capabilities while balancing latency and cost.

## Pattern 1 — Use what Claude knows
- Prefer building with tools Claude already understands well.
- The post highlights using a **bash tool** and a **text editor tool** for viewing/creating/editing files as a strong base.
- Higher-level constructs (e.g., skills, programmatic tool calling, memory) can be built from these general tools.

## Pattern 2 — Ask “what can I stop doing?” (test harness assumptions)
Agent harnesses often include structure that encodes assumptions about what Claude can’t do. As Claude improves, those assumptions can become dead weight.

### Let Claude orchestrate its own actions
- Avoid forcing every tool result into Claude’s context window.
- If Claude only needs a slice of output (e.g., one column in a large table), pushing all rows into context is slow and expensive.
- Instead, give Claude a code execution tool (bash or a REPL) so it can write code that:
  - calls tools,
  - filters/aggregates output,
  - and pipes results to the next action,
  while only returning the minimal final output back into context.

### Let Claude manage its own context
- Avoid overloading system prompts with task-specific instructions that rarely apply.
- Use progressive disclosure:
  - a short overview is preloaded (e.g., a skill’s YAML frontmatter),
  - and Claude reads full content only when needed.
- Remove stale or irrelevant context through selective context editing.
- Use subagents to split work into fresh context windows when isolating a task is beneficial.

### Let Claude persist its own context
- Long-running agents can exceed a single context window.
- Use compaction to summarize past context while maintaining continuity.
- Use a memory folder so Claude can write important information to files and read it later.
- The post’s game example contrasts transcript-like notes versus tactical, distilled learnings organized into a directory.

## Pattern 3 — Set boundaries carefully
Agent harnesses should enforce UX, cost, and security boundaries.

### Design context to maximize cache hits
Because the Messages API is stateless, the harness re-sends prior context each turn. The post provides principles to increase prompt cache reuse:
- **Static first, dynamic last**: put stable content (system prompt, tools) before frequently changing inputs.
- **Messages for updates**: append updates (e.g., a `system-reminder` block) instead of editing earlier prompt text.
- **Don’t change models**: caches are model-specific; switching breaks them (use a subagent if you need a cheaper model).
- **Carefully manage tools**: adding/removing tools invalidates caches; use tool search for dynamic discovery without breaking cache.
- **Update breakpoints**: for multi-turn apps, move the breakpoint forward so the cache reflects the latest stable prefix; use auto-caching.

### Use declarative tools for UX, observability, and security
- A bash tool gives broad power but the harness sees only an untyped command string.
- Promoting actions into typed, declarative tools gives the harness hooks to:
  - intercept and gate actions (e.g., user confirmation for external API calls),
  - add safety checks (e.g., staleness checks for edit tools),
  - render UX affordances (modals, choices, blocking for user input),
  - and log/trace/replay structured arguments for observability.
- Re-evaluate which actions deserve promotion over time; the post describes Claude Code auto-mode using a second Claude to judge bash safety as one possible boundary pattern.

## Ongoing practice
- Re-test assumptions whenever Claude’s capabilities change.
- Prune resets or scaffolding that existed only to compensate for older model limitations.

## Source
Distilled from [Harnessing Claude's Intelligence | 3 Key Patterns for Building Apps](https://claude.com/blog/harnessing-claudes-intelligence) (published 2026-04-02).
