**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Josefina Albert, from Anthropic's Education team, explains how to work with Claude Fable 5 inside Claude Cowork — Anthropic's agentic AI system for knowledge work — when the job is long, complex, and asynchronous.

The premise is that a more capable model asks for a different working style. Cowork already breaks a large job into parts that run at the same time, each with its own subagent, and sets a plan at the start that it checks its results against. Fable 5's lead on long, multi-step tasks fits that shape: on a job like building next year's budget from this year's actuals, it plans the workflow before starting and catches a misread run rate mid-run, before the error flows into every projection after it. Working with it resembles working with a capable colleague — you explain the situation, agree on what a strong result looks like, and let them work.

## When is it useful?
- When a Cowork job runs dozens of steps, or spans days, and each step builds on the last.
- When you are deciding between Sonnet 5, Opus, and Fable 5, or which effort level to set.
- When you are starting from an idea that is not yet formed and want a thought partner with access to your files and tools.
- When you keep writing step-by-step prompts for work where only the outcome matters.
- When a long conversation is consuming more usage than you expected.
- When skills or memory files written for an older model may be constraining a newer one.

## Key points
- **Fable 5 is not the default in Cowork** — you select it. Sonnet 5 is the default and fits everyday tasks; Opus fits deep work with a clear shape; Fable 5 is for the most complex or ambiguous projects, especially those using multiple tools and requiring a series of judgment calls.
- **Effort tunes the choice.** Higher effort means more planning up front and more checking mid-run. At lower effort, Fable 5 often matched or exceeded earlier models at their highest effort in Anthropic's testing.
- **New classifiers reroute to Claude Opus 4.8.** Requests touching cybersecurity or biology and chemistry may trigger them; you are told when it happens, and the chat stays on Opus until you start a new one. Tuned conservatively, so false positives occur.
- **Start with as little as an idea.** Brainstorming in Cowork gives the model your real files and connected tools to think with. Two prompts: *"Before you start, ask me everything you need to know to get this right"* and *"Here is roughly what I want. Give me three ways you could take it, with a quick sample of each."*
- **Context beats constraints.** A constraint only tells Claude what not to do; context tells it what the work is for, so it can decide well in situations your constraints did not anticipate. Give it an early draft and a final version and it works out your standards from the difference.
- **Long conversations cost more.** Claude reads the whole conversation again with every message. Start new tasks fresh, and turn off scheduled tasks you no longer need.
- **Delegate the approach, the procedure, or the timing** — the method, which skills run, or the schedule. Write out steps yourself only when the process itself matters.
- **The plan panel is where you redirect.** It lists what Claude intends to do, then the files and tools it uses. A wrong step in the plan is cheaper to fix than a wrong finished output; one sentence corrects it without restarting.
- **Invest in setup:** connect the tools you use daily, tune the writing to your voice (Fable 5 skews terse in longer sessions), and audit skills and memory written for earlier models.

## Bundled resources
- `skills/delegating-complex-work-in-cowork/SKILL.md` — the full working method: pick model and effort, start from an idea, brief with context, delegate the decision, watch the plan, invest in setup.
- `skills/delegating-complex-work-in-cowork/references/model-and-effort-selection.md` — the model decision table, what higher and lower effort change, and how the Opus 4.8 fallback works.
- `skills/delegating-complex-work-in-cowork/references/setup-checklist.md` — connect tools, tune voice, revisit what you set up for earlier models.
- `skills/delegating-complex-work-in-cowork/templates/kickoff-prompts.md` — every prompt from the post, grouped by what it is for.
- `skills/delegating-complex-work-in-cowork/examples/delegation-patterns.md` — the three delegation patterns plus the budget and dashboard examples worked through.
- `guides/working-with-a-frontier-model-in-cowork.{en,ko,es,ja}.md` — the full walkthrough in four languages.

## Source
[Working with Claude Fable 5 in Claude Cowork](https://claude.com/blog/working-with-claude-fable-5-in-claude-cowork) — Josefina Albert, July 16, 2026.
