# Eval task templates

Three task shapes, following the categories named in the source post. Copy the block you need and fill
it in from a real user prompt — not from a problem statement you wrote.

---

## Shape 1 — Underspecified

The model gets what a real user sends and nothing more. Do not add the file name, the constraints, or
the reproduction steps.

```yaml
id: <short-id>
shape: underspecified
prompt: |
  <paste the artifact the user pasted — stack trace, error output, failing log>
  <the one or two words they actually typed, e.g. "fix">
repo_state: <commit or fixture the task runs against>
hidden_root_cause: <what is actually wrong — never shown to the model>
scoring:
  inferred_intent: <did it work out what the user wanted?>
  found_root_cause: <did it reach the real cause, not a plausible nearby one?>
  fixed: <is the change correct?>
  validated: <did it verify the fix itself, unprompted?>
  reported_back: <did it explain what it found and did?>
  operations_used: <count, recorded alongside outcome>
```

---

## Shape 2 — Wrong premise

The prompt asserts something false. The task is to find out whether the model challenges the
assumption or follows it into a dead end.

```yaml
id: <short-id>
shape: wrong-premise
prompt: |
  <a confident, specific, incorrect diagnosis — e.g. "the X module is broken, fix X">
repo_state: <commit or fixture>
false_assertion: <the specific claim in the prompt that is not true>
actual_cause: <where the problem really is>
scoring:
  challenged_assumption: <did it push back, or at least verify before acting?>
  reached_actual_cause: <did it get there anyway?>
  dead_end_depth: <how far into the wrong module did it go before noticing, if at all>
  reported_the_correction: <did it tell the user their premise was wrong?>
```

A model that produces a correct-looking change *inside the named module* has failed this task even if
the change compiles and the tests pass.

---

## Shape 3 — Whole-system

The prompt looks simple. Cracking it requires understanding how the pieces fit together. These are the
hardest-subset tasks whose traces get read when a score moves.

```yaml
id: <short-id>
shape: whole-system
prompt: |
  <a short, plain request whose correct answer depends on system-wide context>
repo_state: <commit or fixture>
required_understanding:
  - <fact about the system the model must reconstruct on its own>
  - <interaction between components that a local fix would break>
local_fix_trap: <the plausible narrow change that passes tests and is wrong>
scoring:
  avoided_local_fix_trap: <yes/no>
  reconstructed_required_understanding: <yes/no, evidenced from the trace>
  operations_used: <count>
trace_review: required
```

---

## Result record

Record every run with the effort setting attached — a score without it compares to nothing.

```yaml
benchmark: <name>
model: <model id>
effort_setting: <e.g. Max effort>
score: <percent>
hardest_subset_score: <percent>
traces_reviewed: <yes/no — required if the score moved unexpectedly>
operations_relative_to_prior: <fewer / comparable / more>
notes: <what the traces showed>
```

## Source

[Working at the frontier: How Cursor knew Claude Fable 5 was ready for the hardest 1% of problems](https://claude.com/blog/working-at-the-frontier-cursor) — Claude blog, July 17, 2026.
