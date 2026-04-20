**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Customizing Claude Code with CLAUDE.md

## What this skill is
Removes the need to re-explain project structure, coding style, and common commands to Claude Code every session. A `CLAUDE.md` at the project root is **auto-loaded into Claude's system prompt at the start of every conversation**.

## When to use
- A team wants consistent Claude behavior across a shared repo (commit the file)
- A monorepo where sub-projects share rules (place at the parent directory)
- Personal global defaults (`~/CLAUDE.md`)
- You notice yourself repeating the same instructions every session

## Core principles
1. **Start with `/init`** — let Claude analyze the codebase and draft the file.
2. **Organize around three axes**: (1) project map, (2) tool connections, (3) standard workflows.
3. **Capture real problems only.** Skip theoretical concerns.
4. **No secrets.** Never include API keys, credentials, or vulnerability details.

## Recommended sections
| Section | Purpose | Contents |
|---|---|---|
| Project map | Project overview | One-liner, directory tree, key dependencies, architecture patterns |
| Tool connections | Custom commands / MCP | How to call custom commands, rules for MCP servers |
| Workflows | Standard procedures | Pre-work questions, explore→plan→code→commit, TDD rules |

## Example: FastAPI project

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

## Example: MCP tool rules (Slack)

```markdown
## Slack MCP usage

- Posts to `#dev-notifications` channel only
- Use for deployment notifications and build failures
- Do not use for individual PR updates
- Rate limited to 10 messages per hour
```

## Authoring checklist
- [ ] Started from `/init`
- [ ] Directory map matches reality
- [ ] Common bash commands listed
- [ ] Zero secrets / credentials
- [ ] Team workflows (tests, PRs) captured
- [ ] No rule without a real recurring problem behind it

## Maintenance tips
- In chat, press the triple-backtick key to append a repeated instruction directly to CLAUDE.md.
- Put repeated workflows under `.claude/commands/` as custom slash commands (MD files, use `$ARGUMENTS` / `$1`).
- Use `/clear` to reset context; delegate isolated tasks to subagents.
- Split very long guidance into separate `.md` files and reference them from CLAUDE.md.

## Source
Distilled from [Using CLAUDE.MD files: Customizing Claude Code for your codebase](https://claude.com/blog/using-claude-md-files) (2025-11-25). Always defer to the original for authoritative guidance.
