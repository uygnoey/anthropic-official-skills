---
name: memory-curation
description: Audit, correct, and scope what Claude keeps in memory across chat and Cowork. Use when the user asks what Claude remembers about them, wants to fix or delete a saved memory topic, keeps re-explaining the same context between chat and Cowork, is deciding whether to turn on "include sensitive topics in memory", or needs to know which categories are never stored and who controls availability on Team and Enterprise plans.
---

# Memory curation

Claude's memory is shared between chat and Claude Cowork: one store, visible as a list of
short topic files, editable by the user. This skill covers reading that store, correcting it,
and deciding what should be allowed into it.

The behavior described here comes from the product announcement of 2026-08-25; see
[references/memory-controls.md](references/memory-controls.md) for the settings, storage
rules, and availability details in full.

## Instructions

### 1. Establish what is actually stored

Memory content lives in Memory settings under **Topics**, as a list of files. Before advising
on anything, have the user open that list rather than guessing:

- Each entry is a short file that can be read, edited, or deleted individually.
- The same store is used by chat and by Cowork, including Cowork tasks running in the cloud.
- Claude adds topics **during** a conversation, not by summarizing it afterwards, so recent
  turns may already be reflected.

If the user cannot find the list, the path is **Settings > Memory**.

### 2. Correct at the source, once

When Claude uses stale or wrong context, the fix belongs in the topic file, not in a
per-conversation correction:

- Locate the topic file holding the wrong fact.
- Edit that one file (for example, replace a company's old name with the current one).
- Every conversation from then on picks up the corrected version — in chat and in Cowork.

Prefer editing over deleting when only part of a file is wrong; delete the file when the
whole topic is obsolete. Walk through [templates/topic-review-checklist.md](templates/topic-review-checklist.md)
for a repeatable pass over a single file.

### 3. Use memory instead of re-briefing

If the user is repeating context across surfaces, the answer is usually to explain it once in
chat and let it carry:

- Say who a recipient is and how they like updates written, then ask Cowork for the draft.
- Work out a plan in chat (headcount, city, speakers), then ask Cowork for the doc built on it.
- Define the team's metrics once; later decks reuse those definitions without rebriefing.

Worked situations from the announcement are collected in
[examples/curation-scenarios.md](examples/curation-scenarios.md).

### 4. Scope sensitive topics deliberately

By default Claude does **not** store personal or sensitive subject matter — health, race,
ethnicity, religious beliefs, politics, gender identity, and similar areas.

When a user asks Claude to remember something in one of those areas:

- Explain that the **"include sensitive topics in memory"** setting governs it.
- State the three properties that matter for the decision: saves are announced with a notice,
  storage applies **going forward only** (nothing before activation is captured retroactively),
  and the setting can be turned off at any time.
- Let the user make the call. Do not push in either direction — what one person considers
  sensitive, another considers useful context.

### 5. Know the hard limits

Some categories are never stored, even with sensitive topics turned on:

- Sensitive identification numbers (SSN, government ID numbers)
- Criminal history
- Immigration status
- Anything that violates the Acceptable Use Policy

Claude informs the user when it cannot update memory with such information. Do not offer
workarounds for these categories; note the limit and move on.

### 6. Check availability before troubleshooting

If memory appears to be missing entirely, check the plan before anything else:

- **Free, Pro, Max** — memory is on by default across web, desktop, and mobile; saving
  sensitive topics is off by default. On iOS and Android, the app must be on the latest version.
- **Team, Enterprise** — admins control availability for the organization, and memory is off
  for each individual user until they turn it on.

### 7. Pause or reset when the context is wrong for the work

Memory can be paused or reset at any time. Suggest pausing for a session that should not
influence later ones, and resetting when the accumulated context no longer matches the user's
situation. Both are reversible choices the user makes; make the consequence explicit before
a reset, since it clears what has been built up.

## Examples

**"What does Claude actually know about me?"**
Point to Settings > Memory > Topics. Explain that each entry is a short, readable file, that
the same list backs both chat and Cowork, and that anything there can be edited or deleted.

**"Claude keeps calling my company by its old name."**
This is a stored-fact problem, not a prompting problem. Have the user open the topic file
containing the company name and correct it there. One edit fixes every later conversation on
both surfaces instead of a correction repeated per chat.

**"I told Cowork about my Q3 priorities last month and it forgot."**
Check availability first: on Team or Enterprise, an admin must enable memory and the user must
turn it on individually. If memory is on, check the Topics list — if the priorities are not
there, they were never captured; restate them in chat and confirm the topic appears.

**"Remember that I'm gluten intolerant so meal plans work."**
Health is a sensitive topic and is excluded by default. Explain the
"include sensitive topics in memory" setting, that saves in these areas come with a notice,
that it only applies going forward, and that it can be switched off later. Then let the user
decide.

**"Save my passport number so I don't have to look it up."**
Sensitive identification numbers are never stored, regardless of the sensitive-topics setting.
Say so plainly, note that Claude reports when it cannot update memory with such information,
and do not propose an alternative storage trick.

**"Our team's QBR decks keep using the wrong definition of active users."**
Have the user state the team's metric definitions once in chat and confirm a topic file was
written for them. Later Cowork decks then build on those definitions with no rebriefing; if a
definition changes, edit the file rather than restating it per deck.
