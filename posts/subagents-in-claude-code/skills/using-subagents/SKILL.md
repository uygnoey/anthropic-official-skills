---
name: using-subagents
description: Delegates research, parallel edits, or fresh-eyes reviews to subagents (separate AI instances with isolated context) in Claude Code. Use when a task requires reading 10+ files, has 3+ independent subtasks, needs a second opinion before commit, or a complex pipeline like design-then-implement-then-test. Covers four invocation methods (conversational, custom agent file, project policy, slash command skill), four practical patterns, and when NOT to use subagents.
---

# Using Subagents in Claude Code

A subagent is a **separate Claude instance with its own context window**. Delegate tasks that would pollute or overflow the main context, or that benefit from a fresh perspective.

## Instructions

### Step 1: Decide whether a subagent fits

Use a subagent when **any** of these apply:

- The task needs to read 10+ files (e.g., tracing an auth flow)
- There are 3+ independent subtasks with no shared state
- A fresh, implementation-free perspective is valuable (review, verification)
- The task is a pipeline (design → implement → test) where each stage is distinct

Do **not** use a subagent when:

- The work is sequential and each step depends on the last
- Multiple agents would need to edit the same file
- The overhead exceeds the benefit (small tasks)
- Agents must coordinate with each other — subagents can't communicate; use Agent Teams instead

### Step 2: Pick an invocation method

#### Method A: Conversational (lowest friction)

Ask in natural language. Claude decides how to split work.

```
Use subagents to explore this codebase in parallel:

1. Find all API endpoints and summarize their purposes
2. Identify the database schema and relationships
3. Map out the authentication flow

Return a summary of each, not the full file contents.
```

Other valid phrasings: `Use a subagent to explore how authentication works`, `Have a separate agent review this code for security issues`, `Spin up subagents to fix these TypeScript errors across the different packages`.

#### Method B: Custom agent file (reusable specialist)

Drop an MD file under `.claude/agents/` (project) or `~/.claude/agents/` (user). Create with `/agents`.

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

#### Method C: Project policy via CLAUDE.md

Encode a rule so delegation happens automatically.

```markdown
## Code review standards

When asked to review code, ALWAYS use a subagent with READ-ONLY access (Glob, Grep, Read only).
The review should ALWAYS check for:
- Security vulnerabilities
- Performance issues
- Adherence to project patterns in /docs/architecture.md

Return findings as a prioritized list with file:line references.
```

#### Method D: Slash command skill

Create `.claude/skills/deep-review/SKILL.md`. Run with `/deep-review`.

```markdown
---
name: deep-review
description: Comprehensive code review that checks security, performance, and style in parallel. Use when reviewing staged changes before a commit or PR.
---

Run three parallel subagent reviews on the staged changes:

1. Security review - check for vulnerabilities, injection risks, authentication issues, and sensitive data exposure
2. Performance review - check for N+1 queries, unnecessary iterations, memory leaks, and blocking operations
3. Style review - check for consistency with project patterns documented in /docs/style-guide.md

Synthesize findings into a single summary with priority-ranked issues.
Each issue should include the file, line number, and recommended fix.
```

### Step 3: Apply one of four patterns

1. **Research-before-implement** — subagent maps the area first; main agent then writes code.
2. **Parallel edits** — independent files fixed simultaneously.
3. **Fresh-eyes review** — after main agent implements, spawn a read-only subagent to verify.
4. **Pipeline** — design / implement / test each handled by a different subagent.

## Examples

### Research-before-implement

```
Before I implement user notifications, use a subagent to research:
- How are emails currently sent in this codebase?
- Which libraries are available?
- Is there an existing notification abstraction?
```

### Parallel TypeScript fixes across packages

```
Spin up subagents to fix these TypeScript errors across the different packages.
Each subagent should work on one package and return a short summary of what it changed.
```

### Verification before commit

```
I just finished implementing the payment flow. Before I commit, have a read-only
subagent review it for security issues, return a prioritized list of findings.
```

## Operational tips

- Press `Ctrl+B` to send a running subagent to the background.
- Use `/tasks` to inspect running subagents.
- Avoid over-populating specialists; too many candidates weaken auto-delegation.
- Subagents cannot talk to each other. If they must coordinate, use Agent Teams.

## Human-readable descriptions

This skill is summarized for humans in [../../description.en.md](../../description.en.md) and [../../description.ko.md](../../description.ko.md).

## Source

Distilled from [How and when to use subagents in Claude Code](https://claude.com/blog/subagents-in-claude-code) (published 2026-04-07). Defer to the original for authoritative guidance.
