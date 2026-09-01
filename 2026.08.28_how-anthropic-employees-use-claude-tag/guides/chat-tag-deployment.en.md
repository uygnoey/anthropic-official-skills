**English** · [한국어](./chat-tag-deployment.ko.md) · [Español](./chat-tag-deployment.es.md) · [日本語](./chat-tag-deployment.ja.md)

# Deploying Claude Tag across teams

Claude Tag brings Claude into chat tools like Slack. Tag it in a thread and it completes tasks using
the conversation's context: it follows the conversation, uses standing instructions, and decides
when to participate.

This guide covers how teams at Anthropic put it to work, what each deployment required, and what to
plan for before rolling it out.

## What it changes

The bottleneck in most knowledge work is not writing. It is that the inputs — a long thread, reports
scattered across channels, an asset and the sources that back it — have to be found first. Claude
Tag sits where those inputs already are.

The consistent split across every deployment below: Claude handles information synthesis and
processing; humans handle judgment, verification, and decisions.

## Three deployment patterns

### Thread to document

A product marketer turned a 15+ message thread into a review-ready one-pager in 45 minutes. The
prompt was one sentence pointing at the thread and naming the artifact. Claude returned a two-page
draft in two minutes — feature description, business case, implementation details, appendix.

The rest of the 45 minutes was verification: Claude checked its own factual accuracy and separated
verified claims from ones needing the product lead's sign-off; the marketer supplied official
resources; Claude rewrote. Four versions before it was shared.

**Plan for:** the verification loop, not the drafting. That is where the human time goes.

### Scattered mentions to one list

A product strategy team member consolidated feature requests spread across channels, including which
sales reps had asked on behalf of which customers. About 26 minutes, roughly 20 search variants,
deduplicated, about 24 accounts with requester handles, teams, account names, and source links.

Widened to a weekly digest of every product problem reported by enterprise customers: about 120 raw
reports became 23 open and 14 resolved issues organized by product area, each with a summary and a
source link, in 50 minutes. Estimated by hand: a week of full-time work.

**Plan for:** prompts that specify search targets, what counts as a match, and the output format
with an example row. The match definition is what makes deduplication possible.

### A review channel in front of a specialist

A product counsel created a dedicated Slack channel where Claude reviews marketing assets before
legal review. Turnaround went from a day or more to about 30 minutes per asset.

Setup: specific rules and instructions, plus access to company Slack, an internal knowledge index,
and the public web. Claude spots unsubstantiated claims, verifies factual statements, flags issues
with specific remediation instructions, and works with requesters directly. On one newsletter it
flagged three items and resolved one itself after finding support in internal documents.

**Plan for:** an instruction set that improves. A correction became a standing instruction ("verify
flagged claims in real time when possible"), and a Friday routine has Claude propose instruction
updates from the week's feedback — for human approval.

## Access and governance

- Access is **deliberately scoped**: Claude Tag reaches only the channels and documents it has been
  granted.
- When it lacks access a task needs, **users are notified** rather than getting a quiet gap.
- Grant per workflow. A review channel needs the knowledge index; a thread summarizer usually does
  not.

## Availability and setup

- Available on **Team and Enterprise** plans, through Anthropic's first-party service.
- Admin setup at **claude.ai/admin-settings/claude-tag**.
- Currently in **public beta**.

## A rollout sequence that works

1. **Pick one recurring task** whose inputs already live in chat and whose cost is finding things.
2. **Run it ad hoc first** by tagging Claude in threads, and keep the verification loop explicit.
3. **Graduate it to a channel** with standing instructions once the prompt has stabilized.
4. **Grant only the access that workflow needs**, and widen it when a notified gap justifies it.
5. **Schedule an instruction review** so corrections accumulate instead of repeating.

## Source

<https://claude.com/blog/how-anthropic-employees-use-claude-tag> (2026-08-28)
