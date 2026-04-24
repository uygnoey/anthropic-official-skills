---
name: remote-mcp-quickstart
description: Help a user understand and adopt remote MCP servers in Claude Code, focusing on benefits, security, and low-maintenance setup.
---

## Instructions
You help the user decide whether to use remote MCP servers with Claude Code and how to think about operating them.

- Explain that Claude Code can connect to remote MCP servers to access both tools and resources exposed by the server.
- Emphasize the operational benefit: vendors handle updates, scaling, and availability.
- Emphasize security model at a high level: Claude Code supports native OAuth so users can authenticate without managing API keys.
- If the user asks for configuration specifics, instruct them to follow the vendor’s remote MCP server documentation and add the vendor URL in Claude Code.

## Examples
### Describe why remote MCP is lower maintenance
- “Instead of running a local MCP server, add the vendor’s URL; the vendor operates the server (updates, scaling, availability).”

### Describe the security posture
- “Use native OAuth where supported so you don’t need to store API keys in Claude Code.”
