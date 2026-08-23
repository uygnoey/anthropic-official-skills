**English** · [한국어](./working-with-a-frontier-model-in-cowork.ko.md) · [Español](./working-with-a-frontier-model-in-cowork.es.md) · [日本語](./working-with-a-frontier-model-in-cowork.ja.md)

# Working with a frontier model in Claude Cowork

Claude Fable 5 is Anthropic's most capable generally available model, built for long-running, complex
and asynchronous work. It is particularly effective at carrying out multi-step workflows on its own
for extended periods — conducting deep research it then folds into a first-draft memo, performing due
diligence before generating board presentations, going through a folder to redline multiple contracts
— testing and evaluating its results as it goes.

Getting the most out of it requires a change in how you work with it. The existing practices still
matter — prompting best practices, providing context, building skills that capture repeatable
processes like weekly team updates, sales call prep, or customer feedback analysis. The model performs
even better with them in place. What changes is that Fable 5 applies your context, preferences, and
skills across entire tasks, even ones that take days, where previous models may have lost track over
long stretches and needed reminding.

Working with it resembles working with a highly capable colleague: you explain the situation, agree on
what a strong final result looks like, and let your colleague work. Less of your time goes to checking
each step, so more of it can go to deciding what the work should be.

## How Fable 5 complements Claude Cowork

Claude Cowork is built for creating finished work. Give it an objective and it manages the rest, even
when the task is large and complex. A big job gets broken into parts that run at the same time, each
with its own subagent — a separate instance of Claude that takes one part of the job and reports back.
That is how Claude gets through large amounts of information quickly. Cowork also manages large tasks
by setting a plan at the start and checking its own results against it as it goes.

Fable 5 has a wide lead over Anthropic's other models on long, complex tasks, and Cowork tasks are
often exactly that: dozens of steps, each building on the last.

Take building next year's budget from this year's actuals. Claude reads the spreadsheets, pulls the
run rates, projects each line, reconciles the projections against targets, and writes the summary. If
it misreads a run rate early, the error flows into every projection after it. Fable 5 plans the
workflow before starting and checks results as it goes, so it catches the misread number while the job
runs and corrects it.

## Deciding when to use it

Fable 5 is not the default in Cowork — you need to select it. At the time of the post, the default is
Claude Sonnet 5, and it is the right choice for everyday tasks you would handle yourself in quick
passes. Claude Opus is a dependable choice for deep work with a clear shape, where you know what the
end result looks like. Fable 5 is for the projects that feel most complex or ambiguous, and that may
have been out of reach for prior models.

It spends more time thinking and more of your usage limits, which can be worth it on work that is
time-consuming or costly to get wrong. The recommendation: reserve Fable 5 for your most important
work, especially jobs that use multiple tools and require a series of judgment calls.

**Effort.** At higher effort, Fable 5 plans more before it kicks off a job and checks in more
throughout its run — keep effort higher for complex or multi-step projects you expect Claude to
complete from beginning to end. At lower effort you get a faster response while still taking advantage
of frontier intelligence; consider it for tasks that need frontier judgment but not deep exploration,
such as agentic runs made of many easy steps, or work where the result is easy for Claude to check. In
Anthropic's testing, Fable 5 at lower effort often matched or exceeded earlier models at their highest
effort levels.

**Classifiers.** Fable 5 comes with a new set of classifiers: separate AI systems that detect
potential misuse in requests related to cybersecurity or to biology and chemistry. When they trigger,
the response is automatically handled by Claude Opus 4.8 instead, and users are informed whenever this
occurs. Opus 4.8 is a highly capable model in its own right, and the chat stays on Opus from there —
start a new one to get back to Fable 5. The safeguards were tuned conservatively so a Mythos-class
model could be released for general use both safely and quickly, so they will sometimes catch harmless
requests, including phrases that only touch on related topics. Anthropic is working to reduce these
false positives.

## Start with as little as an idea

When you kick off a task you do not always know what you are trying to accomplish. That early stretch
is where Fable 5 can be a powerful thought partner, and in Cowork it works from your skills, tools,
and knowledge.

Say a news announcement lands that is relevant to your industry. You can ask: *"Here's the
announcement, tell me what changes for us, considering everything you know about my organization."*
You read the output, a strategy starts to form, and Claude builds a plan to produce the assets you
need — starting in the same conversation where the brainstorming happened.

Brainstorming in Cowork gives the model your real material to think with. It reads the files you have
shared and uses the tools you have connected while you talk, so its suggestions are relevant. It
notices gaps in an idea while the idea is still easy to change, and shows you directions you had not
considered. And when the task begins in the same conversation, Fable 5 already carries the goal you
settled on, the constraints you named, and the decisions you made along the way.

A data scientist at Anthropic came to Cowork with an idea for a new analytics dashboard while the team
was still figuring out what it should show. Because Fable 5 could read the team's usage data during
the conversation, it knew which problems take weeks to get noticed, and it ranked the metrics that
would have caught them sooner. By the end of the conversation the data scientist had a shortlist of
metrics worth adding and a clickable prototype.

Two prompts to help an idea evolve into an output:

- **Ask Claude to interview you:** "Before you start, ask me everything you need to know to get this
  right."
- **Ask for directions:** "Here is roughly what I want. Give me three ways you could take it, with a
  quick sample of each."

## Provide context with your constraints

Context is the information Claude works from: in Cowork that means your prompt, whatever files and
folders you have shared, and any tools you have connected — Asana, HubSpot, Jira, Slack, and others.

Think of how you would brief a colleague on a report. You would not hand them a list of rules, but you
would tell them who it is for, when it is needed, and what it has to accomplish, and trust them to
make good decisions from there. Fable 5 works the same way.

Constraints are still useful — "keep it under two pages and use plain language" is a fine instruction.
But a constraint only tells Claude what *not* to do. Context tells it what the work is *for*, so it
can make the right call in situations your constraints did not anticipate.

Fable 5 handles long, multi-step tasks well partly because of this: when a question or decision point
comes up while it works, it looks for the answer in the context you shared. It also uses that context
to check its own work, so give it something concrete to judge against — an early draft of a report and
the final version, and Claude will work out what your standards are from what changed between the two.

Context also gives Claude an understanding of your situation, so it can infer or find details you
never specified in the prompt, searching a wider base of knowledge than you could fit in a prompt.

One note on long conversations: to stay caught up, Claude reads the whole conversation again with
every new message, so a long thread may use more of your usage. Start new tasks in a fresh
conversation. Scheduled tasks count toward your limit too — check yours occasionally and turn off any
you no longer need.

## Delegate larger, more complex jobs

You may be used to breaking a task into parts and prompting Claude for each one. Fable 5 needs far
fewer of those intermediate prompts, so you can delegate complete jobs.

Still write out the steps yourself when the process matters to you — for example if a metric has to be
calculated the exact same way each time. But if the outcome is what matters, describe the goal and let
Claude do the rest. A step-by-step prompt can limit it to the steps you thought of; a goal gives it
room to find a better path.

Delegating means handing Claude a decision you would normally make yourself. Three ways to do that:

- **Delegate the approach.** Give Claude the material and describe the outcome you want: *"Here is
  last quarter's customer feedback. Find out why cancellations rose and what we should change."* There
  may be several reasonable ways through that folder, and the right one depends on what is in the
  feedback. Fable 5 reads everything, picks an approach, and checks its conclusion against the
  feedback before bringing it to you. You judge the answer without specifying how it got there.
- **Delegate the procedure.** A skill teaches Claude a procedure your team uses — how you build a
  report, format a deck, run an analysis. You do not need to say which skills to use or in what order.
  Say *"put together the quarterly review the way we always do it"* and Fable 5 picks the right skills
  at the right moment.
- **Delegate the timing.** For work you want repeated, describe the outcome and Claude sets up the
  schedule and turns it into a recurring task: *"I want to start every Monday knowing what changed in
  the pipeline and what needs a decision."*

Bring Fable 5 harder work than you are used to giving AI, even work you assumed was not possible —
messy or unclear, or hours or days long. Describe it and see whether the model can work at that level.
Pick an outcome you are responsible for, say how you would judge it, then let Claude propose the steps
to get there. Some of this work may turn into a scheduled task that runs on its own; Claude can save
the procedure as a skill and put it on a schedule, working through the tools you already connected.

## Review Claude's thought process

Part of what lets Fable 5 carry long work is that it knows how to set and follow a plan. In Cowork you
can see that plan while Claude works: the panel beside the conversation lists what it intends to do,
then the files it is reading and writing and the tools and skills it is using.

That panel is your chance to catch problems and redirect early. A mistake you would otherwise find in
the finished output instead shows up as one wrong step in the plan. Correct the plan in one sentence
and Claude adjusts without starting over.

When the work is finished, review it the way you would a colleague's: open the files Claude produced
and read them. If something appears off, the record of the run is still in the conversation. Scroll
back through the steps Claude listed as it worked, including the files it read and the tools it used,
and expand its thinking to see the reasoning behind a decision. Or ask directly — *"Where did this
figure come from?"* — and Claude will point you to the source.

Start with work you know how to verify, like the first draft of next quarter's plan for your team. If
you know the priorities well, you can quickly tell if Claude's pass holds up. Delegate bigger jobs as
the results prove reliable.

## Invest in your Cowork setup

A more capable model raises the value of each connection you have made, from the folders you have
shared to the tools your team works in.

**Connect your tools.** Start with the tools you use daily — email, calendar, documents, your team's
chat. Each connection widens what Claude can do without you copying things in. Fable 5 is good at
deciding when a tool is worth using: with your tools connected, it notices when the answer is in your
calendar or a chat thread and goes to get it, instead of waiting to be pointed there.

**Tune the writing to your voice.** Each new model arrives with its own writing defaults: voice,
length, and the phrases it reaches for first. Fable 5 has certain defaults, such as a more terse or
hard-to-follow writing style in longer sessions. Voice, tone, and style can be customized by prompting
or in your project instructions — for example, "use plain, straightforward, direct language." If you
use memory, check occasionally what Claude has saved about your writing preferences. For documents
where you want a specific voice, use connectors or existing files to have Claude read through your
past writing and save what it finds as a skill it can call on next time. Fable 5 follows standing
instructions more closely than earlier models, and is better at using saved material when needed.

**Revisit what you set up for earlier models.** Saved instructions — skills and memory files — written
for an earlier model often carry corrections that model needed. Carried forward, old corrections can
constrain a new model. Ask for an audit: *"Go through my skills and saved memory. Which still fit, and
which were written for an older model?"*

## What comes next

As frontier intelligence continues to evolve, Claude Cowork will become increasingly capable, enabling
even longer-running work and unlocking additional knowledge work use cases. Learning how to prompt,
manage context, check Claude's work, and delegate tasks will help you take advantage of all Fable 5
and future models have to offer.

## Source

[Working with Claude Fable 5 in Claude Cowork](https://claude.com/blog/working-with-claude-fable-5-in-claude-cowork)
— Josefina Albert, Anthropic Education team, July 16, 2026.
