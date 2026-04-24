[English](./managed-agents-memory.en.md) · **한국어** · [Español](./managed-agents-memory.es.md) · [日本語](./managed-agents-memory.ja.md)

## 이 가이드에서 다루는 내용
Claude Managed Agents의 파일시스템 기반 메모리를 도입할 때 참고할 수 있는 짧은 체크리스트입니다.

## 체크리스트
- 세션을 가로질러 기억해야 할 내용과 기억하지 말아야 할 내용을 정의합니다.
- 스토어 구조 및 권한 스코프를 결정합니다(예: 조직 공용 읽기 전용 vs 사용자별 읽기/쓰기).
- 운영 제어를 계획합니다: 내보내기, 감사 가능성, 롤백, 삭제(레닥션).
- Claude Console에서 세션 이벤트로 추적 가능성을 확인합니다.

## 출처
https://claude.com/blog/claude-managed-agents-memory
