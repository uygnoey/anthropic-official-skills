# Agent readiness review

A record for assessing whether a model can carry an agent-first product — targeted at planning and tool
use, the abilities the architecture depends on.

## Header

```
Model:             <candidate>
Compared against:  <incumbent, if any>
Product surface:   <what the agent orchestrates>
Tool count:        <how many tools are exposed simultaneously>
Date:              <YYYY-MM-DD>
```

## Planning

```
Unseen request:         <the request given>
Plan constructed:       <the sequence the model chose>
Sensible?               <yes / no — and where it went wrong>
Recovered from a dead end?  <yes / no / not exercised>
```

Run this on requests the model has not been shown before. A plan for a request that matches a known
flow does not test planning.

## Tool use

```
Right tools called:        <yes / no — list wrong or missed calls>
Arguments correct:         <yes / no>
Results actually used:     <did the output reflect what came back, or ignore it?>
Dependable across a chain:  <did tool-calling stay reliable deep into the task, or degrade?>
```

## Context management

```
Chain length:                    <number of tool calls in the run>
Answer still addresses the question asked?  <yes / no>
Thread continuity across the chain:         <held / drifted — where>
```

## The four professional requirements

If the product is one where a professional is accountable for the output, check all four:

```
1. Citations validated before human review:   <yes / no>
2. Context managed across tool chains:        <yes / no>
3. Human brought into developing the work:    <yes / no — or does it deliver a finished artifact?>
4. Capability expansion for complex drafting: <yes / no — what class of work>
```

## Verdict

```
Ready for the agent-first surface:  <yes / no / partially>
Blocking gaps:                      <what has to improve>
What this unlocks if adopted:       <work not previously possible>
```
