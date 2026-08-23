# Invariants brief

A template for the practice the post highlights: on a migration that had tripped up earlier models,
the model **stated the invariants it would hold itself to, then executed against them**.

Use this in two passes. Pass one asks for the invariants and stops. You read them. Pass two runs.

---

## Pass 1 — ask for the invariants

```
Task: <what needs to happen>
Scope: <files, services, or systems in play>
Duration: this may run unattended for several hours.

Before making any change, write out the invariants you will hold yourself to for the
whole run — the properties that must remain true at every intermediate state, not just
at the end. Include:

  1. Correctness invariants — what must never become false about the data or behavior.
  2. Compatibility invariants — what other callers/consumers must keep being able to do
     while the change is in progress.
  3. Reversibility — what you will keep intact so this can be backed out.
  4. Out of scope — what you will not touch even if it looks wrong.

Then stop and wait for my review. Do not begin.
```

---

## Pass 2 — run against them

```
The invariants are approved as written, with these edits: <edits, or "none">.

Execute against them. For the whole run:

  - Check each invariant before and after any step that could affect it.
  - Use the debugging tools directly — logs, traces, the log viewer. Do not wait for me
    to paste anything in.
  - If you find you cannot hold an invariant, stop that line of work, record why, and
    continue with the parts that do not depend on it. Do not relax the invariant on your
    own judgment.
  - If a decision needs information you do not have, record the decision and what is
    missing. Do not guess and proceed.

When you finish, report:
  - What you changed.
  - Each invariant, and how you verified it held.
  - What you are unsure about, explicitly. If you did not confirm something, say so
    rather than asserting the most plausible answer.
```

---

## Review checklist for the invariants you get back

Read these before approving. This review is much cheaper than reading eight hours of output.

- [ ] Does every invariant apply to *intermediate* states, not only the final state?
- [ ] Is each one checkable — could the agent actually test it mid-run?
- [ ] Do they cover the consumers of the thing being changed, not only the thing itself?
- [ ] Is the reversibility plan real, or is it "we can revert the commit"?
- [ ] Is anything in the out-of-scope list something you actually wanted done?
- [ ] Is there an invariant covering the failure that bit you last time?

---

## Why the two passes

The post's expensive failure mode is a prior model that "technically finished the job but introduced a
series of subtle bugs along the way." A finished task is not a signal. The invariants are the thing
that makes a long unattended run auditable, and reviewing them up front is the only cheap moment to
catch a wrong one.

## Source

[Working at the frontier: How Cognition trusts Claude Fable 5 to work through the night](https://claude.com/blog/working-at-the-frontier-how-cognition-trusts-claude-fable-5-to-work-through-the-night) — Claude blog, July 10, 2026.
