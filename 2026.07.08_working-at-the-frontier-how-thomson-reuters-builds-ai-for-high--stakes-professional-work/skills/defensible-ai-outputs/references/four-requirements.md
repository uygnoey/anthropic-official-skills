# What knowledge work demands of a model

Thomson Reuters identified four requirements before it would trust a model with professional work.
Below is each one as the post states it, with what it implies in practice and what the post leaves
open.

## 1. Citation validation

> The system must check citations before presenting findings for human review.

**The order is the requirement.** Validation happens *before* review, not as part of it. A finding that
reaches a professional with unchecked citations has shifted the verification burden onto the person who
is already accountable for the end work product.

Thomson Reuters rebuilt legal research around agents tuned for "citation validation and verification"
rather than just search and retrieval. The distinction: search and retrieval finds candidate sources;
validation and verification establishes that the cited source says what the finding claims it says.

## 2. Context management

> Models must maintain thread continuity across extended tool-use chains.

An agent that plans across hundreds of tools will make many calls before producing anything. If the
thread of what it was asked and what it has established degrades over that chain, the output is
unreliable in a way that is hard to spot at review time — the citations may each check out while the
overall answer has drifted from the question.

## 3. Human collaboration

> Models should "bring the human into the loop of developing a work product rather than just relying on
> the agent."

This is a statement about where the human sits, not how much the agent does. The professional
participates in developing the work product. A design that runs autonomously and then presents a
finished artifact for approval satisfies the letter of "human in the loop" while missing this
requirement.

## 4. Capability expansion

> Advanced drafting for complex work, including motion drafting and filings professionals would "spend
> days or weeks perfecting."

The bar here is set by what the work costs a professional today. Drafting a motion is not a
summarization task with a longer output; it is the work that consumed the days or weeks.

## The system these requirements sit in

The model is one component. Thomson Reuters combines Anthropic's frontier models with:

- its own curated, authoritative content (Westlaw, Practical Law, and more),
- 2,700+ domain experts,
- evaluation infrastructure.

The company's term for the resulting approach is **Fiduciary-Grade AI™**: grounded in authoritative
content, shaped by domain expertise, and embedded in professional workflows so outputs are
"transparent, verifiable, and defensible when the stakes are high."

## What the post does not specify

- How citation validation is implemented, or what it checks against.
- How context management is measured or tested.
- What the evaluation infrastructure consists of.
- How the 2,700+ domain experts feed into model behavior or evaluation.

## Source

[Working at the Frontier: How Thomson Reuters Builds AI for High-Stakes Professional Work](https://claude.com/blog/working-at-the-frontier-how-thomson-reuters-builds-ai-for-high--stakes-professional-work) — Claude blog, July 8, 2026.
