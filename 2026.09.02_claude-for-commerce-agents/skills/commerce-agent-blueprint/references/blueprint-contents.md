# What the blueprint contains

Repository: [github.com/anthropics/commerce-agents](https://github.com/anthropics/commerce-agents)

Two reference implementations, with examples across **retail, travel, telecom and ticketing**.

## The shopping agent

Integrates within an application or website. Integration points:

| Integration point | Purpose |
|---|---|
| Catalog search | What exists, at what price, in what stock. |
| Cart management | What the shopper has assembled. |
| Checkout | The handoff that completes the purchase. |
| Customer preferences | What the shopper has told you before. |
| Order history | What they already bought. |

Capabilities:

- Search catalogs and assemble multi-item requests.
- Remember customer preferences and personalize suggestions.
- Display products and comparisons conversationally.
- Build carts for checkout handoff.
- Answer customer service questions — order tracking, returns, refund policies.

Guardrails that ship with it:

- Prices and products constrained to catalog data.
- No manipulative upsell patterns.

## The merchant agent

Capabilities:

- Answer sales performance questions.
- Track inventory and flag problems.
- Recommend pricing and promotions.
- Draft marketing campaigns.

Key principle:

> Agents suggest changes; humans approve before deployment.

## Reported outcomes

Retailers running shopping agents on Claude have seen carts up to **35% larger** and shoppers
**60% more likely** to complete a purchase.

## Time to first agent

- **Wix** — engineers had working commerce agents within fifteen minutes.
- **Fetch** — both commerce agents ran locally in under an hour, with live conversations working
  on the first attempt.
- **Zomato** — "Setup worked exactly as documented... Teams standing up their first agent on
  Claude will skip weeks of trial and error."

## Source

- https://claude.com/blog/claude-for-commerce-agents
