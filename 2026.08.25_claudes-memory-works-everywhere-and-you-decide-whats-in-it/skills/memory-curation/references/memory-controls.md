# Memory controls reference

Everything below is drawn from the 2026-08-25 announcement, "Claude's memory works everywhere,
and you decide what's in it". Where the post does not say, this file says nothing — check the
source or the Help Center.

## Where the controls live

**Settings > Memory.** That page holds the on/off control, the sensitive-topics setting, and
the **Topics** list of saved memory files.

## What the memory store is

| Property | Behavior |
| --- | --- |
| Scope | One memory shared by chat and Claude Cowork, including Cowork tasks run in the cloud |
| Direction | Bidirectional — chat context reaches Cowork, Cowork context returns to chat |
| Shape | A list of files under **Topics**, one per topic; the files are short |
| User control per file | Read, edit, or delete any file |
| Effect of an edit | Applies to every conversation from then on, on both surfaces |
| When it is written | During the conversation, as topics come up — not by summarizing after it ends |
| Global controls | Memory can be paused or reset at any time |

## Sensitive topics

**Default: off.** Claude does not store topics related to personal or sensitive subject matter.
Named in the post: health, race, ethnicity, religious beliefs, politics, gender identity, "and
other similar areas".

Turning on **"include sensitive topics in memory"**:

- Claude may then remember such details — the post's example is a gluten allergy informing
  weekly meal-prep recipe suggestions.
- A notice appears each time Claude saves something on one of these topics.
- Storage is **forward-only**: anything from before the setting was turned on is not saved
  retroactively.
- The setting can be turned off at any time.

## Never stored

Excluded even with sensitive topics turned on:

- Sensitive identification numbers (SSN, government ID numbers, etc.)
- Criminal history
- Immigration status
- Anything that violates the Acceptable Use Policy (AUP)

Claude tells the user when it is unable to update memory to include this kind of information.
The post points to the Help Center for more detail.

## Availability

| Plan | Memory | Sensitive topics | Notes |
| --- | --- | --- | --- |
| Free, Pro, Max | On by default | Off by default | Web, desktop, and mobile |
| Team, Enterprise | Admin controls availability for the organization; off for individual users until they turn it on | Off by default | — |

On iOS and Android, update to the latest version of the mobile app to get the most recent
updates.

## Source

- https://claude.com/blog/claudes-memory-works-everywhere-and-you-decide-whats-in-it (published 2026-08-25)
