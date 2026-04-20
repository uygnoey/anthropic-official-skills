**English** · [한국어](./routines-overview.ko.md) · [Español](./routines-overview.es.md) · [日本語](./routines-overview.ja.md)

# Routines in Claude Code: An Overview

A narrative walkthrough of *Introducing routines in Claude Code* (April 14, 2026, research preview).

## What routines are

A routine is a Claude Code automation you configure once — including a prompt, repo, and connectors — and then run on a schedule, from an API call, or in response to an event. Routines execute on Claude Code's web infrastructure, so they do not depend on your laptop being open.

Developers already automate their software development cycle with Claude Code, but until now they managed cron jobs, infrastructure, and extra MCP tooling themselves. Routines ship with your repos and connectors attached, so you package the automation once and set it to run.

## The three trigger types

### Scheduled routines

Give Claude Code a prompt and a cadence — hourly, nightly, or weekly — and it runs on that schedule. Example from the announcement:

> Every night at 2am: pull the top bug from Linear, attempt a fix, and open a draft PR.

If you are using `/schedule` in the CLI, those tasks are now scheduled routines.

### API routines

Each routine gets its own endpoint and auth token. POST a message to the endpoint, receive a session URL. You can wire Claude Code into your alerting, your deploy hooks, your internal tools — anywhere you can make an HTTP request. Example prompt:

> Read the alert payload, find the owning service, and post a triage summary to #oncall with a proposed first step.

### Webhook routines (starting with GitHub)

Subscribe a routine to kick off in response to GitHub repository events. Claude creates a new session for every PR matching your filters and runs your routine. Example:

> Please flag PRs that touch the /auth-provider module. Any changes to this module need to be summarized and posted to #auth-changes.

Claude opens one session per PR and keeps feeding updates from that PR (comments, CI failures) into the session, so it can address follow-ups. The post notes plans to expand webhook-based routines to more event sources later.

## What teams are building

### Scheduled
- **Backlog management**: triage new issues nightly, label, assign, and post a summary to Slack.
- **Docs drift**: scan merged PRs weekly, flag docs that reference changed APIs, open update PRs.

### API
- **Deploy verification**: your CD pipeline posts after each deploy; Claude runs smoke checks, scans error logs for regressions, and posts a go/no-go to the release channel.
- **Alert triage**: point Datadog at the routine's endpoint; Claude pulls the trace, correlates it with recent deployments, and has a draft fix waiting before on-call opens the page.
- **Feedback resolution**: a docs feedback widget or internal dashboard posts the report; Claude opens a session against the repo with the issue in context and drafts the change.

### GitHub
- **Library port**: every PR merged to a Python SDK triggers a routine that ports the change to the parallel Go SDK and opens a matching PR.
- **Bespoke code review**: on PR opened, run your team's own checklist across security and performance, leaving inline comments before a human reviewer looks.

## Getting started

Routines are available to Claude Code users on Pro, Max, Team, and Enterprise plans with Claude Code on the web enabled. Head to claude.ai/code to create your first routine, or type `/schedule` in the CLI.

Routines draw down subscription usage limits like interactive sessions. Daily caps:

- Pro: up to 5 routines per day
- Max: up to 15 routines per day
- Team and Enterprise: up to 25 routines per day

You can run beyond these caps with extra usage. See the docs for more information.

## Source

- [Introducing routines in Claude Code](https://claude.com/blog/introducing-routines-in-claude-code) — April 14, 2026.
