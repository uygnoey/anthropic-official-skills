---
name: slack-thread-delegation
description: Hand a task to Claude inside a chat thread — turning a long Slack discussion into a finished document, consolidating requests scattered across channels, or running a first-pass review in a dedicated channel — and keep the output trustworthy through verification and standing instructions. Use when a decision is buried in a 15-message thread, when the same request keeps surfacing in different channels and nobody has a consolidated list, when a review queue is the bottleneck before a specialist looks at something, or when deciding what to delegate to an in-chat agent versus what to keep for human judgment.
---

# Slack thread delegation

Claude Tag puts Claude inside chat tools like Slack. You tag it in a thread and it completes tasks
using the conversation's context: it can follow the conversation, use standing instructions you
have given it, and decide when to participate.

The leverage is not that Claude writes faster. It is that the raw material — a 15-message thread,
120 scattered reports, a marketing asset and the sources that back it — is already in chat, and
gathering it is the part that costs a human hours. Delegate the synthesis; keep the judgment.

This skill covers three delegation shapes drawn from how teams at Anthropic use the feature, and
the verification loop that makes each one safe to trust.

## Instructions

### 1. Decide what to delegate

Delegate work where the inputs live in chat and the cost is information gathering:

- **Synthesis** — a thread contains a decision, a spec, or an argument that someone now needs as a
  document.
- **Consolidation** — the same class of request or report is scattered across channels and nobody
  has the list.
- **First-pass review** — a specialist reviews every item, and most items are fine.

Keep for yourself: which claims need sign-off, what the final call is, and whether the output is
right. In every workflow below, the human focuses on judgment, verification, and decision-making
while Claude handles information synthesis and processing.

### 2. Prompt for the shape of the work

The three shapes need different prompts. See
[references/prompt-patterns.md](references/prompt-patterns.md) for each pattern in full.

- **Synthesis** — point at the thread and name the artifact and its requester. A short prompt is
  enough because the thread is the specification.
- **Consolidation** — state three things: the search targets, what counts as a match, and the
  desired output format with an example row. Without the match definition Claude cannot dedupe;
  without the format example you get prose instead of a list you can act on.
- **Review** — set the rules once as standing instructions for a dedicated channel rather than
  repeating them per asset.

### 3. Verify before you circulate

Do not treat the first draft as the deliverable. Ask Claude to check its own factual accuracy, and
have it separate claims that are verified from claims that need sign-off from the owner. Then feed
it the official resources for the unverified parts and have it rewrite those sections.

In the marketing one-pager case this took four versions before the draft went to the product lead —
each round narrowing what still needed a human. Budget for that loop; it is where the quality comes
from.

### 4. Give a recurring workflow its own channel and standing instructions

For work that repeats, create a dedicated channel and write the rules once. Grant the access the
work actually needs — company chat, an internal knowledge index, the public web — and no more.

Start from [templates/review-channel-instructions.md](templates/review-channel-instructions.md) and
adapt the rules to your domain.

### 5. Make the instructions improve themselves

When you correct Claude, ask it to carry the correction forward as a standing instruction rather
than as a one-off fix. In the legal review channel, "verify flagged claims in real time when
possible" started as feedback on a single review and became the rule for all future ones.

Add a recurring review of the instructions themselves: a weekly routine where Claude reads the
feedback it received that week and proposes instruction updates for approval. Approval stays human.

### 6. Expect scoped access, and notice the gaps

Claude Tag's access is deliberately scoped — only the channels and documents it has been granted.
When it lacks the access a task needs, it tells you. Treat that message as a signal about the task,
not only about permissions: work that keeps hitting inaccessible sources may belong elsewhere.

## Examples

Full case studies with the prompts, timings, and outputs reported in the source post are in
[examples/tag-workflows.md](examples/tag-workflows.md). In brief:

**Thread to document.** A product marketer tagged Claude on a 15+ message thread with roughly "go
through this Slack thread and come up with a one pager that [the requester] is asking for." Claude
produced a two-page draft in two minutes covering feature description, business case,
implementation details, and an appendix. Four verification rounds later it went to the product
lead — 45 minutes total.

**Scattered requests to one list.** A product strategy team member asked Claude to find every place
a feature had been requested and who had asked on a customer's behalf. Claude ran roughly 20 search
variants across channels, deduplicated the results, and returned about 24 accounts with requester
handles, teams, account names, and source links in about 26 minutes. The weekly version of the same
task turned about 120 raw reports into 23 open and 14 resolved issues organized by product area in
50 minutes — work estimated at a full week by hand.

**Review queue triage.** A product counsel set up a channel where Claude reviews marketing assets
before legal review: spotting unsubstantiated claims, verifying factual statements, flagging issues
with specific remediation instructions, and working with requesters directly. On one newsletter it
flagged three items and resolved one itself after finding support in internal documents.
Turnaround went from a day to 30 minutes per asset.

## Setup

Claude Tag is available on Team and Enterprise plans through Anthropic's first-party service, set
up at `claude.ai/admin-settings/claude-tag`. It is in public beta.
