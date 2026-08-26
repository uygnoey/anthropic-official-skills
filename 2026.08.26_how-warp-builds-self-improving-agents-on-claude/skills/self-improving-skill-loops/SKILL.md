---
name: self-improving-skill-loops
description: Build agent skills that improve themselves from human feedback, using a base (inner) skill that does the work and an improver (outer) skill that runs on a schedule, reads accumulated feedback, and proposes small reviewable edits to the base skill. Use when an agent's output is roughly right but noisy, when feedback keeps getting lost at the end of a session, when hand-editing prompts or AGENTS.md no longer scales, or when deciding how many improver loops to run and how to guard against bad feedback.
---

# Self-improving skill loops

An agent that is right 80% of the time is noisy and annoying to work with, and the usual
fixes — rewriting the prompt by hand, adding more to a context file like `AGENTS.md` — do not
scale. The deeper problem is that feedback disappears when a session ends, so the context that
would fix the agent never re-enters the loop.

The pattern below, as described by Warp, closes that loop: keep the knowledge in files, capture
human feedback where people already work, and let a second agent turn that feedback into small
edits to the first agent's skill — through ordinary pull requests that a human approves.

## Instructions

### 1. Split the work into two skills

**Inner / base skill.** Holds the functional domain knowledge and instructions, and runs on the
task itself. For code review, this is what executes when a PR opens and produces the review.

**Outer / improver skill.** An observer that runs *on a schedule*, not per task. It pulls the
human feedback that has accumulated, compares what the agent suggested against how people
responded, and proposes small, focused edits to the base skill.

Because skills are plain files, the improver's proposals arrive as reviewable, approvable,
mergeable PRs. The agent never changes the running system on its own.

### 2. Write the base skill as principles, not rules

Construct the skill as though you are instructing a smart person, not programming a computer.
"Look for repeated code" gives better direction than an exhaustive set of variable-naming rules.
Always explain the *why* behind a rule — rationale lets the agent reason about a new situation
instead of pattern-matching an instruction, which is what makes it generalize.

Keep the skill file small and use progressive disclosure: reference resource files and scripts
rather than dumping everything into context at once. Full authoring guidance is in
[references/authoring-principles.md](references/authoring-principles.md).

### 3. Make feedback effortless to give

Capture feedback where people already work — as direct comments on the PR or the issue — and
collect it automatically, with no extra submission step.

> Low friction is what keeps signal flowing. If you make it too hard you're not going to get the
> feedback and you're not going to be able to improve the skill.

Explicit feedback works best. A human affirming "this was a good, useful comment" is worth
something, but a detailed reason — "our code base convention is this type of global variable
uses this particular naming context" — tells the agent how to improve.

Quality beats volume: detailed, domain-specific feedback from a senior engineer outweighs a pile
of cursory reactions. A small sample can carry very good signal when it is domain knowledge the
agent had no other way of getting. Volume still helps.

### 4. Build the improver skill, and over-invest in it

Put extra effort here — improver skills are highly reusable across use cases, so the investment
pays off repeatedly. A run should:

1. Authenticate to the system holding the feedback.
2. Run a bundled script to pull the recent items that carry feedback — see
   [scripts/collect_feedback.py](scripts/collect_feedback.py).
3. Summarize the findings into JSON and identify concrete signals.
4. Propose the *smallest* edit to the base skill that captures the feedback.
5. Open a PR explaining which signals prompted which change.

Start from [templates/improver-skill.md](templates/improver-skill.md).

### 5. Keep humans in control of the merge

The proposed update moves through standard code review. A human reads the explanation, approves
or rejects, and only then does the change become inherited knowledge for the next run of the
base skill. This is the step that keeps humans in control of actual system changes.

### 6. Assume some feedback is wrong

Do not let the agent accept feedback blindly. Give it enough context to sanity-check what it
reads, filter whose input counts, and keep a human in the loop at the filtering stage, the
final-review stage, or both.

### 7. Answer the deployment questions before scaling

How many improver loops, whether your domain is verifiable, what to do when it is not, and how
to tell whether the whole system is improving — these are covered in
[references/rollout-questions.md](references/rollout-questions.md).

## Examples

### A code review agent producing unhelpful comments

Engineers report that the review agent leaves low-quality comments. Rather than rewriting the
prompt by hand, add an improver loop: engineers reply to the agent's PR comments explaining what
was wrong and why, and a scheduled improver reads those replies and proposes a narrow edit to
the review skill.

### An issue triage agent missing a label

Warp's issue triage agent runs from a GitHub Action when someone files an issue: it analyzes
complexity and feasibility, assigns labels, and suggests a fix direction. On one issue it did
well but missed the `ready to spec` label, which signals that contributors can build product and
technical specs from the issue. A maintainer left feedback on the issue explaining both the
expectation and the rationale.

The improver skill, running on a schedule, pulled recent issues with feedback, summarized them
into JSON, and proposed the smallest edit that captured the signal: apply `ready to spec` when an
issue describes a real problem even though the UI/UX details are undefined. The PR was reviewed,
approved, and merged — and the next triage run inherited it.

Walked through step by step in [examples/issue-triage-loop.md](examples/issue-triage-loop.md).

### Several agents in one repository

Warp runs this pattern across its open-source repo with separate spec-writing, review, and triage
agents, each carrying its own self-improvement loop. With a handful of agents, each can own an
improver; at a hundred, they should share a templated base loop with domain-specific weights
layered on top.

## Source

- https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude (published 2026-08-26)
