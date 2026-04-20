# Extended CLAUDE.md examples

The patterns below come from the [Using CLAUDE.md files](https://claude.com/blog/using-claude-md-files) post. `SKILL.md` keeps only short snippets; richer cases live here so the main instructions stay under the progressive-disclosure budget.

## 1. Monorepo root CLAUDE.md

```markdown
# Repo Overview

Monorepo for the Order Service. Each package is independently versioned.

## Packages

- `packages/api/` — FastAPI public API (pnpm workspace)
- `packages/worker/` — background job runner (Celery)
- `packages/shared/` — shared pydantic models

## Shared conventions

- Python 3.11, ruff + mypy strict
- `make check` runs lint, type check, and unit tests for every package
- Never bypass pre-commit with `--no-verify`

## When editing cross-package code

Update `packages/shared/` first, bump its version, then update consumers.
```

## 2. Next.js app CLAUDE.md

```markdown
# Web Client

Customer-facing Next.js 14 app on Vercel. App Router only.

## Stack

- React 19, TypeScript strict
- Tailwind + shadcn/ui
- Server actions over REST handlers
- Playwright for e2e, Vitest for unit

## Commands

​```bash
pnpm dev            # local dev server
pnpm test           # Vitest
pnpm test:e2e       # Playwright (requires running API)
pnpm typecheck
​```

## Rules

- Never reach into `node_modules` or edit generated files under `.next/`
- Keep server components server-only; mark client components with `"use client"` at the top
- Co-locate tests next to the file under test
```

## 3. Data-science notebook repo CLAUDE.md

```markdown
# Research repo

Exploratory analyses. Notebooks live under `notebooks/`, reusable utilities under `src/`.

## Rules

- Every notebook must have a one-paragraph summary cell at the top
- Lift any function that gets reused into `src/` with a unit test
- Treat notebooks as throwaway; production code belongs in `src/`
- Use `uv` for dependency management, not pip directly
```

## 4. Linking out for long guidance

In the root `CLAUDE.md`:

```markdown
## Deep references

- Migration recipes: [docs/claude/migrations.md](docs/claude/migrations.md)
- Release checklist: [docs/claude/release.md](docs/claude/release.md)
- MCP server catalog: [docs/claude/mcp.md](docs/claude/mcp.md)
```

Keep the root file short; Claude reads linked files on demand.

## 5. Personal global `~/CLAUDE.md`

```markdown
# Personal defaults

- Prefer bullet summaries over prose when replying
- Run tests after every non-trivial change; never say "should work" without proof
- Push back if a request looks destructive — ask first
- Prefer ripgrep, fd, sd; avoid sed/awk unless necessary
```

## 6. MCP usage block

```markdown
## GitHub MCP

- Use only for read-only operations on this repo
- Never create/merge PRs automatically
- Summarize before commenting; no raw diffs in comments

## Postgres MCP

- Read-only credentials only; the write role is not wired in
- Always `EXPLAIN` a query before running it against tables > 1 GB
```

## Source

[Using CLAUDE.md files: Customizing Claude Code for your codebase](https://claude.com/blog/using-claude-md-files) (2025-11-25).
