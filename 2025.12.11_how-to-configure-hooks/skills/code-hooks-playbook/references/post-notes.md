# Notes and constraints (from the source post)

- Hooks have a **60-second default timeout**, configurable per hook.
- Matchers are **case sensitive** (e.g., `bash` will not match the `Bash` tool).
- When multiple hooks match an event, they can run **in parallel** and identical commands may be deduplicated.
- Hook configuration changes require explicit review/approval in the `/hooks` menu before they take effect.
- Hooks execute arbitrary shell commands with your user permissions; validate inputs and avoid operating on sensitive files.

## Source

- https://claude.com/blog/how-to-configure-hooks
