[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude Sonnet 4, 100만 토큰(1M) 컨텍스트 지원

## 이 글이 뭔가요
이 글은 Anthropic API에서 Claude Sonnet 4가 최대 100만 토큰(1M) 컨텍스트를 지원하게 되었음을 알리고, 이를 통해 가능한 활용 사례를 요약합니다.

## 언제 유용한가요
한 번의 요청에서 매우 큰 입력(예: 전체 코드베이스, 방대한 문서 묶음)을 분석하거나, 긴 다단계 워크플로 전반에서 일관성을 유지하는 에이전트를 만들 때 유용합니다.

## 핵심 포인트
- Sonnet 4는 최대 1M 토큰 컨텍스트를 지원합니다(5배 증가).
- 대규모 코드 분석, 문서 종합, 컨텍스트 인지형 에이전트가 대표적 활용 사례입니다.
- Claude Developer Platform에서 공개 베타로 제공되며, Amazon Bedrock 및 Google Cloud Vertex AI에서도 사용할 수 있습니다.
- 200K 토큰 초과 프롬프트에는 가격 정책이 달라지며, 프롬프트 캐싱과 배치 처리로 지연/비용을 줄일 수 있습니다.

## 번들 리소스
- 장문 컨텍스트 사용 여부와 포함할 내용을 결정하는 짧은 Claude Code 스킬

## 출처
- https://claude.com/blog/1m-context
