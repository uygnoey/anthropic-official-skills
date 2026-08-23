---
name: delegating-complex-work-in-cowork
description: Hand a frontier model a whole job in Claude Cowork instead of prompting it step by step — pick the model and effort level, brainstorm from a bare idea, brief with context rather than rules, delegate the approach/procedure/timing, and review the plan panel while it runs. Use when a Cowork task spans dozens of steps or several days, when a job needs multiple tools and a series of judgment calls, when you are unsure which model or effort setting fits, when a long conversation is burning usage, or when skills and memory files written for an older model may be holding a newer one back.
---

# Delegating complex work in Claude Cowork

Claude Cowork is built for finished work: give it an objective and it manages the rest, splitting a
big job into parts that run at the same time, each with its own subagent that completes one part and
reports back. It sets a plan at the start and checks its own results against that plan as it goes.

A frontier model changes how you should use that. Claude Fable 5 has a wide lead on long, complex
tasks — exactly the shape of a Cowork job with dozens of steps, each building on the last. Building
next year's budget from this year's actuals means reading spreadsheets, pulling run rates, projecting
each line, reconciling against targets, and writing the summary. A run rate misread early flows into
every projection after it. Fable 5 plans the workflow before starting and checks results as it goes,
so it can catch the misread number mid-run and correct it.

The working relationship is closer to a capable colleague than a tool: explain the situation, agree on
what a strong final result looks like, and let them work. Less of your time goes to checking each
step, so more can go to deciding what the work should be.

## Instructions

### 1. Choose the model, then the effort

Fable 5 is not the default in Cowork — you select it. As of the post's publication the default is
Claude Sonnet 5, right for everyday tasks you would handle yourself in quick passes. Opus is
dependable for deep work with a clear shape, where you know what the end result looks like. Reserve
Fable 5 for the projects that feel most complex or ambiguous, especially jobs that use multiple tools
and require a series of judgment calls. It spends more time thinking and more of your usage limits,
which is worth it on work that is time-consuming or costly to get wrong.

Then tune effort. Higher effort means more planning before the job kicks off and more checking
throughout the run — keep it high for complex, multi-step projects you expect Claude to complete end
to end. Lower effort returns faster while still using frontier judgment; it suits agentic runs made of
many easy steps, or work whose result is easy for Claude to check. In Anthropic's testing, Fable 5 at
lower effort often matched or exceeded earlier models at their highest effort.

Full decision table, plus how the safety classifiers reroute some requests to Claude Opus 4.8, in
[references/model-and-effort-selection.md](references/model-and-effort-selection.md).

### 2. Start with as little as an idea

You do not need a formed plan to begin. Brainstorming inside Cowork gives the model your real material
to think with — it reads the files you have shared and uses the tools you have connected while you
talk, so it notices gaps while the idea is still easy to change and shows you directions you had not
considered.

Two prompts to move an idea toward an output — both, with more, in
[templates/kickoff-prompts.md](templates/kickoff-prompts.md):

- **Ask Claude to interview you:** "Before you start, ask me everything you need to know to get this
  right."
- **Ask for directions:** "Here is roughly what I want. Give me three ways you could take it, with a
  quick sample of each."

Then start the task in that same conversation. Claude already carries the goal you settled on, the
constraints you named, and the decisions you made along the way.

### 3. Brief with context, not a rulebook

Context in Cowork is your prompt, the files and folders you have shared, and the tools you have
connected — Asana, HubSpot, Jira, Slack, and others.

Brief the way you would brief a colleague on a report: who it is for, when it is needed, what it has
to accomplish. Constraints are still useful — "keep it under two pages and use plain language" is a
fine instruction — but a constraint only says what *not* to do. Context says what the work is *for*,
so Claude can make the right call in situations your constraints never anticipated.

That context is also what Claude checks its own work against, so give it something concrete to judge
by. Share an early draft of a report alongside the final version and Claude works out your standards
from what changed between the two.

One caveat: Claude reads the whole conversation again with every new message, so a long thread uses
more of your usage. Start new tasks in a fresh conversation. Scheduled tasks count toward your limit
too — check yours occasionally and turn off any you no longer need.

### 4. Delegate the decision, not just the task

Fable 5 needs far fewer intermediate prompts, so hand over complete jobs. Still write out the steps
yourself when the *process* matters — a metric that has to be calculated the same way every time. When
the *outcome* is what matters, describe the goal: a step-by-step prompt can limit Claude to the steps
you happened to think of, while a goal gives it room to find a better path.

Three decisions worth handing over — worked examples in
[examples/delegation-patterns.md](examples/delegation-patterns.md):

1. **Delegate the approach.** Give the material and the outcome: "Here is last quarter's customer
   feedback. Find out why cancellations rose and what we should change." Several routes through that
   folder are reasonable and the right one depends on what is in the feedback. Claude reads
   everything, picks an approach, and checks its conclusion against the feedback before bringing it to
   you.
2. **Delegate the procedure.** A skill teaches Claude a procedure your team uses. You do not name
   which skills to use or in what order — say "put together the quarterly review the way we always do
   it" and Claude picks the right skills at the right moment.
3. **Delegate the timing.** For repeated work, describe the outcome and Claude sets up the schedule:
   "I want to start every Monday knowing what changed in the pipeline and what needs a decision."

Bring work you assumed was not possible — messy, unclear, hours or days long. Pick an outcome you are
responsible for, say how you would judge it, and let Claude propose the steps. Some of it may become a
scheduled task; Claude can save the procedure as a skill and put it on a schedule.

### 5. Watch the plan, then review the output

The panel beside the conversation lists what Claude intends to do, then the files it reads and writes
and the tools and skills it uses. That panel is where you catch problems early: a mistake you would
otherwise find in the finished output shows up first as one wrong step in the plan. Correct it in one
sentence and Claude adjusts without starting over.

When the work is done, review it the way you would a colleague's — open the files and read them. If
something looks off, the record of the run is still in the conversation: scroll back through the
steps, the files read, and the tools used, and expand Claude's thinking to see the reasoning behind a
decision. Or ask directly — "Where did this figure come from?" — and Claude points you to the source.

Start with work you know how to verify, like a first draft of next quarter's plan for your team. If
you know the priorities well you can tell quickly whether Claude's pass holds up. Delegate bigger jobs
as the results prove reliable.

### 6. Invest in the setup

A more capable model raises the value of every connection you have made. Work through
[references/setup-checklist.md](references/setup-checklist.md):

- **Connect your tools** — email, calendar, documents, team chat. Fable 5 is good at deciding when a
  tool is worth using: it notices the answer is in your calendar or a chat thread and goes to get it
  rather than waiting to be pointed there.
- **Tune the writing to your voice.** Every model arrives with its own defaults; Fable 5 tends toward
  a terser, harder-to-follow style in longer sessions. Adjust by prompting or in project instructions
  ("use plain, straightforward, direct language"). Have Claude read your past writing and save what it
  finds as a skill for next time.
- **Revisit what you set up for earlier models.** Skills and memory files often carry corrections an
  older model needed, and carried forward those corrections constrain the new one. Ask for an audit.

## Examples

**Budget build, end to end.** "Here are this year's actuals and next year's targets. Build the FY
budget." Fable 5 at high effort plans the workflow first, reads the spreadsheets, pulls run rates,
projects each line, reconciles projections against targets, and writes the summary — catching a
misread run rate mid-run instead of letting it flow into every projection downstream.

**Dashboard from a half-formed idea.** A data scientist at Anthropic came to Cowork with an idea for a
new analytics dashboard while the team was still figuring out what it should show. Because Fable 5
could read the team's usage data during the conversation, it knew which problems take weeks to get
noticed and ranked the metrics that would have caught them sooner. The conversation ended with a
shortlist of metrics worth adding and a clickable prototype.

**Reacting to industry news.** "Here's the announcement, tell me what changes for us, considering
everything you know about my organization." You read the output, a strategy starts to form, and Claude
builds a plan to produce the assets you need — in the same conversation the brainstorming happened in.

**Auditing an older setup.** "Go through my skills and saved memory. Which still fit, and which were
written for an older model?"

## Source

[Working with Claude Fable 5 in Claude Cowork](https://claude.com/blog/working-with-claude-fable-5-in-claude-cowork)
— Josefina Albert, Anthropic Education team, July 16, 2026.
