# What a long run looks like

The runs described in the source post, and what distinguishes the good ones from the ones that get
tuned out.

---

## The eight-hour run

Alberti's account, verbatim:

> "There have been tasks where I was about to go to bed and I was like, 'Okay, just please keep
> working on this and don't stop until I wake up.' And then I wake up, and it's been working for eight
> hours straight and actually making real progress. I hadn't seen that before."

Two clauses matter equally. *Eight hours straight* is the horizon. *Actually making real progress* is
the part that earlier long runs failed — an agent can stay busy indefinitely without staying on task.

The stated reason the horizon held: the model stayed clear-headed in messy context. It was the first
model to properly use Cognition's internal debugging tools, paging through logs in the browser and
drawing conclusions despite the noise.

---

## The migration, before and after

**Before.** A database migration where a prior Opus model technically finished the job but introduced
a series of subtle bugs along the way. The task completed. The damage was downstream and quiet — which
for Devin's customers, ranging from high-growth startups to Fortune 500 companies, is exactly the
expensive kind.

**After.** On a migration that had tripped up earlier models, Claude Fable 5 stated the invariants it
would hold itself to, then executed against them.

The difference is not effort or intelligence applied to the individual steps. It is that the run had a
declared standard to be checked against at every intermediate state, rather than only a definition of
done.

---

## Triage, before and after

**Before — the pattern engineers learned to ignore.** Earlier models tended to stay at the surface of
the logs instead of digging for the relevant line, and they were trained to give an answer no matter
what. So they would, in Alberti's words, "confidently claim the first plausible thing they discover
and then stop."

The cost compounds: once engineers have been burned, they tune the model out even on the occasions it
is right.

**After — what rebuilt trust.** On triage, the model pinned down the root cause **and said what it
didn't know**. Alberti identifies the second half as the load-bearing part.

An answer with a stated boundary can be acted on: you know which part to verify. A confident answer
with no boundary forces you to verify all of it, which is the same as doing the triage yourself.

---

## Where long runs go next

Cognition's founding bet was that agents should run in the cloud for hours at a time. For the
company's first year, the models weren't there yet. Alberti says Claude Fable 5 makes the full version
of that bet viable, and some of it is already in the product:

- Devin can watch a Slack channel and jump into an issue without being tagged.
- It can monitor production and triage a spike on its own.

> When it gets one of those right, he says, it feels "like a real engineer on the team."

He expects proactive sessions to become the default: in a year or two, 90% of agent sessions being
ones that find a problem, scan the codebase, and message you with the fix.

> "A lot of these things we've always wanted to build at the company are now possible."

---

## Source

[Working at the frontier: How Cognition trusts Claude Fable 5 to work through the night](https://claude.com/blog/working-at-the-frontier-how-cognition-trusts-claude-fable-5-to-work-through-the-night) — Claude blog, July 10, 2026.
