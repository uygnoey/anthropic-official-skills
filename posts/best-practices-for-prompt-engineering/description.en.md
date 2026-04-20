[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Prompt Engineering Best Practices for Claude

## What this skill is
A quick reference distilled from Anthropic's official prompt-engineering guidance. Five core techniques (clarity, context, specificity, examples, permission to say "I don't know") and four advanced ones (prefill, chain-of-thought, output format control, prompt chaining). Reflects model-generation guidance — Claude 4.x needs less XML-tag wrangling and role-play than older models.

## When to use
- Prompts return generic or off-topic answers
- Claude appears to be hallucinating information
- Output format (JSON, prose, lists) is inconsistent
- A complex task doesn't land in one shot
- You need to optimize API cost / latency by reshaping prompts

## Five core techniques

### 1. Be explicit and clear
- Vague: `Create an analytics dashboard`
- Explicit: `Create an analytics dashboard. Include as many relevant features and interactions as possible. Go beyond the basics to create a fully-featured implementation.`

### 2. Provide context and motivation
- Less effective: `NEVER use bullet points`
- More effective: `I prefer responses in natural paragraph form rather than bullet points because I find flowing prose easier to read and more conversational.`

### 3. Be specific
- Vague: `Create a meal plan for a Mediterranean diet`
- Specific: `Design a Mediterranean diet meal plan for pre-diabetic management. 1,800 calories daily, emphasis on low glycemic foods. List breakfast, lunch, dinner, and one snack with complete nutritional breakdowns.`

### 4. Use examples
Start one-shot before few-shot. Best when format, tone, or subtle patterns matter.
```
Here's an example of the summary style I want:

Article: [link]
Summary: EU passes comprehensive AI Act targeting high-risk systems. Key provisions include transparency requirements and human oversight mandates. Takes effect 2026.

Now summarize this article in the same style: [new link]
```

### 5. Give permission to express uncertainty
```
Analyze this financial data and identify trends. If the data is insufficient to draw conclusions, say so rather than speculating.
```

## Four advanced techniques

### 1. Prefill the response
```python
messages=[
    {"role": "user", "content": "Extract the name and price from this product description into JSON."},
    {"role": "assistant", "content": "{"}
]
```

### 2. Chain of thought — basic / guided / structured
Structured example:
```
Think before you write the email in <thinking> tags.
First, analyze what messaging would appeal to this donor.
Then, identify relevant program aspects.
Finally, write the personalized donor email in <email> tags, using your analysis.
```

### 3. Control the output format
Explicitly describe the prose/markdown/list policy you want.

### 4. Prompt chaining
Break complex tasks into sequential steps; feed each output into the next prompt.

## Technique selection

| If you need… | Use… |
|---|---|
| Specific output format | Examples, prefilling, or explicit format instructions |
| Step-by-step reasoning | Extended thinking (Claude 4.x) or chain of thought |
| Complex multi-stage task | Prompt chaining |
| Transparent reasoning | Chain of thought with structured output |
| To prevent hallucinations | Permission to say "I don't know" |

## Anti-patterns
- Don't over-engineer.
- Don't ignore the basics.
- Don't assume the AI reads minds.
- Don't use every technique at once.
- Don't forget to iterate.
- Don't rely on outdated techniques (heavy XML / role-play).

## Troubleshooting

| Symptom | Fix |
|---|---|
| Too generic | Add specificity / examples |
| Off-topic | More explicit goal / context |
| Inconsistent format | Examples or prefilling |
| Too complex / unreliable | Chaining |
| Unnecessary preambles | Prefill / explicit skip |
| Makes up info | Permission to say "I don't know" |
| Suggests instead of implements | Explicit action verbs |

## Source
Distilled from [Best practices for prompt engineering](https://claude.com/blog/best-practices-for-prompt-engineering) (2025-11-10). See the original for authoritative guidance.
