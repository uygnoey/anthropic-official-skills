**English** · [한국어](./README.ko.md) · [Español](./README.es.md) · [日本語](./README.ja.md)

# skills-from-claude-blog

> Artifacts distilled from posts on [claude.com/blog](https://www.claude.com/blog),
> organized by Claude Code's official extension specs.
> Not affiliated with Anthropic — this is a third-party summary project.

A repository that converts official Claude blog posts into **Claude Code's official specs matching each post's character**. A batch runs every 4 hours to reflect new posts and unprocessed ones.

## Layout (per blog post)

One blog post = one `<YYYY.MM.DD>_<blog-slug>/` folder at the repo root, where the date prefix is the post's `published_date` and `<blog-slug>` is the last URL segment. Folders sort naturally from newest to oldest on GitHub. The subfolders below appear conditionally based on the post's character.

```
<YYYY.MM.DD>_<blog-slug>/
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
| [New connectors in Claude for everyday life](https://claude.com/blog/connectors-for-everyday-life) | 2026-04-23 | 1 skill |
| [Built-in memory for Claude Managed Agents](https://claude.com/blog/claude-managed-agents-memory) | 2026-04-23 | 1 skill + 1 guide |
| [Building agents that reach production systems with MCP](https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp) | 2026-04-22 | 1 skill |
| [Meet the winners of our Built with Opus 4.6 Claude Code hackathon](https://claude.com/blog/meet-the-winners-of-our-built-with-opus-4-6-claude-code-hackathon) | 2026-04-20 | 1 skill |
| [Best practices for using Claude Opus 4.7 with Claude Code](https://claude.com/blog/best-practices-for-using-claude-opus-4-7-with-claude-code) | 2026-04-16 | 1 skill + 1 guide |
| [Using Claude Code: session management and 1M context](https://claude.com/blog/using-claude-code-session-management-and-1m-context) | 2026-04-15 | 1 skill + 1 guide |
| [Introducing routines in Claude Code](https://claude.com/blog/introducing-routines-in-claude-code) | 2026-04-14 | 1 skill + 1 guide |
| [Redesigning Claude Code on desktop for parallel agents](https://claude.com/blog/claude-code-desktop-redesign) | 2026-04-14 | 1 skill |
| [Seeing like an agent: how we design tools in Claude Code](https://claude.com/blog/seeing-like-an-agent) | 2026-04-10 | 1 skill |
| [Preparing your security program for AI-accelerated offense](https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense) | 2026-04-10 | 2 skill + 3 agent + 1 guide |
| [Multi-agent coordination patterns: Five approaches and when to use them](https://claude.com/blog/multi-agent-coordination-patterns) | 2026-04-10 | 1 skill + 1 guide |
| [The advisor strategy: Give agents an intelligence boost](https://claude.com/blog/the-advisor-strategy) | 2026-04-09 | 1 skill |
| [Making Claude Cowork ready for enterprise](https://claude.com/blog/cowork-for-enterprise) | 2026-04-09 | 1 skill |
| [Claude Managed Agents: get to production 10x faster](https://claude.com/blog/claude-managed-agents) | 2026-04-08 | 1 guide |
| [How Carta Healthcare gets AI to reason like a clinical abstractor](https://claude.com/blog/carta-healthcare-clinical-abstractor) | 2026-04-08 | 1 skill |
| [How and when to use subagents in Claude Code](https://claude.com/blog/subagents-in-claude-code) | 2026-04-07 | 2 skill + 1 agent + 1 hook |
| [Harnessing Claude's Intelligence: 3 Key Patterns for Building Apps](https://claude.com/blog/harnessing-claudes-intelligence) | 2026-04-02 | 1 skill + 1 guide |
| [Audit Claude Platform activity with the Compliance API](https://claude.com/blog/claude-platform-compliance-api) | 2026-03-30 | 1 skill |
| [Auto mode for Claude Code](https://claude.com/blog/auto-mode) | 2026-03-24 | 1 skill |
| [Put Claude to work on your computer](https://claude.com/blog/dispatch-and-computer-use) | 2026-03-23 | 1 skill |
| [Code with Claude comes to San Francisco, London, and Tokyo](https://claude.com/blog/code-with-claude-san-francisco-london-tokyo) | 2026-03-18 | 1 skill + 1 guide |
| [Claude builds interactive visuals right in your conversation](https://claude.com/blog/claude-builds-visuals) | 2026-03-12 | 1 skill |
| [Advancing Claude for Excel and PowerPoint](https://claude.com/blog/claude-excel-powerpoint-updates) | 2026-03-11 | 1 skill + 1 guide |
| [Common workflow patterns for AI agents](https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them) | 2026-03-05 | 1 skill + 1 guide |
| [Cowork and plugins for finance](https://claude.com/blog/cowork-plugins-finance) | 2026-02-24 | 1 guide |
| [Cowork and plugins for teams across the enterprise](https://claude.com/blog/cowork-plugins-across-enterprise) | 2026-02-24 | 1 guide |
| [Behind the model launch: What customers discovered testing Claude Opus 4.6 early](https://claude.com/blog/behind-model-launch-what-customers-discovered-testing-claude-opus-4-6-early) | 2026-02-09 | 1 skill |
| [Customize Cowork with plugins - Claude.ai](https://claude.com/blog/cowork-plugins) | 2026-01-30 | 1 guide |
| [Measure Claude Code's impact with contribution metrics](https://claude.com/blog/contribution-metrics) | 2026-01-29 | 1 skill |
| [A complete guide to building skills for Claude](https://claude.com/blog/complete-guide-to-building-skills-for-claude) | 2026-01-29 | 1 skill + 1 guide |
| [Updates to Claude Team](https://claude.com/blog/claude-team-updates) | 2026-01-28 | 1 skill |
| [Building multi-agent systems: When and how to use them](https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them) | 2026-01-23 | 1 skill |
| [Building agents with Skills: Equipping agents for specialized work](https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work) | 2026-01-22 | 1 skill + 1 guide |
| [Eight trends defining how software gets built in 2026](https://claude.com/blog/eight-trends-defining-how-software-gets-built-in-2026) | 2026-01-21 | 1 skill |
| [Extending Claude's capabilities with skills and MCP servers](https://claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers) | 2025-12-19 | 1 skill |
| [How enterprises are building AI agents in 2026](https://claude.com/blog/how-enterprises-are-building-ai-agents-in-2026) | 2025-12-09 | 1 guide |
| [Claude Code and Slack](https://claude.com/blog/claude-code-and-slack) | 2025-12-08 | 1 skill |
| [Using CLAUDE.MD files: Customizing Claude Code for your codebase](https://claude.com/blog/using-claude-md-files) | 2025-11-25 | 1 skill |
| [How three YC startups built their companies with Claude Code](https://claude.com/blog/building-companies-with-claude-code) | 2025-11-17 | 1 skill + 1 guide |
| [Improving frontend design through Skills](https://claude.com/blog/improving-frontend-design-through-skills) | 2025-11-12 | 1 skill + 1 guide |
| [Best practices for prompt engineering](https://claude.com/blog/best-practices-for-prompt-engineering) | 2025-11-10 | 1 skill |
| [Building AI agents for startups](https://claude.com/blog/building-ai-agents-for-startups) | 2025-11-03 | 1 skill |
| [Building AI agents in healthcare and life sciences](https://claude.com/blog/building-ai-agents-in-healthcare-and-life-sciences) | 2025-10-30 | 1 skill + 1 guide |
| [Building AI agents for financial services](https://claude.com/blog/building-ai-agents-in-financial-services) | 2025-10-30 | 1 skill + 3 agent + 1 guide |
| [Claude Code on the web](https://claude.com/blog/claude-code-on-the-web) | 2025-10-20 | 1 skill |
| [Build responsive web layouts](https://claude.com/blog/build-responsive-web-layouts) | 2025-10-10 | 1 skill |
| [Customize Claude Code with plugins](https://claude.com/blog/claude-code-plugins) | 2025-10-09 | 1 skill + 1 guide + 1 plugin |
| [Beyond permission prompts: making Claude Code more secure and autonomous](https://claude.com/blog/beyond-permission-prompts-making-claude-code-more-secure-and-autonomous) | 2025-10-08 | 1 skill |
| [How enterprises are driving AI transformation with Claude](https://claude.com/blog/driving-ai-transformation-with-claude) | 2025-10-01 | 1 skill |
| [Claude and Slack](https://claude.com/blog/claude-and-slack) | 2025-10-01 | 1 skill + 1 guide |
| [Managing context on the Claude Developer Platform](https://claude.com/blog/context-management) | 2025-09-29 | 1 skill |
| [Building agents with the Claude Agent SDK](https://claude.com/blog/building-agents-with-the-claude-agent-sdk) | 2025-09-29 | 1 skill |
| [Claude is now available in Microsoft 365 Copilot](https://claude.com/blog/claude-now-available-in-microsoft-365-copilot) | 2025-09-24 | 1 skill + 1 guide |
| [Claude can now create and edit files](https://claude.com/blog/create-files) | 2025-09-09 | 1 skill |
| [Piloting Claude in Chrome](https://claude.com/blog/claude-for-chrome) | 2025-08-25 | 1 skill + 1 guide |
| [Claude Code and new admin controls for business plans](https://claude.com/blog/claude-code-and-new-admin-controls-for-business-plans) | 2025-08-20 | 1 skill |
| [Claude Sonnet 4 now supports 1M tokens of context](https://claude.com/blog/1m-context) | 2025-08-12 | 1 skill |
| [Automate security reviews with Claude Code](https://claude.com/blog/automate-security-reviews-with-claude-code) | 2025-08-06 | 1 skill |
| [Build and share AI-powered apps with Claude](https://claude.com/blog/claude-powered-artifacts) | 2025-07-25 | 1 skill |
| [Discover tools that work with Claude](https://claude.com/blog/connectors-directory) | 2025-07-14 | 1 skill |
| [Turn ideas into interactive AI-powered apps](https://claude.com/blog/build-artifacts) | 2025-06-25 | 1 skill |
| [Remote MCP support in Claude Code](https://claude.com/blog/claude-code-remote-mcp) | 2025-06-18 | 1 skill + 1 guide |
| [Mcp Connector](https://claude.com/blog/agent-capabilities-api) | 2025-05-22 | 1 skill |
| [Claude on Google Cloud’s Vertex AI: FedRAMP High and IL2 Authorized](https://claude.com/blog/claude-on-google-cloud-fedramp-high) | 2025-04-02 | 1 skill |
| [Introducing the analysis tool in Claude.ai](https://claude.com/blog/analysis-tool) | 2024-10-24 | 1 skill |
| [Claude for Enterprise](https://claude.com/blog/claude-for-enterprise) | 2024-09-10 | 1 skill + 1 guide |
| [Claude Android app](https://claude.com/blog/android-app) | 2024-07-16 | 1 skill |
| [Evaluate prompts in the developer console](https://claude.com/blog/evaluate-prompts) | 2024-07-09 | 1 skill |
| [Long context prompting for Claude 2.1](https://claude.com/blog/claude-2-1-prompting) | 2023-12-06 | 1 skill |
| [Claude on Amazon Bedrock now available to every AWS customer](https://claude.com/blog/amazon-bedrock-general-availability) | 2023-09-28 | 1 skill |
| [Claude 2 on Amazon Bedrock](https://claude.com/blog/claude-2-amazon-bedrock) | 2023-08-23 | 1 skill |

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
9. **Artifacts are self-contained.** `SKILL.md`, `agents/*.md`, `hooks/*.md`, and `output-styles/*.md` must not reference anything outside their own folder — no `../` paths, no cross-artifact links, no links back to `description.*.md` or `guides/`. If outside material is needed, copy it into a local companion file (`references/`, `examples/`, `templates/`, `scripts/`, `prompts/`, `assets/`, or a sibling `.md`).

## Files

```
.
├── <YYYY.MM.DD>_<blog-slug>/           # One folder per blog post, date-prefixed
├── scripts/
│   ├── list_pending.py          # List pending URLs
│   ├── mark_processed.py        # Mark a URL processed
│   ├── update_last_run.py       # Stamp batch timestamp
│   ├── validate.py              # Pre-commit validator for all specs
│   └── strip_parent_refs.py     # Rewrite artifacts to drop ../ escapes
└── state/
    └── processed.json           # Processed URLs + last_run_at
```

## License

- Source posts (Claude blog) are © Anthropic. This repo contains summaries and quotations for study and reference only.
- Repository code: MIT License.
