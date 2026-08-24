# From feedback to rule: worked examples

The operating loop of this system is that each correction from a recipient becomes a documented
rule in the prompt. These are the conversions reported in the source case, written out in the
three-part form: what came back, what it actually means, and the rule text that went into the
prompt.

---

## 1. The broken registration link

**Feedback.** A rep clicked a registration link in their digest and it went nowhere.

**Diagnosis.** The source row for that event had no registration URL. Rather than leaving the
field empty, Claude produced a plausible-looking URL.

**Rule added.**

> Never invent a URL. Render a link only when the exact URL is present in the source data. If an
> event has no registration link, name the event and omit the link. Do not construct or
> pattern-match a URL from other events.

---

## 2. The wrong audience

**Feedback.** A rep pointed out that a VP of Engineering at one of their accounts had been
surfaced as an invitee for a knowledge-worker workshop.

**Diagnosis.** Events were being matched to accounts by territory alone, with no check against
the event's stated audience.

**Rule added.**

> Check the titles of the contacts at the rep's accounts against the stated audience of the
> event. Do not surface an event whose audience does not match the titles available at those
> accounts.

---

## 3. The industry mismatch

**Feedback.** Retail accounts were being shown finance-focused events.

**Diagnosis.** Nothing in the prompt tied an industry-scoped event to account industry.

**Rule added.**

> Apply an industry gate. An event scoped to an industry may only appear for accounts in that
> industry.

---

## 4. The blank message

**Feedback.** New sellers received a digest with nothing in it.

**Diagnosis.** They had no accounts assigned in the CRM yet, so every section resolved to empty.
The template had no empty case.

**Rule added.**

> If a recipient has no accounts assigned in the CRM, do not emit the standard structure. Write a
> custom welcome note appropriate to a new seller instead.

---

## 5. The reshuffled spreadsheet

**Feedback.** Event details came out scrambled — dates in the location field, and similar.

**Diagnosis.** Not recipient feedback about content but a source-system change: the field events
sheet had rearranged its columns. It did so three times in six weeks.

**Rule added.**

> Read the header row first and map each required field by header name. Refer to columns
> semantically — "the column with the event URL" — never by position. Confirm the mapping before
> processing any data rows; if a required header is missing, stop and report it rather than
> guessing.

---

## Recording the conversion

Keep the middle column of this table alongside the prompt, not just in your head. It is what lets
you retire a rule when the reason behind it disappears.

| Rule | Originating feedback | Version added |
| --- | --- | --- |
| Never invent a URL | Broken registration link reported by pilot rep | v2 |
| Title/audience check | VP Engineering invited to knowledge-worker workshop | v3 |
| Industry gate | Retail account shown finance event | v3 |
| New-seller welcome note | Blank digest to reps with no accounts | v4 |
| Header-row column mapping | Field events sheet reshuffled columns | v5 |

Version numbers above are illustrative of the numbering practice — save each prompt update as a
numbered version with a one-line change note.

## Source

- https://claude.com/blog/how-an-anthropic-field-marketer-uses-claude-code-to-send-weekly-personalized-updates-to-every-sales-rep
