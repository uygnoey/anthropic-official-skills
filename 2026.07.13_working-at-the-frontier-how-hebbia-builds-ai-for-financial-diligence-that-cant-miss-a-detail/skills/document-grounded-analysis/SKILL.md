---
name: document-grounded-analysis
description: Run analysis over large sets of dense, unstructured documents so that every answer is traceable to its source — decompose a plain-language request into per-step questions, answer each one in its own cell, cite it back to the document it came from, and keep the human able to see and steer each step. Use when working through data rooms, credit agreements, public filings, or any pile of proprietary documents where a missed detail is a real cost, and when turning that analysis into first-draft memos or covenant reviews.
---

# Analyzing dense document sets without losing the thread

Hebbia is an AI platform used by more than a third of the top 50 asset managers, alongside tier-1
investment banks and law firms. Its customers make decisions from analyses spanning thousands of dense
documents, where accuracy is critical — public filings, credit agreements, internal documents, and
structured data pulled from CRMs.

The information that gives those customers a competitive advantage lives in unstructured, proprietary
documents. That material has historically been harder to analyze at scale than the structured,
quantitative data finance already models well. Hebbia built its Matrix product to systematize that
qualitative work.

Two properties define the approach:

- **Meta-prompting.** A plain-language request is converted into prompts, and the model analyzes each
  step across hundreds of documents rather than answering the whole request in one pass.
- **Cell-level answers.** Results land in individual cells on a grid, which is what makes the analysis
  transparent, traceable, and steerable — you can see which step produced which answer and where it
  came from.

Adithya Ramanathan, who leads Hebbia's applied AI research team, frames the goal as finding signal by
getting models to draw on the right data in the right context: "When you're connecting it to the right
data and putting it in the right ecosystem, that's when you get the alpha that finance professionals
actually chase."

## Instructions

### 1. Convert the request into steps before answering any of it

Do not hand a dense corpus a single broad question. Turn the plain-language request into a sequence of
narrower prompts, each one answerable against the documents. Hebbia's meta-prompting does this
conversion; the model then works each step across the document set.

The reason to keep this discipline is not model weakness. As the post puts it, decomposing work into
steps remains important "no matter how brilliant the model is," because firms require control over
which documents feed the analysis and how each step is constructed.

See [references/decomposition.md](references/decomposition.md) for what the post says about how these
steps are built and where it stops short.

### 2. Give every answer its own cell, and cite it

Each step's answer belongs in its own addressable place, next to the evidence it rests on. That layout
buys three things the post names explicitly:

- **Transparency** — the intermediate answers are visible, not buried inside one long response.
- **Traceability** — each answer points back at the document it came from.
- **Steerability** — a step that went wrong can be corrected without rerunning everything.

Use [templates/analysis-grid.md](templates/analysis-grid.md) as the shape for this: one row per
document or deal, one column per question, one citation per cell.

### 3. Score the two abilities that actually matter

Divya Mehta, Hebbia's founding product manager, reduces the job to two qualities: "the ability to find
the right information from a dense data set, and then synthesize it correctly."

Evaluate work along both axes separately. A retrieval that surfaces the right passage but draws the
wrong conclusion, and a sound conclusion built on the wrong passage, fail differently and are fixed
differently.

### 4. Hold every part of a multi-part request

On Hebbia's agent test, the behavior worth having was holding every component of a multi-part request
simultaneously — answering all of them, and citing each answer back to its source. The failure mode to
watch for is a request that arrives with five parts and comes back thoroughly answering three.

Joe Renner, a researcher on the applied AI team, attributes this to long task coherence: keeping every
part of a request in view, prompting sub-agents and tools to retrieve the relevant facts, and grounding
each claim in its source rather than inferring it.

### 5. Ground claims rather than inferring them

The distinction is the whole point of the exercise. A claim is grounded when it can be pointed back at
a specific passage in a specific document. A claim is inferred when it is plausible given what the
model has read. In diligence work, only the first kind survives review.

### 6. Compose the job as repeatable, verified steps

Hebbia is adopting the Claude Agent SDK to compose these jobs as smaller, repeatable, verified steps
rather than single model runs. Once a job is decomposed and each step is verified, the whole job can be
codified and rerun — which is what turns a multi-day analysis into a repeatable pipeline.

## Examples

Two applications from the post, worked through in
[examples/diligence-workflows.md](examples/diligence-workflows.md):

- **Data room analysis.** Thousands of documents, where the work is finding relevant signals, citing
  them, and drafting sections of an investment memo.
- **Credit deal review.** Every document tied to a credit deal — credit agreements, amendments, side
  letters running hundreds of dense technical pages — with the complete covenant package, financial
  terms, and operating restrictions extracted from that unstructured mass.

The credit example shows the progression the post describes. With earlier Sonnet and Opus models,
Matrix could already extract and synthesize covenants — the dense protections lenders write for
themselves. With Claude Fable 5, Hebbia is pursuing the complete job: multi-step analysis on top of
those covenants, comparison against live monitoring data, risk flagging, and first-draft covenant
reviews and internal memos. That review work traditionally required credit firms to pay outside teams
substantial sums for hand-produced analysis.

## Source

[Working at the frontier: How Hebbia builds AI for financial diligence that can't miss a detail](https://claude.com/blog/working-at-the-frontier-how-hebbia-builds-ai-for-financial-diligence-that-cant-miss-a-detail) — Claude blog, July 13, 2026.
