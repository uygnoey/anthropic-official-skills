# Three workflows, as reported

Case studies from Anthropic teams using Claude Tag. Numbers and prompts are as described in the
source post; treat them as reference points, not guarantees.

---

## 1. A 15-message thread becomes a review-ready one-pager

**Team:** product marketing
**Elapsed:** 45 minutes, start to shareable draft

A marketing one-pager had been requested inside a Slack thread that had grown past 15 messages. The
marketer tagged Claude in the thread itself:

> go through this Slack thread and come up with a one pager that [the requester] is asking for

**What came back in two minutes:** a two-page draft covering the feature description, the business
case, implementation details, and an appendix.

**Then the verification loop:**

1. The marketer asked Claude to verify the draft's factual accuracy.
2. Claude distinguished claims it had verified from claims that needed the product lead's sign-off.
3. The marketer supplied the official resources for the unverified claims.
4. Claude rewrote those sections against the sources.

Four versions in total before the draft went to the product lead.

**Where the time went:** not into research and drafting, which Claude absorbed, but into deciding
what was accurate and what belonged in the document.

---

## 2. Feature requests scattered across channels become one list

**Team:** product strategy
**Elapsed:** about 26 minutes

The question was which customers had asked for a particular piece of functionality, and which sales
reps had asked on their behalf — information spread across many channels with no consolidated list
anywhere.

**Prompt structure:** search targets, a definition of what counts as a match, and the desired output
format with an example.

**What Claude did:**

- Ran roughly 20 search variants across the channels.
- Deduplicated findings that appeared in more than one place.
- Returned about 24 accounts, each with the requester's Slack handle, their team, the account name,
  and a link to the source message.

### The weekly version

The same pattern, widened: consolidate every product problem reported by enterprise customers that
week.

- **Input:** roughly 120 raw reports.
- **Output:** 23 open issues and 14 resolved issues, organized by product area, each with a summary
  and a link to its source thread.
- **Elapsed:** 50 minutes.

Estimated cost of doing it by hand: about a week of full-time work. The human cost became the
minutes it took to write the instruction, plus waiting while Claude worked in the background.

---

## 3. A review channel cuts legal turnaround from a day to 30 minutes

**Team:** legal (product counsel Molly Villagra)
**Elapsed:** about 30 minutes per asset, down from a day or more

Marketing assets needed legal review, and legal was the bottleneck. The fix was a dedicated Slack
channel where Claude reviews assets *before* a lawyer sees them.

**Setup:** specific rules and instructions for Claude, plus access to company Slack, an internal
knowledge index, and the public web.

**What Claude does in the channel:**

- Spots unsubstantiated marketing claims.
- Verifies factual statements in the content.
- Flags issues with specific remediation instructions.
- Works directly with requesters to resolve what it finds.

**A concrete review:** on a newsletter, Claude flagged three items — then resolved one of them on
its own after locating the supporting information in internal documents.

### How the instructions improve

- Molly told Claude to verify flagged claims in real time where it could. Claude carried that
  forward as a standing instruction for every future review, not just that one.
- A Friday routine was added: Claude reviews the week's counsel feedback and proposes updates to
  its own instructions, which Molly approves.

---

## The common pattern

Across all three, the split is the same. Claude handles information synthesis and processing —
searching, gathering, deduplicating, drafting. The human handles judgment, verification, and
decisions. The time saved is the time that used to go into finding things.
