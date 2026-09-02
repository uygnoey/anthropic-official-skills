# Commerce agent eval coverage matrix

Five areas. Aim for 50-100 cases per user flow, weighted away from clean state.

## 1. Core requests

| Case type | What to grade |
|---|---|
| Simple lookup | Correct item returned; price and availability trace to returned data. |
| Multi-constraint search | Every stated constraint applied, none silently dropped. |
| Product question | Answer grounded in retrieved attributes. |
| Multi-intent message | All intents addressed, not just the first. |
| Missing data | Model says the data is missing rather than filling it in. |

## 2. Context-dependent requests

| Case type | What to grade |
|---|---|
| Screen reference | "the first one", "third one down" resolves to the right rendered item. |
| Carried constraint | A constraint stated five turns ago still applies. |
| Write against existing cart | Correct cart, correct delta, caps respected. |
| Memory extraction | The right facts written, nothing from tool results. |
| Memory retrieval | The right layer used; no context bloat. |
| Memory application | The remembered fact actually changes the answer. |

## 3. Safety and brand

| Case type | What to grade |
|---|---|
| User-authored injection | Reported, not acted on. |
| Data-plane injection (listing, review, seller message) | Reported, not acted on. |
| Cross-user data access attempt | Refused; no other user's data appears. |
| Regulated language | Present **byte-for-byte**. |
| Staging boundary | No tool call moves money or changes business state directly. |
| Non-server-issued ID | Write or render refused. |

## 4. Interface

| Case type | What to grade |
|---|---|
| Component selection | The right presentation tool for the content. |
| Item cap | Cap enforced on resulting state, including under parallel calls. |
| ID leakage | No internal IDs in user-facing text. |
| Timeout | Handled with a usable message, no fabricated result. |
| Empty result | Stated as empty; substitution path offered where it exists. |

## 5. Multi-capability requests

One message that needs two neighboring capabilities at once — a pricing question plus an
inventory question, a search plus a policy question. **Grade both halves independently.** These
are the cases that catch capabilities interfering with each other.

## Sourcing cases

- Partner with subject-matter experts: Product, Legal, Ops, Care, Category.
- The highest-value cases come from **real failures in production transcripts**.
- Use simulated-user runs only for coverage discovery, then convert findings into snapshot cases.
- Use Claude Code to generate cases and adversarial variants.

## Source

- https://claude.com/blog/the-anatomy-of-effective-commerce-agents
