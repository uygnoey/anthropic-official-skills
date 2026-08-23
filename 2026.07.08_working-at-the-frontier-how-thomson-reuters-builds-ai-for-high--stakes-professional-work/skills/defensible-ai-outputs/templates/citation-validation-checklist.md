# Citation validation checklist

A gate an AI-produced finding passes through **before** it is presented for human review. Built from
the requirement Thomson Reuters states: the system must check citations before presenting findings for
human review.

## Per-claim check

Run for every claim in the output, not for the output as a whole.

```
Claim:              <the assertion as written>
Cited source:       <authority / document / passage>
Source exists:      <verified / not found>
Source says this:   <verified / partially supports / does not support>
Source is current:  <current / superseded / unknown>
Authoritative:      <is this drawn from the curated authoritative corpus, or from elsewhere?>
Verdict:            <passes / returns to the agent / flagged for the reviewer>
```

A claim whose source does not support it does not go to review with a caveat attached. It goes back.

## Per-output check

```
Every claim carries a citation:            <yes / no — list the uncited claims>
Every citation was validated:              <yes / no>
Claims that failed validation were removed
or corrected before review:                <yes / no>
Thread continuity held across the tool chain:  <does the output still answer the question asked?>
```

That last line is the context-management requirement applied at the output level. Individually valid
citations do not guarantee the answer is still about the original question after a long tool-use chain.

## Handoff to the accountable professional

The human professional is the one accountable for the end work product. State plainly what they are
receiving:

```
Validated:            <what the system checked and confirmed>
Not validated:        <what the system could not check, and why>
Open for judgment:    <what requires professional judgment rather than verification>
Sources consulted:    <the corpus and tools used>
```

## Transparency, verifiability, defensibility

Before handoff, confirm each property of the output:

- **Transparent** — can the reviewer see the reasoning and the sources, rather than a summary of them?
- **Verifiable** — can the reviewer independently confirm each claim against its source?
- **Defensible** — would the work survive a challenge from someone motivated to overturn it?

Any "no" is a reason to hold the output back, not to caveat it.
