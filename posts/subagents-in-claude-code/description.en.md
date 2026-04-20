[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Using Subagents in Claude Code

## What this skill is
A subagent is a **separate Claude instance with its own context window**. This skill captures the patterns for delegating research, parallel work, or fresh reviews to subagents so your main session stays focused.

## When to use (strong signals)
- Research-heavy tasks (10+ files)
- 3+ independent subtasks
- Need for a fresh perspective
- Verification before committing
- Pipeline workflows (design → implement → test)

## When NOT to use
- Sequential / dependent work
- Simultaneous edits to the same file
- Small tasks where overhead > benefit
- When agents must coordinate — subagents can't talk to each other; use Agent Teams

## Four ways to invoke

### A. Conversational
```
Use subagents to explore this codebase in parallel:

1. Find all API endpoints and summarize their purposes
2. Identify the database schema and relationships
3. Map out the authentication flow

Return a summary of each, not the full file contents.
```

### B. Custom subagent file (`.claude/agents/`)
```markdown
---
name: security-reviewer
description: Reviews code changes for security vulnerabilities, injection risks, auth issues, and sensitive data exposure. Use proactively before commits touching auth, payments, or user data.
tools: Read, Grep, Glob
model: sonnet
---

You are a security-focused code reviewer. Analyze the provided changes for:
- SQL injection, XSS, and command injection risks
- Authentication and authorization gaps
- Sensitive data in logs, errors, or responses
- Insecure dependencies or configurations

Return a prioritized list of findings with file:line references and a recommended fix for each.
Be critical. If you find nothing, say so explicitly rather than inventing issues.
```
Invoke: `Have the security-reviewer look at the staged changes.`

### C. CLAUDE.md policy
```markdown
## Code review standards

When asked to review code, ALWAYS use a subagent with READ-ONLY access (Glob, Grep, Read only).
The review should ALWAYS check for:
- Security vulnerabilities
- Performance issues
- Adherence to project patterns in /docs/architecture.md
```

### D. Slash command skill
`.claude/skills/deep-review/SKILL.md` → run with `/deep-review`.

## Four practical patterns
1. **Research-before-implement** — explore the area first, then code
2. **Parallel edits** — independent files fixed simultaneously
3. **Fresh-eyes review** — after implementation, a read-only subagent verifies
4. **Pipeline** — design / implement / test handled by different subagents

## Operational tips
- `Ctrl+B` — send a subagent to the background.
- `/tasks` — inspect running subagents.
- Don't over-populate specialists; too many candidates destabilize auto-delegation.
- Subagents can't communicate. Use Agent Teams when they must.

## Bundled resources
- Skills (2): `skills/using-subagents/SKILL.md`, `skills/deep-review/SKILL.md`
- Agent (1): `agents/security-reviewer.md`
- Hook (1): `hooks/check-tests.json` / `hooks/check-tests.md`

## Source
Distilled from [How and when to use subagents in Claude Code](https://claude.com/blog/subagents-in-claude-code) (2026-04-07). Defer to the original for authoritative guidance.
