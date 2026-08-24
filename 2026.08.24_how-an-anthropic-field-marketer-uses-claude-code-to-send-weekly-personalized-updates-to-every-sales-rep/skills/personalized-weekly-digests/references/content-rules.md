# Content rules

Every rule here exists because a recipient reported something wrong. After the first week of the
pilot in the source case, the prompt contained nine explicit content rules, each traceable to
specific feedback. Keep that traceability: record which feedback produced which rule, so a rule
can be revisited when the underlying reason changes.

## Data-integrity rules

### Never invent a URL

Claude had produced plausible-looking URLs for events that were missing registration links.

> Render a link only when the exact URL is present in the source data. If an event has no
> registration link, name the event and omit the link. Do not construct, guess, or pattern-match
> a URL from other events.

### Verify the column mapping before reading data

The field events sheet rearranged its columns three times in six weeks.

> Read the header row first and map each required field by header name. Refer to columns
> semantically — "the column with the event URL" — never by position or letter. Confirm the
> mapping before processing any data rows, and stop and report if a required header is missing.

## Relevance rules

### Match contact titles to the event audience

Engineering VPs were being invited to knowledge-worker workshops.

> Check the titles of the contacts at the rep's accounts against the stated audience of the event.
> Do not surface an event whose audience does not match the titles available at those accounts.

### Gate by industry

Retail accounts were receiving finance-focused events.

> Apply an industry gate. An event scoped to an industry may only appear for accounts in that
> industry.

## Completeness rules

### Never send a blank message

New sellers without assigned accounts were receiving empty messages.

> If a recipient has no accounts assigned in the CRM, do not emit the standard structure. Write a
> custom welcome note appropriate to a new seller instead.

### Prefer fewer real items over padding

> If fewer than three actionable items exist for a recipient this week, send fewer. Do not fill
> the list with generic content to reach three.

## Adding a rule

1. Capture the feedback verbatim, with the recipient and date.
2. Write the rule as an instruction Claude can follow without knowing the backstory.
3. Note the originating feedback next to the rule.
4. Save the prompt as a new numbered version with a one-line change note.

Worked examples of steps 1–3 are in `examples/feedback-to-rule.md`.

## Note on scope

The source article names the rules above and states that the prompt reached nine explicit rules
after the first week; it does not enumerate all nine. Treat this file as the starting catalog and
grow it from your own recipients' feedback rather than inventing the remainder.

## Source

- https://claude.com/blog/how-an-anthropic-field-marketer-uses-claude-code-to-send-weekly-personalized-updates-to-every-sales-rep
