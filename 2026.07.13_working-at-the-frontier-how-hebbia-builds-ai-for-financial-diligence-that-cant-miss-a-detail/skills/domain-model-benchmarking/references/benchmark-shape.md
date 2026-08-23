# The shape of Hebbia's benchmark

What the post states about how the benchmark is built, and what it leaves unspecified.

## Stated

**It is finance-specific.** The benchmark replicates key finance knowledge worker use cases. It is not
a general capability suite.

**Every new model goes through it.** The team runs every new model through the benchmark, comparing
head-to-head against the model it would replace.

**It grows.** Benchmark measurements are expanded with each release.

**Two tests are named:**

| Test | What it covers |
| --- | --- |
| Question answering and citation finding | Over financial documents. Measures whether the model locates the right evidence and answers from it. |
| Agent system run with chat product tools | Simulates open-ended, multi-source analysis. |

**Who runs it.** Joe Renner, a researcher on the applied AI team, tests each new Claude model against
the benchmark.

**What the team is optimizing for.** Adithya Ramanathan leads the applied AI research team, focused on
finding signals by getting models to draw on the right data, in the right context, surfacing what
customers need to know. His framing: "When you're connecting it to the right data and putting it in the
right ecosystem, that's when you get the alpha that finance professionals actually chase."

## Scored dimensions that appear in the results

- **Accuracy over financial documents** — reported as a relative gain against the incumbent model.
- **Citation matching** — reported separately, and in the Fable 5 run it moved independently of
  accuracy.
- **Holding multi-part requests** — whether every component of a request is held simultaneously,
  answered, and cited back to source.
- **Breadth of data reasoned over** — on open-ended analysis, how wide a cross-section of the data the
  model drew on.

## Unspecified

- How many tasks the benchmark contains.
- How accuracy is scored, and by whom or what.
- What "citation matching" is measured against.
- Which tools the chat product exposes in the agent run.
- What margin counts as enough to adopt a new model.
- Whether the benchmark is public or shared with customers.

## Source

[Working at the frontier: How Hebbia builds AI for financial diligence that can't miss a detail](https://claude.com/blog/working-at-the-frontier-how-hebbia-builds-ai-for-financial-diligence-that-cant-miss-a-detail) — Claude blog, July 13, 2026.
