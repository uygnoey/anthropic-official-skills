---
name: code-team-playbook
description: A practical playbook of Claude Code usage patterns across teams (navigation, testing, debugging, prototyping, docs, and automation), distilled from Anthropic’s internal examples.
---

# Claude Code Team Playbook

## Instructions
Use this skill to apply Claude Code effectively across common engineering and operations tasks.

### 1) Codebase navigation and understanding
- Ask Claude Code to read the repository (including any CLAUDE.md files).
- Request a map of relevant modules and dependencies for your task (bugfix, feature, analysis).

### 2) Testing and code review
- Ask for comprehensive tests for new features.
- If tests fail due to formatting or brittle cases, ask Claude to refactor the tests and rerun.

### 3) Debugging and troubleshooting
- Provide the observed behavior and ask for a fix proposal.
- When debugging incidents, provide stack traces plus relevant docs; ask Claude to trace control flow.

### 4) Prototyping and feature development
- For ambiguous problems, run an iterative loop: let Claude write code, run tests, and iterate; you review the result.
- For one-shot prototypes, describe the app and constraints and let Claude generate an initial end-to-end implementation.

### 5) Documentation and knowledge management
- Ask Claude to synthesize multiple sources into runbooks and troubleshooting guides.

### 6) Automation and workflow optimization
- For repetitive analysis (e.g., large CSVs), ask Claude to process data, identify underperformers, and generate constrained variations.
- If your workflow benefits from specialization, split tasks across multiple subagents with distinct responsibilities.

## Examples
- See: [Reusable prompt snippets](./templates/prompt-snippets.md)
- See: [Team patterns (examples catalog)](./examples/team-patterns.md)

## Source
- https://claude.com/blog/how-anthropic-teams-use-claude-code
