# Capability map: prompt vs. skills

The placement rule is frequency-based.

- **System prompt** — needed on most turns (roughly one third of traffic or higher).
- **Skill** — long-tail features and conditional capabilities.
- **Always system prompt regardless of frequency** — safety rules, legal requirements, brand
  constraints, and user-safety facts.

## Reference implementation distribution

### Shopping agent — system prompt

- Grounding
- Cart and checkout semantics
- Presentation rules
- Product search

### Shopping agent — skills

| Skill | Scope |
|---|---|
| `search-discovery` | Finding and narrowing candidates in the catalog. |
| `purchase-research` | Comparison and product questions before committing. |
| `planning-goals` | Multi-item and goal-shaped requests. |
| `customer-care` | Order tracking, returns, refund policy questions. |
| `memory-personalization` | Applying remembered customer facts and preferences. |

### Merchant agent — skills

| Skill | Scope |
|---|---|
| `performance-insights` | Sales performance questions. |
| `catalog-listings` | Listing content and catalog upkeep. |
| `inventory-operations` | Inventory tracking and problem flagging. |
| `pricing-promotions` | Price and promotion recommendations. |
| `marketing-campaigns` | Campaign drafting. |

## Loading note

Skills should be loaded as **tool results**, not appended to the system prompt — that keeps them
in the cached conversation prefix. Where a signal makes the skill predictable (for example, the
page the user arrived from), inject it upfront and skip the skill-loading turn entirely.

## Source

- https://claude.com/blog/the-anatomy-of-effective-commerce-agents
