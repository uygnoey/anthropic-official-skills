**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude in Chrome is generally available

## What is this post?

A product announcement: Claude in Chrome is now generally available on all paid Claude plans,
bringing autonomous browser actions with safety verification. The post covers what browser control
is for — reaching tools that have no native integration — how safe actions are now approved
automatically, and the three layers deployed against prompt injection, with red-team evaluation
numbers.

## When is it useful?

- A workflow depends on an internal dashboard, legacy system, or vendor portal that no connector
  covers.
- You are deciding whether to let an agent act inside a browser session, and want to know what is
  approved automatically and what is not.
- You need to explain the prompt-injection risk and the mitigations to a security reviewer.
- You are an enterprise admin scoping which domains browser control may reach.

## Key points

- **Generally available on all paid plans.** Individuals install from the Chrome Web Store.
- **The use case is reach.** Internal dashboards, legacy systems, and vendor portals that have no
  native integration.
- **What it can do in the browser.** View pages and act on them — read text, click links, navigate,
  fill forms — work across tabs, and authenticate using existing logins, while the conversation
  continues in the desktop, mobile, and web apps.
- **Safe actions are approved automatically**, using the same mechanism as auto mode in Claude
  Code, with user override available.
- **The threat is injected instructions.** Malicious actors hide instructions in web content — a
  web page, an email, or a form field — to redirect AI agents.
- **Three protective layers.** Enhanced model training against a growing attack library (fed by
  internal automators, external red-teamers, and real-world monitoring); probe screening of web
  content before Claude acts; and action verification classifiers checking that actions match the
  user's request.
- **Evaluation results.** Against stronger red-teamed attacks, Claude Opus 5 showed a 3.8% attack
  success rate before safeguards. With probes and safety classifiers: 0% against Sonnet 5 and Opus
  5, and 0.3% against Fable 5.
- **Admin controls.** Enterprise admins manage it through Organization Settings, including domain
  restrictions.

## Bundled resources

- `skills/browser-control-safety/SKILL.md` — when to route a task through browser control, and how
  to work safely once you do.
- `skills/browser-control-safety/references/prompt-injection-defenses.md` — the attack, the three
  layers, and the evaluation table.
- `skills/browser-control-safety/references/rollout-and-admin-controls.md` — availability,
  capabilities, installation, and enterprise administration.
- `guides/browser-control-rollout.{en,ko,es,ja}.md` — the full rollout picture in four languages.

## Source

- https://claude.com/blog/claude-in-chrome-generally-available (published 2026-08-26)
