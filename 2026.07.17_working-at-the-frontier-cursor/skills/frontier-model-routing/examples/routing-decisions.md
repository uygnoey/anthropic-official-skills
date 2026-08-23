# Routing decisions, worked through

Three decisions from the source post, with the reasoning that produced them.

---

## 1. The moon landing — path completely unknown

**Setup.** A programmable space-flight simulator, wired to a model, with a one-line blank-slate
prompt: *build a rocket and land it on the moon.* No constraints, no intermediate goals, no scoring
function beyond the outcome.

**Run A — previous-generation model.** Left running on a second monitor for twelve to sixteen hours.
The behavior was a loop:

1. Launch.
2. Run out of fuel in orbit.
3. Add a lot more fuel.
4. Fail to clear the atmosphere, because the rocket was now too heavy.

Each step is a locally correct response to the step before it. Nothing in the loop is a reasoning
error at the level of a single decision. There was no result at the end of the run.

**Run B — frontier model, same blank-slate prompt.** A few minutes in, the rocket went up, parked in
low orbit, and came back down. The same failure, apparently. Then Schmidt read the transcript:

> "Fable decided it wouldn't go to the moon on its first attempt. It wanted to do an initial mission
> just to go into orbit and collect telemetry, then use that to inform the next trip."

A few attempts later the engine noise stopped and there was a lander on the moon. The whole run took a
couple of hours, against twelve-plus with no result.

**Routing lesson.** The task had no known path — that is the whole point of a blank-slate prompt into
a simulator. Reading only the outcome of the first orbit would have scored Run B as the same failure
as Run A. The difference was in the plan, not the first result. When you are at A with no idea where B
is, the frontier model is the choice, and you have to read the reasoning to see why.

---

## 2. The shelved rewrite — path unknown, and previously unaffordable

**Setup.** Rewrites everyone on the team agreed would be better, but that nobody could justify
spending weeks on. Classic backlog residue: rejected on effort, not on merit.

**Decision.** Route to the frontier model, because it can carry enough of the skeleton to make
starting cheap.

> "It lowers the activation energy to work on these types of tasks. It lets us move in search of a
> global optimum rather than a local one."

**Routing lesson.** Adopting a more capable model is not only a per-task decision. Go back through the
work you declined and check which items were declined for a reason that no longer holds.

---

## 3. Coordinating on shared code — path fully known

**Setup.** Cursor runs lean, with intense individual ownership and few standups. Before touching
shared code, an engineer needs to know whether a teammate is already in there.

**Decision.** An agent reads the teammate's recent commits and flags conflicts. Neither engineer has
to stop what they are doing to check in.

**Routing lesson.** This is a path-known task: the input is defined (recent commits), the output is
defined (conflicts with the files I am about to touch), and validation is trivial. It does not need
the model that can plan a moon mission. Route small, well-specified support tasks to a lighter model
and spend the capability budget on the p99 problems.

---

## Source

[Working at the frontier: How Cursor knew Claude Fable 5 was ready for the hardest 1% of problems](https://claude.com/blog/working-at-the-frontier-cursor) — Claude blog, July 17, 2026.
