**English** · [한국어](./automating-a-recurring-personalized-briefing.ko.md) · [Español](./automating-a-recurring-personalized-briefing.es.md) · [日本語](./automating-a-recurring-personalized-briefing.ja.md)

# Automating a recurring personalized briefing

A rollout methodology for turning a hand-built recurring update into an automated, per-recipient
system — drawn from how an Anthropic field marketer replaced a Sunday-evening slide deck with a
Monday-morning digest for every sales rep he supported.

## The shape of the problem

The manual version fails in a predictable way. It works while you support one team. As you take
on more teams, the preparation time grows linearly, and the first thing you cut is the
personalization — the part that made the update worth reading. You end up spending more time to
deliver something less useful.

Automation is not the goal here; personalization at scale is. The automation is what makes the
personalization affordable.

## Stage 1 — Build the first version fast

The source system was built in about an hour, during a marketing hackathon: a dedicated block of
time set aside for rebuilding processes with Claude.

Three things go into that hour:

1. **A brief describing the business problem**, with you positioned as the product manager of the
   output rather than the technician building it. You do not need coding skills; you need to
   explain your problem clearly.
2. **Business context delivered as you would to a new colleague** — recording a voice explanation
   of the problem works well for the history and constraints you would otherwise skip.
3. **A template example of the desired output**, structured as the top three things for the week
   with actionable items first.

Do not try to get the data model right in this hour. Get one plausible message for one recipient.

## Stage 2 — Wire the real data

Connect the warehouse rather than the individual tools. In the source case that was BigQuery over
MCP, itself fed by HubSpot, Clay, and Salesforce.

The personalization join is: the rep's territory from the CRM, relevant account updates from
Slack, matched against current marketing initiatives. Over time the content set widened to blog
articles, eBooks, customer stories, webinars, and partner ecosystem events.

Assume source schemas will move. The field events spreadsheet rearranged its columns three times
in six weeks. The durable fix is semantic column mapping: have Claude read the header row and
verify the mapping before processing, referring to "the column with the event URL" rather than a
fixed position.

## Stage 3 — Pilot with a committed group

Pick one team, small enough to give real feedback and willing to invest in giving it. The source
pilot was a single sales team of ten reps who had agreed to respond.

Route early runs to yourself before they go to anyone else, and judge the output against the
quality baseline you already carry from having done the task by hand.

The pilot exists to surface failures you would not predict. In the source case those were:

- **Fabricated data.** Plausible URLs invented for events that had no registration link.
- **Relevance failures.** Engineering VPs surfaced for knowledge-worker workshops; retail accounts
  shown finance-focused events.
- **Unhandled empty cases.** New sellers with no assigned accounts receiving blank messages.

## Stage 4 — Convert feedback into explicit rules

This is the stage that actually builds the system. Each correction becomes a documented rule in
the prompt, and you track which rule came from which feedback. After the first week the source
prompt held nine explicit content rules.

Rules named in the source case include: never invent a URL and render links only from exact
source data; verify contact titles against the event audience; gate events by account industry;
and write a custom welcome note for new sellers who have no accounts yet.

Version the prompt as it grows — each update saved as a numbered version with a one-line change
note. Start in a document and move to a collaborative platform such as GitHub as more of the team
needs access.

## Stage 5 — Scale by duplication

Each additional audience is the working prompt copied, with one field changed: how that audience
maps to accounts in the CRM. BDRs map differently from account executives, so that field is the
whole difference. In the source case the BDR version launched two days after it was requested.
Customer success, alliances, and cross-functional partners outside sales followed.

## Stage 6 — Make it operational

- **Archive every send** for audit and accountability.
- **Give managers a consolidated roll-up** of the recommendations made to their team.
- **Move from approval to review.** The point of arrival is that you read the output but are no
  longer a gate on it. The source system ran on its own while its author was on holiday.

## What to measure

The source case reports one concrete result: registrations for an executive dinner doubled within
a week of the digest rolling out, attributed to the right reps getting relevant information on
Monday morning. Pick the downstream action your briefing is supposed to drive and measure that,
rather than measuring the briefing itself.

## Getting started checklist

1. Choose a repetitive task you already do by hand, so you have a quality baseline to judge
   against.
2. Brief Claude in plain language, as you would a new colleague.
3. Route the first runs to yourself.
4. Pilot with a small, committed group.
5. Turn every correction into a rule, and note which feedback produced it.
6. Version each prompt update with a one-line change note.
7. Duplicate and change the mapping field for each new audience.

## Source

- https://claude.com/blog/how-an-anthropic-field-marketer-uses-claude-code-to-send-weekly-personalized-updates-to-every-sales-rep (published 2026-08-24, by Adam Ward)
