---
name: slack-to-code-session-routing
description: Guidance for delegating coding tasks from Slack to Claude Code sessions, including setup, when it works best, and what to expect in the workflow.
---

# Claude Code and Slack → Delegating coding tasks from Slack

## Instructions
1. In Slack, mention @Claude in a channel or thread that contains the relevant engineering discussion.
2. Make the request explicit as a coding task (bug investigation, small feature, refactor, quick review).
3. Ensure Claude has access to the target repository in Claude Code on the web.
4. Expect status updates posted back into the original Slack thread, plus a link to the Claude Code session and a link to open a pull request when done.

## Notes
- This feature uses recent Slack channel/thread messages as context for the coding session.
- Repository selection is based on what you have authenticated to Claude Code on the web.

## Examples
- “@Claude investigate this error and propose a fix.”
- “@Claude implement the change discussed above and open a PR.”

## Source
- https://claude.com/blog/claude-code-and-slack
