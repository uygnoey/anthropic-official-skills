**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post shares how Brex teams use Claude Code in day-to-day work, including engineering review workflows, content/design-system maintenance, and data access via text-to-SQL.

## When is it useful?
Use it if you are introducing Claude Code across an organization and want concrete adoption patterns such as structured context files, documentation checks in CI/CD, and custom context-aware commands.

## Key points
- Claude Code enables a “reviewer mindset”: engineers guide direction and review changes rather than focusing on implementation details.
- Non-technical roles can ship changes directly (e.g., making PRs for simple string updates) and build tooling like a Figma plugin to review designs against standards.
- Teams can democratize data access with a text-to-SQL interface powered by Claude Code plus MCP servers.
- Scaling patterns highlighted: directory-level CLAUDE.md context files, CI/CD checks that prompt documentation updates, and custom commands like /submit-pr that load relevant context.

## Bundled resources
- One Agent Skill that turns the post’s adoption patterns into a reusable “Claude Code org adoption playbook” (context management, documentation hygiene, custom commands).

## Source
- https://claude.com/blog/how-brex-improves-code-quality-and-productivity-with-claude-code
