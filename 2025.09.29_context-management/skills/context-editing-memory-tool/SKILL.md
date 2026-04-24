---
name: context-editing-memory-tool
description: Apply practical rules for what to keep in an agent’s context vs what to persist to memory when building long-running workflows on the Claude Developer Platform.
---

## Instructions
Use this skill to keep long-running agents effective as tool results accumulate.

1. **Classify new information** as one of:
   - *Ephemeral*: needed only for the next 1–3 steps.
   - *Session state*: needed until the current workflow completes.
   - *Long-lived knowledge*: needed across sessions (decisions, constraints, learned facts).
2. **Keep context minimal**: leave only what is required to reason about the next steps.
3. **Persist long-lived knowledge** to memory (file-based storage you control).
4. **Write memory entries like documentation**:
   - Title
   - Date/when learned
   - Why it matters
   - How to use it next time
5. **When nearing limits**, rely on context editing to remove stale tool results, but make sure any *long-lived knowledge* has already been written to memory.

See `references/store-vs-keep-checklist.md` for common decisions.

## Examples
### Example: coding agent over a large codebase
- Keep in context: current file, failing test, immediate hypotheses.
- Persist to memory: root cause analysis, architectural decisions, conventions, and next steps.

### Example: research agent
- Keep in context: current question, the 1–2 most relevant findings.
- Persist to memory: validated conclusions, citations, and a bibliography pointer.
