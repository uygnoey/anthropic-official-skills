**English** · [한국어](./building-ai-for-high-stakes-work.ko.md) · [Español](./building-ai-for-high-stakes-work.es.md) · [日本語](./building-ai-for-high-stakes-work.ja.md)

# How Thomson Reuters builds AI for high-stakes professional work

Thomson Reuters is a global content and technology company with over 175 years of history. It is
applying AI to legal, tax, accounting, compliance, and professional workflows that demand precision.

"We're a technology company focused on professions that demand accuracy and precision," explains Joel
Hron, the company's CTO. Its products include Westlaw and Practical Law for legal research, and
CoCounsel Legal — a professional-grade legal AI platform designed to make legal professionals more
effective with defensible answers.

Hron joined Thomson Reuters four years ago, when his startup was acquired. He notes that AI has
fundamentally reshaped software development, which makes technology partner selection critically
important.

## The test a model has to pass

Thomson Reuters evaluates language models by asking whether their work can withstand professional legal
review.

The reason that is the test, rather than a benchmark score, is where accountability sits:

> "That human professional is still the one who is accountable for the end work product."

The company leverages three advantages: authoritative content, deep domain expertise, and workflow
integration. The system combines Anthropic's frontier models with Thomson Reuters' curated content,
2,700+ domain experts, and evaluation infrastructure.

The approach has a name — **Fiduciary-Grade AI™**: grounded in authoritative content, shaped by domain
expertise, and embedded in professional workflows so that outputs are "transparent, verifiable, and
defensible when the stakes are high."

In practice, that meant rebuilding legal research around agents tuned for citation validation and
verification, rather than just search and retrieval — so professionals can review, verify, and apply
judgment with confidence.

## Building an agent-first product

Instead of creating smarter chatbots, Thomson Reuters rebuilt its products as agent-based systems. A
single agent now accesses hundreds of company tools simultaneously.

> "Our big test for Claude is to assess how good it is at making plans and using tools effectively."

CoCounsel Legal is the example. It previously ran separate skills sequentially; it has been rebuilt on
the Claude Agent SDK, planning and orchestrating across tools in real time. Customer data remains
protected and is not used for third-party model training.

Thomson Reuters chose Anthropic based on its approaches to transparency, safety, and responsible AI
development. Early proof came through deep research capabilities built collaboratively.

## What knowledge work demands of a model

Four requirements had to be met before the company would trust a model with this work:

1. **Citation validation.** The system must check citations before presenting findings for human
   review.
2. **Context management.** Models must maintain thread continuity across extended tool-use chains.
3. **Human collaboration.** Models should "bring the human into the loop of developing a work product
   rather than just relying on the agent."
4. **Capability expansion.** Advanced drafting for complex work, including motion drafting and filings
   professionals would "spend days or weeks perfecting."

## The ROI question

Hron's position here is deliberately contrarian:

> "If you try to optimize too much for the rate of return calculation, you miss the forest for the
> trees."

He prioritizes cultural mindset shifts before optimizing for cost-per-task metrics. The company still
tracks engineering measures like DORA and time-to-production, and has concrete results to point at: an
internal error-remediation tool built on Claude reduced root cause analysis from three hours to four
minutes.

But the deeper change is to the work itself. Of engineers, Hron notes: "The act of writing lines of
code is no longer the job." Now skills like systems thinking, judgment, and taste matter most. The same
pattern spreads across organizations, making people "more T-shaped," able to reach across product,
design, and finance.

## What's next

Hron's team prioritizes longer-horizon work, better context management, and dependable tool-calling
across agent task chains. He personally uses Claude Code to rapidly onboard codebases and Claude Cowork
for strategic analysis.

For work that "ultimately has to hold up in court," he sees pushing model capabilities as "the frontier
worth pushing on next. After all, professional AI has to work in environments where being almost right
is not good enough."

## Source

[Working at the Frontier: How Thomson Reuters Builds AI for High-Stakes Professional Work](https://claude.com/blog/working-at-the-frontier-how-thomson-reuters-builds-ai-for-high--stakes-professional-work) — Claude blog, July 8, 2026.
