[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
이 글은 헬스케어 및 생명과학 분야에서 AI 에이전트를 실제로 운영 환경에 적용하는 사례를 소개하고, 이 도메인이 특히 어려운 이유(데이터 파편화, 규제, 환자 안전)를 중심으로 구현상의 고려사항을 정리합니다.

## 언제 유용한가요
헬스케어 워크플로에 에이전트가 적합한지 평가해야 하거나, 데이터 연동·지연시간·컴플라이언스·임상의(사람) 감독을 포함한 실무 의사결정 체크리스트가 필요할 때 유용합니다.

## 핵심 포인트
- 실제 성과: Pfizer는 연간 연구 시간 16,000시간 절감, Novo Nordisk는 임상 연구 보고서 생성 시간을 수 주에서 수 분으로 단축했다고 소개합니다.
- 상호운용성 3가지 결정: 연결 방식, 데이터 포맷, 동기화 요구사항.
- 컴플라이언스/안전: 감사 추적(audit trail), 거버넌스, 관측 가능성, 검증, 그리고 명확한 에스컬레이션을 포함한 fail-safe 기본값.

## 번들 리소스
- Skill: `skills/healthcare-agent-implementation/SKILL.md`
- Reference: `skills/healthcare-agent-implementation/references/healthcare-agent-checklist.md`
- Guide: `guides/healthcare-agent-deployment.ko.md`

## 출처
- https://claude.com/blog/building-ai-agents-in-healthcare-and-life-sciences
