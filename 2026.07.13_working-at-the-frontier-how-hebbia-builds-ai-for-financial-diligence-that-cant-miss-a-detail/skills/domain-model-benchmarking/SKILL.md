---
name: domain-model-benchmarking
description: Decide whether a new model is worth adopting by running it against a domain-specific benchmark head-to-head with the model it would replace, rather than reading public scores — build tests that replicate the real jobs your users do, expand the benchmark with each release, and separate retrieval quality from synthesis quality when reading the results. Use when a new model ships and someone asks whether to switch, when building an internal eval for a high-accuracy domain, or when a benchmark result jumps and you need to know what actually improved.
---

# Benchmarking a new model against the one it would replace

Hebbia runs every new model through a finance-specific benchmark, comparing head-to-head against the
model it would replace, and expands the benchmark's measurements with each release. The reason is the
bar its customers set. As Divya Mehta, the company's founding product manager, puts it: "The bar is
extremely high, and our customers hold us to that extremely high bar — and rightfully so."

This skill describes that evaluation pattern as the post presents it.

## Instructions

### 1. Build the benchmark from your domain, not from public tasks

Hebbia's benchmark is finance-specific and replicates key finance knowledge worker use cases. The tests
exist because the customers' work is specific: analyses spanning thousands of dense documents where
accuracy is critical, drawn from public filings, credit agreements, internal documents, and structured
CRM data.

Start from the jobs your users actually do, and build tests that replicate them.

### 2. Run at least two shapes of test

Joe Renner, a researcher on the applied AI team, tests each new Claude model against the benchmark
using two distinct shapes:

- **A question-answering and citation-finding test over financial documents.** Narrow, scoreable,
  measures whether the model finds the right evidence and answers from it.
- **A run through the agent system with the chat product's tools.** Open-ended, multi-source analysis —
  the messier case, where the model plans, calls tools, and holds a multi-part request together.

The two tests catch different failures. A model can be strong at grounded question answering and still
lose parts of a multi-part request once it is running as an agent.

See [references/benchmark-shape.md](references/benchmark-shape.md) for what the post specifies about
each test and what it leaves open.

### 3. Compare head-to-head with the incumbent

The comparison is always against the model the new one would replace — not against an abstract
threshold and not against a leaderboard. That framing is what makes the result actionable: the question
being answered is "should we switch," not "is this model good."

Record results with [templates/model-eval-record.md](templates/model-eval-record.md).

### 4. Read the result as two separate signals

On Hebbia's question-answering and citation test, Claude Fable 5 achieved approximately a 20% relative
accuracy gain over financial documents — the best performance Renner had recorded from any new model.
Citation matching held roughly steady.

Those two numbers together are the interesting part. Citations did not improve; accuracy did. Renner
attributes the gain to the model better understanding the evidence it identifies. Reading only the
headline number would have missed which half of the job got better.

Mehta reduces the whole thing to two qualities: "the ability to find the right information from a dense
data set, and then synthesize it correctly." Score them separately.

### 5. Look for reach, not just correctness, on the open-ended test

On open-ended analysis, the model reasoned from a broader cross-section of the data and reached
conclusions the team found worthy of closer examination. Renner attributes this to long task coherence:
keeping every part of a request in view, prompting its own sub-agents and tools to retrieve relevant
facts, and grounding each claim in its source rather than inferring it.

A benchmark that only scores whether the expected answer appeared will not register this. Leave room in
the eval to note where a model drew on data the previous one ignored.

### 6. Expand the benchmark with each release

Hebbia expands its benchmark measurements with each release. A benchmark that stays fixed across model
generations gradually stops discriminating: the tests that separated models two releases ago are the
ones every candidate now passes.

## Examples

The Claude Fable 5 evaluation as the post reports it, with the results and what was concluded from
them, is in [examples/fable-5-evaluation.md](examples/fable-5-evaluation.md).

Summary of that run:

- **Both tests cleared by the widest margin Renner had measured.**
- **Question answering and citation finding:** approximately 20% relative accuracy gain over financial
  documents; citation matching roughly steady.
- **Agent run:** every component of multi-part requests held simultaneously, all answered, each answer
  cited back to its source.
- **Open-ended analysis:** reasoning from a broader cross-section of data, reaching conclusions worth
  closer examination.

## Source

[Working at the frontier: How Hebbia builds AI for financial diligence that can't miss a detail](https://claude.com/blog/working-at-the-frontier-how-hebbia-builds-ai-for-financial-diligence-that-cant-miss-a-detail) — Claude blog, July 13, 2026.
