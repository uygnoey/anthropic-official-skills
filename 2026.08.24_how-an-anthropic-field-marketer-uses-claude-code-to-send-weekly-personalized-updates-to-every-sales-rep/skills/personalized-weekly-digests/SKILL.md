---
name: personalized-weekly-digests
description: Build and operate a recurring, per-person digest (weekly sales updates, field-marketing briefings, team roll-ups) with Claude Code. Use when a repeating update has to be personalized per recipient from CRM, event, and content data, when a manual Sunday-night briefing needs to become an automated Monday-morning send, or when an existing digest needs to be piloted, corrected through feedback, and scaled to more teams. Covers framing the business problem instead of the technical one, showing the output format by example, wiring real data sources, converting each piece of recipient feedback into an explicit content rule, and surviving schema drift in source spreadsheets.
---

# Personalized weekly digests

A recurring update loses its value when there is no time to personalize it. The pattern in this
skill turns a hand-built briefing into a system that composes one message per recipient, and it
treats every correction from a recipient as a rule that gets written down rather than remembered.

The approach comes from a field marketer at Anthropic who replaced a Sunday-evening slide deck
with an automated Monday-morning digest for every sales rep he supported. The first version took
about an hour to build; the value came from the weeks of pilot feedback that followed.

## Instructions

### 1. Brief the business problem, not the implementation

You do not need coding skills to build this. You need to explain the problem clearly.

- Open by describing your challenge and positioning yourself as the product manager of the
  output, not the technician building it.
- Give business context the way you would brief a new colleague. Recording a voice explanation
  of the problem is an effective way to get the full context across.
- Use [templates/kickoff-prompt.md](templates/kickoff-prompt.md) as the opening brief.

### 2. Show the output format with a template example

Abstract instructions about tone and structure underperform a concrete example of what a good
message looks like. Provide a filled-in sample.

- Structure the message around the "top three things for the week," prioritizing items the
  recipient can act on.
- Use [templates/digest-message-template.md](templates/digest-message-template.md) as the shape,
  and fill it in once by hand so Claude has a target to match.

### 3. Connect the real data sources

Personalization comes from joining the recipient to the data, not from generic phrasing.

- Connect Claude to your marketing/CRM warehouse over MCP. In the source case that was BigQuery,
  which itself pulls from HubSpot, Clay, and Salesforce.
- Pull the recipient's territory from the CRM, relevant account updates from Slack, and match
  those against the current marketing initiatives.
- Expand the source set over time — blog articles, eBooks, customer stories, webinars, and
  partner ecosystem events all became part of the briefing.
- See [references/data-sources.md](references/data-sources.md) for the wiring and for the
  schema-drift instructions below.

### 4. Make the prompt survive schema drift

Source spreadsheets change without warning. The field events sheet in the source case rearranged
its columns three times in six weeks.

- Instruct Claude to read the header row and verify the column mapping before processing rows.
- Refer to columns semantically — "look at the column with the event URL" — instead of
  hard-coding column positions or letters.

### 5. Pilot with a committed group and route early runs to yourself

- Pick one team small enough to give real feedback and willing to invest in it; the source pilot
  was a single sales team of ten reps.
- Send early runs to yourself first and judge the output against the quality baseline you
  already hold from doing the task by hand.
- Only widen distribution once the obvious data-quality and relevance failures are gone.

### 6. Convert every correction into an explicit rule

This is the core operating loop. Each piece of feedback becomes a documented rule, and you track
which rule came from which feedback. After the first week the source prompt held nine explicit
content rules.

Rules that emerged in the source case:

- **Never invent a URL.** Claude had produced plausible-looking URLs for events that were missing
  registration links. Render links only from exact source data.
- **Verify contact titles against the event audience.** Engineering VPs were being invited to
  knowledge-worker workshops.
- **Gate by industry.** Retail accounts should not receive finance-focused events.
- **Handle the empty case.** New sellers without assigned accounts were getting blank messages;
  they need a custom welcome note instead.

The full catalog is in [references/content-rules.md](references/content-rules.md), and worked
conversions from raw feedback to rule text are in
[examples/feedback-to-rule.md](examples/feedback-to-rule.md).

### 7. Version the prompt as it grows

- Save each update as a numbered version with a one-line change note.
- Start in a document, and move to a collaborative platform such as GitHub as more of the team
  needs access.

### 8. Scale by duplicating, then changing the mapping field

Each new audience is a copy of the working prompt with the one field that describes how that
audience maps to accounts in the CRM changed. In the source case, a BDR version launched two
days after the request; customer success, alliances, and cross-functional partners followed.

### 9. Run it as an operational system

- Archive every send for audit and accountability.
- Give managers a consolidated roll-up of their team's recommendations.
- Move from approving each send to reviewing output, so the system keeps running when you are
  away.

## Examples

### Framing the opening brief

> I'm a field marketer supporting three sales segments. Every Monday each rep needs to know the
> three things that matter for their accounts this week. I'm the product manager for this
> output, not the engineer — here's the problem, and here's what a good message looks like.

Attaching a filled-in sample message alongside this framing does more than any amount of
description of the desired tone.

### A rule written from a single piece of feedback

Feedback: *"You sent me a registration link that 404s."*

Rule added to the prompt:

> Never invent a URL. Only render a link when the exact URL is present in the source data. If an
> event has no registration link, name the event and omit the link rather than constructing one.

### A column reference that survives a reshuffled sheet

Instead of "column D holds the event URL," write:

> Read the header row first and map each needed field by its header name. Look at the column with
> the event URL. Confirm the mapping before reading any data rows; if a required header is
> missing, stop and report it rather than guessing.

### Standing up a second audience

The account-executive prompt already works. For BDRs, duplicate it and change only the field
describing how BDRs map to accounts in the CRM — BDRs map differently from AEs. Everything else,
including the nine content rules, carries over unchanged.

## Source

- https://claude.com/blog/how-an-anthropic-field-marketer-uses-claude-code-to-send-weekly-personalized-updates-to-every-sales-rep (published 2026-08-24, by Adam Ward)
