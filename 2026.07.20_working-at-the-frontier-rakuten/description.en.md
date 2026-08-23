**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Yusuke Kaji, General Manager of AI for Business at Rakuten, has tested Claude models since September 2024 — across nearly a dozen launches — and describes Claude Fable 5 as a step change for long-running enterprise agents. His job is to "find the seeds of transformative innovation and scale them across the company," and one of those seeds was Claude.

Two threads run through the post. The first is Rakuten's company-wide effort it calls AI-nization: since March 2025, Claude Code speeding up software development, agents stood up across product, sales, marketing, and finance within a week of Claude Managed Agents arriving, and AI features serving millions of customers. The second is why unattended multi-hour runs used to fail and no longer do — the model checks its own work as it goes, which lets Kaji hand over a whole task instead of pre-chunking it, run several at once, and sleep while a job finishes overnight.

## When is it useful?
- When an agent is meant to run for five hours or a full day without a human checking in.
- When a long run keeps failing because one early wrong assumption compounded unnoticed.
- When deciding how large a unit of work to hand an agent — a well-defined chunk, or the whole task.
- When the number of tasks an organization takes on is rising faster than the judgment available to review them.
- When frontier pricing limits how widely a model can be deployed and work has to be routed.
- When preparing a standing set of hard tasks to point each new model at.

## Key points
- **Self-verification is what makes an unattended run viable.** "We tested Fable, and we love its capability for self-reflection and self-verification. Compared with previous models, it understands its mistake before I point it out at 2 a.m. or 3 a.m.—so that I can sleep." — Yusuke Kaji
- **The old failure mode was not the wrong first step, but that nothing caught it.** "If they choose the right path in the first step, everything is fine. But if they choose the wrong direction in the first pass, the agent spends significant time to fix the path, or even fails to reach the destination."
- **Three behaviors mark the step change:** it re-checks its own assumptions when task state changes midway; it returns to first principles at each step, re-validating against the original intent without being told; and its judgment on ambiguous calls matches the team's.
- **Taste alignment** is Kaji's own coined term for that third behavior — "smoother with Fable than any previous model from your company, or any other model we've used."
- **The unit of work rose.** "Before Fable, we had to break work into well-defined chunks for the agent to execute." Now he hands over a whole task and runs several at once.
- **Sign-off became feasible,** and the unit of work Kaji handles shifts from the task to the decision.
- **Agents carry memory between runs:** "Our agents with memory remember what went wrong in past sessions and avoid repeating those mistakes."
- **AI-nization moved fast:** agents deployed across product, sales, marketing, and finance inside a week, plugged into Slack, Microsoft Teams, and Rakuten's own task system.
- **The constraint moved twice** — from who could write code, to who understands the business problem, to human judgment. Agents close issues roughly 10x faster, but adding more agents does not add judgment.
- **Cost routing is explicit:** measure task completion ratio alongside cost per task, send Fable 5 the work where the extra capability changes the outcome, let smaller models keep the rest. Two things make the math work: fewer tokens and fewer wrong turns, and less hand-holding.
- **Stretch tasks are prepared deliberately.** "The way a good leader prepares stretch goals for their people, we prepare stretch tasks for a new Claude."
- **What's next is coordination, not speed** — agents that "coordinate or organize, more like a manager," holding the nuance usually lost between team members.

## Bundled resources
- `skills/overnight-agent-delegation/SKILL.md` — hand over the whole task, check for the three self-verification behaviors, give agents memory, expect judgment to become the constraint.
- `skills/overnight-agent-delegation/references/self-verification-behaviors.md` — each behavior as the post states it, and what it leaves unspecified.
- `skills/overnight-agent-delegation/templates/stretch-task-brief.md` — a reusable brief for the stretch task a new model is pointed at.
- `skills/overnight-agent-delegation/examples/rakuten-agent-runs.md` — the overnight run, the AI-nization rollout, and the constraint that replaced writing code.
- `skills/intelligence-cost-routing/SKILL.md` — measure completion ratio and cost per task together, route by whether extra capability changes the outcome.
- `skills/intelligence-cost-routing/references/cost-signals.md` — how self-verification becomes a cost property, and what the post does not specify.
- `skills/intelligence-cost-routing/templates/task-routing-record.md` — a per-task-class routing record with a re-evaluation log.
- `guides/building-an-ai-native-workforce.{en,ko,es,ja}.md` — the full account in four languages.

## Source
[Working at the frontier: How Rakuten builds agents overnight with Claude Fable 5](https://claude.com/blog/working-at-the-frontier-rakuten) — Claude blog, July 20, 2026.
