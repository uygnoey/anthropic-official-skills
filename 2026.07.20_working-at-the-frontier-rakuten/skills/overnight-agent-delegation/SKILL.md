---
name: overnight-agent-delegation
description: Hand an agent a whole task instead of a pre-chunked sequence, and let it run unattended for hours or a full day — because the model re-checks its own assumptions mid-run, returns to first principles at each step, and carries memory of past failures between runs. Use when deciding how large a unit of work to delegate, when a long agentic run keeps failing on an early wrong turn, when setting up agents to run overnight without a human checking in, or when the number of tasks is rising faster than the human judgment available to review them.
---

# Delegating whole tasks to agents that run unattended

Yusuke Kaji, General Manager of AI for Business at Rakuten, has tested Claude models since September
2024 — across nearly a dozen model launches — and describes Claude Fable 5 as a step change for
long-running enterprise agents. The change he points to is not raw speed. It is that the model checks
its own work as it goes, which is what makes an unattended multi-hour run worth starting.

This skill describes the delegation pattern as the post presents it.

## Instructions

### 1. Understand why long runs used to fail

Before Fable 5, setting an agent loose on a multi-hour task without human oversight was a gamble. Kaji
describes the failure directly: "If they choose the right path in the first step, everything is fine.
But if they choose the wrong direction in the first pass, the agent spends significant time to fix the
path, or even fails to reach the destination."

On a job meant to run five hours or a full day, one early wrong assumption could burn the entire run,
and the only way to catch it was a person checking in.

The failure mode was a lack of self-verification. Any model can take a wrong first step. The problem
with earlier models was that they did not check their own work as they went, so an early wrong turn
went unnoticed, compounded over the run, and produced a suboptimal result hours later.

### 2. Check for the three behaviors that make an unattended run viable

Kaji's team cite three behaviors that distinguish Claude Fable 5 from its predecessors. Before you
extend a run's length, confirm the model actually does these things on your work:

- **It re-checks its own assumptions.** When the state of the task changes midway, it notices and
  corrects a wrong assumption before acting on it, rather than committing to a bad path and
  discovering it hours later.
- **It returns to first principles at each step.** It re-validates against the original intent without
  being told — the course-correction Kaji used to have to make himself.
- **It matches the team's taste.** Even with minimal guidance, its judgment on ambiguous calls lines up
  with theirs. Kaji coined a term for this: *taste alignment*.

The full description of each behavior, and what the post does and does not specify about it, is in
[references/self-verification-behaviors.md](references/self-verification-behaviors.md).

### 3. Raise the unit of work from the chunk to the whole task

"Before Fable, we had to break work into well-defined chunks for the agent to execute," Kaji says. Now
he can hand over a whole task and run several at once.

This is the practical shift. Stop decomposing the job for the agent as a defensive measure against
early wrong turns, and hand it the outcome instead. The corollary is that you can run several such
tasks in parallel, because none of them needs you watching it.

Brief the task with [templates/stretch-task-brief.md](templates/stretch-task-brief.md).

### 4. Prepare stretch tasks deliberately when a new model arrives

Kaji likens testing a new model to embarking on a "new quest," and describes a deliberate practice:
"The way a good leader prepares stretch goals for their people, we prepare stretch tasks for a new
Claude. Maybe Claude is nudging us to stretch, too."

Keep a standing set of tasks that the current model cannot reliably finish, and point each new model
at them. That is how you find out whether the unit of work you can delegate has grown.

### 5. Give agents memory across runs

"Our agents with memory remember what went wrong in past sessions and avoid repeating those mistakes."

Memory between runs is part of what makes long autonomy compound rather than repeat. A run that fails
in a particular way should make the next run less likely to fail that way.

### 6. Expect human judgment to become the constraint

Rakuten's agents close issues roughly 10x faster across every domain, and the number of tasks the
organization takes on keeps rising. Adding more agents does not add judgment. The faster the agents
run, the more the organization's progress depends on a person closing the loop.

Because the model self-corrects mid-run, sign-off becomes feasible for the first time, and the unit of
work delegated shifts from the task to the decision. The absolute number of tasks keeps climbing, but
the ones that truly need a human stay at a focusable level.

Kaji names not having to jump in and steer mid-run as the biggest productivity win of all: it lets his
team spend its time on the decisions only people should make, and keeps an AI-native organization
accelerating instead of stalling on human course-correction.

## Examples

The Rakuten runs as the post reports them — the overnight job, the parallel whole-task delegation, and
the 2 a.m. self-correction — are in [examples/rakuten-agent-runs.md](examples/rakuten-agent-runs.md).

The line Kaji uses to describe the difference:

> "We tested Fable, and we love its capability for self-reflection and self-verification. Compared with
> previous models, it understands its mistake before I point it out at 2 a.m. or 3 a.m. — so that I can
> sleep."

## Source

[Working at the frontier: How Rakuten builds agents overnight with Claude Fable 5](https://claude.com/blog/working-at-the-frontier-rakuten) — Claude blog, July 20, 2026.
