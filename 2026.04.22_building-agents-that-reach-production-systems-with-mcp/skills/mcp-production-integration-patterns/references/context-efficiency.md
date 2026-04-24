# Client-side context efficiency patterns

## Load tool definitions on demand
Prefer tool search / dynamic loading so you do not inject every tool definition into every prompt.

## Process tool results in code
When tool outputs are large (lists, logs, datasets), process them programmatically in the sandbox and return a compact summary to the model.

## Source
- https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp
