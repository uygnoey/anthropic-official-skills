**English** · [한국어](./analyzing-dense-document-sets.ko.md) · [Español](./analyzing-dense-document-sets.es.md) · [日本語](./analyzing-dense-document-sets.ja.md)

# How Hebbia analyzes dense document sets without missing a detail

Hebbia is an AI platform serving more than a third of the top 50 asset managers, alongside tier-1
investment banks and law firms. Its customers make decisions based on analyses spanning thousands of
dense documents, where accuracy is critical.

Divya Mehta, the company's founding product manager, works extensively with major investment banking,
private equity, and credit customers. Adithya Ramanathan leads the applied AI research team, focused on
finding signals by getting models to draw on the right data, in the right context, surfacing what
customers need to know.

## The problem

Bankers and investors weighing opportunities have to work through all the relevant data: public
filings, credit agreements, internal documents, and structured data from CRMs. The information that
gives them a competitive advantage typically sits in unstructured, proprietary documents — historically
harder to analyze at scale than the structured, quantitative data finance already models effectively.

Hebbia built Matrix to systematize that qualitative work, and each model generation has expanded what
it can do.

## How Matrix works

Hebbia's meta-prompting converts plain-language requests into prompts, with Claude analyzing each step
across hundreds of documents. Answers appear in individual cells on a grid in Matrix, which is what
gives the analysis full transparency, traceability, and steerability.

Ramanathan's framing of the objective:

> "When you're connecting it to the right data and putting it in the right ecosystem, that's when you
> get the alpha that finance professionals actually chase."

## How new models get evaluated

The team runs every new model through Hebbia's finance-specific benchmark, comparing head-to-head
against the model it would replace, and expands the benchmark's measurements with each release.

Mehta on the standard: "The bar is extremely high, and our customers hold us to that extremely high
bar — and rightfully so."

Joe Renner, a researcher on the applied AI team, tests each new Claude model against the benchmark,
replicating key finance knowledge worker use cases. Two tests do the work:

1. **Question answering and citation finding** over financial documents.
2. **A run through Hebbia's agent system** with the chat product's tools, simulating open-ended,
   multi-source analysis.

Claude Fable 5 cleared both by the widest margin Renner had measured.

On the question-answering and citation test, it achieved approximately a 20% relative accuracy gain
over financial documents — the best performance Renner had recorded from any new model. Citation
matching held roughly steady; Renner attributes the gain to the model better understanding the evidence
it identifies.

Mehta reduces the job to two qualities:

> "It comes down to two seemingly fundamental qualities: the ability to find the right information from
> a dense data set, and then synthesize it correctly."

On the agent run, the model held every component of multi-part requests simultaneously, answering all
of them and citing each answer back to its source.

It also showed wider reach. On open-ended analysis, it reasoned from a broader cross-section of data
and reached conclusions the team found worthy of closer examination. Renner attributes this to how the
model maintains long task coherence: keeping every part of a request in view, prompting its own
sub-agents and tools to retrieve relevant facts, and grounding each claim in its source rather than
inferring it.

## What this makes possible

**Data rooms.** Thousands of documents where the work is finding relevant signals, citing them, and
drafting sections of an investment memo.

**Credit deals.** Every document tied to a deal — credit agreements, amendments, side letters running
hundreds of dense technical pages — with the complete covenant package, financial terms, and operating
restrictions extracted from that unstructured mass.

Mehta on this class of material: "These are actually the types of documents that Anthropic models have
always done really well at."

With earlier Sonnet and Opus models, Matrix could already extract and synthesize credit agreement
covenants — the dense protections lenders write for themselves. With Claude Fable 5, Hebbia is pursuing
the complete job: multi-step analysis on top of those covenants, comparison against live monitoring
data, risk flagging, and first-draft covenant reviews and internal memos. That review work traditionally
required credit firms to pay outside teams substantial sums for hand-produced analysis.

## The measure that replaced the old one

With models capable of carrying work end to end, the comparison focuses on specialist hours replaced.

Historically, when a managing director needed a pitch deck for a CEO, a junior banker would spend two
to three days learning the company, pulling financials, and building slides. In pre-Opus days, that
timeline compressed by 12 to 24 hours. With earlier Opus models on Hebbia, Mehta indicates it dropped
to approximately one day end to end. Hebbia then codified the entire job into a Matrix that gathers
data across sources through deterministic agentic steps, conducts the analysis, and builds the final
decks, financial models, and internal research — in a couple of minutes. Bankers spend their time
identifying buyers and working out positioning instead. Claude Fable 5 tightens this further.

## Why decomposition survives capable models

Decomposing work into steps remains important "no matter how brilliant the model is," because firms
require control over which documents feed the analysis and how each step is constructed. Hebbia is
adopting the Claude Agent SDK to compose these jobs as smaller, repeatable, verified steps rather than
single model runs.

## What customers ask for now

> "Two or three years ago the questions were defensive, about hallucinations and whether the math was
> right. Today, those conversations have changed completely. They're: how can I automate more of my
> workflow? How do I sequence more steps together? How can I generate ten, fifteen, twenty slide decks
> in one click with high fidelity and consistency?" — Divya Mehta

## Source

[Working at the frontier: How Hebbia builds AI for financial diligence that can't miss a detail](https://claude.com/blog/working-at-the-frontier-how-hebbia-builds-ai-for-financial-diligence-that-cant-miss-a-detail) — Claude blog, July 13, 2026.
