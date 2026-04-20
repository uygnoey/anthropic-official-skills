---
name: slack-slack-integration
description: A reusable workflow for using Claude in Slack (and Slack as a connector) to draft replies, summarize threads, and pull relevant workspace context with permission-aware access.
---

# Claude and Slack

## Instructions
- Choose the mode you need:
  - Use Claude in Slack when you want help directly in channels, threads, or DMs.
  - Connect Slack to Claude when you want Claude to search your Slack messages and shared files for relevant context during a conversation.
- In Slack, use Claude in the appropriate place:
  - Direct messages: message @Claude for one-on-one help.
  - AI assistant panel: open Claude from Slack's AI assistant header when you want help without interrupting the channel.
  - Threads: mention @Claude to draft a response based on thread context; review/edit before posting.
- For the Slack connector, follow the org enablement flow:
  - Ensure your org/admin has enabled the connector.
  - Set up the connector in the Connectors tab in Claude settings.
- Apply common team workflows:
  - Meeting prep: review recent discussions and decisions.
  - Project coordination: gather status updates and identify blockers.
  - Onboarding: summarize channel history and shared context.
  - Documentation: turn thread outcomes into structured docs.
- Keep permissions and privacy in mind: Claude can only access channels and conversations you are allowed to view.

## Examples
- Ask @Claude in a project thread to propose a concise reply summarizing the current decision and next steps; edit before posting.
- Connect Slack to Claude, then ask for a briefing that cites key Slack updates relevant to a meeting agenda.

## Companion resources (optional)
- Guide: [../../guides/slack-slack-integration.en.md](../../guides/slack-slack-integration.en.md)

## Human-readable descriptions
Summarized in [../../description.en.md](../../description.en.md), [../../description.ko.md](../../description.ko.md), [../../description.es.md](../../description.es.md), [../../description.ja.md](../../description.ja.md).

## Source
Distilled from [Claude and Slack](https://claude.com/blog/claude-and-slack) (published 2025-10-01).
