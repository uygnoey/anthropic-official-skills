# Model evaluation record

One record per candidate model, structured around the head-to-head comparison Hebbia runs. Copy and
fill in.

## Header

```
Candidate model:   <model being evaluated>
Incumbent model:   <the model this one would replace>
Evaluated by:      <name>
Date:              <YYYY-MM-DD>
Benchmark version: <which revision of the benchmark, since it expands each release>
Added this round:  <measurements added for this release>
```

## Test 1 — Question answering and citation finding

```
Corpus:              <document set used>
Accuracy:            <candidate> vs <incumbent>   → <relative gain/loss>
Citation matching:   <candidate> vs <incumbent>   → <moved / held steady>
Best result on record?  <yes / no — and against which prior models>
```

**Reading the two numbers together.** If accuracy moved and citations did not, the model is
understanding evidence it was already finding. If citations moved and accuracy did not, it is finding
better evidence without drawing better conclusions. Write down which of these happened:

```
Interpretation: <which half of the job improved, and the reasoning>
```

## Test 2 — Agent run with product tools

```
Request shape:        <single-part / multi-part, number of components>
All components held simultaneously?   <yes / no — if no, which were dropped>
All components answered?              <yes / no>
Every answer cited back to source?    <yes / no>
```

## Open-ended analysis

```
Breadth of data reasoned over: <narrower / comparable / broader than incumbent>
Conclusions worth closer examination: <list, or none>
Long task coherence observed:  <did it keep every part of the request in view, prompt sub-agents and
                                tools for facts, and ground claims rather than infer them?>
```

## Two-quality summary

The post reduces the job to two qualities. Score each on its own:

```
Finding the right information from a dense data set: <verdict + evidence>
Synthesizing it correctly:                           <verdict + evidence>
```

## Decision

```
Adopt / hold / re-test:  <decision>
Margin vs incumbent:     <how much better, on which tests>
What this unlocks:       <work that was out of reach with the incumbent, if any>
Open questions:          <what the benchmark did not answer>
```
