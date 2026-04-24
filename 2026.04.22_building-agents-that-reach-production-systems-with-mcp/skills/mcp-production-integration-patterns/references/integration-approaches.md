# Integration approaches: direct API vs CLI vs MCP

This reference expands the comparison described in the blog post and provides a lightweight decision checklist.

## Direct API calls
- Best when you have a small number of endpoints and a tight, single-service integration.
- You manage auth, retries, pagination, and schema evolution yourself.

## CLI-based automation
- Best when your agent runs in an environment with a shell and filesystem (e.g., local dev or a controlled runner).
- Often easiest when a mature CLI already exists and encapsulates auth and workflows.

## MCP tool servers (remote)
- Best when you want a reusable integration layer that many clients (web, IDE, mobile, cloud agents) can use.
- Prefer remote servers for distribution and shared improvements.

## Checklist
- Do you need broad reuse across clients/environments? → MCP server.
- Do you only need a few operations for a single agent? → direct API calls.
- Do you already have a robust CLI workflow and local execution is acceptable? → CLI.

## Source
- https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp
