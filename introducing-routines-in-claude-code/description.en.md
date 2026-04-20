**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Introducing routines in Claude Code

## What is this post?

Announcement of **routines** in Claude Code, in research preview as of April 14, 2026. A routine is a Claude Code automation configured once — prompt, repo, and connectors — and then run on a schedule, from an API call, or in response to an event. Routines run on Claude Code's web infrastructure, so nothing depends on your laptop being open.

## When useful

- You already use Claude Code for dev-cycle automations but manage cron jobs, infrastructure, and extra MCP tooling yourself.
- You want Claude Code attached to your alerting, deploy hooks, or internal tools via HTTP endpoints.
- You want GitHub PR events to automatically trigger a Claude Code session with your routine.
- You need scheduled tasks like nightly backlog triage or weekly docs-drift scans.
- You operate CI/CD and want deploy verification, alert triage, or feedback-to-PR workflows in Claude Code.

## Key points

- **Three trigger types** ship in research preview: scheduled (hourly / nightly / weekly), API (HTTP endpoint with auth token per routine), and webhook (starting with GitHub repo events).
- Scheduled routines replace the `/schedule` CLI flow — existing `/schedule` tasks become routines.
- Each API routine gets its own endpoint and auth token: POST a message, receive a session URL.
- GitHub webhook routines open one Claude session per matching PR and keep feeding that PR's updates (comments, CI failures) into the session.
- Common early patterns: backlog triage, docs-drift scans, deploy verification, alert triage, feedback resolution, library ports across SDKs, bespoke code review.
- Availability: Pro, Max, Team, and Enterprise plans with Claude Code on the web enabled. Create at claude.ai/code or via `/schedule` in the CLI.
- Daily caps: Pro ≤ 5, Max ≤ 15, Team / Enterprise ≤ 25 routines per day. Extra usage allowed beyond these caps. Routines draw from subscription limits like interactive sessions.

## Bundled resources

- `skills/code-routines/SKILL.md` — how to choose a trigger type and write a useful routine prompt.
- `skills/code-routines/examples/prompts.md` — the scheduled, API, and GitHub webhook prompt examples quoted in the post.
- `skills/code-routines/references/patterns.md` — the full list of early-user patterns from the post.
- `guides/routines-overview.{en,ko,es,ja}.md` — four-language narrative guide.

## Source

- [Introducing routines in Claude Code](https://claude.com/blog/introducing-routines-in-claude-code) — published April 14, 2026.
