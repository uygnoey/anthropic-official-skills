---
name: building-on-evolving-models
description: Applies three patterns for building applications on a model whose intelligence keeps improving — use general tools the model already knows, remove scaffolding the model can now do itself, and set boundaries only where UX, observability, or security demand it. Use when the user is designing an agent, LLM-powered app, or tool layer and is deciding how much structure to impose around the model.
---

# Building on Evolving Models

A framework for designing applications that ride rather than fight a model's improving capability. Distilled from the three-pattern framework in the source post; the goal is an app that gets better as the model gets better, instead of one that locks in today's workarounds.

## Instructions

Apply these three patterns in order. Re-evaluate them each time the model meaningfully improves — assumptions about what the model cannot do need to be retested.

### Pattern 1 — Use what the model already knows
Build on general tools the model has seen extensively. Favor:
- A **bash tool** for shell actions.
- A **text editor tool** for viewing, creating, and editing files.
- Composed patterns built on top of these: Agent Skills, programmatic tool calling, a memory tool.

Avoid inventing bespoke tools for behaviors the model already handles with bash + editor.

### Pattern 2 — Ask "what can I stop doing?"
At each layer of scaffolding, check whether the model can now do it itself. Three sub-patterns:

1. **Let the model orchestrate its own actions.** Give it a code-execution tool (bash or a language REPL) so it writes code to express tool calls and filter/pipe outputs, instead of piping everything through its context window.
2. **Let the model manage its own context.**
   - Use Skills — YAML frontmatter for a short description, full skill body loaded via a read-file tool on demand.
   - Use context editing to remove stale or irrelevant turns.
   - Spawn subagents to fork fresh context windows when a subtask does not need the main history.
3. **Let the model persist its own context.**
   - Use compaction to summarize past context into a shorter form.
   - Give it a memory folder it can write to and read from across turns.

If a piece of orchestration, context management, or persistence used to be your job but the model now handles it, delete your code and let the model do it.

### Pattern 3 — Set boundaries carefully
Add structure only where you need one of three things: UX, observability, or security.

- **Design context to maximize cache hits** (see cache-hit principles below). Cached tokens cost about 10% of base input tokens.
- **Promote bash actions to dedicated, declarative tools** when you need:
  - typed arguments for gating (security checks, confirmation on irreversible actions such as external API calls);
  - rendering affordances (e.g., a modal to show a diff before applying);
  - observability (structured logging and tracing).
- Dedicated tools can carry invariants bash cannot — e.g., an `edit` tool with a staleness check so the model does not overwrite a file that changed since it was last read.

### Cache-hit principles (quick reference)

| Principle | Description |
|---|---|
| Static first, dynamic last | Order requests so stable content (system prompt, tools) comes first. |
| Messages for updates | Append a `<system-reminder>` in messages instead of editing the prompt. |
| Don't change models | Caches are model-specific; switching breaks them. Use a subagent if you need a cheaper model for a subtask. |
| Carefully manage tools | Tools sit in the cached prefix; adding or removing one invalidates it. For dynamic discovery, use tool search, which appends without breaking the cache. |
| Update breakpoints | For multi-turn applications, move the breakpoint to the latest message to keep the cache up to date. Use auto-caching. |

## Examples

Benchmarks cited in the source that illustrate the patterns (not fabricated):

- **Use general tools**: Claude 3.5 Sonnet reached 49% on SWE-bench Verified with only a bash tool and a text editor tool. Claude Code is grounded in these same tools.
- **Let the model orchestrate**: On BrowseComp, giving Opus 4.6 the ability to filter its own tool outputs brought accuracy from 45.3% to 61.6%.
- **Let the model manage context via subagents**: With Opus 4.6, spawning subagents improved BrowseComp by 2.8% over the best single-agent runs.
- **Compaction scaling**: On BrowseComp, Sonnet 4.5 stayed flat at 43%; Opus 4.5 scaled to 68% and Opus 4.6 reached 84%.
- **Memory folder**: On BrowseComp-Plus, giving Sonnet 4.5 a memory folder lifted accuracy from 60.4% to 67.2%. In the Pokémon game example, Opus 4.6 kept ~10 well-organized memory files with tactical notes like `/gameplay/learnings.md: - Bellsprout Sleep+Wrap combo: KO FAST with BITE before Sleep Powder lands.`
- **Boundaries for safety**: Claude Code's auto-mode uses a second Claude call to judge bash command safety before execution.

## Anti-patterns

- Building a bespoke tool for behavior the model already handles with bash + editor.
- Keeping orchestration/filtering/summarization scaffolding after the model has become capable enough to do it itself.
- Adding structure without a concrete UX, observability, or security reason.
- Switching models mid-session for cost reasons (breaks the cache) instead of delegating to a subagent.
- Invalidating the cached prefix by mutating the tool list inside a session.
- Assuming yesterday's limitation still holds — retest with each model step change.

## Companion resources

Additional material from the same blog post lives next to this skill in the post folder:

- [`../../guides/three-patterns-app-harness.en.md`](../../guides/three-patterns-app-harness.en.md) / [`../../guides/three-patterns-app-harness.ko.md`](../../guides/three-patterns-app-harness.ko.md) — narrative walk-through of the same three patterns with all source quotes preserved.

## Human-readable descriptions

This skill is summarized for humans in [../../description.en.md](../../description.en.md) and [../../description.ko.md](../../description.ko.md).

## Source

Distilled from [Harnessing Claude's Intelligence — 3 Key Patterns for Building Apps](https://claude.com/blog/harnessing-claudes-intelligence) (published 2026-04-02). Defer to the original for authoritative guidance.
