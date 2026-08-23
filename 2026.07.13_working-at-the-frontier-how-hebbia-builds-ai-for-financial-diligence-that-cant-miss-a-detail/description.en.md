**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Hebbia is an AI platform used by more than a third of the top 50 asset managers, alongside tier-1 investment banks and law firms. Its customers decide from analyses spanning thousands of dense documents, where accuracy is critical. This post is an account from three people who build that system — founding product manager Divya Mehta, applied AI research lead Adithya Ramanathan, and researcher Joe Renner — of how they hold the line on accuracy and how they decided Claude Fable 5 was ready.

Two threads run through it. The first is Matrix, Hebbia's product for systematizing qualitative work: meta-prompting converts a plain-language request into prompts, the model analyzes each step across hundreds of documents, and answers land in individual cells on a grid — which is what makes the whole thing transparent, traceable, and steerable. The second is the finance-specific benchmark every new model is run through, head-to-head against the model it would replace.

## When is it useful?
- When analysis has to run over thousands of dense, unstructured documents and a missed detail is a real cost.
- When deciding whether a new model is worth adopting, and public scores are not the evidence you need.
- When building an internal benchmark for a domain where the accuracy bar is set by customers.
- When a benchmark number jumps and you need to know which half of the job actually improved.
- When choosing between one long model run and a decomposed, step-by-step pipeline.
- When turning a multi-day expert workflow into something repeatable.

## Key points
- **The alpha is in the connection, not the model alone.** "When you're connecting it to the right data and putting it in the right ecosystem, that's when you get the alpha that finance professionals actually chase." — Adithya Ramanathan
- **Cells, not one long answer.** Answers appear in individual cells on a grid in Matrix, which is what gives the analysis full transparency, traceability, and steerability.
- **Meta-prompting does the decomposition.** Plain-language requests become prompts; Claude analyzes each step across hundreds of documents.
- **Two qualities are the whole job.** "The ability to find the right information from a dense data set, and then synthesize it correctly." — Divya Mehta
- **Every model runs head-to-head against the one it would replace,** on a finance-specific benchmark whose measurements expand with each release.
- **Two test shapes.** Question answering and citation finding over financial documents; and a run through the agent system with the chat product's tools, simulating open-ended multi-source analysis.
- **Fable 5 cleared both by the widest margin Renner had measured** — roughly a 20% relative accuracy gain on the question-answering test, the best he had recorded from any new model.
- **Citations held steady while accuracy moved.** Renner attributes the gain to the model better understanding the evidence it identifies — not to finding different evidence.
- **Multi-part requests were held whole.** Every component held simultaneously, all answered, each answer cited back to its source.
- **Long task coherence explains the wider reach:** keeping every part of a request in view, prompting its own sub-agents and tools for facts, and grounding each claim in its source rather than inferring it.
- **The credit-deal job is now the complete job.** Earlier models could extract and synthesize covenants; with Fable 5 Hebbia is pursuing multi-step analysis on top of them, comparison against live monitoring data, risk flagging, and first-draft covenant reviews and memos — work credit firms traditionally paid outside teams substantial sums to produce by hand.
- **The pitch deck timeline:** 2–3 junior-banker days historically → 12–24 hours faster pre-Opus → about one day with earlier Opus models → a couple of minutes once codified as a Matrix. Fable 5 tightens it further.
- **Decomposition survives better models.** It stays important "no matter how brilliant the model is," because firms require control over which documents feed the analysis and how each step is constructed. Hebbia is adopting the Claude Agent SDK to compose jobs as smaller, repeatable, verified steps.
- **Customer questions have flipped** from hallucinations and whether the math was right, to how much more of the workflow can be automated and sequenced.

## Bundled resources
- `skills/document-grounded-analysis/SKILL.md` — decompose the request, give each answer its own cell with a citation, hold every part of a multi-part request, ground claims rather than infer them.
- `skills/document-grounded-analysis/references/decomposition.md` — why decomposition outlives capable models, what the steps are made of, and what the post leaves unspecified.
- `skills/document-grounded-analysis/templates/analysis-grid.md` — the grid layout, a step record, and a retrieval-vs-synthesis check.
- `skills/document-grounded-analysis/examples/diligence-workflows.md` — data room analysis, the credit covenant review, and the codified pitch deck job.
- `skills/domain-model-benchmarking/SKILL.md` — build the benchmark from your domain, run two test shapes, compare head-to-head, read accuracy and citations as separate signals.
- `skills/domain-model-benchmarking/references/benchmark-shape.md` — everything the post states about the benchmark, and the questions it does not answer.
- `skills/domain-model-benchmarking/templates/model-eval-record.md` — a head-to-head record with separate retrieval and synthesis verdicts.
- `skills/domain-model-benchmarking/examples/fable-5-evaluation.md` — the Fable 5 run, its numbers, and what the team did with the result.
- `guides/analyzing-dense-document-sets.{en,ko,es,ja}.md` — the full account in four languages.

## Source
[Working at the frontier: How Hebbia builds AI for financial diligence that can't miss a detail](https://claude.com/blog/working-at-the-frontier-how-hebbia-builds-ai-for-financial-diligence-that-cant-miss-a-detail) — Claude blog, July 13, 2026.
