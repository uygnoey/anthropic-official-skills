---
name: prompt-engineering-techniques
description: Applies Anthropic's prompt engineering techniques to fix prompts that return generic, off-topic, inconsistent, or hallucinated output. Use when a user asks how to write better prompts, wants to improve an existing prompt, asks about chain-of-thought, response prefilling, output format control, or prompt chaining, or is debugging unreliable model behavior. Covers five core techniques and four advanced techniques with examples and a troubleshooting cheatsheet.
---

# Prompt Engineering Techniques

Apply the core techniques first. Reach for the advanced ones only when a core technique alone doesn't land the result.

## Instructions

### Step 1: Diagnose the failure

Match the symptom to the fix in the table, then apply the matching technique below.

| Symptom | Apply |
|---|---|
| Too generic | Specificity + examples |
| Off-topic | Explicit goal + context |
| Inconsistent format | Examples or prefilling |
| Too complex, unreliable | Prompt chaining |
| Unnecessary preambles | Prefilling, or explicit "skip preamble" |
| Makes up information | Permission to say "I don't know" |
| Suggests instead of implements | Explicit action verbs |

### Step 2: Apply the five core techniques

#### 2.1 Be explicit and clear
State exactly what you want. Start with an action verb. Specify quality bar.

- Vague: `Create an analytics dashboard`
- Explicit: `Create an analytics dashboard. Include as many relevant features and interactions as possible. Go beyond the basics to create a fully-featured implementation.`

#### 2.2 Provide context and motivation
Explain why, not just what.

- Less effective: `NEVER use bullet points`
- More effective: `I prefer responses in natural paragraph form rather than bullet points because I find flowing prose easier to read and more conversational. Bullet points feel too formal and list-like for my casual learning style.`

#### 2.3 Be specific
Replace abstract goals with concrete constraints.

- Vague: `Create a meal plan for a Mediterranean diet`
- Specific: `Design a Mediterranean diet meal plan for pre-diabetic management. 1,800 calories daily, emphasis on low glycemic foods. List breakfast, lunch, dinner, and one snack with complete nutritional breakdowns.`

#### 2.4 Use examples (one-shot before few-shot)
Best when format, tone, or subtle patterns matter.

```
Here's an example of the summary style I want:

Article: [link]
Summary: EU passes comprehensive AI Act targeting high-risk systems. Key provisions include transparency requirements and human oversight mandates. Takes effect 2026.

Now summarize this article in the same style: [new link]
```

#### 2.5 Give permission to express uncertainty
Prevents hallucination.

```
Analyze this financial data and identify trends. If the data is insufficient to draw conclusions, say so rather than speculating.
```

### Step 3: Apply advanced techniques when needed

#### 3.1 Prefill the response (API)

```python
messages=[
    {"role": "user", "content": "Extract the name and price from this product description into JSON."},
    {"role": "assistant", "content": "{"}
]
```

In chat UIs without prefill support, emulate: `Output only valid JSON with no preamble. Begin your response with an opening brace.`

#### 3.2 Chain of thought — basic / guided / structured

- Basic: `Think step-by-step before you write the email.`
- Guided: `Think before you write the email. First, think through what messaging might appeal to this donor given their donation history. Then, consider which aspects of the program would resonate with them. Finally, write the personalized donor email using your analysis.`
- Structured: `Think before you write the email in <thinking> tags. First, analyze... Then, identify... Finally, write the email in <email> tags, using your analysis.`

On Claude 4.x, extended thinking is often a better default than manual chain-of-thought. Use manual CoT when reasoning must be visible in the response.

#### 3.3 Control the output format

```
When writing reports or analyses, write in clear, flowing prose using complete paragraphs.
Use standard paragraph breaks for organization.
Reserve markdown primarily for inline code, code blocks, and simple headings.

DO NOT use ordered lists or unordered lists unless you're presenting truly discrete items
where a list format is the best option, or the user explicitly requests a list.
```

#### 3.4 Prompt chaining

Break complex tasks into sequential prompts. Each step's output feeds the next.

1. `Summarize this medical paper covering methodology, findings, and clinical implications.`
2. `Review the summary above for accuracy, clarity, and completeness. Provide graded feedback.`
3. `Improve the summary based on this feedback: [feedback from step 2]`

## Examples

### Structured extraction combining multiple techniques

```
Extract key financial metrics from this quarterly report and present them in JSON format.

I need this data for automated processing, so it's critical that your response contains
ONLY valid JSON with no preamble or explanation.

Use this structure:
{
  "revenue": "value with units",
  "profit_margin": "percentage",
  "growth_rate": "percentage"
}

If any metric is not clearly stated in the report, use null rather than guessing.

Begin your response with an opening brace: {
```

This prompt applies: explicit action verb, context ("for automated processing"), output format control, example schema, permission to say null, and prefill-emulation.

## Anti-patterns

- Do not over-engineer. Long prompts are not automatically better.
- Do not skip the basics to reach for advanced techniques.
- Do not assume the model reads minds.
- Do not stack every technique at once. Pick the fewest that solve the problem.
- Do not skip iteration. First prompts are rarely optimal.
- Do not rely on outdated tricks. XML tags and heavy role-play matter less on modern Claude models.

## Human-readable descriptions

This skill is summarized for humans in [../../description.en.md](../../description.en.md) and [../../description.ko.md](../../description.ko.md).

## Source

Distilled from [Best practices for prompt engineering](https://claude.com/blog/best-practices-for-prompt-engineering) (published 2025-11-10). Defer to the original for authoritative guidance.
