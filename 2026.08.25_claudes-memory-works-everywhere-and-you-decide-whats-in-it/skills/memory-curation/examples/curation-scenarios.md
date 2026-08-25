# Curation scenarios

The situations below are the ones the announcement describes. Each pairs the situation with the
memory behavior that handles it.

## Drafting an update for a manager

**Situation.** You ask Cowork to draft an update for your manager.

**Behavior.** It already knows who that is and how she likes updates written, because that came
up in chat earlier. No re-briefing at the start of the Cowork task.

**Curation note.** If the recipient or their preference changes, edit the topic file that holds
it rather than correcting each draft.

## Conference planning that starts in chat and finishes in Cowork

**Situation.** You brainstorm the agenda for a conference you're organizing in chat. Later,
Cowork builds the budget and logistics doc.

**Behavior.** The doc knows the headcount, the city, and the speakers — the details established
during the chat session are in the shared memory.

**Curation note.** This is the bidirectional path in practice: what came up in chat reaches
Cowork, and what surfaces during the Cowork task carries back to chat.

## Metric definitions reused across quarterly decks

**Situation.** You explain once, in chat, how your team defines its metrics.

**Behavior.** Every quarterly business review deck Cowork builds after that uses those
definitions, with no rebriefing.

**Curation note.** When a definition changes, the change belongs in the topic file. Editing
once beats restating it per deck.

## A deadline that moved

**Situation.** Mid-conversation, you mention that your project deadline moved to September.

**Behavior.** Because Claude adds topics to memory as you chat rather than summarizing after
the conversation ends, your next conversation already knows — you never have to say
"remember this".

**Curation note.** If a date shifts again, the topic file is the place to correct it.

## A company that changed its name

**Situation.** Claude keeps using your company's old name.

**Behavior.** The name lives in one short topic file. Correct it there and every conversation
from then on gets it right.

**Curation note.** This is the general shape of a memory fix: one file, one edit, applied
everywhere — instead of a correction repeated in each conversation.

## A gluten allergy for meal planning

**Situation.** You want Claude to account for a gluten allergy when suggesting recipes for
weekly meal prep.

**Behavior.** Health is a sensitive topic and is excluded from memory by default. Turning on
"include sensitive topics in memory" lets Claude remember it. Each save in these areas comes
with a notice, only new information is stored, and the setting can be turned off at any time.

**Curation note.** The post's framing is that what some consider sensitive, others consider
useful for Claude to remember. The choice belongs to the user.

## Something Claude will not store

**Situation.** You try to have Claude remember a sensitive identification number, criminal
history, or immigration status.

**Behavior.** These are excluded even with sensitive topics turned on, along with anything that
violates the Acceptable Use Policy. Claude tells you when it is unable to update memory with
this kind of information.

**Curation note.** There is no setting that changes this. Treat it as a boundary of the
feature, not a configuration problem.

## Source

- https://claude.com/blog/claudes-memory-works-everywhere-and-you-decide-whats-in-it (published 2026-08-25)
