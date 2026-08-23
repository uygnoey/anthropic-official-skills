**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Base44 is a vibe-coding platform that lets anyone, regardless of technical ability, build full stack applications and websites — customers range from small businesses with no developers to companies building full SaaS products. Yoav Orlev, its first employee and now head of product, describes what changed when a model could finally be trusted with the work that had been reserved for the company's most senior engineers.

Two threads run through the post. The first is Base44's evaluation practice: every new Claude model runs through evals across different app types measuring latency, cost, and build errors, plus stress builds like a Minecraft clone to see how it handles game physics and mechanics. The second is the tier of work that opened up once Claude Fable 5 cleared those evals — rebuilding a system prompt with hundreds of permutations, fixing the harness behind the in-app agent, and a product manager standing up native mobile app building on his own.

## When is it useful?
- When a core change touching interdependent parts is queued behind one or two specific engineers.
- When designing an eval suite for a codegen or app-generation product.
- When an eval passes but production cost regresses anyway — for instance because a prompt change broke the cache.
- When calibrating how much specification a model actually needs before a long unattended run.
- When deciding whether a non-engineer can own a piece of technical work.
- When a review-test-approve gate has to replace step-by-step supervision.

## Key points
- **The bottleneck was blast radius, not difficulty.** Small and medium-scope features always moved quickly; changes to the platform's core that touch multiple interdependent parts could only be entrusted to the most senior engineers.
- **Two named bottlenecks:** the system prompt and its hundreds of permutations (first app or fifth, free user or subscriber, app category and features), and the native mobile infrastructure, which only engineers with mobile expertise could change.
- **The behavior that disqualified earlier models:** when stuck on an error, a model would keep working the spot in front of it instead of recognizing the fix probably already existed elsewhere in the code and searching for it. "The decision on what to do next is a crucial one and most of the time [earlier] models would take, I would say, a naive approach." — Yoav Orlev
- **Claude Fable 5 was the first model the team tested that could reason as if it had an understanding of how software is built.**
- **The eval suite:** evals across different app types measuring latency, cost, and build errors, plus stress builds like a Minecraft clone for game physics and mechanics.
- **Two things stood out:** far fewer turns to completion, and more complete apps from the first prompt — including the edge cases earlier models skipped.
- **The system prompt rebuild:** about an hour of back-and-forth questions, then four hours running on its own, returning 90% to 95% of what the team needed; measured and shipped via A/B testing infrastructure that afternoon.
- **The model found a gap in Base44's own evals:** the team wasn't testing for cache hits, even though a prompt change can break the cache — and at the scale of millions of users that drives up cost.
- **The harness fix:** stuck on a change to the harness behind the in-app agent, it reasoned the problem had probably been solved elsewhere, went to investigate, and came back with the fix. "This reasoning of 'this probably has been solved somewhere else, so I should go there to investigate' is something we haven't seen so often in other models."
- **Brief the goal and the why.** Orlev compares it to a senior engineer: a junior needs every step specified and constant checking; a senior needs the goal and the why.
- **A product manager did the native mobile job** — roughly two and a half hours to a working environment at about 90% of what was needed for production.
- **Review became the gate, not supervision the method.** The model executes; the team reviews, tests, and approves before shipping.
- **What's next:** turning Base44 from a tool that builds apps into one that helps people manage and grow them, with Base44 Superagents now public. "Fable has given us the confidence to make bolder moves with the business."

## Bundled resources
- `skills/app-generation-model-evals/SKILL.md` — evaluate across app types, add stress builds, score turns and first-prompt completeness, test for cache hits, ship behind A/B measurement.
- `skills/app-generation-model-evals/references/eval-dimensions.md` — each dimension, why the app-type spread matters, and what the post leaves unspecified.
- `skills/app-generation-model-evals/templates/model-eval-run.md` — a comparable per-model run record including caching and edge cases.
- `skills/app-generation-model-evals/examples/fable-5-evaluation.md` — the Fable 5 run with its numbers and a before/after table.
- `skills/senior-scope-delegation/SKILL.md` — identify work queued behind people, check where-to-work reasoning, brief goal and why, front-load questions, gate on review.
- `skills/senior-scope-delegation/references/review-gate.md` — what review-test-approve replaced, and what makes same-day shipping defensible.
- `skills/senior-scope-delegation/templates/goal-and-why-brief.md` — a brief that states the outcome and the constraint instead of the steps.
- `skills/senior-scope-delegation/examples/base44-handoffs.md` — the three handoffs, the bottleneck they cleared, and what Base44 is building next.
- `guides/trusting-a-model-with-core-changes.{en,ko,es,ja}.md` — the full account in four languages.

## Source
[Working at the frontier: Why Base44 trusts Claude Fable 5 with their most challenging engineering work](https://claude.com/blog/working-at-the-frontier-why-base44-trusts-claude-fable-5-with-their-most-challenging-engineering-work) — Claude blog, July 15, 2026.
