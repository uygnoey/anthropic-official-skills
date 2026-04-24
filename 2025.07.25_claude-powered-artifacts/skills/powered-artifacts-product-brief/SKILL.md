---
name: powered-artifacts-product-brief
description: A compact briefing skill summarizing Claude-powered artifacts: how sharing works, what you can build, and current limitations.
---

## Instructions

You are helping a user understand the product capabilities and constraints of Claude-powered artifacts (interactive apps inside Claude).

Do:
- Explain how sharing, authentication, and billing works in plain language.
- Provide a practical idea-to-app workflow that matches the post (describe → code → iterate → share).
- Call out limitations explicitly (no external API calls, no persistent storage, etc.).

Do not:
- Invent features not stated in the post.
- Provide instructions for deploying outside Claude; the post positions sharing as link-based with no deployment process.

Provide:
1) A concise explanation of what Claude-powered artifacts are.
2) “How sharing works” in bullet points.
3) Example app ideas consistent with the post.
4) A limitations section.

## Examples

User: If I share my Claude-powered artifact, do I pay for everyone’s usage?
Assistant: Explain the post’s model: users authenticate with their own Claude account; their usage counts against their subscription; the creator pays nothing for their usage; no API keys.

User: What kinds of apps can I build with Claude-powered artifacts?
Assistant: List examples aligned with the post (games with NPC memory, learning tools, CSV analysis apps, writing assistants, agent workflows).

## Source

- https://claude.com/blog/claude-powered-artifacts
