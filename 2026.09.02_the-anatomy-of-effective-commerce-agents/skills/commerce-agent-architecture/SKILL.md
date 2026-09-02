---
name: commerce-agent-architecture
description: Architect a production commerce agent as a single model in a standard agent loop, with agent skills for modularity instead of subagents. Covers the frequency rule for deciding what belongs in the system prompt versus a skill, how to design tools that call existing commerce systems, how to reshape tool results so they read as context, and how to expose UI components as tools. Use when designing a shopping or merchant agent, when tempted to split a commerce agent into subagents, or when deciding where a capability should live.
---

# Commerce agent architecture

A commerce agent makes buying and selling across an online catalog simpler. Consumer-facing
agents handle search, comparison, substitution and order assembly; business-facing agents handle
sales analytics, promotions, inventory and pricing. Both are the same shape: **one model in a
standard agent loop — reasoning about a goal, exploring context, taking actions through tools.**

## Instructions

### 1. Start with one agent, not a fleet

Resist the subagent design. Commerce conversations stay tightly coupled across multiple intents
and turns, so every handoff loses state and degrades the answer, multiplies token cost, and adds
latency. Domain boundaries in commerce do not separate cleanly.

Use **agent skills** to get modularity without handoff overhead. In practice a single agent with
skills has consistently outperformed both the one-prompt-for-everything design and the subagent
design on quality, and often at lower cost and latency per task.

Keep subagents for the two cases where they still earn their place: a narrow, self-contained task
such as deep research, or a domain that already runs its own dedicated agent with its own
compliance requirements. Details and the full trade-off are in
[references/skills-vs-subagents.md](references/skills-vs-subagents.md).

### 2. Place content by frequency, not by topic

Decide between the system prompt and a skill by how often the content is needed:

- **System prompt** — content needed on most turns. A working threshold is roughly one third of
  traffic or higher.
- **Skill** — long-tail features and conditional capabilities.

Critical instructions are the exception and always live in the system prompt regardless of
frequency: safety rules, legal requirements, brand constraints, and facts that matter for user
safety.

For a worked split across a shopping agent and a merchant agent, see
[references/capability-map.md](references/capability-map.md).

### 3. Build tools on top of the systems you already run

You already have a catalog, a cart service, a pricing engine, an order system. The agent's tools
should **call** those systems, not reimplement them. The tool boundary is where their logic ends
and the model's judgment takes over.

### 4. Treat tool results as context, not as API responses

Return only the fields the model needs to reason with. Reshape the raw response inside the tool,
including appending a next step when it is not obvious from the data. For failures, return
instructional guidance the model can act on rather than an error code it has to guess about.

### 5. Make each UI component a tool

Instead of inventing custom markup for the model to emit, give it one tool per component —
`present_products`, `present_itinerary`, and so on. This buys you:

- Components stored in their native format in the messages array, so conversation history keeps
  them.
- Type safety and validation on the arguments.
- Layout preserved for later reference — the user can say "the first hotel" or "third one down"
  and the model knows what they mean.
- Progressive streaming of the component to the client.

The trade-off is that presentation tool arguments buffer on the server, which hurts perceived
latency. Setting `eager_input_streaming: true` gives token-level streaming with reduced schema
guarantees; schema violations are very rare on Claude Sonnet-class models and up. See
[references/ui-components-as-tools.md](references/ui-components-as-tools.md).

## Examples

### Deciding where a capability goes

> "Where do I put return-policy handling for my shopping agent?"

Ask how much traffic touches it. Returns and refunds are a small share of shopping conversations,
so it belongs in a `customer-care` skill, not in the system prompt. Cart and checkout semantics,
by contrast, are needed on most turns of a shopping session and belong in the system prompt.

> "Where do I put the brand rule that we never claim a price we did not retrieve?"

System prompt, regardless of frequency — it is a grounding and brand constraint.

### Rejecting a subagent split

> "We want a pricing subagent and an inventory subagent for the merchant side."

A merchant asking "why did margin drop on this SKU last week?" needs pricing history *and*
inventory movement in the same reasoning step. Splitting them forces a handoff mid-question,
loses the conversational state, and pays double the tokens. Make them two skills —
`pricing-promotions` and `inventory-operations` — on one merchant agent instead.

### Reshaping a tool result

A raw catalog search response with 40 fields per item becomes, inside the tool, a list of items
with id, title, price, availability, and the two attributes the query filtered on — plus, when
the search returns nothing in stock, a line telling the model that substitutions are available
through `search_similar`.

## Source

- https://claude.com/blog/the-anatomy-of-effective-commerce-agents (published 2026-09-02)
