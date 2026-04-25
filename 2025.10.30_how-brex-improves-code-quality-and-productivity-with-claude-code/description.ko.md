[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
이 글은 Brex 팀이 Claude Code를 일상 업무에 어떻게 활용하는지(엔지니어링 리뷰 워크플로, 콘텐츠/디자인 시스템 유지보수, 텍스트→SQL 기반 데이터 접근 등)를 사례 중심으로 소개합니다.

## 언제 유용한가요
조직 전반에 Claude Code 도입을 추진하면서, 구조화된 컨텍스트 파일 운영, CI/CD에서의 문서 갱신 점검, 컨텍스트-인식 커스텀 커맨드 같은 구체적인 확산 패턴이 필요할 때 유용합니다.

## 핵심 포인트
- Claude Code는 “리뷰어 마인드셋”을 가능하게 합니다. 엔지니어는 구현 디테일보다 방향을 잡고 변경사항을 검토하는 데 집중합니다.
- 비기술 직군도 간단한 문자열 수정 PR을 직접 올리거나, 표준 준수 여부를 자동 점검하는 Figma 플러그인 같은 도구를 만들 수 있습니다.
- Claude Code와 MCP 서버를 결합해 텍스트→SQL 인터페이스로 데이터 접근을 민주화할 수 있습니다.
- 확산을 위한 운영 패턴으로 디렉터리별 CLAUDE.md 컨텍스트, 문서 갱신을 유도하는 CI/CD 체크, /submit-pr 같은 컨텍스트-인식 커스텀 커맨드가 강조됩니다.

## 번들 리소스
- 글의 확산 패턴을 재사용 가능한 “Claude Code 조직 도입 플레이북”(컨텍스트 관리, 문서 위생, 커스텀 커맨드) 형태로 정리한 Agent Skill 1개.

## 출처
- https://claude.com/blog/how-brex-improves-code-quality-and-productivity-with-claude-code
