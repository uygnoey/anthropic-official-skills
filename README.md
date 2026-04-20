**English** · [한국어](./README.ko.md) · [Español](./README.es.md) · [日本語](./README.ja.md)

# skills-from-claude-blog

> Artifacts distilled from posts on [claude.com/blog](https://www.claude.com/blog),
> organized by Claude Code's official extension specs.
> Not affiliated with Anthropic — this is a third-party summary project.

A repository that converts official Claude blog posts into **Claude Code's official specs matching each post's character**. A batch runs every 4 hours to reflect new posts and unprocessed ones.

## Layout (per blog post)

One blog post = one `posts/<blog-slug>/` folder. The subfolders below appear conditionally based on the post's character.

```
posts/<blog-slug>/
├── description.en.md               # Human-readable English summary (always)
├── description.ko.md               # Korean summary (always)
├── description.es.md               # Spanish summary (always)
├── description.ja.md               # Japanese summary (always)
├── source.json                     # Source metadata (always)
│
├── skills/<name>/SKILL.md          # A. Agent Skills spec
├── agents/<name>.md                # B. Claude Code Subagent spec
├── guides/<name>.{en,ko,es,ja}.md  # C. Free-form multilingual guides
├── hooks/<name>.json +.md          # D. Claude Code Hooks JSON + notes
├── output-styles/<name>.md         # E. Output Style spec
└── plugin/                         # G. Plugin bundle (rare)
    ├── .claude-plugin/plugin.json
    └── skills|agents|hooks|output-styles/...
```

### Official spec references
- [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) — `SKILL.md`
- [Claude Code Subagents](https://code.claude.com/docs/en/sub-agents) — `agents/<name>.md`
- [Claude Code Hooks](https://code.claude.com/docs/en/hooks) — `hooks/<name>.json`
- [Output Styles](https://code.claude.com/docs/en/output-styles) — `output-styles/<name>.md`
- [Plugins](https://code.claude.com/docs/en/plugins) — `plugin/` bundle

### Spec selection matrix

| Verdict | Trigger question | Artifact |
|---|---|---|
| **A. Skill** | Does the post describe a reusable **pattern / principle / framework / how-to**? | `skills/<name>/SKILL.md` |
| **B. Subagent** | Does the post explicitly define **2+ named agent roles**? | `agents/<name>.md` each |
| **C. Guide** | Is the post **deployment / architecture / methodology / survey** in character? | `guides/<name>.{en,ko,es,ja}.md` |
| **D. Hook** | Does the post automate a **lifecycle event** (PreToolUse, PostToolUse, Stop, SessionStart…)? | `hooks/<name>.json` + `.md` notes |
| **E. Output Style** | Does the post define a **full system-prompt tone/role/format swap** (not a one-line tip)? | `output-styles/<name>.md` |
| **G. Plugin** | Does the post center on **bundling multiple artifacts for distribution**? | whole `plugin/` bundle |

- **F. Slash Commands are not produced.** Official docs mark `.claude/commands/` as legacy and recommend `.claude/skills/`, so posts covering slash commands are **converted into Skills**.
- Multiple verdicts applying at once is normal. Produce all.
- When uncertain, **default to including A**. Skills are the most practically reusable.
- **Never invent roles, patterns, or scripts that aren't in the source.** If unsure, quote the source.

## Drop-in usage

Each artifact can be copied into a project as-is.

| Artifact | Destination |
|---|---|
| `skills/<name>/` | `.claude/skills/<name>/` or `~/.claude/skills/<name>/` |
| `agents/<name>.md` | `.claude/agents/<name>.md` or `~/.claude/agents/<name>.md` |
| `hooks/<name>.json` content | Merge into the `hooks` field of `.claude/settings.json` |
| `output-styles/<name>.md` | `.claude/output-styles/<name>.md` |
| `plugin/` | Load with `--plugin-dir ./plugin` |

## Index

| Blog post | Published | Artifacts |
|---|---|---|
| [Best practices for using Claude Opus 4.7 with Claude Code](https://claude.com/blog/best-practices-for-using-claude-opus-4-7-with-claude-code) | 2026-04-16 | 1 skill + 1 guide |
| [Redesigning Claude Code on desktop for parallel agents](https://claude.com/blog/claude-code-desktop-redesign) | 2026-04-14 | 1 skill |
| [Preparing your security program for AI-accelerated offense](https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense) | 2026-04-10 | 2 skills + 3 agents + 1 guide |
| [Claude Managed Agents: get to production 10x faster](https://claude.com/blog/claude-managed-agents) | 2026-04-08 | 1 guide |
| [Subagents in Claude Code](https://claude.com/blog/subagents-in-claude-code) | 2026-04-07 | 2 skills + 1 agent + 1 hook |
| [Harnessing Claude's Intelligence \| 3 Key Patterns for Building Apps](https://claude.com/blog/harnessing-claudes-intelligence) | 2026-04-02 | 1 skill + 1 guide |
| [Auto mode for Claude Code](https://claude.com/blog/auto-mode) | 2026-03-24 | 1 skill |
| [Claude builds interactive visuals right in your conversation](https://claude.com/blog/claude-builds-visuals) | 2026-03-12 | 1 skill |
| [How enterprises are building AI agents in 2026](https://claude.com/blog/how-enterprises-are-building-ai-agents-in-2026) | 2025-12-09 | 1 guide |
| [Using CLAUDE.md files](https://claude.com/blog/using-claude-md-files) | 2025-11-25 | 1 skill |
| [Improving frontend design through Skills](https://claude.com/blog/improving-frontend-design-through-skills) | 2025-11-12 | 1 skill + 1 guide |
| [Best practices for prompt engineering](https://claude.com/blog/best-practices-for-prompt-engineering) | 2025-11-10 | 1 skill |
| [Building AI agents for financial services](https://claude.com/blog/building-ai-agents-in-financial-services) | 2025-10-30 | 1 skill + 3 agents + 1 guide |
| [Claude Code on the web](https://claude.com/blog/claude-code-on-the-web) | 2025-10-20 | 1 skill |
| [Claude and Slack](https://claude.com/blog/claude-and-slack) | 2025-10-01 | 1 skill + 1 guide |

All guides and summaries are available in English, Korean, Spanish, and Japanese. Click the language switcher at the top of each file.

## Batch operation

- A Perplexity Computer cron runs every 4 hours.
- Post list is harvested from `https://www.claude.com/sitemap.xml` and the `/blog` index.
- Priority: new since last run (newest → oldest) → unprocessed older posts (oldest → newest) → unknown pub-date.
- Up to 2 posts per run.

## Authoring guidelines

1. `SKILL.md` and `agents/*.md` follow the official spec (English).
2. Hook JSON reflects the post's behavior verbatim; shell commands cite the source in comments.
3. Output Styles copy the post's tone/role/format; if unsure, downgrade to a guide.
4. `name` fields (Skill, Subagent, Output Style, Plugin): `^[a-z0-9-]+$`, ≤64 chars, forbidden reserved words `claude`, `anthropic`.
5. `description` is third-person and ≤1024 chars (Skill / Subagent).
6. `guides/` are authored in all four languages (`.en.md`, `.ko.md`, `.es.md`, `.ja.md`) with a language switcher at the top.
7. Human summaries (`description.*.md`) cover the same four languages with a language switcher.
8. **Never invent content not in the source.** If unsure, fall back to "see source".

## Files

```
.
├── posts/                       # One folder per blog post
├── scripts/
│   ├── list_pending.py          # List pending URLs
│   ├── mark_processed.py        # Mark a URL processed
│   ├── update_last_run.py       # Stamp batch timestamp
│   └── validate.py              # Pre-commit validator for all specs
└── state/
    └── processed.json           # Processed URLs + last_run_at
```

## License

- Source posts (Claude blog) are © Anthropic. This repo contains summaries and quotations for study and reference only.
- Repository code: MIT License.
