# Context Management Decision Table

Reproduced from the "Putting it together" table in *Using Claude Code: session management and 1M context* (Anthropic, April 15, 2026).

| Situation | Consider reaching for | Why |
|---|---|---|
| Same task, context is still relevant | Continue | Everything in the window is still load-bearing; don't pay to rebuild it. |
| Claude went down a wrong path | Rewind (double-Esc) | Keep the useful file reads, drop the failed attempt, re-prompt with what you learned. |
| Mid-task but the session is bloated with stale debugging/exploration | `/compact <hint>` | Low effort; Claude decides what mattered. Steer it with instructions if needed. |
| Starting a genuinely new task | `/clear` | Zero rot; you control exactly what carries forward. |
| Next step will generate lots of output you'll only need the conclusion from (codebase search, verification, doc writing) | Subagent | Intermediate tool noise stays in the child's context; only the result comes back. |

## Source

- [Using Claude Code: session management and 1M context](https://claude.com/blog/using-claude-code-session-management-and-1m-context)
