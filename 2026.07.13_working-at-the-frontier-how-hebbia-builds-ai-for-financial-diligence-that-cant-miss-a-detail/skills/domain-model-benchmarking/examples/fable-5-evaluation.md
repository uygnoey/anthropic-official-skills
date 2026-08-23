# The Claude Fable 5 evaluation at Hebbia

The run as the post reports it.

## Result

Claude Fable 5 cleared both tests by the widest margin Joe Renner had measured.

### Test 1 — Question answering and citation finding over financial documents

- **Approximately 20% relative accuracy gain** over financial documents — the best performance Renner
  had recorded from any new model.
- **Citation matching held roughly steady.**

Renner attributes the accuracy gain to the model better understanding the evidence it identifies. The
model was not finding materially different evidence; it was reading what it found better.

Mehta's framing of why this is the whole game:

> "It comes down to two seemingly fundamental qualities: the ability to find the right information from
> a dense data set, and then synthesize it correctly."

### Test 2 — Agent run through the chat product's tools

The model held every component of multi-part requests simultaneously, answered all of them, and cited
each answer back to its source.

### Open-ended analysis

The model reasoned from a broader cross-section of data and reached conclusions the team found worthy
of closer examination.

Renner attributes this wider reach to how the model maintains **long task coherence**:

- keeping every part of a request in view,
- prompting its own sub-agents and tools to retrieve relevant facts,
- grounding each claim in its source rather than inferring it.

## What the team did with the result

The evaluation is what licensed a change in ambition rather than a swap of model names.

With earlier Sonnet and Opus models, Matrix could already extract and synthesize credit agreement
covenants. With Claude Fable 5, Hebbia is pursuing the complete job: multi-step analysis on top of those
covenants, comparison against live monitoring data, risk flagging, and first-draft covenant reviews and
internal memos.

Alongside that, Hebbia is adopting the Claude Agent SDK to compose these jobs as smaller, repeatable,
verified steps rather than single model runs — because firms require control over which documents feed
the analysis and how each step is constructed, no matter how brilliant the model is.

## The standing bar

> "The bar is extremely high, and our customers hold us to that extremely high bar — and rightfully so."
> — Divya Mehta

## Source

[Working at the frontier: How Hebbia builds AI for financial diligence that can't miss a detail](https://claude.com/blog/working-at-the-frontier-how-hebbia-builds-ai-for-financial-diligence-that-cant-miss-a-detail) — Claude blog, July 13, 2026.
