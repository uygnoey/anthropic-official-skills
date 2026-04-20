# Subagent Delegation Prompts

Exact prompts quoted in *Using Claude Code: session management and 1M context* as examples of when to explicitly ask Claude to spin up a subagent rather than continue in the parent context.

## Verification against a spec

> Spin up a subagent to verify the result of this work based on the following spec file.

Use when you want the verification tool output kept out of your main context — only the verdict should return.

## Learning from another codebase

> Spin off a subagent to read through this other codebase and summarize how it implemented the auth flow, then implement it yourself in the same way.

Use when exploratory reads across an unfamiliar codebase would otherwise flood the parent window. The subagent synthesizes a summary; implementation happens in the parent.

## Documentation from git changes

> Spin off a subagent to write the docs on this feature based on my git changes.

Use when documentation writing requires diff exploration that has no reuse value beyond the resulting doc.

## The mental test

> *Will I need this tool output again, or just the conclusion?*

If the answer is "just the conclusion," delegate to a subagent.

## Source

- [Using Claude Code: session management and 1M context](https://claude.com/blog/using-claude-code-session-management-and-1m-context)
