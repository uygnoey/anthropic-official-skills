---
name: agent-capabilities-adoption-checklist
description: Checklist and implementation notes for adopting Claude API capabilities for agentic applications (code execution, MCP connector, Files API, and extended prompt caching).
---

## Instructions
Use this skill when translating the announcement of new agent-building capabilities into concrete engineering decisions.

1. **Identify which capabilities you need**
   - **Code execution**: You need Python-based analysis, report generation, or iterative data work.
   - **MCP connector**: You want Claude to use third-party tools exposed via remote MCP servers.
   - **Files API**: You need to upload files once and reuse them across sessions.
   - **Extended prompt caching**: You repeat long prompts and want lower cost and latency with longer TTL.

2. **Plan your integration approach**
   - Decide how your agent will call these capabilities (single workflow vs. multiple specialized flows).
   - Define failure handling for external tool calls (timeouts, auth, retries).

3. **Operationalize**
   - Track cost and latency impacts (especially with caching).
   - Establish evaluation criteria for agent reliability.

See [the evaluation checklist](./references/evaluation-checklist.md) for suggested acceptance checks.

## Examples
- Use the MCP connector when your agent must coordinate tasks across SaaS tools exposed through an MCP server.
- Use the Files API when you want a user to upload a document once and reference it across multiple sessions.
- Use extended prompt caching when the agent repeatedly uses the same long system instructions or large context blocks.

## Source
- https://claude.com/blog/agent-capabilities-api
