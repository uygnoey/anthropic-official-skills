---
name: code-routines
description: Design and deploy routines in Claude Code — automations bundling a prompt, repo, and connectors that run on a schedule, via an API call, or in response to GitHub events. Covers trigger selection, prompt shape, and common patterns from the research preview announcement.
---

# Claude Code Routines

Routines are Claude Code automations configured once and then run on a schedule, from an API call, or in response to events. They run on Claude Code's web infrastructure — no local machine required. Based on *Introducing routines in Claude Code* (April 14, 2026, research preview).

## When to use

Use this skill when you want to package a recurring Claude Code task so it runs without manual invocation. Typical triggers:

- You currently copy-paste the same prompt into Claude Code on a schedule.
- You have an HTTP-capable system (alerting, CI/CD, internal tooling) that should start a Claude Code session with context.
- You want PR events in GitHub to launch Claude Code runs automatically.

## Instructions

Configure a routine by choosing **one** trigger type and writing a prompt that gives Claude Code enough context to act without you in the loop.

### 1. Pick a trigger

- **Scheduled** — for recurring background work (nightly backlog triage, weekly docs-drift scan). Cadences available: hourly, nightly, weekly. Existing `/schedule` CLI tasks already are scheduled routines.
- **API** — when an external system (alerting, CD pipeline, internal dashboard) should start a session. Each routine has its own endpoint and auth token. POST a message to the endpoint and you get back a session URL.
- **Webhook** — currently GitHub repository events. Claude opens one session per matching PR and keeps feeding that PR's updates (comments, CI failures) into the session so it can address follow-ups.

Only one trigger per routine. Pick the one that matches how the task naturally starts.

### 2. Write the prompt

Treat the prompt as standing instructions for Claude Code with no human nearby to clarify:

- State the action verb first ("pull the top bug from Linear, attempt a fix, and open a draft PR").
- Name the target repo, connector, or channel explicitly. Routines come with your repos and connectors attached; reference them by name.
- For API routines, describe what the incoming payload looks like and which field carries the signal (e.g. "Read the alert payload, find the owning service, and post a triage summary to #oncall with a proposed first step").
- For GitHub webhooks, specify a filter (file path, label, module) so the routine only wakes on relevant PRs ("flag PRs that touch the /auth-provider module").
- Keep the scope of one routine run bounded — a routine is not a long-lived agent, it is a scoped job that runs and ends.

See [`examples/prompts.md`](./examples/prompts.md) for the exact scheduled, API, and GitHub webhook prompts published in the announcement.

### 3. Respect usage caps

Routines draw down subscription usage limits just like interactive sessions, plus daily caps: Pro ≤ 5, Max ≤ 15, Team / Enterprise ≤ 25 per day. Beyond the cap you need extra usage. Design routines to do useful work per run rather than firing frequently for small deltas.

### 4. Pick a pattern that already works

The post lists patterns early users are already running. See [`references/patterns.md`](./references/patterns.md) for the full list grouped by trigger. High-leverage starting points:

- **Scheduled**: backlog management, docs drift.
- **API**: deploy verification, alert triage, feedback resolution.
- **GitHub**: library ports across SDKs, bespoke code review.

### 5. Where to create them

Head to claude.ai/code to create a routine, or type `/schedule` in the CLI. Available on Pro, Max, Team, and Enterprise plans with Claude Code on the web enabled.

## Examples

### Example 1 — Nightly bug-fix routine (scheduled)

Prompt:

> Every night at 2am: pull the top bug from Linear, attempt a fix, and open a draft PR.

Trigger: scheduled (nightly). Connectors: Linear + the relevant repo. Output: a draft PR you review in the morning.

### Example 2 — Alert triage (API)

Prompt:

> Read the alert payload, find the owning service, and post a triage summary to #oncall with a proposed first step.

Trigger: API. Wire Datadog (or any alerting tool) at the routine's endpoint. The routine runs once per alert and posts its triage into Slack.

### Example 3 — Auth-provider change watcher (GitHub webhook)

Prompt:

> Please flag PRs that touch the /auth-provider module. Any changes to this module need to be summarized and posted to #auth-changes.

Trigger: GitHub webhook with a path filter on `/auth-provider`. Claude opens one session per matching PR and keeps updating as comments and CI runs land on that PR.

### Example 4 — Docs-drift weekly scan (scheduled)

Based on the "docs drift" pattern in the post:

> Every Monday, scan merged PRs from the last week, flag docs that reference changed APIs, and open update PRs for each.

### Example 5 — Library port (GitHub webhook)

Based on the "library port" pattern in the post:

> On every PR merged to this Python SDK, port the change to our parallel Go SDK and open a matching PR.

## Source

- [Introducing routines in Claude Code](https://claude.com/blog/introducing-routines-in-claude-code)
