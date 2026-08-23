---
name: frontier-model-routing
description: Decide when a task deserves the most capable model and when a lighter, faster one is enough, using the A-to-B heuristic Cursor settled on — if you know the path from A to B, a cheaper model will do; if you are at A with no idea where B is, reach for the frontier model. Use when configuring a mixed-model setup, when choosing a model for a gnarly refactor or an open-ended migration, when a task keeps stalling under a cheaper model, or when deciding whether a long-shelved rewrite is now worth starting.
---

# Routing work between frontier and lighter models

Cursor supports every major frontier model alongside its own, which puts its engineers in the unusual
position of having to decide, task by task, which one to spend. Nate Schmidt — who works on evals and
model behavior there — settled on a rule simple enough to apply without deliberating.

> "If you have a good sense of what the path from A to B looks like, you might not need Fable. If
> you're at A and you have no idea where B is, Fable is an excellent choice."

The underlying distinction he draws is between **local reasoning** and **global reasoning**. A model
doing local reasoning thinks about what just happened and what is immediately about to happen. A model
doing global reasoning thinks about the entire mission. Tasks that only need the next step do not need
the model that can hold the whole mission.

## Instructions

### 1. Classify the task by how well you know the destination

Ask one question before picking a model: *do I know what "done" looks like, and roughly how to get
there?*

- **Path known.** A defined change, a bug with an obvious fix, a mechanical edit, a routine query.
  Route to a faster, lighter model.
- **Path unknown.** You are at A and B is not yet legible: an ambiguous report, a refactor nobody has
  scoped, a migration whose shape you would have to discover, a problem where the first plausible
  answer is probably wrong. Route to the frontier model.

Schmidt's own framing for the second bucket: "When I want to build something the right way, Fable is
the first model I think of."

See [references/routing-heuristics.md](references/routing-heuristics.md) for the full set of signals.

### 2. Run a mixed setup rather than picking one model

Cursor's team pairs the frontier model with faster, lighter models for routine work and brings the
expensive one in for the problems where capability — not speed, not cost — is the binding constraint.
In that configuration, Schmidt says, the combination is the most effective setup they've run.

Do not standardize on a single model for everything. Standardize on the *rule* for choosing.

### 3. On the hardest problems, optimize for time to solution

For what Schmidt calls "the p99 of problems" — the gnarly ones — the variable worth optimizing is
time to solution, not tokens or per-call price. A cheaper model that burns twelve hours without
finishing is not the cheaper option.

His moon-landing test is the concrete version of this. A previous-generation model ran twelve to
sixteen hours in a space-flight simulator without ever landing: launch, run out of fuel in orbit, add
much more fuel, then fail to clear the atmosphere because the rocket had become too heavy. Given the
same blank-slate prompt, the newer model decided *not* to attempt the moon on the first try — it flew
an initial orbital mission purely to collect telemetry, then used that to inform the next trip. It
landed, and the whole run took a couple of hours.

Walked through step by step in [examples/routing-decisions.md](examples/routing-decisions.md).

### 4. Reconsider the work you shelved

The routing rule has a second-order effect worth acting on deliberately. Cursor's team went back to
projects they had abandoned — rewrites everyone agreed would be better but nobody could justify
spending weeks on — because the model can carry enough of the skeleton.

> "It lowers the activation energy to work on these types of tasks. It lets us move in search of a
> global optimum rather than a local one."

When you adopt a more capable model, re-examine the backlog of things that were rejected on effort
grounds rather than on merit. Some of them have changed category.

### 5. Use agents to remove coordination overhead, not just to write code

Cursor runs lean, with intense individual ownership and few standups. Before touching shared code,
Schmidt has an agent read his teammate's recent commits and flag conflicts — so neither engineer has
to stop what they are doing to check in.

This is a routing decision too: a small, well-defined, path-known task, and a good fit for a lighter
model on a schedule.

## Examples

### Route to a lighter model

- A failing test with a clear cause and a one-line fix.
- Renaming a symbol across a package.
- Writing the boilerplate half of a component whose interface you already specified.
- Reading a teammate's recent commits and flagging overlap with the file you are about to edit.

### Route to the frontier model

- A stack trace pasted in with the word "fix" and nothing else, in a system you do not know well.
- A database migration where correctness depends on invariants nobody has written down.
- A rewrite that has been in the backlog for a year because scoping it alone would take a week.
- Any problem where you cannot yet describe what the finished state looks like.

### The A-to-B rule applied

| Task | Do you know the path? | Route |
| --- | --- | --- |
| Bump a dependency and fix the two call sites it breaks | Yes | Lighter model |
| Find out why p99 latency doubled last Tuesday | No | Frontier model |
| Add a field to an existing API response | Yes | Lighter model |
| Decide how to restructure a module everyone avoids | No | Frontier model |

## Source

[Working at the frontier: How Cursor knew Claude Fable 5 was ready for the hardest 1% of problems](https://claude.com/blog/working-at-the-frontier-cursor) — Claude blog, July 17, 2026.
