[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Extending Claude's capabilities with skills and MCP servers

## 이 글이 뭔가요
이 글은 에이전트를 만들 때 Skill과 Model Context Protocol(MCP) 서버가 어떻게 역할을 분담하며 함께 동작하는지 설명합니다.

## 언제 유용한가요
여러 도구를 쓰는 다단계 워크플로에서 ‘절차적 지식(스킬)’과 ‘실시간 도구 연결(MCP)’ 중 무엇을 어디에 넣을지 결정해야 할 때 유용합니다.

## 핵심 포인트
- MCP는 외부 시스템에 대한 안전한 접근(연결성)을 제공하고, 스킬은 그 접근을 어떻게 활용할지에 대한 절차적 지식(전문성)을 제공합니다.
- 스킬은 다단계 워크플로·일관성 요구·도메인 전문성·조직의 암묵지 보존에 적합합니다.
- MCP는 실시간 데이터 조회, 외부 시스템에서의 액션, 파일 작업, API 통합이 필요할 때 적합합니다.
- 두 요소를 결합할 때 JSON 반환 등 MCP 지침과 스킬의 출력 형식 지침이 충돌하지 않게 주의해야 합니다.

## 번들 리소스
- 스킬: `skills-and-mcp-architecture-playbook` (Agent Skills)

## 출처
- https://claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers
