---
name: agent-first-product-rebuild
description: Rebuild a product from sequential, separate skills into a single agent that plans and orchestrates across tools in real time, and test candidate models on the ability that architecture depends on — planning and effective tool use. Use when a product is a collection of one-shot features that users have to sequence themselves, when evaluating whether a model can carry an agent across hundreds of tools, or when deciding what to measure about an AI initiative beyond cost per task.
---

# Rebuilding a product as an agent rather than a smarter chatbot

Thomson Reuters did not respond to better models by making its chatbots smarter. It rebuilt its
products as agent-based systems. A single agent now accesses hundreds of company tools simultaneously.

CoCounsel Legal is the worked example. It previously ran separate skills sequentially. It has been
rebuilt on the Claude Agent SDK, planning and orchestrating across tools in real time.

That architecture puts the load on one specific model ability, which is what Joel Hron, the company's
CTO, says they test for:

> "Our big test for Claude is to assess how good it is at making plans and using tools effectively."

## Instructions

### 1. Find the sequencing the user is currently doing

The shape you are replacing is a product where capabilities exist as separate skills and the user
decides which to run in what order. That sequencing work is the thing the agent takes over.

Before rebuilding, write down the sequences users actually run. Those are the plans the agent will have
to construct on its own.

### 2. Expose tools broadly rather than pre-wiring flows

A single agent accessing hundreds of tools simultaneously is a different design from a workflow that
routes between a handful of them. The agent plans across the tool surface in real time instead of
following a path someone laid out in advance.

See [references/agent-architecture.md](references/agent-architecture.md) for what the post specifies
about this rebuild and what it leaves open.

### 3. Test candidate models on planning and tool use

Because the architecture depends on it, that is what the evaluation should target — not general
capability. Assess:

- **Plan quality** — does the model construct a sensible sequence for a request it has not seen before?
- **Tool use** — does it call the right tools, with the right arguments, and use what comes back?
- **Thread continuity** — does it maintain continuity across extended tool-use chains, so the answer at
  the end still addresses the question at the start?

Use [templates/agent-readiness-review.md](templates/agent-readiness-review.md) to record this.

### 4. Keep the human inside the work, not at the end of it

One of Thomson Reuters' four model requirements is that models should "bring the human into the loop of
developing a work product rather than just relying on the agent." An agent-first rebuild is not a move
toward removing the person — the human professional remains accountable for the end work product.

### 5. Protect customer data as part of the architecture

In the rebuilt CoCounsel Legal, customer data remains protected and is not used for third-party model
training. Treat this as a property of the system design rather than a policy layered on afterward.

### 6. Measure the initiative on more than rate of return

Hron takes a deliberately contrarian position:

> "If you try to optimize too much for the rate of return calculation, you miss the forest for the
> trees."

He prioritizes cultural mindset shifts before optimizing for cost-per-task metrics. Thomson Reuters
still tracks engineering measures — DORA and time-to-production among them — and has concrete results
such as an internal error-remediation tool built on Claude that cut root cause analysis from three
hours to four minutes.

But the deeper change the post points to is in the work itself. On engineers: "The act of writing lines
of code is no longer the job." What matters instead is systems thinking, judgment, and taste. The
pattern spreads across organizations, making people "more T-shaped," able to reach across product,
design, and finance.

See [references/measuring-the-shift.md](references/measuring-the-shift.md) for how the post frames what
to track.

### 7. Choose the model partner on transparency, safety, and responsible development

Hron notes that AI has fundamentally reshaped software development, which makes technology partner
selection critically important. Thomson Reuters chose Anthropic based on its approaches to
transparency, safety, and responsible AI development; early proof came through deep research
capabilities built collaboratively.

## Examples

The CoCounsel Legal rebuild — before and after, and what the architecture demands of the model — is in
[examples/cocounsel-rebuild.md](examples/cocounsel-rebuild.md).

Where the team is heading next, per the post: longer-horizon work, better context management, and
dependable tool-calling across agent task chains. Hron personally uses Claude Code to rapidly onboard
codebases and Claude Cowork for strategic analysis.

## Source

[Working at the Frontier: How Thomson Reuters Builds AI for High-Stakes Professional Work](https://claude.com/blog/working-at-the-frontier-how-thomson-reuters-builds-ai-for-high--stakes-professional-work) — Claude blog, July 8, 2026.
