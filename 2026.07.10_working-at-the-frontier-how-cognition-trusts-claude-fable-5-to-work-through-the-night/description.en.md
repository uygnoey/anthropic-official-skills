**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Silas Alberti, SVP of Research at Cognition, has tested nearly every Claude model inside Devin, the company's autonomous AI software engineer. Claude Fable 5 is the first he'd trust to leave running overnight.

The post has two threads. One is how Cognition decides a model is better: not by a score — "we trust no eval" — but by having its highest-taste developers put each new model through a real day of work, with the bar being whether the code is something they'd actually keep. The other is what specifically changed: **horizon**, meaning how long an agent stays self-sufficient before it loses the thread, and the three behaviors that made a long run hold together.

## When is it useful?
- When deciding whether a task is safe to hand an agent unattended for hours.
- When an agent finishes a migration and you cannot tell whether the result is trustworthy.
- When your engineers have started tuning out an agent's triage output.
- When a model aces a benchmark and you need a way to check it before believing it.
- When building an internal benchmark and choosing what it should reward.
- When arguing internally about whether a new release is actually an improvement.

## Key points
- **"We trust no eval."** Cognition has watched models ace a benchmark and then fall apart the moment its engineers tried to use them — "we've been burned like this a bunch of times." Its highest-taste developers run each new model through a real day of work; the bar is whether the code is something they'd keep.
- **Frontier Code is an anti-slop benchmark.** Cognition built it because existing ones kept rewarding code that passed tests but wouldn't survive a real codebase. On its hardest subset: prior Opus model ~10%, Claude Fable 5 ~30%.
- **A jump should be met with suspicion.** First reaction: "Is there a bug? This can't be true." Usually engineers argue for weeks; this time the dogfooding agreed with the numbers. "It was kind of a shocker, honestly."
- **The old ceiling was horizon.** "Before Fable, you could delegate agents that could stay on-task for a couple of minutes, maybe an hour." After that, sessions drifted; five ideas at once made earlier models lose track.
- **Finishing is not succeeding.** On one database migration, a prior Opus model technically finished the job but introduced a series of subtle bugs along the way.
- **Surface-level triage destroyed trust.** Earlier models stayed at the surface of the logs and were trained to answer no matter what, so they'd "confidently claim the first plausible thing they discover and then stop." Engineers learned to tune them out.
- **Eight hours, unattended, with real progress.** "I was about to go to bed and I was like, 'Okay, just please keep working on this and don't stop until I wake up.' And then I wake up, and it's been working for eight hours straight and actually making real progress."
- **Three behaviors held the horizon:** properly using Cognition's internal debugging tools (paging through logs in the browser, drawing conclusions despite the noise); stating the invariants it would hold itself to before executing a migration; and on triage, pinning down the root cause *and saying what it didn't know* — which Alberti says is what rebuilds trust.
- **A step change, roughly once a year.** Alberti's reference point is Claude 3.6 Sonnet in late 2024, the first model that could reliably chain tools and hold a multi-step task; internal usage tripled when it went into Devin.
- **Proactive sessions are next.** Devin can already watch a Slack channel and jump into an issue without being tagged, or monitor production and triage a spike. Alberti expects 90% of agent sessions to be proactive within a year or two.

## Bundled resources
- `skills/long-horizon-agent-runs/SKILL.md` — decide whether a task is horizon-shaped, require invariants up front, wire up the real debugging tools, and demand a stated confidence boundary.
- `skills/long-horizon-agent-runs/references/failure-modes.md` — the five ways long runs fail, each paired with the behavior that fixed it.
- `skills/long-horizon-agent-runs/templates/invariants-brief.md` — the two-pass brief that gets invariants stated and reviewed before the run starts.
- `skills/long-horizon-agent-runs/examples/overnight-run.md` — the eight-hour run, the migration before and after, and triage output that earns trust versus output that gets ignored.
- `skills/dogfood-model-evaluation/SKILL.md` — make the dogfood day the primary signal, pick evaluators by taste, and treat score-plus-dogfooding agreement as the real result.
- `skills/dogfood-model-evaluation/references/anti-slop-criteria.md` — what the post says about Frontier Code, plus the criteria implied by "would it survive a real codebase."
- `skills/dogfood-model-evaluation/templates/dogfood-day.md` — setup, per-task log, the binary verdict, and corroboration against your benchmark.
- `guides/trusting-long-running-agents.{en,ko,es,ja}.md` — the full account in four languages.

## Source
[Working at the frontier: How Cognition trusts Claude Fable 5 to work through the night](https://claude.com/blog/working-at-the-frontier-how-cognition-trusts-claude-fable-5-to-work-through-the-night) — Claude blog, July 10, 2026.
