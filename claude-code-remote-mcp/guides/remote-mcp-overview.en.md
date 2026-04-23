**English** · [한국어](./remote-mcp-overview.ko.md) · [Español](./remote-mcp-overview.es.md) · [日本語](./remote-mcp-overview.ja.md)

## What is remote MCP in Claude Code?
Remote MCP support lets Claude Code connect to vendor-hosted MCP servers so you can use third-party tools and resources directly in your coding workflow.

## Why it matters
- Lower maintenance than local servers (vendors handle updates, scaling, availability).
- Secure connections via native OAuth.
- Lets Claude Code pull structured context from external systems (e.g., issue trackers, error monitoring).

## Typical flow
1. Choose a vendor MCP server.
2. Add the vendor URL in Claude Code.
3. Authenticate once (OAuth).
4. Use the exposed tools/resources in your workflow.

## Source
- https://claude.com/blog/claude-code-remote-mcp
