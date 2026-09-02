**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# A guide to the anatomy of effective commerce agents

## What is this post?

A long engineering guide by Ali Shazal and Matthew Koen, distilled from Anthropic's work with
enterprise teams across retail, marketplaces, travel, entertainment and telecom. It walks through
building a production commerce agent in four parts: the architecture, making it fast and
affordable, running it in production, and what stays true as models change.

The central claim is architectural: a commerce agent should be **one model in a standard agent
loop**, with agent skills for modularity — not a fleet of subagents. Commerce conversations stay
tightly coupled across intents and turns, so every subagent handoff loses state, multiplies token
cost and adds latency. A single agent with skills has consistently outperformed both the
one-prompt-for-everything design and the subagent design on quality, often at lower cost and
latency per task.

## When is it useful?

- You are designing a shopping agent or a merchant agent and have to decide how to decompose it.
- Your agent works but is too slow, or costs too much per task, and you need to know which lever
  to pull first.
- You need long-term memory across sessions without paying latency for it on every turn.
- Your agent can touch carts, orders, prices, refunds or budgets, and you need enforcement that
  does not depend on the model behaving.
- You are building an eval suite for a non-deterministic system that several teams change at
  once.

## Key points

- **Skills, not subagents.** Handoffs lose state, multiply cost and add latency, and commerce
  domain boundaries do not separate cleanly. Keep subagents for narrow self-contained tasks like
  deep research, or a domain that already runs its own compliance-bound agent.
- **Placement is decided by frequency.** System prompt for content needed on most turns (roughly
  one third of traffic or higher); skills for the long tail. Safety, legal, brand and user-safety
  content goes in the system prompt regardless.
- **Tools call systems you already run.** The tool boundary is where their logic ends and the
  model's judgment takes over. Reshape the raw response inside the tool, and return instructional
  guidance on errors rather than error codes.
- **UI components are tools.** `present_products`, `present_itinerary` — native storage in the
  messages array, type safety, referenceable layout ("the third one down"), progressive
  streaming. Arguments buffer on the server; `eager_input_streaming: true` trades some schema
  guarantee for token-level streaming.
- **Latency = (turns × time to last token) + tool time.** Fewer turns, faster tools, faster
  tokens. Pre-load context, let intelligence buy back turns, enable parallel tool calls, dispatch
  eagerly.
- **Perceived latency is a separate problem.** Stream components progressively, and show short
  progress lines built from tool arguments or a `user_facing_message` parameter.
- **Prompt caching is the biggest cost lever.** Three segments by change frequency — global
  (byte-identical), session, volatile (at the end). Load skills as tool results, roll breakpoints
  forward. The best deployments run at 90-99% hit rates.
- **Choose the model by sweep.** Define quality, latency and cost metrics, run the full eval
  suite across models and effort levels, re-tune prompts per model, and measure per-task cost.
  When it is close, choose intelligence.
- **Write memory asynchronously, outside the agent.** A separate process reads the conversation
  and creates, updates or deletes typed facts — no latency cost, 13% higher fact recall in
  internal evals. The extractor reads only user and assistant text, never tool results.
- **Read memory in three layers.** Always in context, pre-fetched per turn, and behind a lookup
  tool.
- **Safety enforcement lives in the harness.** The model stages and a person or policy applies;
  writes and renders accept only server-issued IDs; caps are enforced on resulting state with
  serialized per-session writes; all third-party content is sanitized, and fenced text is
  reportable, never actionable.
- **Snapshot evals, not conversation simulation.** Construct state directly and grade final state
  and response. Simulated-user runs are for coverage discovery only. Start from long, messy,
  contradictory histories — that is where emergent failures live.
- **Ship with ownership and a selective CI suite.** Core high-traffic cases plus all safety cases
  plus the cases the change touches. The agent is a single deployment unit, so canary it and put
  it on the release calendar.

## Bundled resources

- `skills/commerce-agent-architecture/SKILL.md` — the single-agent-plus-skills design, placement
  rule, tool engineering, and UI components as tools.
- `skills/commerce-agent-architecture/references/skills-vs-subagents.md` — the full trade-off and
  the two cases where subagents still fit.
- `skills/commerce-agent-architecture/references/capability-map.md` — the reference
  implementation's prompt/skill split for shopping and merchant agents.
- `skills/commerce-agent-architecture/references/ui-components-as-tools.md` — benefits, the
  buffering trade-off, and `eager_input_streaming`.
- `skills/commerce-agent-latency-and-cost/SKILL.md` — the three latency levers, perceived
  latency, caching, and model selection.
- `skills/commerce-agent-latency-and-cost/references/prompt-cache-segments.md` — the three-segment
  layout and a checklist.
- `skills/commerce-agent-latency-and-cost/references/model-selection-sweep.md` — the sweep
  procedure and the tie-breaker.
- `skills/commerce-agent-memory/SKILL.md` — typed records, async extraction, the three read
  layers.
- `skills/commerce-agent-memory/templates/memory-fact-record.json` — the fact record shape.
- `skills/commerce-agent-memory/references/memory-data-handling.md` — retention, correction,
  deletion, per-deployment toggle.
- `skills/commerce-agent-safety-harness/SKILL.md` — the four enforcement principles.
- `skills/commerce-agent-safety-harness/references/safety-principles.md` — each principle in full.
- `skills/commerce-agent-safety-harness/scripts/sanitize_untrusted_content.py` — a runnable
  sanitizer for listings, reviews, policies, seller messages and stored memory.
- `skills/commerce-agent-evals/SKILL.md` — snapshot testing and the five coverage areas.
- `skills/commerce-agent-evals/references/eval-coverage-matrix.md` — the full case matrix.
- `skills/commerce-agent-evals/references/ci-suite-selection.md` — ownership, CI selection, and
  release calendar practices.
- `skills/commerce-agent-evals/templates/snapshot-case.md` — a fill-in snapshot case.
- `guides/anatomy-of-a-commerce-agent.{en,ko,es,ja}.md` — the whole guide in four languages.

## Source

- https://claude.com/blog/the-anatomy-of-effective-commerce-agents (published 2026-09-02)
