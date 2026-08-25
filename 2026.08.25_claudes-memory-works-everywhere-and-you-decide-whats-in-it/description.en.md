**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude's memory works everywhere, and you decide what's in it

## What is this post?

A product announcement: the memory you use in chat is now the same memory used in Claude Cowork. Wherever you work with Claude, it starts from what it already knows about you. Everything Claude remembers is visible topic by topic in Memory settings, and you can read, edit, or delete any of it.

The post also covers three related changes: memory now updates while you chat instead of summarizing conversations after they end; sensitive subjects are excluded from memory by default but can be turned on; and some categories are never stored regardless of settings.

## When is it useful?

- You keep re-explaining the same context — your priorities, your team's metrics, who your manager is — every time you move between chat and Cowork.
- You want to see and correct what Claude has stored about you instead of guessing at it.
- You are deciding whether to turn on "include sensitive topics in memory" and want to know exactly what that changes.
- You administer a Team or Enterprise organization and need to know who controls memory availability.

## Key points

- **One memory across Cowork and chat.** Cowork now has memory, and it is the same one used in chat. When Cowork runs a task in the cloud, what Claude remembers from your chats is there, and what comes up in Cowork carries back to chat. Context built over months of conversations — Q3 priorities, project status — is present the moment you hand Cowork a task.
- **Explaining once is enough.** Ask Cowork to draft an update for your manager and it already knows who that is and how she likes updates written. Brainstorm a conference agenda in chat, and the budget and logistics doc Cowork builds knows the headcount, the city, and the speakers. Explain how your team defines its metrics once, and later quarterly business review decks use them without rebriefing.
- **Memory updates as you chat.** Claude adds topics to memory during the conversation rather than summarizing after it ends. Mention that a deadline moved to September and the next conversation already knows, with no "remember this" needed. Memory can be paused or reset at any time.
- **Saved memories are editable files.** Everything Claude remembers appears as a list of files under Topics in Memory settings, where each one can be read, edited, or deleted. The files are short, and one fix pays off everywhere: correct your company's old name in one file and every later conversation gets it right.
- **Sensitive topics are off by default.** By default Claude does not store topics related to personal or sensitive subject matter — health, race, ethnicity, religious beliefs, politics, gender identity, and similar areas. Turning on "include sensitive topics in memory" lets Claude remember things like a gluten allergy when suggesting weekly meal-prep recipes.
- **The sensitive setting is forward-only and visible.** With it on, you see a notice each time Claude saves something on one of these topics. Only new information is saved; nothing from before you turned it on is captured retroactively. The setting can be turned off at any time.
- **Some things are never stored.** Even with sensitive topics on, Claude does not store sensitive identification numbers (SSN, government ID numbers), criminal history, immigration status, or anything violating the Acceptable Use Policy. Claude tells you when it cannot update memory with such information.
- **Availability.** Memory is on by default on Free, Pro, and Max plans across web, desktop, and mobile; saving sensitive topics is off by default. On iOS and Android, update to the latest app version. For Team and Enterprise, admins control availability for the organization, and memory is off for individual users until they turn it on. Controls live under Settings > Memory.

## Bundled resources

- `skills/memory-curation/SKILL.md` — audit, correct, and scope what Claude keeps in memory.
- `skills/memory-curation/references/memory-controls.md` — the settings, storage rules, and availability matrix from the post.
- `skills/memory-curation/templates/topic-review-checklist.md` — a pass-by-pass checklist for reviewing a topic file.
- `skills/memory-curation/examples/curation-scenarios.md` — the worked situations described in the post.
- `guides/unified-memory-across-chat-and-cowork.{en,ko,es,ja}.md` — what changed and how to roll it out, in four languages.

## Source

- https://claude.com/blog/claudes-memory-works-everywhere-and-you-decide-whats-in-it (published 2026-08-25)
