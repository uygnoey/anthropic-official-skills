**English** · [한국어](./evaluating-frontier-coding-models.ko.md) · [Español](./evaluating-frontier-coding-models.es.md) · [日本語](./evaluating-frontier-coding-models.ja.md)

# Evaluating frontier coding models the way Cursor does

Cursor is an AI coding agent for building professional software. It supports every major frontier
model alongside its own, which makes the company an unusually neutral judge of how each one actually
performs.

Nate Schmidt is the engineer who maintains that scorecard. He works on evals and model behavior at
Cursor: studying how models succeed, how they fail, and what makes a developer quietly switch away
from one mid-task. When colleagues and customers want a read on a new release, they come to him.

## Why they built their own benchmark

Over time, Schmidt's team noticed that public benchmark scores and real developer reception had
stopped lining up. So they built CursorBench — an internal eval designed to capture the messy,
underspecified ways engineers actually prompt their models.

> "Many evals look like this: here's a well-defined problem, here are the constraints, go fix it. But
> the prompts we get from real users don't really look like that. The model has to infer that the user
> has a problem and what they're trying to convey, identify the root cause, fix it, validate the fix,
> and report back."

Two of its tasks show what that means in practice. One is just a stack trace pasted in with the single
word "fix" — the model has to infer the intent, find the root cause, and validate the change on its
own. Another tells the model the wrong module is broken, to see whether it challenges the user's
assumption or follows it into a dead end.

What gets scored is not the diff. As the post puts it: the right answer is table stakes; what they are
scoring is whether the model understood what it was being asked.

## Verify a surprising score by reading the traces

Claude Fable 5 scored 72.9% at Max effort on CursorBench, setting a new high. The Cursor team's first
reaction was not celebration.

> "One of two things is happening: either the model's very smart, or the model is cheating."

So they read the traces — the model's actual reasoning on the hardest tasks, the ones where the prompt
looks simple but cracking it requires understanding the whole system.

> "We just kept seeing the model dig out wins that no other model was doing previously."

It was also getting there with fewer operations: token-efficient relative to the work it completed.

The transferable practice is the check itself. A number you have not investigated is not yet a result,
and the way to investigate it is to read what the model actually reasoned on the tasks that separate
models.

## Local reasoning and global reasoning

Schmidt's second test was personal rather than institutional: a programmable space-flight simulator
and a one-line prompt — build a rocket and land it on the moon.

He had run it weeks earlier with Claude Opus, left on a second monitor for twelve to sixteen hours.
The model would launch, run out of fuel in orbit, add a lot more fuel, then fail to clear the
atmosphere because the rocket was now too heavy. Every step in that loop is a locally reasonable
response to the step before it.

He re-ran the experiment with the same blank-slate prompt using Claude Fable 5. A few minutes in, the
rocket went up, parked in low orbit, and came back down — apparently the same failure. Then he read
the transcript.

> "Fable decided it wouldn't go to the moon on its first attempt. It wanted to do an initial mission
> just to go into orbit and collect telemetry, then use that to inform the next trip."

A few attempts later the engine noise stopped, and there was a lander on the moon. The whole run took
a couple of hours, against Opus's twelve-plus with no result.

> "With Opus, it was doing local reasoning — thinking about what just happened and what's immediately
> about to happen. With Fable it's global reasoning. It's thinking about the entire mission."

Note what would have happened if only the outcome of the first orbit had been scored: two identical
failures. The difference lived in the plan.

## When to reach for the global optimum

Schmidt's rule for choosing a model is short enough to apply without deliberating:

> "If you have a good sense of what the path from A to B looks like, you might not need Fable. If
> you're at A and you have no idea where B is, Fable is an excellent choice. When I want to build
> something the right way, Fable is the first model I think of."

Three consequences follow.

**The backlog changes category.** Fable has let his team take on projects they had shelved — rewrites
everyone agreed would be better but nobody could justify spending weeks on — because the model can
carry enough of the skeleton. "It lowers the activation energy to work on these types of tasks. It
lets us move in search of a global optimum rather than a local one."

**Coordination overhead can be delegated.** Cursor runs lean, with intense individual ownership and
few standups. Before touching shared code, Schmidt has an agent read his teammate's recent commits and
flag conflicts, so neither of them has to stop what they are doing to check in.

**Mix models rather than standardizing on one.** To balance cost and performance, his team pairs
Claude Fable 5 with faster, lighter models for routine work and brings it in for the problems where
capability is the constraint. In that configuration, he says, the combination is the most effective
setup they have run.

> "If I'm getting into a really gnarly problem — the p99 of problems — the thing I'm trying to
> optimize for is time to solution. And I think Fable is the best model for solving our hardest
> problems."

Schmidt also describes what he stopped having to do: the constant babysitting — reminding the model of
context, spelling out the solution, auditing the results. "I don't feel like I have to bootstrap
Claude Fable 5 to understand the world I exist in and the problem I'm trying to solve. The model just
has a sense of it out-of-the-box."

## What's next at Cursor

Schmidt is still looking for the model's limits. Next he wants to see how long it can manage a
back-end system unattended; days-to-weeks runs are his next experiment. Inside Cursor, the team is
using the model to hunt performance bottlenecks and user pain points proactively rather than waiting
for reports, and to build the more sophisticated, closer-to-reality eval environments that will
measure whatever comes next.

> "There's a class of problems people weren't even thinking about because it didn't seem approachable.
> With Fable, I'm excited to push at that."

## Source

[Working at the frontier: How Cursor knew Claude Fable 5 was ready for the hardest 1% of problems](https://claude.com/blog/working-at-the-frontier-cursor) — Claude blog, July 17, 2026.
