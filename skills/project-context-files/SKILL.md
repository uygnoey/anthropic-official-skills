---
name: project-context-files
description: Authors and audits CLAUDE.md project-context files that get auto-loaded into every Claude Code conversation. Use when a developer asks how to create a CLAUDE.md, wants to stop re-explaining project structure or conventions each session, needs a team-wide configuration for consistent AI behavior in a repo, or asks to review/clean up an existing CLAUDE.md.
---

# Project Context Files (CLAUDE.md)

A `CLAUDE.md` file supplies persistent project context that Claude Code auto-loads at the start of every conversation in that project. It eliminates repeated re-explanation of structure, conventions, and commands.

## Instructions

### 1. Decide where the file belongs

- **Project root, committed**: team-wide rules for the repo.
- **Parent directory above sub-projects**: monorepo rules shared by all children.
- **`~/CLAUDE.md`**: personal global defaults.

### 2. Bootstrap from `/init`

Run `/init` inside the project. Claude analyzes the codebase and writes a draft. Always start here rather than writing from scratch.

### 3. Keep only three kinds of content

| Kind | Contents |
|---|---|
| Project map | One-line purpose, key directory tree, main dependencies, architecture pattern |
| Tool connections | Custom slash commands, MCP server rules, preferred build tools |
| Workflows | Pre-work checks, coding loop, testing expectations, PR conventions |

### 4. Enforce hard rules

- Never include secrets (API keys, credentials, vulnerability details).
- Every line must solve a **real recurring problem**. Delete theoretical rules.
- Update when the codebase changes. Stale rules are worse than none.
- For long guidance, link out to a separate `.md` (see [EXAMPLES.md](EXAMPLES.md)).

### 5. Review checklist

Before committing, verify:

- [ ] Directory map matches the current structure
- [ ] Common bash commands listed
- [ ] No secrets or credentials
- [ ] Workflow rules (tests, PRs) captured
- [ ] Nothing included without a concrete recurring motivation

## Examples

### FastAPI project CLAUDE.md

```markdown
# Project Context

When working with this codebase, prioritize readability over cleverness.
Ask clarifying questions before making architectural changes.

## About This Project

FastAPI REST API for user authentication and profiles.
Uses SQLAlchemy for database operations and Pydantic for validation.

## Key Directories

- `app/models/` - database models
- `app/api/` - route handlers
- `app/core/` - configuration and utilities

## Standards

- Type hints required on all functions
- pytest for testing (fixtures in `tests/conftest.py`)
- PEP 8 with 100 character lines

## Common Commands

​```bash
uvicorn app.main:app --reload  # dev server
pytest tests/ -v               # run tests
​```

## Notes

All routes use `/api/v1` prefix. JWT tokens expire after 24 hours.
```

### MCP server usage rules

```markdown
## Slack MCP usage

- Posts to `#dev-notifications` channel only
- Use for deployment notifications and build failures
- Do not use for individual PR updates
- Rate limited to 10 messages per hour
```

## Maintenance tips

- During a chat, append a recurring instruction directly by pressing the triple-backtick key.
- Put repeatable workflows under `.claude/commands/` as slash commands (use `$ARGUMENTS` or `$1`).
- Use `/clear` to reset polluted context; delegate isolated explorations to subagents.
- Split long guidance into referenced `.md` files; keep `CLAUDE.md` itself short.

## Human-readable descriptions

This skill is summarized for humans in [description.en.md](description.en.md) and [description.ko.md](description.ko.md).

## Source

Distilled from [Using CLAUDE.MD files: Customizing Claude Code for your codebase](https://claude.com/blog/using-claude-md-files) (published 2025-11-25). Always defer to the original for authoritative guidance.
