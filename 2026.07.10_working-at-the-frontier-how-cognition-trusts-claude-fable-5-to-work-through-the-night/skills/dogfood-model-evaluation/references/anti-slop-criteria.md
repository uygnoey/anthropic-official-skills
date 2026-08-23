# Anti-slop criteria

Cognition grades models on **Frontier Code**, a benchmark it built "because existing ones kept
rewarding code that passed tests but wouldn't survive a real codebase." Alberti calls it an
"anti-slop" standard.

This file records what the post says about it and turns the stated principle into criteria you can
apply. The criteria beyond the first section are a reading of the principle, not text from the post.

## What the post states

- **Name:** Frontier Code.
- **Why it exists:** existing benchmarks rewarded code that passed tests but wouldn't survive a real
  codebase.
- **What Alberti calls it:** an "anti-slop" standard.
- **Results reported:** on its hardest subset, the prior Opus model scored around 10%; Claude Fable 5
  scored about 30%.
- **How the result was received:** "Is there a bug? This can't be true." Then dogfooding agreed with
  the numbers.

The post does not describe the task set, the scoring rubric, the size of the hardest subset, or
whether Frontier Code is published. Do not infer those.

## The principle to carry over

> Score whether the code would survive the codebase — not whether it passes the tests.

Passing tests is a floor. It is satisfied by code that is correct today and unmaintainable, correct
today and inconsistent with everything around it, or correct only for the cases someone happened to
write a test for.

## Criteria implied by that principle

Apply these as the questions your own benchmark or review should answer. Each is a way code can pass
tests and still be slop.

1. **Would a reviewer merge it?** Not "is it correct" but "would this get through your actual code
   review, from the person who reviews most strictly."
2. **Does it match the codebase?** Naming, structure, error handling, and idiom consistent with the
   surrounding code, rather than a locally reasonable style imported from elsewhere.
3. **Does it fail loudly?** Code that swallows an error to make a test pass is the archetypal
   test-passing failure.
4. **Is the abstraction earned?** New indirection, new config surface, or a new helper introduced to
   satisfy one case is debt paid by everyone afterward.
5. **Did it change the tests to fit the code?** A test weakened or deleted to get green is the
   clearest form of the failure the benchmark was built to catch.
6. **Are the untested paths right too?** Test coverage defines what was checked, not what was
   changed.
7. **Would it be safe to run unattended?** For Cognition this is the operative question — "a small
   bug introduced quietly can cause real problems downstream."

## Pairing with the dogfood bar

Frontier Code sits alongside, not instead of, the human bar: Cognition's highest-taste developers put
each new model through a real day of work, and the bar is whether the code is something they'd
actually keep. The benchmark is what makes results comparable across releases; the dogfood day is what
makes them believable.

The strong signal is the two agreeing. In this case they did, which the post notes is unusual —
"usually a benchmark jump comes with engineers arguing for weeks over whether the model is actually
better in practice."

## Source

[Working at the frontier: How Cognition trusts Claude Fable 5 to work through the night](https://claude.com/blog/working-at-the-frontier-how-cognition-trusts-claude-fable-5-to-work-through-the-night) — Claude blog, July 10, 2026.
