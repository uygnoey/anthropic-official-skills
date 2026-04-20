# Early-User Routine Patterns

Reproduced from the "What teams are building" section of *Introducing routines in Claude Code* (April 14, 2026).

## Scheduled routines

- **Backlog management**: triage new issues nightly, label, assign, and post a summary to Slack.
- **Docs drift**: scan merged PRs weekly, flag docs that reference changed APIs, and open update PRs.

## API routines

- **Deploy verification**: your CD pipeline posts after each deploy, Claude runs smoke checks against the new build, scans error logs for regressions, and posts a go/no-go to the release channel.
- **Alert triage**: point Datadog at the routine's endpoint, Claude pulls the trace, correlates it with recent deployments, and has a draft fix waiting before on-call opens the page.
- **Feedback resolution**: a docs feedback widget or internal dashboard posts the report, Claude opens a session against the repo with the issue in context, and drafts the change.

## GitHub routines

- **Library port**: every PR merged to a Python SDK triggers a routine that ports the change to the parallel Go SDK, and opens a matching PR.
- **Bespoke code review**: on PR opened, run your team's own checklist across security and performance, leaving inline comments before a human reviewer looks.

## Source

- [Introducing routines in Claude Code](https://claude.com/blog/introducing-routines-in-claude-code)
