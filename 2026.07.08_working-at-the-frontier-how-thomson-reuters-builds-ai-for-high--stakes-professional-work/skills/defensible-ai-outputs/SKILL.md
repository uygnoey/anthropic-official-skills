---
name: defensible-ai-outputs
description: Build AI output that a professional can put their name on — grounded in authoritative content, checked for citation validity before a human ever reviews it, and transparent enough to defend when the stakes are high. Use when the work product has to hold up under professional review (legal, tax, accounting, compliance), when deciding what to require of a model before trusting it with that work, or when deciding what the human in the loop is actually accountable for.
---

# Producing work that holds up under professional review

Thomson Reuters is a global content and technology company with over 175 years of history, applying AI
to legal, tax, accounting, compliance, and other professional workflows that demand precision. Joel
Hron, its CTO, describes the company as "a technology company focused on professions that demand
accuracy and precision."

The test the company applies to a language model is not a benchmark score. It is whether the model's
work can withstand professional legal review.

The reason that test is the right one is the accountability structure underneath it:

> "That human professional is still the one who is accountable for the end work product."

The AI does not absorb the liability. So the output has to arrive in a form the accountable person can
check.

## Instructions

### 1. Ground the work in authoritative content

Thomson Reuters leverages three advantages, and the first is authoritative content: reference tools
including Westlaw and Practical Law for legal research, plus curated content that the models work
against. CoCounsel Legal — the company's professional-grade legal AI platform — is built to make legal
professionals more effective with defensible answers.

A frontier model on its own is not the system. The system is the model combined with curated content,
2,700+ domain experts, and evaluation infrastructure.

### 2. Validate citations before a human sees the findings

This is the first of the four requirements Thomson Reuters identified before it would trust a model
with this work: the system must check citations before presenting findings for human review.

The order matters. Handing a professional an uncited or unverified finding moves the checking work onto
the person who is already accountable for it. Thomson Reuters rebuilt legal research around agents
tuned for citation validation and verification rather than just search and retrieval, so that
professionals can review, verify, and apply judgment with confidence.

Use [templates/citation-validation-checklist.md](templates/citation-validation-checklist.md) as the
gate an output passes through before review.

### 3. Meet the other three requirements before trusting the model

The full set of four, described in
[references/four-requirements.md](references/four-requirements.md):

1. **Citation validation** — check citations before presenting findings for human review.
2. **Context management** — maintain thread continuity across extended tool-use chains.
3. **Human collaboration** — "bring the human into the loop of developing a work product rather than
   just relying on the agent."
4. **Capability expansion** — advanced drafting for complex work, including motion drafting and
   filings professionals would "spend days or weeks perfecting."

Requirement 3 is the one most easily lost. The human is not a reviewer bolted onto the end of an
autonomous run; they are part of developing the work product.

### 4. Make outputs transparent, verifiable, and defensible

Thomson Reuters calls its approach **Fiduciary-Grade AI™**: grounded in authoritative content, shaped
by domain expertise, and embedded in professional workflows so that — in the company's framing —
outputs are transparent, verifiable, and defensible when the stakes are high.

Treat those three as properties of the output, and check each one:

- **Transparent** — the reasoning and the sources are visible, not summarized away.
- **Verifiable** — a reviewer can independently confirm each claim against a source.
- **Defensible** — the work survives challenge by someone with an interest in overturning it.

### 5. Keep customer data out of third-party training

CoCounsel Legal is rebuilt on the Claude Agent SDK, planning and orchestrating across tools in real
time, and customer data remains protected and is not used for third-party model training. For work of
this kind, that constraint is part of the product, not an afterthought.

### 6. Pick a model partner on more than capability

Thomson Reuters chose Anthropic based on its approaches to transparency, safety, and responsible AI
development. Hron notes that AI has fundamentally reshaped software development, which makes technology
partner selection critically important. Early proof came through deep research capabilities built
collaboratively.

## Examples

Worked through in [examples/professional-workflows.md](examples/professional-workflows.md):

- **Legal research rebuilt around verification.** Agents tuned for citation validation and verification
  rather than search and retrieval, so professionals review, verify, and apply judgment with
  confidence.
- **Advanced drafting.** Motion drafting and filings that professionals would spend days or weeks
  perfecting — the capability-expansion requirement in its concrete form.
- **Internal error remediation.** A tool built on Claude that reduced root cause analysis from three
  hours to four minutes.

Hron's closing standard for this class of work: for output that "ultimately has to hold up in court,"
professional AI has to work in environments "where being almost right is not good enough."

## Source

[Working at the Frontier: How Thomson Reuters Builds AI for High-Stakes Professional Work](https://claude.com/blog/working-at-the-frontier-how-thomson-reuters-builds-ai-for-high--stakes-professional-work) — Claude blog, July 8, 2026.
