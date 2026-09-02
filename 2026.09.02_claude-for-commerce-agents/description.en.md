**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Building commerce agents with Claude

## What is this post?

A product announcement. Anthropic released an open blueprint for building commerce agents, with
reference implementations for a **shopping agent** and a **merchant agent**, plus examples across
retail, travel, telecom and ticketing. The headline number: retailers running shopping agents on
Claude have seen carts up to 35% larger and shoppers 60% more likely to complete a purchase.

The shopping agent embeds in an application or website and handles catalog search, multi-item
assembly, preferences, product comparison, cart building for checkout handoff, and customer
service questions. The merchant agent answers sales performance questions, tracks inventory,
recommends pricing and promotions, and drafts campaigns — always as suggestions a human approves
before deployment.

Shopify, Priceline, Wix, Zomato, Fetch and Square are named as builders on it, with Accenture,
Mastercard and Visa as partners.

## When is it useful?

- You are starting a commerce agent project and want a working reference rather than a blank
  repository.
- You need to scope which of your existing systems — catalog, cart, checkout, preferences, order
  history — the agent will need to call.
- You are deciding whether to build the shopper side or the seller side first.
- You need to know where the deployment can run: Claude API, Amazon Bedrock, Microsoft Foundry,
  or Google Cloud Vertex AI.

## Key points

- **Two reference agents, one blueprint.** Shopping (consumer-facing) and merchant
  (business-facing), at [github.com/anthropics/commerce-agents](https://github.com/anthropics/commerce-agents).
- **The shopping agent's integration points** are catalog search, cart management, checkout,
  customer preferences and order history. The agent calls systems you already run.
- **Shopping guardrails ship with it:** prices and products are constrained to catalog data, and
  manipulative upsell patterns are out.
- **The merchant principle:** agents suggest changes; humans approve before deployment.
- **Deploy anywhere Claude runs** — Claude API, Amazon Bedrock, Microsoft Foundry, Google Cloud
  Vertex AI.
- **Setup is reported as fast.** Wix engineers had working commerce agents within fifteen
  minutes; Fetch had both agents running locally in under an hour with live conversations working
  on the first attempt.
- **Trust is the stated constraint.** Both payment partners frame it the same way — Visa: *"AI
  will fundamentally reshape commerce, but trust must remain at the center of every
  transaction."*
- **The engineering detail is a separate post.** Architecture, latency, caching, memory, safety
  and evals live in the companion deep-dive, *A guide to the anatomy of effective commerce
  agents*.

## Bundled resources

- `agents/shopping-agent.md` — the consumer-facing agent: integration points, capabilities, and
  the catalog-grounding and no-manipulative-upsell guardrails.
- `agents/merchant-agent.md` — the business-facing agent: capabilities and the suggest-don't-apply
  operating principle.
- `skills/commerce-agent-blueprint/SKILL.md` — how to scope and stand up a deployment from the
  blueprint.
- `skills/commerce-agent-blueprint/references/blueprint-contents.md` — what ships in the
  repository, capability by capability.
- `skills/commerce-agent-blueprint/references/deployment-options.md` — where it runs, the partner
  ecosystem, and who is building on it.

## Source

- https://claude.com/blog/claude-for-commerce-agents (published 2026-09-02)
- Engineering deep-dive: https://claude.com/blog/the-anatomy-of-effective-commerce-agents
