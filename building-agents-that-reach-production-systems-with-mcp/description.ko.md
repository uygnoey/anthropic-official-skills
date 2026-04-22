[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Building agents that reach production systems with MCP

## 이 글이 뭔가요
이 글은 Claude 기반 에이전트가 실제 프로덕션 시스템과 워크플로에 연결되는 방법을 설명하고, 제약 조건에 따라 어떤 통합 방식을 선택해야 하는지 정리합니다.

## 언제 유용한가요
이슈 트래커, 데이터 웨어하우스, 인프라 등 내부/외부 시스템에 에이전트를 **안전하고 신뢰성 있게** 연결해야 할 때, 특히 클라우드/프로덕션 환경에서 유용합니다.

## 핵심 포인트
- 직접 API 호출, CLI 자동화, MCP 기반 툴 서버라는 3가지 통합 접근을 비교합니다.
- 프로덕션에서는 원격 MCP 서버가 다양한 클라이언트/환경에서 재사용 가능한 통합 계층이 될 수 있습니다.
- 툴은 API 엔드포인트를 그대로 노출하기보다 사용자 의도(작업 목적) 중심으로 묶어 표면적을 줄이는 것이 좋습니다.
- 툴 정의를 필요할 때만 불러오고, 큰 툴 결과는 코드로 처리해 컨텍스트 사용량을 줄일 수 있습니다.
- OAuth 등 표준 인증과 토큰 보관 패턴을 활용해 프로덕션 운용에 대비합니다.

## 번들 리소스
- Agent Skill: `skills/mcp-production-integration-patterns/SKILL.md`

## 출처
- https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp
