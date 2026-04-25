**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Extending Claude's capabilities with skills and MCP servers

## What is this post?
This post explains how skills and Model Context Protocol (MCP) servers complement each other when building agents that follow your team's workflows.

## When is it useful?
Useful when you're deciding what to encode as reusable workflow knowledge (skills) versus what to connect as live tool access (MCP), especially for multi-step tool-driven workflows.

## Key points
- Treat MCP as the connectivity layer (secure access to external systems) and skills as the expertise layer (workflow logic and standards).
- Use skills for multi-step workflows, consistency requirements, domain expertise, and institutional knowledge.
- Use MCP when you need real-time data access, actions in external systems, file operations, or API integrations.
- When combining both, avoid conflicting instructions (e.g., MCP says return JSON while the skill says format Markdown tables).

## Bundled resources
- Skill: `skills-and-mcp-architecture-playbook` (Agent Skills)

## Source
- https://claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers
