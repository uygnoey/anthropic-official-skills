# SessionStart: append transcript path to a sessions log

Appends the session transcript path to `~/.claude/sessions.log`.

## Notes

This hook uses `jq` to read the hook payload and extract `.transcript_path`.

## Source

- https://claude.com/blog/how-to-configure-hooks
