# Decomposing document analysis into steps

Everything below is drawn from Hebbia's account. Where the post does not specify something, it says so
rather than filling the gap.

## Why decomposition survives better models

The intuition that a more capable model removes the need to break work down is the one the post argues
against directly. Decomposing work into steps remains important "no matter how brilliant the model is,"
for a reason that has nothing to do with model quality:

> Firms require control over which documents feed the analysis and how each step is constructed.

That control is a requirement of the domain, not a workaround for model limits. A single model run over
a data room may produce a good answer, but it does not let a firm say which documents were consulted at
which stage, or inspect how a particular conclusion was reached.

## What the steps are made of

- **Meta-prompting turns the request into prompts.** The user writes in plain language. The system
  converts that into the prompts that will actually run.
- **Each step runs across the corpus.** The model analyzes each step across hundreds of documents,
  rather than one pass over everything.
- **Sources are mixed.** Public filings, credit agreements, internal documents, and structured data
  from CRMs all feed the same analysis.
- **Steps can be deterministic.** In the pitch-deck job Hebbia codified, data is gathered across
  sources through deterministic agentic steps before analysis begins.

## Where the model's own decomposition fits

The post describes the model prompting its own sub-agents and tools to retrieve relevant facts during a
run. This sits *inside* a step rather than replacing the step structure: the outer decomposition is
what the firm controls and inspects; the inner retrieval is how the model services a step it has been
given.

## Composing steps with the Claude Agent SDK

Hebbia is adopting the Claude Agent SDK to compose these jobs as smaller, repeatable, verified steps
rather than single model runs. The post names the adoption and the reason — repeatability and
verification — but does not describe the SDK wiring itself.

## What the post does not specify

- How many steps a typical job decomposes into.
- How a step is verified, or by what.
- How meta-prompting decides where one step ends and the next begins.
- Which parts of a codified job are deterministic and which are left to the model.

Treat these as open when adapting the pattern; do not assume a particular answer.

## Source

[Working at the frontier: How Hebbia builds AI for financial diligence that can't miss a detail](https://claude.com/blog/working-at-the-frontier-how-hebbia-builds-ai-for-financial-diligence-that-cant-miss-a-detail) — Claude blog, July 13, 2026.
