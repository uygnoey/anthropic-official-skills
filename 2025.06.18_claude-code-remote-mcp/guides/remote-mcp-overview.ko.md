[English](./remote-mcp-overview.en.md) · **한국어** · [Español](./remote-mcp-overview.es.md) · [日本語](./remote-mcp-overview.ja.md)

## Claude Code의 원격 MCP란?
원격 MCP 지원을 통해 Claude Code는 벤더가 운영하는 MCP 서버에 연결하여, 서드파티 도구와 리소스를 코딩 워크플로 안에서 직접 사용할 수 있습니다.

## 왜 중요한가요
- 로컬 서버 대비 유지보수 부담이 낮습니다(업데이트/스케일링/가용성을 벤더가 관리).
- 네이티브 OAuth로 안전하게 연결할 수 있습니다.
- 외부 시스템(예: 이슈 트래커, 에러 모니터링)에서 구조화된 컨텍스트를 가져올 수 있습니다.

## 일반적인 흐름
1. 벤더 MCP 서버를 선택합니다.
2. Claude Code에 벤더 URL을 추가합니다.
3. 한 번 인증합니다(OAuth).
4. 노출된 도구/리소스를 워크플로에서 사용합니다.

## 출처
- https://claude.com/blog/claude-code-remote-mcp
