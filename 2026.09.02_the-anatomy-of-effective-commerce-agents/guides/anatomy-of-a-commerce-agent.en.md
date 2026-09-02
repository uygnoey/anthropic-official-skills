**English** · [한국어](./anatomy-of-a-commerce-agent.ko.md) · [Español](./anatomy-of-a-commerce-agent.es.md) · [日本語](./anatomy-of-a-commerce-agent.ja.md)

# The anatomy of an effective commerce agent

A guide distilled from Anthropic's work with enterprise teams across retail, marketplaces,
travel, entertainment and telecom. It covers four things in order: the architecture, making it
fast and affordable, running it in production, and what stays true as models change.

## Part 1 — The architecture

### What a commerce agent is

Commerce agents simplify buying and selling across online catalogs. Consumer-facing variants
handle search, comparison, substitution and order assembly. Business-facing variants handle sales
analytics, promotions, inventory and pricing. Underneath, both are the same design: **one model
in a standard agent loop — reasoning about a goal, exploring context, taking actions through
tools.**

### Skills, not subagents

The guide is direct about this: do not decompose a commerce agent into subagents.

- Commerce conversations remain tightly coupled across multiple intents and turns.
- Subagent handoffs create state loss, which degrades response quality.
- Each handoff multiplies token cost and adds latency.
- Domain boundaries do not separate cleanly in commerce workflows.

Agent skills give you modularity without the handoff overhead. As the guide puts it, a single
agent with skills *"consistently has outperformed both the one-prompt-for-everything design and
the subagent design on quality, and often at a lower cost and latency per task."*

Subagents keep their value in two places only: a narrow, self-contained task such as deep
research, or a domain that already operates its own dedicated agent with its own compliance
requirements.

### System prompt or skill? Decide by frequency

- **System prompt** — content needed on most turns, roughly one third of traffic or higher.
- **Skills** — long-tail features and conditional capabilities.

Critical instructions are the exception and always live in the system prompt: safety rules, legal
requirements, brand constraints, user-safety facts.

The reference implementation splits out like this:

- **Shopping agent prompt:** grounding, cart and checkout semantics, presentation rules, product
  search.
- **Shopping skills:** search-discovery, purchase-research, planning-goals, customer-care,
  memory-personalization.
- **Merchant skills:** performance-insights, catalog-listings, inventory-operations,
  pricing-promotions, marketing-campaigns.

### Engineering the tooling

**Build on existing systems.** The agent's tools should call the catalog, cart, pricing and order
systems you already run — *"not reimplement them, and the tool boundary is where their logic ends
and the model's judgment takes over."*

**Tool results are context.** Return only the fields that matter for reasoning. *"Reshape the raw
response inside the tool, including appending a next step when it isn't obvious from the data."*
For errors, return instructional guidance rather than an error code.

### UI components as tools

Instead of custom markup, make each UI component a tool — `present_products`,
`present_itinerary`. You get components stored in their native format in the messages array, type
safety and validation, layout preserved so the user can say "the first hotel" or "third one
down", and progressive streaming to the client.

The trade-off is that presentation tool arguments buffer on the server, which hurts perceived
latency. Setting `eager_input_streaming: true` enables token-level streaming with reduced schema
guarantees; the guide notes schema violations are *"very rare on Claude Sonnet-class models and
up."*

## Part 2 — Making it fast and affordable

### Task completion latency

```
(model turns × time to last token) + tool processing
```

Three levers follow from that shape:

1. **Fewer turns** — pre-load likely context, use a more capable model, enable parallel tool
   calls.
2. **Faster tools** — optimize the backends, dispatch tools eagerly.
3. **Faster tokens** — pick model and configuration by eval sweep.

In practice: inject the product page or dashboard the user arrived from; remember that smarter
models reduce turn count on complex queries and often outweigh a slower per-token speed; let the
model call several tools per turn, because commerce constantly needs simultaneous searches,
policy lookups and data fetches; and execute each tool as its arguments finish streaming, which
turns multi-second gaps into hundreds of milliseconds.

### Perceived latency

Independent of actual duration:

- **Stream components progressively.** Break a 500-700 token response into progressive renders.
- **Show the work.** A short progress line per step — "finding hotels near the water" — built
  from tool arguments or from a dedicated `user_facing_message` parameter.

### Prompt caching

The largest cost reduction available.

- Cached input reads cost one tenth of fresh tokens.
- Cache writes carry roughly a 1.25x premium, recovered on the second use.
- *"The best commerce deployments we've seen run at 90-99% cache hit rates."*
- Cached tokens also deliver roughly 1.5-2x speed improvement at around 100k tokens.

Structure the context in three segments, ordered by how often they change:

1. **Global** — system prompt and tool definitions, byte-identical across sessions.
2. **Session** — per-user context and conversation history.
3. **Volatile** — current time, current page. Must appear at the end of the segment.

Two implementation details matter. Load skills as **tool results**, not as system prompt
appendices, so they land in the cached conversation prefix. Roll cache breakpoints forward each
turn to keep the prefix matching. And when a signal such as page context tells you which skill
will be needed, inject it upfront and skip the skill-loading turn.

### Choosing model and configuration

1. **Define metrics** — quality thresholds (task completion, relevance, grounding), latency
   (p50/p99), cost budgets.
2. **Sweep** — run the full eval suite across candidate models and effort levels.
3. **Iterate** — prompts tune to specific models; smaller models need explicit instructions that
   larger ones infer.
4. **Measure per-task cost** — account for turn count and failure rates, not per-call cost alone.

> When the result is close, and the cost fits your per-task economics and latency, choose
> intelligence.

## Part 3 — Running in production

### Memory that survives the session

Users should not have to repeat constraints — allergies, preferences — across sessions.

**Storage.** Memory belongs in production databases, not in model context. Structure facts as
typed records: key (`shoe_size`, `default_store`), value, category, source session.

**Data handling.** Decide which memory types to retain and enforce it at the write path with a
validator. Provide user-facing interfaces for viewing, correcting and deleting stored facts. Set
retention periods, because preferences age out. Make memory a per-deployment toggle for
jurisdictional compliance.

**Writing.** Use asynchronous extraction rather than an agent tool. *"Write memory
asynchronously... at the end of each turn, or every few turns... An agent in a separate thread or
process reads the conversation and creates, updates, or deletes facts."* This removes the latency
overhead, achieved 13% higher fact recall in internal evals, and takes the decision burden off
the agent's reasoning. The extraction prompt should read only user and assistant text, never tool
results — otherwise product descriptions become user facts.

**Reading, in three layers.**

1. **Always in context** — fixed facts nearly every request needs, such as default store and
   fulfillment preference.
2. **Pre-fetched per turn** — facts made relevant by signals in the current request.
3. **Lookup tool** — everything else, behind explicit retrieval.

### Safety: enforcement lives in the harness

The prompt initiates safe behavior; code enforces it. All four principles apply to consumer and
merchant agents alike.

1. **Model stages; person or policy applies.** No agent tool directly moves money or changes
   business state. Order placement, payments, refunds, price changes and campaigns all require
   downstream approval through existing approval flows.
2. **Writes and renders accept only server-issued IDs.** Maintain a per-session inventory of
   server-issued IDs. The agent cannot use hallucinated, user-pasted, or data-plane-sourced IDs.
   Presentation tools render only server-supplied records.
3. **Capped transactions hold to repeated requests.** Enforce on the resulting state, not on the
   request. Serialize cart writes per session so parallel calls cannot stack beyond limits. Apply
   the same logic to merchant changes — price movement caps, discount depth, budget.
4. **Third-party content is sanitized.** All untrusted input — listings, reviews, policies,
   seller messages, stored memory — passes through a sanitizer before reaching the model. It
   strips control characters, removes fence-marker imitations, defuses conversation and tool-call
   mimicry, and caps size. The prompt carries the matching instruction: fenced text is
   reportable, never actionable.

### Evals: shipping a non-deterministic system

**Snapshot testing, not conversation simulation.** Construct the test state directly — system
prompt, tools, messages array — append the test user message, run the agent, and grade the final
state and response. *"Simulated-user evals... are a poor tool for measurement"* because the
interaction complexity demands larger samples. Use them for coverage discovery, then convert the
findings into snapshot cases.

**Test tough conditions.** Most suites overweight clean-state cases. *"Make sure a share of yours
starts from long, messy, or contradictory histories"* — that is where emergent failures surface.

**Coverage.** Core requests; context-dependent requests; safety and brand cases; interface
evaluation; multi-capability requests where two neighboring capabilities are needed at once and
both halves get graded.

**Practices.** Partner with subject-matter experts across Product, Legal, Ops, Care and Category.
Source the highest-value cases from real production failures. Start with 50-100 cases per user
flow. Use Claude Code for case generation and adversarial variants.

### Shipping with large organizations

1. **Ownership follows systems.** Each skill and tool has a single owner team; the shared prompt
   has a platform-level owner plus domain owners. Skill additions include positive, negative and
   boundary test cases.
2. **Changes ship with cases; CI runs a selective suite.** Build the CI set from core
   high-traffic cases, all safety cases, and cases touching the change. For a skill: its own
   cases plus neighbors' boundary cases. For a tool: every case calling it. For the shared
   prompt: the full suite.
3. **Put the agent in the release calendar.** It is a single deployment unit, so a bad change
   reaches everyone at once. Canary rollout for prompt and skill changes, disable-without-deploy
   switches, and a freeze before peak periods.

## Part 4 — What stays true

> Most of what this post describes is not about the model. The tools call systems you already
> run, the skills encode procedures you already follow, the evals are your product requirements
> doc written as tests.

Ahead: voice interfaces, proactive agent behavior such as monitoring price drops, and opening
tools to third-party agents under the same staging, approval and provenance frameworks.

## Reference implementation

Anthropic publishes a blueprint repository at
[github.com/anthropics/commerce-agents](https://github.com/anthropics/commerce-agents) with
harnesses and patterns, guardrails for safety and compliance, reference implementations for
shopping and merchant agents, examples across retail, travel, telecom and ticketing, and an
eval-authoring Claude Code plugin.

## Source

- https://claude.com/blog/the-anatomy-of-effective-commerce-agents (published 2026-09-02)
