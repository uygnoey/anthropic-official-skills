# Harnessing Claude's Intelligence | 3 Key Patterns for Building Apps

## 이 글이 뭔가요
이 글은 Claude Platform에서 애플리케이션(에이전트 포함)을 만들 때, 모델의 지능이 빠르게 변화해도 **지연(latency)·비용(cost)** 균형을 유지하면서 성능을 따라잡기 위한 **3가지 패턴**을 제시합니다.

## 언제 유용한가요
에이전트 하네스(agent harness: 프롬프트·도구·컨텍스트·메모리·보안/UX 경계)를 설계/개선할 때, 무엇을 하네스에서 고정하고 무엇을 Claude에게 위임할지 기준이 필요할 때 유용합니다.

## 핵심 포인트
- Claude가 이미 잘 이해하는 범용 도구(예: bash, 텍스트 편집)를 바탕으로 애플리케이션을 구성하되, 상위 패턴은 시간이 지나며 자연스럽게 진화하게 둡니다.
- Claude의 역량이 향상될수록 하네스에 들어간 가정(“Claude는 못 할 것”)이 낡을 수 있으므로, 지속적으로 “내가 이제 무엇을 그만해도 되지?”를 질문하며 재검증합니다.
- 경계를 신중히 설정합니다: 캐시 효율을 높이는 컨텍스트 설계 원칙을 적용하고, 보안/UX/관측성을 위해 고위험 행동은 선언형(declarative) 도구로 승격합니다.

## 번들 리소스
- Skill 1개: `skills/building-on-evolving-models/SKILL.md` — 3패턴 + 캐시 히트 원칙을 Agent Skills 규격으로 정리
- Guide 1개(영/한): `guides/three-patterns-app-harness.en.md`, `guides/three-patterns-app-harness.ko.md`

## 출처
[Harnessing Claude's Intelligence | 3 Key Patterns for Building Apps](https://claude.com/blog/harnessing-claudes-intelligence) (게시일: 2026-04-02) 내용을 바탕으로 정리했습니다.
