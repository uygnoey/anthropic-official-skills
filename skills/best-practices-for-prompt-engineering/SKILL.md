# Claude 프롬프트 엔지니어링 베스트 프랙티스 / Prompt Engineering Best Practices

> **출처 / Source**: [Best practices for prompt engineering](https://claude.com/blog/best-practices-for-prompt-engineering)
> **게시일 / Published**: 2025-11-10

---

## 🇰🇷 한국어

### 핵심 요약
Claude 공식 팀이 정리한 프롬프트 엔지니어링 가이드. 기본 5가지(명확성·맥락·구체성·예시·불확실성 허용)와 고급 4가지(프리필·사고 사슬·출력 형식 제어·프롬프트 체이닝)를 중심으로 설명. Claude 4.x에서는 XML 태그와 과한 역할 프롬프팅의 필요성이 줄었다.

### 기본 5가지 기법
#### 1. Be explicit and clear (명확하고 직접적으로)
- Vague: `Create an analytics dashboard`
- Explicit: `Create an analytics dashboard. Include as many relevant features and interactions as possible. Go beyond the basics to create a fully-featured implementation.`
- 행동 동사(`Write`, `Analyze`, `Generate`)로 시작, 서론 생략, 품질 수준 명시.

#### 2. Provide context and motivation (이유와 맥락 제공)
- Less effective: `NEVER use bullet points`
- More effective: `I prefer responses in natural paragraph form rather than bullet points because I find flowing prose easier to read and more conversational. Bullet points feel too formal and list-like for my casual learning style.`

#### 3. Be specific (구체적으로)
- Vague: `Create a meal plan for a Mediterranean diet`
- Specific: `Design a Mediterranean diet meal plan for pre-diabetic management. 1,800 calories daily, emphasis on low glycemic foods. List breakfast, lunch, dinner, and one snack with complete nutritional breakdowns.`

#### 4. Use examples (예시 사용)
포맷/톤/미묘한 패턴이 있을 때 효과적. 원샷부터 시작.
```
Here's an example of the summary style I want:

Article: [link]
Summary: EU passes comprehensive AI Act targeting high-risk systems. Key provisions include transparency requirements and human oversight mandates. Takes effect 2026.

Now summarize this article in the same style: [new link]
```

#### 5. Give permission to express uncertainty (모른다고 말할 여지 주기)
- 예: `Analyze this financial data and identify trends. If the data is insufficient to draw conclusions, say so rather than speculating.`
- 할루시네이션 억제에 효과적.

### 고급 4가지 기법
#### 1. Prefill the AI's response (응답 프리필)
API 호출에서 assistant 메시지를 일부 미리 채워 형식을 강제.
```python
messages=[
    {"role": "user", "content": "Extract the name and price from this product description into JSON."},
    {"role": "assistant", "content": "{"}
]
```
채팅 UI에서는: `Output only valid JSON with no preamble. Begin your response with an opening brace.`

#### 2. Chain of thought (사고 사슬)
세 수준으로 제공:
- **Basic**: `Think step-by-step before you write the email.`
- **Guided**: `Think before you write the email. First, think through what messaging might appeal to this donor given their donation history. Then, consider which aspects of the program would resonate with them. Finally, write the personalized donor email using your analysis.`
- **Structured**: `Think before you write the email in <thinking> tags. First, analyze... Then, identify... Finally, write the email in <email> tags, using your analysis.`

Claude 4.x의 extended thinking이 대안이지만, 추론 투명성이 필요하면 CoT를 쓴다.

#### 3. Control the output format (출력 형식 제어)
```
When writing reports or analyses, write in clear, flowing prose using complete paragraphs.
Use standard paragraph breaks for organization.
Reserve markdown primarily for inline code, code blocks, and simple headings.

DO NOT use ordered lists or unordered lists unless you're presenting truly discrete items
where a list format is the best option, or the user explicitly requests a list.
```

#### 4. Prompt chaining (프롬프트 체이닝)
복잡한 작업을 단계로 쪼개고 이전 출력을 다음 입력으로 사용. 지연은 늘지만 정확도 상승.
1. `Summarize this medical paper covering methodology, findings, and clinical implications.`
2. `Review the summary above for accuracy, clarity, and completeness. Provide graded feedback.`
3. `Improve the summary based on this feedback: [feedback from step 2]`

### 기법 선택 가이드
| 원하는 것 | 쓰는 기법 |
|---|---|
| 특정 출력 형식 | 예시 / 프리필 / 명시적 형식 지시 |
| 단계별 추론 | Extended thinking (Claude 4.x) / CoT |
| 복잡 다단계 과제 | 프롬프트 체이닝 |
| 투명한 추론 | 구조화된 CoT |
| 할루시네이션 방지 | "모른다" 허용 문구 |

### 복합 예시 (Putting it all together)
```
Extract key financial metrics from this quarterly report and present them in JSON format.

I need this data for automated processing, so it's critical that your response contains
ONLY valid JSON with no preamble or explanation.

Use this structure:

  "revenue": "value with units",
  "profit_margin": "percentage",
  "growth_rate": "percentage"

If any metric is not clearly stated in the report, use null rather than guessing.

Begin your response with an opening brace: {
```

### 피해야 할 안티 패턴
- **과도한 엔지니어링 금지** — 길고 복잡한 프롬프트가 늘 좋은 것은 아님.
- **기본기 무시 금지** — 고급 기법도 기본이 불명확하면 의미 없음.
- **AI가 마음을 읽는다고 가정 금지.**
- **모든 기법 동시 사용 금지** — 목적에 맞는 기법만 선택.
- **반복 개선 포기 금지** — 첫 프롬프트가 완벽한 경우는 드물다.
- **낡은 기법 의존 금지** — 현대 모델에선 XML 태그/무거운 역할 프롬프팅의 필요성이 줄었다.

### 문제 해결 치트시트
| 증상 | 처방 |
|---|---|
| 응답이 너무 일반적 | 구체성/예시 추가 |
| 주제 이탈 | 목표/맥락 더 명시 |
| 형식 일관성 부족 | 예시 / 프리필 |
| 너무 복잡/불안정 | 체이닝으로 분해 |
| 불필요한 서론 | 프리필 / "생략해" 지시 |
| 정보 지어냄 | "모른다" 허용 문구 |
| 제안만 하고 구현 안 함 | 명시적 행동 동사 사용 |

---

## 🇺🇸 English

### Core summary
Official Anthropic guide to prompt engineering. Five core techniques (clarity, context, specificity, examples, permission to say "I don't know") plus four advanced (prefill, chain-of-thought, output format control, prompt chaining). With Claude 4.x, XML tags and heavy role prompting are less necessary.

### Five core techniques
#### 1. Be explicit and clear
- Vague: `Create an analytics dashboard`
- Explicit: `Create an analytics dashboard. Include as many relevant features and interactions as possible. Go beyond the basics to create a fully-featured implementation.`

#### 2. Provide context and motivation
- Less effective: `NEVER use bullet points`
- More effective: `I prefer responses in natural paragraph form rather than bullet points because I find flowing prose easier to read and more conversational.`

#### 3. Be specific
- Vague: `Create a meal plan for a Mediterranean diet`
- Specific: `Design a Mediterranean diet meal plan for pre-diabetic management. 1,800 calories daily, emphasis on low glycemic foods. List breakfast, lunch, dinner, and one snack with complete nutritional breakdowns.`

#### 4. Use examples
Start one-shot before few-shot. Best when format/tone/subtle patterns matter.

#### 5. Give permission to express uncertainty
`Analyze this financial data and identify trends. If the data is insufficient to draw conclusions, say so rather than speculating.`

### Four advanced techniques
#### 1. Prefill the response
```python
messages=[
    {"role": "user", "content": "Extract the name and price from this product description into JSON."},
    {"role": "assistant", "content": "{"}
]
```

#### 2. Chain of thought — basic / guided / structured
Structured example:
```
Think before you write the email in <thinking> tags.
First, analyze what messaging would appeal to this donor.
Then, identify relevant program aspects.
Finally, write the personalized donor email in <email> tags, using your analysis.
```

#### 3. Control the output format
Explicitly describe the prose/markdown/list policy you want.

#### 4. Prompt chaining
Break complex tasks into sequential steps; feed each output into the next prompt.

### Technique selection table
| If you need… | Use… |
|---|---|
| Specific output format | Examples, prefilling, or explicit format instructions |
| Step-by-step reasoning | Extended thinking (Claude 4.x) or chain of thought |
| Complex multi-stage task | Prompt chaining |
| Transparent reasoning | Chain of thought with structured output |
| To prevent hallucinations | Permission to say "I don't know" |

### Anti-patterns
- Don't over-engineer.
- Don't ignore the basics.
- Don't assume the AI reads minds.
- Don't use every technique at once.
- Don't forget to iterate.
- Don't rely on outdated techniques (heavy XML / role-play).

### Troubleshooting
| Symptom | Fix |
|---|---|
| Too generic | Add specificity/examples |
| Off-topic | More explicit goal/context |
| Inconsistent format | Examples / prefilling |
| Too complex/unreliable | Chaining |
| Unnecessary preambles | Prefilling / explicit skip |
| Makes up info | Permission to say "I don't know" |
| Suggests instead of implements | Explicit action verbs |

---

## 주의 / Notes
- 본 문서는 원문 요약이며, 공식 가이드는 [원문](https://claude.com/blog/best-practices-for-prompt-engineering)을 참조하세요.
- Distilled summary. See the [original post](https://claude.com/blog/best-practices-for-prompt-engineering) for the authoritative version.
