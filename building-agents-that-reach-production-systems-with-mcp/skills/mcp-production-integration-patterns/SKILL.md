---
name: mcp-production-integration-patterns
description: Patterns for connecting agents to production systems, including when to use direct APIs vs CLIs vs MCP, and how to design MCP servers and clients for scale, security, and context efficiency.
---

# Building agents that reach production systems with MCP → Production integration patterns (API / CLI / MCP)

## Scope
This skill helps you choose and implement an integration approach so an agent can reach real production systems reliably.

## Instructions
1. Identify what the agent must do (user intent) and what systems it must access.
2. Choose an integration approach:
   - Direct API calls for small, single-service integrations.
   - CLI automation when a robust CLI exists and shell access is acceptable.
   - MCP server when you need reuse across clients/environments and want a dedicated integration layer.
3. If using MCP, design the server:
   - Group tools around intent (avoid endpoint mirrors).
   - Keep tool surface compact.
   - For very large surfaces, expose a small “search + execute” interface and orchestrate details in code.
   - Add richer semantics only where they improve UX (e.g., interactive UI or structured elicitation).
   - Use standardized auth and central token storage for production.
4. Optimize client context usage:
   - Load tool definitions only when needed.
   - Process large tool outputs in code and return summaries.

## Bundled resources
- `references/integration-approaches.md`
- `references/mcp-server-design-patterns.md`
- `references/context-efficiency.md`

## Examples
### Example: picking an approach
User goal: “Create a ticket from this Slack thread and link it to the incident.”
- If you will support this across Slack, email, web, and IDE: build an MCP server with a single high-level tool such as `create_incident_ticket_from_thread`.
- If it is only for one internal bot and a few endpoints: direct API calls may be enough.

### Example: designing intent-based tools
Bad: `jira_create_issue`, `jira_update_issue`, `jira_add_comment`, … (hundreds of endpoint-like tools)
Good: `create_issue_from_thread`, `triage_issue`, `summarize_issue_status`

## Source
- https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp
