**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# How Warp builds self-improving agents on Claude

## What is this post?

A customer engineering story. Warp — the AI-powered terminal and agentic development environment —
found that agents running at 80% accuracy produce a "noisy and annoying" experience, and that
hand-rewriting prompts and context files like `AGENTS.md` doesn't scale as a fix. The underlying
problem is that human feedback disappears when a session ends.

Their answer is a two-skill loop: a base (inner) skill that does the work, and an improver (outer)
skill that runs on a schedule, reads accumulated human feedback, and proposes small edits to the
base skill as ordinary pull requests. The post covers how to write skills for that loop, walks
through Warp's issue triage agent as a worked example, and closes with the questions to answer
before scaling the pattern.

## When is it useful?

- An agent of yours is mostly right but noisy, and you are rewriting its prompt by hand every week.
- You have feedback from engineers on agent output but no mechanism that turns it into a change.
- You are deciding how many improver loops to run — one per agent, or one shared template.
- You need to guard against the agent acting on feedback that is simply wrong.
- You want to know whether your domain supports a verification harness, and what to do if it
  doesn't.

## Key points

- **Feedback disappearing at session end is the real bug.** Manually rewriting prompts and
  improving `AGENTS.md` doesn't scale, because it treats the symptom.
- **Inner / base skill.** Holds the functional domain knowledge and instructions, and runs on the
  task — for code review, when a PR opens.
- **Outer / improver skill.** An observer running on a schedule, not per task. It pulls accumulated
  human feedback, compares agent suggestions against human responses, and proposes small, focused
  edits to the base skill.
- **Skills are plain files, so updates are PRs.** Agents propose changes through reviewable,
  approvable, mergeable workflows, which keeps humans in control of actual system changes.
- **Write principles, not rules; explain the why.** Instruct a smart person rather than program a
  computer. Rationale lets the agent reason about new situations, which improves generalization.
- **Make feedback effortless.** Capture it where people already work — PR and issue comments —
  automatically. "Low friction is what keeps signal flowing."
- **Explicit feedback beats affirmation.** "This was a good, useful comment" is weaker than a
  stated convention and the reason behind it.
- **Quality exceeds volume, but volume helps.** A small sample of detailed, domain-specific feedback
  from senior engineers carries signal the agent had no other way of getting.
- **Over-invest in the improver skill.** It is highly reusable across use cases.
- **The worked example.** Warp's issue triage agent missed a `ready to spec` label; a maintainer
  explained why on the issue; the scheduled improver pulled recent feedback with a bundled Python
  script, summarized it to JSON, and proposed the smallest edit — apply `ready to spec` when an
  issue describes a real problem despite undefined UI/UX details — which shipped as a reviewed PR.
- **Before scaling, answer six questions.** Skills vs memory, one improver or many, what to do when
  feedback is wrong, whether the domain is verifiable, what to fall back on when it isn't, and which
  global metrics tell you the whole system is improving.

## Bundled resources

- `skills/self-improving-skill-loops/SKILL.md` — build a base skill plus a scheduled improver skill
  that edits it from human feedback.
- `skills/self-improving-skill-loops/references/authoring-principles.md` — the writing guidance from
  the post, in full.
- `skills/self-improving-skill-loops/references/rollout-questions.md` — the six best-practice
  questions and their answers.
- `skills/self-improving-skill-loops/templates/improver-skill.md` — a fill-in scaffold for the outer
  skill.
- `skills/self-improving-skill-loops/scripts/collect_feedback.py` — reference implementation of the
  feedback-collection step, emitting JSON.
- `skills/self-improving-skill-loops/examples/issue-triage-loop.md` — the triage loop, step by step.
- `agents/skill-improver.md` — the scheduled observer agent.
- `agents/issue-triage.md` — the base triage agent it improves.
- `guides/self-improving-agent-loops.{en,ko,es,ja}.md` — the full method in four languages.

## Source

- https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude (published 2026-08-26)
