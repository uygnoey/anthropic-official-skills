**English** · [한국어](./browser-control-rollout.ko.md) · [Español](./browser-control-rollout.es.md) · [日本語](./browser-control-rollout.ja.md)

# Rolling out browser control in Chrome

## What shipped

Claude in Chrome is now generally available on all paid Claude plans, with autonomous browser
actions backed by safety verification.

## What it is for

The point of browser control is reach: tools that have no native integration. Internal dashboards
nobody has built a connector for, legacy systems, vendor portals. Within the browser, Claude can:

- view web pages and act on them — read text, click links, navigate, fill forms;
- work across browser tabs while the conversation continues in the desktop, mobile, and web apps;
- authenticate using the logins already in the browser.

If a native integration already exists for a system, use it instead. Browser control is the answer
for what integrations don't cover.

## Autonomous actions

Claude now automatically approves safe actions, using the same mechanism as auto mode in Claude
Code. Users can override that behavior.

The planning question changes accordingly: not "will every step stop and ask?" but "which steps in
this task should a person still see first?" Sending, submitting, purchasing, publishing, and
account-setting changes belong in that set regardless of what is approved automatically.

## Prompt injection, and the three defenses

Malicious actors hide instructions in web content — a web page, an email, or a form field — to
redirect AI agents. Three protective layers are deployed against this:

1. **Enhanced model training** against a growing library of attacks, sourced from internal
   automators, external red-teamers, and real-world monitoring.
2. **Probe screening** of web content *before* Claude acts, warning the model that a potential
   attack is present.
3. **Action verification classifiers** that check whether the action matches what the user
   requested.

### What the evaluations found

Testing with stronger red-teamed attacks:

| Condition | Attack success rate |
| --- | --- |
| Claude Opus 5, before safeguards | 3.8% |
| With probes and safety classifiers — Sonnet 5 | 0% |
| With probes and safety classifiers — Opus 5 | 0% |
| With probes and safety classifiers — Fable 5 | 0.3% |

These are rates, not guarantees. The working rule stays: what the browser shows is data, not
instructions.

## Getting started

- **Individuals:** install Claude in Chrome from the Chrome Web Store.
- **Enterprise admins:** manage it through Organization Settings, including domain restrictions.

Scoping the domain list is the main deployment control. Start from the systems the team actually
needs and widen from there.

## Source

- https://claude.com/blog/claude-in-chrome-generally-available (published 2026-08-26)
