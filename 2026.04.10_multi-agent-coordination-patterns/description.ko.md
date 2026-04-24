[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
이 글은 다중 에이전트 협업을 위한 5가지 대표 조정 패턴(Generator-verifier, Orchestrator-subagent, Agent teams, Message bus, Shared state)을 비교하고, 각 패턴의 동작 방식/장단점/선택 기준을 설명합니다.

## 언제 유용한가요
단일 에이전트가 아니라 다중 에이전트 시스템이 적절하다고 판단한 뒤, 작업 분해 방식, 컨텍스트 경계, 정보 흐름, 운영 제약에 따라 어떤 조정 아키텍처를 선택하거나 언제 다른 패턴으로 진화해야 하는지 결정할 때 유용합니다.

## 핵심 포인트
- 가능한 가장 단순한 패턴으로 시작하고, 실패 양상을 관찰한 뒤 필요에 따라 진화합니다.
- Generator-verifier는 명시적 평가 기준이 있고 품질이 중요한 산출물에 적합하며, 반복 횟수 제한과 폴백이 중요합니다.
- Orchestrator-subagent는 분해가 명확하고 하위 작업이 경계가 있을 때 적합하지만, 오케스트레이터가 정보 병목이 될 수 있습니다.
- Agent teams는 장시간 독립 하위 작업에 적합하고 워커가 컨텍스트를 유지하지만, 작업 분할/충돌 해결이 필요합니다.
- Message bus는 이벤트 기반 파이프라인과 확장되는 에이전트 생태계에 적합하지만, 라우팅/디버깅 복잡도가 증가합니다.
- Shared state는 발견을 즉시 공유하는 협업형 작업에 적합하지만, reactive loop를 막기 위한 강한 종료 조건이 필요합니다.

## 번들 리소스
- Skill: 다중 에이전트 조정 패턴 선택/적용 가이드(요약 표 + 진화 가이드 포함)

## 출처
- https://claude.com/blog/multi-agent-coordination-patterns
