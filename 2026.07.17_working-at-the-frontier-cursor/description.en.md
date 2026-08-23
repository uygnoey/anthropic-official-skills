**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Nate Schmidt evaluates frontier models at Cursor — an AI coding agent that supports every major frontier model alongside its own, which makes the company an unusually neutral judge of how each one performs. This post is his account of how he decided Claude Fable 5 was ready for the hardest problems, and what changed once it was.

Two things drive the story. The first is CursorBench, the internal eval Cursor built after public benchmark scores and real developer reception stopped lining up — designed around underspecified prompts rather than well-defined problems. The second is the distinction Schmidt draws between local reasoning, which thinks about the step just taken and the step about to be taken, and global reasoning, which thinks about the entire mission.

## When is it useful?
- When public benchmark scores no longer predict how your developers actually respond to a model.
- When designing an internal eval and deciding what its tasks should look like.
- When a benchmark result jumps and you need a way to check whether to believe it.
- When choosing between a frontier model and a cheaper one for a specific task.
- When configuring a mixed-model setup and needing a rule for what goes where.
- When deciding whether a long-shelved rewrite is now worth starting.

## Key points
- **CursorBench was built because scores and reception diverged.** It captures the messy, underspecified ways engineers actually prompt models — one task is a stack trace pasted in with the single word "fix"; another tells the model the wrong module is broken, to see whether it challenges the assumption or follows it into a dead end.
- **The full chain is what gets exercised.** "The model has to infer that the user has a problem and what they're trying to convey, identify the root cause, fix it, validate the fix, and report back."
- **The right answer is table stakes.** What Cursor scores is whether the model understood what it was being asked.
- **72.9% at Max effort** on CursorBench, a new high — and the team's first reaction was suspicion: "either the model's very smart, or the model is cheating."
- **The check is reading traces.** On the hardest tasks, "we just kept seeing the model dig out wins that no other model was doing previously" — with fewer operations, token-efficient relative to the work completed.
- **The moon test.** A prior model ran twelve to sixteen hours in a space-flight simulator without landing, looping between running out of fuel and being too heavy to launch. Fable 5 planned an orbital telemetry mission first, then used it to inform the landing; the whole run took a couple of hours.
- **Local vs. global reasoning.** "With Opus, it was doing local reasoning… With Fable it's global reasoning. It's thinking about the entire mission."
- **The A-to-B routing rule.** "If you have a good sense of what the path from A to B looks like, you might not need Fable. If you're at A and you have no idea where B is, Fable is an excellent choice."
- **Shelved work changes category.** Rewrites nobody could justify spending weeks on became viable: "It lowers the activation energy… It lets us move in search of a global optimum rather than a local one."
- **Pair models rather than standardize.** Frontier model for capability-constrained problems, faster and lighter models for routine work — the most effective setup the team has run.
- **Agents remove coordination overhead.** Before touching shared code, an agent reads a teammate's recent commits and flags conflicts, so neither engineer has to interrupt the other.
- **Next up:** days-to-weeks unattended runs on a back-end system, proactive hunting of performance bottlenecks, and closer-to-reality eval environments.

## Bundled resources
- `skills/frontier-model-routing/SKILL.md` — apply the A-to-B rule, run a mixed setup, optimize the p99 for time to solution, and revisit the backlog.
- `skills/frontier-model-routing/references/routing-heuristics.md` — the signals that push a task toward each model, and what the post leaves unspecified.
- `skills/frontier-model-routing/examples/routing-decisions.md` — the moon landing, the shelved rewrite, and the commit-conflict agent, worked through.
- `skills/realistic-agent-evals/SKILL.md` — source tasks from real prompts, include wrong premises, score comprehension, and read traces when a score moves.
- `skills/realistic-agent-evals/references/benchmark-design.md` — everything the post states about how CursorBench is built, and where it stops.
- `skills/realistic-agent-evals/templates/eval-task-template.md` — task templates for the three shapes, plus a result record that carries the effort setting.
- `skills/realistic-agent-evals/examples/eval-tasks.md` — the two tasks named in the post, plus filled-in illustrations of each shape.
- `guides/evaluating-frontier-coding-models.{en,ko,es,ja}.md` — the full account in four languages.

## Source
[Working at the frontier: How Cursor knew Claude Fable 5 was ready for the hardest 1% of problems](https://claude.com/blog/working-at-the-frontier-cursor) — Claude blog, July 17, 2026.
