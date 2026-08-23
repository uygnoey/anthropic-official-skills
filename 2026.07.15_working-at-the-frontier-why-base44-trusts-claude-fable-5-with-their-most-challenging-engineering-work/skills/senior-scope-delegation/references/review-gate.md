# The review gate

What the post states about how Base44 ships work the model produced.

## The arrangement

> "Now, the model executes tasks while Orlev's team reviews, tests, and approves the code before
> shipping it."

Three things, in order: **review**, **test**, **approve**. Then ship.

The distinction worth holding: review did not go away. What went away was steering during the work.
Earlier, the constraint was that this tier of change "had to wait for Base44's top three engineers or a
specialist to free up" — the senior engineer's time was needed *for the work*. Now it is needed for the
gate.

## What makes same-day shipping defensible

Base44 used its **A/B testing infrastructure** to measure and ship the rebuilt system prompt the same
afternoon the model finished.

The sequence in full:

1. ~1 hour of back-and-forth questions.
2. 4 hours of unattended work.
3. 90–95% of what the team needed, returned.
4. Reviewed, tested, approved.
5. Measured and shipped via A/B infrastructure — that afternoon.

Without step 5, a same-afternoon ship of a change to a system prompt with hundreds of permutations
would be a leap. The measurement infrastructure is what converts "the model returned 90–95%" into a
shippable decision.

## What the model added to the gate

While working, Claude Fable 5 flagged a gap in Base44's own evals: the team was not testing for cache
hits, even though a prompt change can break the cache, and at the scale of millions of users that
drives up cost.

So the gate itself was incomplete, and the model raised the blind spot rather than passing through it.
Worth noting when designing a review gate: the thing being reviewed can also tell you what the gate is
not checking.

## What widened afterward

Orlev now encourages product managers and designers to build in parts of the platform they were
previously not willing to touch for fear of breaking anything. The review gate is what makes that safe
— the work is no longer restricted by who can write it, only checked by who can approve it.

## What the post does not specify

- Who performs the review, or whether it differs by blast radius.
- Which A/B metrics gate a ship.
- How long review takes relative to the run.
- What happens to the remaining 5–10% the model does not return.

## Source

[Working at the frontier: Why Base44 trusts Claude Fable 5 with their most challenging engineering work](https://claude.com/blog/working-at-the-frontier-why-base44-trusts-claude-fable-5-with-their-most-challenging-engineering-work) — Claude blog, July 15, 2026.
