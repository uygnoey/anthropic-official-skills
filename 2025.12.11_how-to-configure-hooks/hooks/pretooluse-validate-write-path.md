# PreToolUse: validate file path before Write

Installs a `PreToolUse` hook that runs a path validation script before the `Write` tool runs.

## Install

1. Copy `pretooluse-validate-write-path.json` into your Claude Code hooks configuration location.
2. Update the command path to point at your validator script.

## Notes

- The matcher is case-sensitive (`Write`).
- The referenced validator script is not included because the original post uses a placeholder path.

## Source

- https://claude.com/blog/how-to-configure-hooks
