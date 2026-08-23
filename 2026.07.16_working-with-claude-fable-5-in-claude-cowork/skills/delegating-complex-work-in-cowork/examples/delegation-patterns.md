# Delegation patterns, with the post's worked examples

You may be used to breaking a task into parts and prompting Claude for each one. Claude Fable 5 needs
far fewer of those intermediate prompts, so you can delegate complete jobs.

Still write out the steps yourself when the process matters to you — for example if a metric has to be
calculated the exact same way each time. But if the outcome is what matters, describe the goal and let
Claude do the rest. A step-by-step prompt can limit Claude to the steps you thought of; a goal gives
it room to find a better path.

---

## Pattern 1 — Delegate the approach

**You hand over:** the method.

**Prompt**

> Here is last quarter's customer feedback. Find out why cancellations rose and what we should change.

**Why it works.** There may be several reasonable ways through that folder, and the right one depends
on what is in the feedback. Claude Fable 5 reads everything, picks an approach, and checks its
conclusion against the feedback before bringing it to you. You judge the answer without needing to
specify the details of how it got there.

---

## Pattern 2 — Delegate the procedure

**You hand over:** which skills run, and in what order.

**Prompt**

> Put together the quarterly review the way we always do it.

**Why it works.** A skill teaches Claude a procedure your team uses — how you build a report, format a
deck, run an analysis. You do not need to name the skills or sequence them; Fable 5 picks the right
skills at the right moment.

---

## Pattern 3 — Delegate the timing

**You hand over:** the schedule.

**Prompt**

> I want to start every Monday knowing what changed in the pipeline and what needs a decision.

**Why it works.** For work you want repeated, describing the outcome is enough — Claude sets up the
schedule and turns it into a recurring task. Claude can also save the procedure as a skill and put it
on a schedule, working through the tools you already have connected.

---

## Worked example — the budget build

**The job.** Build next year's budget based on this year's actuals.

**The steps Claude runs.** Gets access to and reads the spreadsheets → pulls the run rates → projects
each line → reconciles the projections against targets → writes the summary.

**The failure mode this avoids.** If it misreads a run rate early, the error flows into every
projection after it. Claude Fable 5 plans the workflow before starting and checks results as it goes,
so it catches the misread number while the job runs and corrects it.

**Settings.** High effort — a complex, multi-step project you expect Claude to complete from beginning
to end.

---

## Worked example — the analytics dashboard

A data scientist at Anthropic came to Claude Cowork with an idea for a new analytics dashboard while
the team was still figuring out what it should show.

Because Claude Fable 5 could read the team's usage data during the conversation, it knew which
problems take weeks to get noticed, and it ranked the metrics that would have caught them sooner.

**Result:** by the end of the conversation, the data scientist had a shortlist of metrics worth adding
and a clickable prototype.

**What made it work.** Brainstorming in Cowork gives the model your real material to think with — it
reads the files you have shared and uses the tools you have connected while you talk. It notices gaps
in an idea while the idea is still easy to change, and shows you directions you had not considered.

---

## Reviewing what came back

While it runs, the panel beside the conversation lists what Claude intends to do, then the files it is
reading and writing and the tools and skills it is using. A mistake you would otherwise find in the
finished output shows up there as one wrong step in the plan — correct the plan in one sentence and
Claude adjusts without starting over.

When it finishes, open the files Claude produced and read them. If something appears off, the record
of the run is still in the conversation: scroll back through the steps, the files read, and the tools
used, and expand Claude's thinking to see the reasoning behind a decision. Or ask directly — *"Where
did this figure come from?"* — and Claude will point you to the source.

Start with work you know how to verify, like the first draft of next quarter's plan for your team. If
you know the priorities well, you can quickly tell if Claude's pass holds up. Delegate bigger jobs as
the results prove reliable.

## Source

[Working with Claude Fable 5 in Claude Cowork](https://claude.com/blog/working-with-claude-fable-5-in-claude-cowork)
— Josefina Albert, July 16, 2026.
