**English** · [한국어](./building-an-ai-native-workforce.ko.md) · [Español](./building-an-ai-native-workforce.es.md) · [日本語](./building-an-ai-native-workforce.ja.md)

# Building an AI-native workforce: Rakuten's account

Yusuke Kaji, General Manager of AI for Business at Rakuten, has been testing Claude models since
September 2024. His job is to "find the seeds of transformative innovation and scale them across the
company." One of those seeds was Claude. This guide follows the account as the post tells it.

## The deployment, in order

Since March 2025, Rakuten has used Claude to speed up software development with Claude Code, stand up
agents across its business functions, and power AI features for millions of customers. Rakuten chose to
partner with Anthropic for its enterprise focus, leadership, and product taste.

Across nearly a dozen model launches, the work Kaji can hand to an agent has kept growing: first using
Claude Code to ship production software, then building custom Claude Managed Agents for teams across
the company.

Rakuten calls the company-wide effort **AI-nization** — infusing AI into everything it does for
customers, business partners, and employees. When Claude Managed Agents arrived, Rakuten deployed
agents across product, sales, marketing, and finance **inside a week**, plugged into Slack, Microsoft
Teams, and the company's own task system.

## The constraint moved

For Kaji and his team, the constraint on building agents used to be who could write code. Now it is who
understands the business problem.

> "The modern corporation is designed to minimize the cost of communication. I believe agents like
> Claude Code can shine when we work with them to minimize the cost of new innovation as well, like a
> quick transition from idea to production."

Give a capable person agents that hold context and taste, and "it allows the hidden talent to unlock
their potential and scale their potential 100 times more."

## Then it moved again, to judgment

Running agents in every function around the clock surfaces a new constraint: human judgment.

Rakuten's agents close issues roughly **10x faster** across every domain, and the number of tasks the
organization takes on keeps rising. Adding more agents does not add judgment. So the faster the agents
run, the more the organization's progress depends on a person closing the loop.

## Why long runs used to fail

For most builders, the hardest part of building long-running agents is setting them up to succeed with
minimal oversight. Connecting an agent to the right tools and context is one thing, but in Kaji's
experience there were always limits to how long it could go without a human validating its work.

> "If they choose the right path in the first step, everything is fine. But if they choose the wrong
> direction in the first pass, the agent spends significant time to fix the path, or even fails to reach
> the destination."

On a job meant to run five hours or a full day, one early wrong assumption could burn the entire run,
and the only way to catch it was a person checking in.

The failure mode was a **lack of self-verification**. Any model can take a wrong first step. The problem
with earlier models was that they did not check their own work as they went, so an early wrong turn went
unnoticed, compounded over the run, and produced a suboptimal result hours later.

## What changed with Claude Fable 5

Kaji says Fable 5 changes the calculus for days-long agentic runs because it checks its own work as it
goes, far more often than any prior model.

> "We tested Fable, and we love its capability for self-reflection and self-verification. Compared with
> previous models, it understands its mistake before I point it out at 2 a.m. or 3 a.m. — so that I can
> sleep."

His team cite three behaviors that mark the step change:

- **It re-checks its own assumptions.** When the state of the task changes midway, Fable 5 notices and
  corrects a wrong assumption before acting on it, rather than committing to a bad path and discovering
  it hours later.
- **It returns to first principles at each step.** It re-validates against the original intent without
  being told — the course-correction Kaji used to have to make himself.
- **It matches the team's taste.** Even with minimal guidance, its judgment on ambiguous calls lines up
  with theirs. Kaji coined a term for this: *taste alignment*. "Taste alignment is smoother with Fable
  than any previous model from your company, or any other model we've used."

## The unit of work changed

> "Before Fable, we had to break work into well-defined chunks for the agent to execute."

Now Kaji hands over a whole task and runs several at once. The model reflects at each step, catches a
bad early assumption, and finds its own way back to first principles — re-navigating to the right
outcome without anyone steering it.

Because the model self-corrects mid-run, sign-off becomes feasible for the first time, and the unit of
work Kaji delegates shifts **from the task to the decision**. The agents also carry memory between runs:
"Our agents with memory remember what went wrong in past sessions and avoid repeating those mistakes."

As a result, the absolute number of tasks keeps climbing, but the ones that truly need a human stay at a
focusable level. Not having to jump in and steer mid-run is, Kaji says, the biggest productivity win of
all — it lets his team spend its time on the decisions only people should make, and keeps an AI-native
organization accelerating instead of stalling on human course-correction.

## Preparing stretch tasks

Kaji likens testing a new model to embarking on a "new quest."

> "The way a good leader prepares stretch goals for their people, we prepare stretch tasks for a new
> Claude. Maybe Claude is nudging us to stretch, too."

## Balancing cost and efficiency

Frontier capability comes at a frontier price, and Kaji is direct that cost decides how widely he can
deploy. "As a large enterprise, we want to balance intelligence and cost."

His team measures **task completion ratio** alongside **cost per task**, then sends Fable 5 the work
where the extra capability changes the outcome and lets smaller models keep the rest.

Two things make the math work in Fable 5's favor: it gets more done with fewer tokens and fewer wrong
turns, and it needs less hand-holding.

## What's next

The frontier Kaji is testing now is not individual speed. It is getting agents to **coordinate people**.
Claude Code has sped up his own work and his colleagues', but the hard part of any organization is the
alignment between people — matching one person's context and taste to another's. He is exploring agents
that "coordinate or organize, more like a manager," holding the nuance that usually gets lost between
team members.

> "We do not see AI agents as future colleagues or competitors. They are systems around us."

He holds Anthropic to its own advice, that you should build for the model coming in three or six months
rather than the one in front of you.

> "I think we as a society still haven't found the model–task fit yet for Claude Fable 5, but it already
> stands out as a model that crossed the line and came over to our world."

## Source

[Working at the frontier: How Rakuten builds agents overnight with Claude Fable 5](https://claude.com/blog/working-at-the-frontier-rakuten) — Claude blog, July 20, 2026.
