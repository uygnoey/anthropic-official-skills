**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post introduces new API capabilities for building better AI agents: a code execution tool, an MCP connector, a Files API, and extended prompt caching.

## When is it useful?
Use these capabilities when you need agents that can analyze data with Python, connect to external systems via MCP servers, store and reuse files across sessions, or reduce latency and cost for long prompts through caching.

## Key points
- Code execution lets Claude run Python in a sandbox for analysis and iteration.
- The MCP connector lets Claude connect to remote MCP servers and use their tools without you writing client integration code.
- The Files API lets you upload documents once and reuse them across sessions.
- Extended prompt caching supports longer TTL options (including up to 60 minutes) to reduce cost and improve latency for repeated long prompts.

## Bundled resources
- Skill: A reusable checklist and implementation notes for adopting these agent-building capabilities.

## Source
- https://claude.com/blog/agent-capabilities-api
