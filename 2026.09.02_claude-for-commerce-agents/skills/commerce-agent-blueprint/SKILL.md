---
name: commerce-agent-blueprint
description: Stand up a commerce agent from Anthropic's open blueprint, which ships reference implementations of a shopping agent and a merchant agent with examples across retail, travel, telecom and ticketing. Covers what the blueprint contains, the integration points each agent needs, the guardrails that ship with it, and where the deployment can run - the Claude API, Amazon Bedrock, Microsoft Foundry, or Google Cloud Vertex AI. Use when starting a commerce agent project, or when scoping what a shopping or merchant agent will need from your existing systems.
---

# Commerce agent blueprint

Anthropic publishes a blueprint for building commerce agents at
[github.com/anthropics/commerce-agents](https://github.com/anthropics/commerce-agents), with
reference implementations for a **shopping agent** and a **merchant agent** across retail,
travel, telecom and ticketing.

Reported results from retailers running shopping agents on Claude: carts up to **35% larger**,
and shoppers **60% more likely** to complete a purchase.

## Instructions

### 1. Pick which agent you are building first

The blueprint ships two, and they have different owners inside most companies.

- **Shopping agent** — consumer-facing. Search, comparison, multi-item assembly, preferences,
  cart building, and customer service questions.
- **Merchant agent** — business-facing. Sales performance, inventory, pricing and promotions,
  campaign drafting.

Full capability lists are in [references/blueprint-contents.md](references/blueprint-contents.md).

### 2. Map the integration points against systems you already have

The shopping agent embeds in an application or website and needs integration points for:

- catalog search
- cart management
- checkout
- customer preferences
- order history

Scope the project by which of these already exist. The agent calls them; it does not replace
them.

### 3. Keep the guardrails that ship with it

Two guardrails come with the reference shopping agent and are worth treating as non-negotiable:

- **Prices and products are constrained to catalog data.** The agent does not state a price or an
  attribute it did not retrieve.
- **No manipulative upsell patterns.**

And one for the merchant side:

- **Agents suggest changes; humans approve before deployment.**

### 4. Choose where it runs

The same deployment can run on the Claude API, Amazon Bedrock, Microsoft Foundry, or Google Cloud
Vertex AI. See [references/deployment-options.md](references/deployment-options.md).

### 5. Fork, then read the engineering guide

1. Fork [github.com/anthropics/commerce-agents](https://github.com/anthropics/commerce-agents).
2. Read the engineering deep-dive at
   [claude.com/blog/the-anatomy-of-effective-commerce-agents](https://claude.com/blog/the-anatomy-of-effective-commerce-agents)
   for the architecture, latency, caching, memory, safety and eval practices behind the
   blueprint.
3. See vertical demos and request a working session at
   [claude.com/solutions/commerce](https://claude.com/solutions/commerce).

Teams report the setup is fast: engineers at Wix had working commerce agents within fifteen
minutes; at Fetch, both agents ran locally in under an hour with live conversations working on
the first attempt.

## Examples

### Scoping a retail deployment

A retailer has catalog search and an order system, but no stored customer preferences. The
shopping agent still works — search, comparison, cart building and order tracking are all
available. Personalization is the gap, and it is a separate piece of work (see the memory
guidance in the engineering deep-dive), not a blocker for a first deployment.

### Deciding which agent goes first

A marketplace wants both. The merchant agent has a smaller blast radius — it suggests and a human
approves, so a bad suggestion costs a review rather than a customer — which makes it the safer
first deployment while the shopping agent's guardrails and evals are built out.

### A guardrail question

> "Can the agent offer a discount to close a hesitant shopper?"

Not by inventing one. Prices are constrained to catalog data, and manufactured urgency is
explicitly out of scope. A promotion the merchant has actually created, retrieved from the
catalog, is fine.

## Source

- https://claude.com/blog/claude-for-commerce-agents (published 2026-09-02)
