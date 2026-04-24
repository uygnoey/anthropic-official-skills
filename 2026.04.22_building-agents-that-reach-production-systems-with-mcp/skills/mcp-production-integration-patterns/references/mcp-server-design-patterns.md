# MCP server design patterns

## Group tools around intent
Instead of mirroring every API endpoint, expose tools aligned to tasks users actually want done (e.g., “create issue from a thread”).

## Keep the surface compact
Fewer, higher-level tools tend to be easier for an agent to select correctly and cheaper in context.

## Large surfaces: orchestrate in code
When the underlying system has thousands of endpoints, consider exposing a small set of tools such as:
- `search`: discover the right operation
- `execute`: run it

This shifts complexity into code orchestration while keeping tool definitions small.

## Rich semantics where they help
If your host supports it, consider returning:
- interactive UI elements (“apps”) for charts/forms
- elicitation steps that pause for user input

## Auth patterns
Use standardized auth (e.g., OAuth) and central token storage (e.g., managed vaults) when running in production.

## Source
- https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp
