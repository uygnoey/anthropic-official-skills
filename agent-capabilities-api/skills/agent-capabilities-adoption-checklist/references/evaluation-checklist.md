# Evaluation checklist (agent capability adoption)

Use this checklist to validate that the selected capabilities are working end-to-end in your agent.

## Capability checks
- **Code execution**: Can the agent run Python for the intended analyses and iterate on outputs when errors occur?
- **MCP connector**: Can the agent discover tools from the configured MCP server and call them with correct arguments?
- **Files API**: Can the agent reuse uploaded files across sessions as intended?
- **Extended prompt caching**: Are repeated long prompts measurably cheaper and faster, and is TTL behavior aligned with your workflow?

## Reliability checks
- Timeouts and retries are defined for external tool calls.
- Authentication failures are handled gracefully.
- The agent surfaces uncertainty and requests needed clarifications before taking irreversible actions.

## Source
- https://claude.com/blog/agent-capabilities-api
