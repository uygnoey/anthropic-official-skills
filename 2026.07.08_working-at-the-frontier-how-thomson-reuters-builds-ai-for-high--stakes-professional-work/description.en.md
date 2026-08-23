**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Thomson Reuters is a 175-year-old content and technology company applying AI to legal, tax, accounting, compliance, and other professional workflows that demand precision. This post is CTO Joel Hron's account of how the company decides whether a model is fit for work that has to hold up in court — and what it changed about its products once it decided one was.

The organizing idea is where accountability sits. "That human professional is still the one who is accountable for the end work product," which is why the test applied to a model is whether its work can withstand professional legal review, rather than a benchmark score. The company's name for the resulting approach is Fiduciary-Grade AI™: grounded in authoritative content, shaped by domain expertise, embedded in professional workflows.

The second half is architectural. Rather than building smarter chatbots, Thomson Reuters rebuilt its products as agent-based systems — CoCounsel Legal moved from separate skills running sequentially to a single agent on the Claude Agent SDK, planning and orchestrating across hundreds of tools in real time.

## When is it useful?
- When the output has to survive review by someone accountable for it, and "mostly right" is a failure.
- When deciding what to require of a model before trusting it with regulated or high-stakes work.
- When a product is a set of separate features and users are doing the sequencing themselves.
- When evaluating a model for an agent that plans across a large tool surface.
- When designing where citation checking happens relative to human review.
- When reporting on an AI initiative and cost-per-task is the only number being asked for.

## Key points
- **The test is professional review, not a benchmark.** Thomson Reuters evaluates models by asking whether their work can withstand professional legal review.
- **Accountability is unchanged by the AI.** "That human professional is still the one who is accountable for the end work product." — Joel Hron
- **Three advantages, one system.** Authoritative content, deep domain expertise, and workflow integration — Anthropic's frontier models combined with curated content, 2,700+ domain experts, and evaluation infrastructure.
- **Fiduciary-Grade AI™** means outputs are "transparent, verifiable, and defensible when the stakes are high."
- **Legal research was rebuilt around verification.** Agents tuned for citation validation and verification rather than just search and retrieval, so professionals can review, verify, and apply judgment with confidence.
- **Four requirements before trusting a model:** citation validation before human review; context management across extended tool-use chains; human collaboration — bringing the person into developing the work product rather than relying on the agent; and capability expansion into advanced drafting, including motions and filings professionals would spend days or weeks perfecting.
- **Agent-first, not chatbot-smarter.** A single agent now accesses hundreds of company tools simultaneously.
- **CoCounsel Legal's rebuild:** from separate skills running sequentially to the Claude Agent SDK, planning and orchestrating across tools in real time. Customer data stays protected and out of third-party model training.
- **What they test for:** "Our big test for Claude is to assess how good it is at making plans and using tools effectively."
- **Why Anthropic:** approaches to transparency, safety, and responsible AI development; early proof came through deep research capabilities built collaboratively.
- **The contrarian ROI take.** "If you try to optimize too much for the rate of return calculation, you miss the forest for the trees." Cultural mindset shifts come before cost-per-task metrics — while DORA and time-to-production are still tracked.
- **One concrete number:** an internal error-remediation tool built on Claude cut root cause analysis from three hours to four minutes.
- **The job itself changed.** "The act of writing lines of code is no longer the job" — systems thinking, judgment, and taste matter most now, and the pattern makes people "more T-shaped" across product, design, and finance.
- **Next:** longer-horizon work, better context management, dependable tool-calling across agent task chains. Hron uses Claude Code to onboard codebases and Claude Cowork for strategic analysis.
- **The standard:** professional AI has to work in environments "where being almost right is not good enough."

## Bundled resources
- `skills/defensible-ai-outputs/SKILL.md` — ground the work in authoritative content, validate citations before review, meet all four requirements, and check transparency, verifiability, and defensibility.
- `skills/defensible-ai-outputs/references/four-requirements.md` — each requirement, what it implies in practice, and what the post leaves unspecified.
- `skills/defensible-ai-outputs/templates/citation-validation-checklist.md` — a per-claim and per-output gate, plus the handoff to the accountable professional.
- `skills/defensible-ai-outputs/examples/professional-workflows.md` — legal research rebuilt around verification, advanced drafting, and the error-remediation tool.
- `skills/agent-first-product-rebuild/SKILL.md` — replace user-side sequencing with a planning agent, expose tools broadly, and test models on planning and tool use.
- `skills/agent-first-product-rebuild/references/agent-architecture.md` — the before-and-after, what the architecture demands of a model, and the open questions.
- `skills/agent-first-product-rebuild/references/measuring-the-shift.md` — the ROI position, what is still tracked, and the deeper change to the work.
- `skills/agent-first-product-rebuild/templates/agent-readiness-review.md` — planning, tool use, context management, and the four professional requirements as a record.
- `skills/agent-first-product-rebuild/examples/cocounsel-rebuild.md` — the CoCounsel Legal rebuild in detail.
- `guides/building-ai-for-high-stakes-work.{en,ko,es,ja}.md` — the full account in four languages.

## Source
[Working at the Frontier: How Thomson Reuters Builds AI for High-Stakes Professional Work](https://claude.com/blog/working-at-the-frontier-how-thomson-reuters-builds-ai-for-high--stakes-professional-work) — Claude blog, July 8, 2026.
