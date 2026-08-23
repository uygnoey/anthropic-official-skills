# Diligence workflows from the Hebbia post

Three concrete jobs the post describes, laid out as steps. Only the details the post states are
included; nothing here is invented to fill out a workflow.

## 1. Data room analysis

**Setup.** A data room with thousands of documents.

**The work.** Finding relevant signals, citing them, and drafting sections of an investment memo.

**Grid shape.** One row per document, one column per diligence question, one citation per cell. Memo
sections are drafted from the cells rather than from a fresh pass over the corpus, so every sentence in
the draft traces back to a cell and every cell traces back to a document.

## 2. Credit deal covenant review

**Setup.** Every document tied to a credit deal — credit agreements, amendments, side letters, running
hundreds of dense technical pages.

**The extraction.** From that unstructured mass, pull:

- the complete covenant package,
- the financial terms,
- the operating restrictions.

Covenants are the dense protections lenders write for themselves. Extracting and synthesizing them was
already possible on Matrix with earlier Sonnet and Opus models.

**The complete job.** With Claude Fable 5, Hebbia is pursuing the whole thing rather than the
extraction alone:

1. Extract the covenant package, financial terms, and operating restrictions.
2. Run multi-step analysis on top of those covenants.
3. Compare against live monitoring data.
4. Flag risks.
5. Produce first-draft covenant reviews and internal memos.

**Why it matters.** This review work traditionally required credit firms to pay outside teams
substantial sums for hand-produced analysis.

As Mehta puts it about documents of this kind: "These are actually the types of documents that
Anthropic models have always done really well at."

## 3. The pitch deck job, codified

The post uses this one to show what changes when a job is decomposed and codified rather than done by
hand each time.

| Stage | Time to produce a pitch deck for a CEO |
| --- | --- |
| Historically | A junior banker spends 2–3 days learning the company, pulling financials, and building slides |
| Pre-Opus | Compressed by 12–24 hours |
| Earlier Opus models on Hebbia | Approximately one day, end to end |
| Codified as a Matrix | A couple of minutes |
| Claude Fable 5 | Tightens this further |

The codified version gathers data across sources through deterministic agentic steps, conducts the
analysis, and builds the final decks, financial models, and internal research. What the bankers do
instead is identify buyers and work out positioning strategies.

The measure that matters at this point, per the post, is specialist hours replaced — the comparison
shifts once models can carry work end to end.

## What customers now ask for

Mehta describes the shift in customer conversations:

> "Two or three years ago the questions were defensive, about hallucinations and whether the math was
> right. Today, those conversations have changed completely. They're: how can I automate more of my
> workflow? How do I sequence more steps together? How can I generate ten, fifteen, twenty slide decks
> in one click with high fidelity and consistency?"

## Source

[Working at the frontier: How Hebbia builds AI for financial diligence that can't miss a detail](https://claude.com/blog/working-at-the-frontier-how-hebbia-builds-ai-for-financial-diligence-that-cant-miss-a-detail) — Claude blog, July 13, 2026.
