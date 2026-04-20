[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude Code에 루틴(Routines) 도입

## 이 글이 뭔가요

2026년 4월 14일 리서치 프리뷰로 출시된 Claude Code **루틴(routines)** 기능 안내. 루틴은 한 번 구성해 두는 Claude Code 자동화입니다. 프롬프트, 리포지토리, 커넥터를 묶어 스케줄, API 호출, 이벤트 트리거로 실행할 수 있습니다. 루틴은 Claude Code의 웹 인프라에서 동작하므로 노트북을 켜 둘 필요가 없습니다.

## 언제 유용한가요

- 개발 사이클 자동화에 Claude Code를 쓰지만 크론 잡, 인프라, 추가 MCP 툴링을 직접 관리하고 있을 때
- 알림 시스템, 배포 훅, 사내 툴과 Claude Code를 HTTP로 붙이고 싶을 때
- GitHub PR 이벤트에 반응해 자동으로 Claude Code 세션이 시작되길 원할 때
- 야간 백로그 트리아지, 주간 문서 드리프트 스캔 같은 스케줄 작업이 필요할 때
- CI/CD 파이프라인에서 배포 검증, 알림 트리아지, 피드백→PR 워크플로를 Claude Code로 돌리고 싶을 때

## 핵심 포인트

- 리서치 프리뷰에서 **세 가지 트리거**: 스케줄(시간/일/주간 단위), API(루틴별 엔드포인트 + 인증 토큰), 웹훅(우선 GitHub 리포 이벤트)
- 스케줄 루틴은 기존 `/schedule` CLI 플로우를 대체합니다. 기존 `/schedule` 태스크가 루틴으로 전환됩니다.
- API 루틴은 각자의 엔드포인트와 인증 토큰을 받습니다. 메시지를 POST하면 세션 URL을 받습니다.
- GitHub 웹훅 루틴은 매칭되는 PR마다 Claude 세션을 하나씩 열고, 해당 PR의 코멘트·CI 실패 같은 업데이트를 계속 세션에 공급합니다.
- 초기 사용 패턴: 백로그 트리아지, 문서 드리프트 스캔, 배포 검증, 알림 트리아지, 피드백 해결, SDK 간 라이브러리 포트, 팀 맞춤 코드 리뷰
- 제공 범위: Pro, Max, Team, Enterprise (Claude Code on the web 활성화). claude.ai/code 또는 CLI `/schedule`로 생성
- 일일 한도: Pro 최대 5개, Max 최대 15개, Team/Enterprise 최대 25개. 초과분은 extra usage로 가능. 루틴은 인터랙티브 세션과 동일하게 구독 사용량을 소비

## 번들 리소스

- `skills/code-routines/SKILL.md` — 트리거 타입 선택과 좋은 루틴 프롬프트 작성법
- `skills/code-routines/examples/prompts.md` — 본문의 스케줄/API/GitHub 웹훅 프롬프트 예시
- `skills/code-routines/references/patterns.md` — 본문의 초기 사용 패턴 전체 목록
- `guides/routines-overview.{en,ko,es,ja}.md` — 네 언어 서술형 가이드

## 출처

- [Introducing routines in Claude Code](https://claude.com/blog/introducing-routines-in-claude-code) — 2026년 4월 14일 게시.
