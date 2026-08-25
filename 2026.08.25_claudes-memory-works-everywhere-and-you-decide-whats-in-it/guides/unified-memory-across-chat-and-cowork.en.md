**English** · [한국어](./unified-memory-across-chat-and-cowork.ko.md) · [Español](./unified-memory-across-chat-and-cowork.es.md) · [日本語](./unified-memory-across-chat-and-cowork.ja.md)

# Unified memory across chat and Cowork

## What changed

As of 2026-08-25, the memory you use in chat is the same memory Claude Cowork uses. Wherever
you work with Claude, it starts from what it already knows about you.

Three changes ship alongside that:

1. **Memory updates as you chat.** Claude adds topics to memory during the conversation instead
   of summarizing it after it ends.
2. **Saved memories are visible and editable.** Everything Claude remembers appears as a list of
   short files under **Topics** in Memory settings.
3. **You decide the boundary.** Sensitive subjects are excluded by default and can be turned on;
   a small set of categories is never stored either way.

## How the shared memory behaves

The store is one store, read and written from both surfaces:

- When Cowork runs a task in the cloud, what Claude remembers from your chats is there.
- What comes up during a Cowork task carries back to chat.
- Context built over months of conversations — Q3 priorities, project status — is present the
  moment you hand Cowork a task.

In practice that removes the re-briefing step at the start of delegated work:

- Ask Cowork to draft an update for your manager and it already knows who that is and how she
  likes updates written.
- Brainstorm a conference agenda in chat; the budget and logistics doc Cowork builds knows the
  headcount, the city, and the speakers.
- Explain how your team defines its metrics once, and every later quarterly business review deck
  uses those definitions with no rebriefing.

## Reviewing and correcting what is stored

Open **Settings > Memory** and look under **Topics**. Each entry is a short file you can read,
edit, or delete.

The files being short and separate is what makes correction cheap: fix your company's old name
in one file and every conversation from then on gets it right, on both surfaces. Prefer editing
a file when part of it is stale and deleting it when the whole topic is obsolete.

Memory can also be paused or reset at any time — pause for work that should not shape later
conversations, reset when the accumulated context no longer matches your situation.

## Deciding about sensitive topics

By default, Claude does not store topics related to personal or sensitive subject matter: health,
race, ethnicity, religious beliefs, politics, gender identity, and other similar areas.

What one person considers sensitive, another considers useful for Claude to remember. If you turn
on **"include sensitive topics in memory"**, Claude will remember things like a gluten allergy
when suggesting recipes for weekly meal prep. Three properties matter for the decision:

- **Visible.** You see a notice each time Claude saves something on one of these topics.
- **Forward-only.** Claude saves sensitive topics going forward; nothing from before you turned
  the setting on is saved retroactively.
- **Reversible.** You can turn the setting off at any time.

### Never stored

Regardless of that setting, Claude does not store sensitive identification numbers (SSN,
government ID numbers, and the like), criminal history, immigration status, or anything that
violates the Acceptable Use Policy. Claude will tell you when it is unable to update memory to
include this information. The Help Center covers this in more detail.

## Availability and rollout

| Plan | Memory | Sensitive topics |
| --- | --- | --- |
| Free, Pro, Max | On by default, across web, desktop, and mobile | Off by default |
| Team, Enterprise | Admins control availability for the organization; off for individual users until they turn it on | Off by default |

On iOS and Android, update to the latest version of the mobile app to get the most recent
updates.

### For Team and Enterprise admins

- Availability is an organization-level decision you make first; individual users then turn
  memory on for themselves.
- Saving sensitive topics stays off by default, so enabling memory for the organization does not
  by itself put health, belief, or identity information into the store.
- Tell people where the controls are — **Settings > Memory** — and that the Topics list is
  readable and editable, so reviewing what is stored is part of normal use rather than a support
  request.

## Getting started

1. Open **Settings > Memory** and confirm memory is on (on Team and Enterprise, after your admin
   has enabled it for the organization).
2. Read the **Topics** list once end to end. Correct anything stale; delete anything obsolete.
3. Decide, deliberately, whether to turn on sensitive topics.
4. Explain a piece of recurring context once in chat, then hand a related task to Cowork and
   confirm it carried.

## Source

- https://claude.com/blog/claudes-memory-works-everywhere-and-you-decide-whats-in-it (published 2026-08-25)
