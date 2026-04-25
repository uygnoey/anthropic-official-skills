**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# How Anthropic teams use Claude Code

## What is this post?
This post shares concrete examples of how teams across Anthropic use Claude Code for codebase navigation, testing, debugging, prototyping, documentation, and automation.

## When is it useful?
- When onboarding into an unfamiliar codebase and you need fast dependency understanding.
- When you want to accelerate debugging, incident response, test writing, and rapid prototyping.
- When you have repetitive workflows (e.g., analyzing large CSVs, generating many ad variants) that benefit from automation or specialized subagents.

## Key points
- Teams use Claude Code to read repositories (including CLAUDE.md), locate relevant files, and explain dependencies and data pipelines.
- Claude Code is used to generate and refactor comprehensive test suites, sometimes integrated into automated PR feedback loops.
- During incidents, teams provide stack traces and documentation so Claude can trace control flow and propose mitigations.
- Teams use iterative autonomous loops (write code → run tests → iterate) for feature development and to explore edge cases.
- Claude Code can synthesize multiple documentation sources into markdown runbooks.
- Some workflows use multiple specialized subagents to generate large volumes of constrained outputs (e.g., ad variations).
- The post also mentions a Figma plugin used to generate ad variations from design frames.

## Bundled resources
- Skill: **code-team-playbook** (patterns distilled from the post).

## Source
- https://claude.com/blog/how-anthropic-teams-use-claude-code
