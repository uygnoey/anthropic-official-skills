# Cost signals in a frontier deployment

What the post states about cost, and how the signals connect.

## The constraint

> "As a large enterprise, we want to balance intelligence and cost." — Yusuke Kaji

Frontier capability comes at a frontier price, and Kaji is direct that cost decides how widely he can
deploy. The routing decision exists because the model cannot simply be given everything.

## The two measured numbers

| Metric | Role |
| --- | --- |
| Task completion ratio | Whether the work actually gets finished on this class of task |
| Cost per task | What finishing it costs |

The team measures them together, then routes. The post does not state a threshold or ratio between
them.

## The two second-order signals

### Fewer tokens and fewer wrong turns

This connects directly to the self-verification behavior described in the sibling
`overnight-agent-delegation` skill. The pre-Fable failure mode was that an early wrong turn went
unnoticed and "the agent spends significant time to fix the path, or even fails to reach the
destination." That wasted time is tokens spent. A model that catches the wrong turn early spends fewer
of them.

So self-verification is not only a reliability property — it is a cost property. The same behavior that
makes an unattended overnight run viable also shortens the run.

### Less hand-holding

Human check-ins do not appear in a token bill but are a real cost. The post frames the removal of
mid-run steering as the biggest productivity win of all: it lets the team spend its time on the
decisions only people should make.

Related: as agents close issues roughly 10x faster across every domain, the number of tasks rises, but
"the ones that truly need a human stay at a focusable level." That is the cost of human attention held
flat while throughput rises.

## What the post does not specify

- Rakuten's actual completion ratios or cost-per-task figures.
- Which smaller models handle the remaining work.
- How the routing decision is implemented — whether by policy, by a router, or by team choice.
- Any threshold at which a task class moves between models.

## Source

[Working at the frontier: How Rakuten builds agents overnight with Claude Fable 5](https://claude.com/blog/working-at-the-frontier-rakuten) — Claude blog, July 20, 2026.
