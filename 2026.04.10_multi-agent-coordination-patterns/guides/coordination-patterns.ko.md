[English](./coordination-patterns.en.md) · **한국어** · [Español](./coordination-patterns.es.md) · [日本語](./coordination-patterns.ja.md)

# 다중 에이전트 조정 패턴: 선택 가이드

## 이 가이드가 뭔가요
이 가이드는 원문에서 소개한 5가지 다중 에이전트 조정 패턴을 선택·진화시키기 위한 요약 가이드입니다.

## 언제 유용한가요
다중 에이전트 접근이 필요하다고 결정한 뒤, 작업 구조와 운영 제약에 맞는 아키텍처를 고를 때 사용합니다.

## 빠른 선택 표

| 상황 | 패턴 |
| --- | --- |
| 품질이 중요한 산출물 + 명시적 평가 기준 | Generator-verifier |
| 작업 분해가 명확하고 하위 작업이 경계가 있음 | Orchestrator-subagent |
| 병렬/독립/장시간 하위 작업 | Agent teams |
| 이벤트 기반 파이프라인 + 확장되는 에이전트 생태계 | Message bus |
| 발견을 서로 축적·공유하는 협업형 작업 | Shared state |
| 단일 장애점(SPOF) 제거가 중요 | Shared state |

## 진화 방법
- 가능한 가장 단순한 패턴으로 시작합니다.
- 주요 실패 양상을 관찰합니다.
- 실패 양상이 지속적이고 구조적일 때만 더 복잡한 패턴으로 진화합니다.

## 출처
- https://claude.com/blog/multi-agent-coordination-patterns
