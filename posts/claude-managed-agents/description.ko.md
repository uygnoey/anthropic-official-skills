[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude Managed Agents: 프로덕션까지 10배 빠르게

## 이 글이 뭔가요

Claude Platform 위에서 돌아가는 에이전트 런타임 제품군 **Claude Managed Agents**의 출시 공지입니다. 관리형 에이전트 하네스와 프로덕션 인프라(샌드박스 코드 실행, 체크포인팅, 자격증명 관리, 범위 한정 권한, 트레이싱)를 함께 제공하고, Managed Agents가 대신 처리해주는 범위를 정리합니다. Notion, Rakuten, Asana, Vibecode, Sentry, Atlassian, Casetext 등 초기 고객 사례도 담깁니다.

## 언제 유용한가요

- 에이전트 런타임을 자체 구축할지 관리형을 도입할지 판단할 때
- 프로덕션에 올리기 전 "에이전트 하네스"가 어디까지 다뤄야 하는지 체계적으로 보고 싶을 때
- 새 에이전트형 제품을 스코핑하면서 구체적 배포 패턴과 레퍼런스가 필요할 때
- 2026년 4월 기준 프로덕션 에이전트 인프라 현황을 이해관계자에게 브리핑할 때

## 핵심 포인트

- 오케스트레이션 하네스와 프로덕션 인프라를 묶어 프로토타입에서 런칭까지 수 개월이 아닌 수 일로 단축
- 핵심 기능: 프로덕션급 샌드박스 에이전트, 연결이 끊겨도 유지되는 장시간 세션, 멀티 에이전트 코디네이션(research preview), 범위 한정 권한 거버넌스와 실행 트레이싱
- 원하는 결과와 성공 기준을 정의하면 Claude가 자체 평가·반복하는 모드(research preview) 제공. 기존 prompt-and-response 방식도 지원
- 내부 structured-file-generation 테스트에서 일반 프롬프팅 루프 대비 과업 성공률 최대 10점 개선. 어려운 문제일수록 개선 폭이 큼
- 가격: 표준 Claude Platform 토큰 요금에 더해 활성 런타임 세션 시간당 $0.08
- 접근: Claude Console, 신규 CLI, Claude Code의 내장 claude-api Skill("start onboarding for managed agents in Claude API")

## 번들 리소스

- `guides/managed-agents-adoption.{en,ko,es,ja}.md` — 글의 판단 기준, 기능 체크리스트, 사례 패턴을 4개 언어 배포 플레이북으로 정리

글에 재사용 가능한 개발자 관점의 독립 패턴이나 운영 규칙이 명시된 named 에이전트 역할이 따로 없어 Skill·Subagent artifact는 생성하지 않습니다.

## 출처

[Claude Managed Agents: get to production 10x faster](https://claude.com/blog/claude-managed-agents) (게시 2026-04-08)를 바탕으로 정리했습니다.
