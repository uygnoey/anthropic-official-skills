**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Building agents that reach production systems with MCP

## What is this post?
This post explains how Claude-based agents can connect to real production systems and workflows, and what integration approach to choose based on your constraints.

## When is it useful?
Use this when you want an agent to safely and reliably reach internal or third-party systems (e.g., issue trackers, data warehouses, infra), especially in cloud/production settings.

## Key points
- Compare three integration approaches: direct API calls, CLI-based automation, and MCP-based tool servers.
- For production usage, remote MCP servers can make an integration reusable across many clients and environments.
- Design tools around user intent (not 1:1 API endpoint mirrors) and keep tool surfaces compact.
- Improve context efficiency by loading tool definitions on demand and handling large tool outputs in code.
- Use standardized auth (e.g., OAuth) and token storage patterns when operating in production.

## Bundled resources
- Agent Skill: `skills/mcp-production-integration-patterns/SKILL.md`

## Source
- https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp
