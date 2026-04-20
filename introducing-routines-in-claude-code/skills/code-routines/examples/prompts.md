# Routine Prompt Examples

Exact prompts quoted in *Introducing routines in Claude Code* (April 14, 2026), grouped by trigger type.

## Scheduled routine

> Every night at 2am: pull the top bug from Linear, attempt a fix, and open a draft PR.

Runs on a cadence (hourly / nightly / weekly). Existing `/schedule` CLI tasks are already scheduled routines.

## API routine

> Read the alert payload, find the owning service, and post a triage summary to #oncall with a proposed first step.

Each API routine has its own endpoint and auth token. POST a message, get back a session URL. Wire it into alerting, deploy hooks, or internal tools.

## GitHub webhook routine

> Please flag PRs that touch the /auth-provider module. Any changes to this module need to be summarized and posted to #auth-changes.

Claude opens one session per matching PR and continues feeding updates from that PR (comments, CI failures) into the session so it can address follow-ups.

## Source

- [Introducing routines in Claude Code](https://claude.com/blog/introducing-routines-in-claude-code)
