---
name: skills-and-mcp-architecture-playbook
description: Guidance for designing workflows where MCP servers provide tool access and skills encode procedural expertise, sequencing, and output standards.
---

## Instructions

Use this skill when designing an agent workflow that uses both skills and MCP servers.

Principles:
- MCP servers provide *connectivity*: secure, standardized access to external systems and tools.
- Skills provide *expertise*: procedural knowledge, sequencing, and output standards for a specific workflow.

Decision rules:
1. Put a requirement in a **skill** if it describes *how to do the work*:
   - multi-step workflow sequencing
   - team standards for what "done" looks like
   - domain methodology and edge-case handling
   - institutional knowledge about which sources matter
2. Use **MCP** when you need Claude to *access or act on* external systems:
   - real-time data retrieval
   - creating/updating artifacts in tools (issues, docs, tickets)
   - file operations
   - API integrations
3. When combining both, avoid conflicting instructions between MCP-provided guidance and the skill's requirements (e.g., JSON vs Markdown formatting).

Constraints:
- Do not assume tool availability beyond the connected MCP servers.
- If the workflow depends on a specific output format, document it in the skill.

## Examples

### Example: Meeting preparation

- Skill responsibilities: define which pages to pull (project page → previous notes → stakeholder profiles), and define the structure of an internal pre-read and an external agenda.
- MCP responsibilities: search/read/create pages in Notion, then save the generated documents back to Notion.

### Example: Financial analysis

- Skill responsibilities: define valuation methodology, sequencing, and compliance checks.
- MCP responsibilities: pull live market data from connected data providers.
