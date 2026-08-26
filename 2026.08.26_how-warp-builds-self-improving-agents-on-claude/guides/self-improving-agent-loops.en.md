**English** · [한국어](./self-improving-agent-loops.ko.md) · [Español](./self-improving-agent-loops.es.md) · [日本語](./self-improving-agent-loops.ja.md)

# Self-improving agent loops: how Warp does it

## The problem

Warp — the AI-powered terminal and agentic development environment — found that agents executing
tasks at 80% accuracy create a "noisy and annoying" user experience. The team hit this with their
own internal code review agent: engineers reported unhelpful comments and low-quality output.

The obvious fixes did not scale. Manually rewriting prompts and improving context files like
`AGENTS.md` is work that never ends. The real issue sits one level down: **feedback typically
disappears when sessions end**, which removes essential context from the agentic loop.

## The framework

Warp's solution is built on **skills** — file-based encodings of knowledge — with two components
plus the humans in between.

### Inner / base skill

Holds the functional domain knowledge and instructions. For code review, it executes when a PR
opens and produces the review.

### Human feedback

The critical ingredient. Explicit feedback works best: explaining not just what was wrong, but
*why*. As Zach Lloyd, Warp's CEO, puts it — a human could affirm "this was a good, useful
comment," but detailed reasons like "our code base convention is this type of global variable uses
this particular naming context" tell the agent how to improve.

### Outer / improver skill

An observer agent that runs **on a schedule**, not per task. It pulls the accumulated human
feedback, compares the agent's suggestions against the human responses, and proposes small,
focused edits to the base skill.

Because skills are plain files, agents effectively update them through reviewable, approvable,
mergeable PR workflows. Nothing changes in the running system without a human merge.

## How to write self-improving skills

- **Write principles, not rules.** Instruct a smart person, don't program a computer. "Look for
  repeated code" beats an exhaustive variable-naming rulebook.
- **Explain the why.** Rationale lets the agent reason about problems instead of following rigid
  instructions, which improves generalization.
- **Make feedback effortless to give.** Capture it where people already work — direct PR or issue
  comments — automatically, with no extra submission step. Low friction is what keeps signal
  flowing; make it hard and the feedback stops, and so does the improvement.
- **Keep skills small and use progressive disclosure.** Good skill files reference resource files
  and scripts rather than dumping everything into context at once.
- **Feedback quality exceeds volume, but volume helps.** Detailed, domain-specific feedback from
  senior engineers outweighs cursory feedback. Even a small sample gives good signal when it
  carries domain knowledge the agent had no other way of getting.
- **Put extra effort into the improver skill.** It pays dividends, because improver skills are
  highly reusable across use cases.

## The loop in action: issue triage

Warp's [issue triage agent](https://github.com/warpdotdev/warp-agents-demo-github-issue-triage)
demonstrates the framework end to end.

1. Someone files a GitHub issue. A GitHub Action triggers the agent, which analyzes complexity and
   feasibility, assigns labels, and suggests a fix direction.
2. On a sample issue the inner skill performed well but missed the `ready to spec` label — the one
   signaling that contributors can build product and technical specs.
3. A maintainer left feedback directly on the issue, explaining both the expectation and the
   rationale.
4. The outer improver skill, running in Warp's orchestration platform Oz as a scheduled "update
   triage" agent, authenticated to GitHub, ran a bundled Python script to pull recent issues with
   feedback, summarized the findings into JSON, and identified concrete signals.
5. It proposed the smallest edit capturing the feedback: apply `ready to spec` when an issue
   describes a real problem despite undefined UI/UX details.
6. The update moved through standard code review. The PR explained which signals prompted which
   changes. After human approval, the merged change became inherited knowledge for the next triage
   run.

Warp now runs this pattern across its open-source repo with separate spec-writing, review, and
triage agents, each carrying its own self-improvement loop.

## Questions to answer before you scale

**Are you conflating skills with memory?** Skills are procedural and stable — "how to do X,"
run-agnostic, deliberately changed. Memory is auto-written by agents at inference time and
constantly changes.

**One improver loop, or one per agent?** Meet in the middle: a templated base loop captures the
overlap across agents, with domain-specific weights layered on. A handful of agents can each own
an improver; a hundred should share.

**What happens when the feedback is wrong?** Assume it will be. Don't let agents accept feedback
blindly — give them context to sanity-check it, filter whose input counts, and keep humans in the
loop at the filtering or final-review stages.

**Is your domain verifiable?** Build the verification harness first, then let the agent tune
against it: generate a reference corpus, compare output to reference, fix, repeat.

**And if it isn't verifiable?** Lean on deterministic evals against golden outputs wherever they
exist. Where human feedback is necessary, restrict it to domain experts — don't open the
floodgates.

**How do you know the whole system is improving?** Track the global metrics humans already
monitor — time to merge, contributor count, cost — and feed them back into the improver agents.
Progress gradually from crawl to walk to run on deployment.

## About Warp

Founded in 2020 by CEO Zach Lloyd. Stack: Rust, Golang, GitHub Actions, an internal agent
orchestration platform called Oz, and the Claude Platform. $73M raised, 800K monthly developers,
56% of the Fortune 500, 10M Claude Code sessions run inside Warp to date (400K+ per week), and 40M
total Warp Agent conversations.

## Source

- https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude (published 2026-08-26,
  by Michael Segner)
