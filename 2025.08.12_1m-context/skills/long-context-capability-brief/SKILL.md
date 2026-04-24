---
name: long-context-capability-brief
description: Summarize what a 1M-token context window enables and help decide when to use long context (codebases, document synthesis, long-running agent workflows), based on the Claude Sonnet 4 announcement.
---

# Long context capability brief

## Instructions
You are assisting a developer or team deciding how to use very long context windows (up to 1M tokens) for Claude Sonnet 4.

Do the following:
1) Identify the workload type
- Large-scale code analysis (entire codebases)
- Document synthesis (large sets of contracts/papers/specs)
- Context-aware agents (multi-step workflows across many tool calls)

2) Recommend what to include in the prompt
- For codebases: source, tests, and key docs needed to understand architecture.
- For document sets: the full set (or curated subsets) plus a clear synthesis question.
- For agents: relevant tool definitions, key policies/specs, and interaction history.

3) Call out operational considerations
- Note that pricing changes apply for prompts over 200K tokens.
- Suggest prompt caching and batch processing when appropriate to reduce latency/cost.

## Examples
### Example 1: Codebase analysis request
Create a one-page plan describing:
- What files you would include (source/tests/docs)
- What questions you would ask to understand architecture and cross-file dependencies

### Example 2: Document synthesis request
Draft a synthesis prompt that:
- States the synthesis goal
- Specifies how to cite evidence from documents
- Requests a coherent output structure

## Source
Derived from: https://claude.com/blog/1m-context
