---
name: agent-tool-design-playbook
description: Practical heuristics from the Claude Code team for designing, iterating, and pruning agent tools by thinking from the model’s perspective (“seeing like an agent”), with an emphasis on progressive disclosure.
---

## Instructions

Use this skill when you are designing or refining tools for an AI agent (e.g., a coding agent) and want to reduce confusion while increasing capability.

### 1) Start from the agent’s perspective (“see like an agent”)

- Assume the agent’s core loop is: read tool outputs → update its plan → choose the next tool call.
- Evaluate whether your tool outputs are legible and actionable for the model (not just for humans).

### 2) Keep a high bar for adding new tools

- Every new tool increases the set of options the agent must consider.
- Prefer improving an existing primitive or documentation before introducing a brand-new tool.

### 3) Match the tool interface to the model’s current capabilities

- Revisit earlier design assumptions as model capability changes.
- If a tool becomes a bottleneck because it is too restrictive, replace it with a more expressive primitive.

### 4) Use progressive disclosure to avoid “tool explosion”

- Prefer a small set of general primitives plus documentation that the agent can consult on demand.
- When a workflow requires lots of detail, move the detail into referenced files instead of the main skill text.

### 5) Use a dedicated question/clarification tool when reliability matters

If you need the agent to ask the user a question and safely pause until it is answered, a dedicated question tool can be more reliable than overloading a different tool’s interface.

## Examples

### Example: deciding whether to add a new tool

**Situation:** You want to add a narrowly scoped tool that performs one action.

**Apply the playbook:**
- First, see if an existing primitive plus better instructions (or progressive disclosure) can accomplish the same result.
- If the agent still repeatedly fails or wastes tokens due to missing affordances, consider introducing a new tool.

### Example: replacing a restrictive primitive

**Situation:** A “todo” list tool tracks steps, but you now need dependencies and cross-agent coordination.

**Apply the playbook:**
- Replace the todo primitive with a task abstraction that can represent dependencies and share updates across subagents.

## Source

- https://claude.com/blog/seeing-like-an-agent
