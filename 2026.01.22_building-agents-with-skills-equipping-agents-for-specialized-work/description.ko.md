[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Skills로 에이전트 만들기: 전문 작업을 위한 역량 부여

## 이 글이 뭔가요
이 글은 Agent Skills가 무엇인지, 도메인 지식을 어떻게 파일로 패키징하는지, 그리고 단계적 공개(메타데이터 → SKILL.md → references)가 많은 스킬을 확장 가능하게 만드는 이유를 설명합니다.

## 언제 유용한가요
- 매 대화마다 규칙/표준/워크플로를 다시 설명하지 않고도 에이전트가 일관되게 적용하게 하고 싶을 때.
- 스킬 수가 많아도 컨텍스트 사용량을 통제해야 할 때.

## 핵심 포인트
- 스킬의 YAML 프런트매터(name + description)가 먼저 노출되고, 필요할 때만 SKILL.md와 더 깊은 레퍼런스 파일을 읽습니다.
- 글은 3단 구조를 강조합니다: 메타데이터(~50 토큰), SKILL.md(~500 토큰), 레퍼런스 파일(2,000+ 토큰 이상, 필요 시 로드).
- 스킬은 문서, 가이드, 스크립트 같은 보조 파일을 함께 번들링하고 SKILL.md에서 이를 참조할 수 있습니다.

## 번들 리소스
- Skill: `skills-packaging-principles` (구조 가이드 + 템플릿)
- Guide: `skills-packaging-guide` (개요, 권장 레이아웃)

## 출처
- https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work
