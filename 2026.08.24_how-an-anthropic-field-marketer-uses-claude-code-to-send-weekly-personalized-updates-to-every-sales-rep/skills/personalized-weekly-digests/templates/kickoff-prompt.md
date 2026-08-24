# Kickoff prompt template

The opening brief. Its job is to convey the business problem and your role, not an
implementation plan. Fill in the bracketed parts and paste it as your first message.

> I want your help turning a recurring manual task into an automated, personalized one.
>
> **The problem.** Every [cadence, e.g. Monday morning] I need to tell [audience, e.g. each sales
> rep I support] the [N, e.g. three] things that matter most for their [scope, e.g. accounts and
> territory] this week. Today I do this by hand — [describe the manual process and roughly how
> long it takes, e.g. building slides on Sunday evening]. It does not scale as I take on more
> teams, and the personalization is the first thing I lose when I run out of time.
>
> **My role.** I'm the product manager for this output, not the engineer building it. I know what
> a good message looks like and I will judge your output against that. Ask me business questions
> when you need them answered.
>
> **What I'll give you.** A template example of the message I want, the data sources that hold
> the underlying information, and the rules that make a message correct for a given recipient.
>
> **Where to start.** Read the template example first, then tell me what data you need from me to
> produce one message for one recipient. Route this first run to me, not to the recipients.

## Giving business context by voice

Recording a voice explanation of the problem is an effective way to hand over the full context —
the history, the constraints, and the judgment calls you make without thinking about them. Speak
it the way you would brief a new colleague on their first day, then pass the recording or its
transcript alongside the written brief.

## What to attach with this prompt

1. A filled-in sample of the message you want (see `templates/digest-message-template.md`).
2. The list of data sources and how the recipient joins to them (see `references/data-sources.md`).
3. Any rules you already know about (see `references/content-rules.md`).

## Source

- https://claude.com/blog/how-an-anthropic-field-marketer-uses-claude-code-to-send-weekly-personalized-updates-to-every-sales-rep
