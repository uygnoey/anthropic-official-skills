# Prompt caching for commerce agents

## Economics

- A cached input read costs about **one tenth** of a fresh input token.
- A cache write carries roughly a **1.25x** premium, recovered on the second use.
- Cached tokens are also faster to process — roughly **1.5-2x** at around 100k tokens.
- The best commerce deployments observed run at **90-99% cache hit rates**.

## Three segments, ordered by change frequency

Order the context so that everything stable comes first and everything volatile comes last. A
single changed byte early in the prefix invalidates everything after it.

### 1. Global

System prompt and tool definitions. Must be **byte-identical across sessions** — no timestamps,
no user names, no per-session experiment flags, no dictionary iteration order that varies.

### 2. Session

Per-user context and conversation history. Stable within a session, different across sessions.

### 3. Volatile

Current time, current page, anything that changes turn to turn. **Must appear at the end of the
segment**, after everything cacheable.

## Implementation rules

- **Load skills as tool results, not as system prompt appendices.** A skill appended to the
  system prompt changes the global segment for that session and breaks the shared prefix. As a
  tool result, it lands in the cached conversation prefix instead.
- **Roll cache breakpoints forward each turn** so the growing prefix keeps matching.
- **Inject predictable skills upfront.** When a signal — such as the page the user arrived
  from — tells you which skill will be needed, inject it at the start and skip the skill-loading
  turn.

## Checklist

- [ ] Global segment is byte-identical across two fresh sessions (diff it).
- [ ] No volatile value appears before the end of the volatile segment.
- [ ] Skills arrive as tool results.
- [ ] Breakpoints roll forward every turn.
- [ ] Hit rate is monitored per deployment, not just averaged.

## Source

- https://claude.com/blog/the-anatomy-of-effective-commerce-agents
