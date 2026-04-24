[English](./routines-overview.en.md) · **한국어** · [Español](./routines-overview.es.md) · [日本語](./routines-overview.ja.md)

# Claude Code 루틴(Routines) 개요

*Introducing routines in Claude Code* (2026년 4월 14일, 리서치 프리뷰)를 서술형으로 정리했습니다.

## 루틴이란

루틴은 한 번 구성해 두는 Claude Code 자동화입니다. 프롬프트, 리포지토리, 커넥터를 묶어 스케줄, API 호출, 이벤트 트리거로 실행합니다. Claude Code의 웹 인프라에서 실행되므로 노트북을 켜 둘 필요가 없습니다.

개발자들은 이미 Claude Code로 개발 사이클을 자동화하고 있지만, 지금까지는 크론 잡, 인프라, 추가 MCP 툴링을 직접 관리해야 했습니다. 루틴은 리포지토리와 커넥터가 붙은 상태로 배포되기 때문에 자동화를 한 번만 패키징해 두면 됩니다.

## 세 가지 트리거

### 스케줄 루틴

프롬프트와 주기(시간/일/주간)를 주면 그 일정으로 실행됩니다. 공식 예시:

> Every night at 2am: pull the top bug from Linear, attempt a fix, and open a draft PR.

CLI의 `/schedule`을 사용 중이었다면 그 태스크들이 이제 스케줄 루틴입니다.

### API 루틴

루틴마다 고유 엔드포인트와 인증 토큰을 받습니다. 엔드포인트로 메시지를 POST하면 세션 URL이 돌아옵니다. 알림 시스템, 배포 훅, 사내 툴 등 HTTP 요청을 보낼 수 있는 어디든 Claude Code를 붙일 수 있습니다. 예시:

> Read the alert payload, find the owning service, and post a triage summary to #oncall with a proposed first step.

### 웹훅 루틴 (GitHub부터 시작)

GitHub 리포지토리 이벤트에 반응해 루틴을 자동 실행할 수 있습니다. 필터에 매칭되는 PR마다 Claude가 새 세션을 만들어 루틴을 돌립니다. 예시:

> Please flag PRs that touch the /auth-provider module. Any changes to this module need to be summarized and posted to #auth-changes.

PR마다 세션이 하나 열리고, 해당 PR의 코멘트나 CI 실패 같은 업데이트가 계속 세션으로 공급되므로 후속 반응이 가능합니다. 향후 더 많은 이벤트 소스로 웹훅 루틴을 확장할 계획도 언급돼 있습니다.

## 팀들이 만들고 있는 것들

### 스케줄
- **백로그 관리**: 매일 밤 새 이슈를 트리아지하고 라벨/담당자를 붙이고 Slack에 요약을 올린다
- **문서 드리프트**: 주 단위로 머지된 PR을 훑어 변경된 API를 참조하는 문서를 찾아 업데이트 PR을 연다

### API
- **배포 검증**: CD 파이프라인이 배포마다 호출 → Claude가 새 빌드에 대해 스모크 체크를 돌리고 에러 로그에서 리그레션을 찾고 릴리스 채널에 go/no-go를 올린다
- **알림 트리아지**: Datadog이 루틴 엔드포인트를 호출 → Claude가 트레이스를 가져와 최근 배포와 상관 분석을 해 두고, on-call이 페이지를 열기 전에 초안 픽스를 준비해 둔다
- **피드백 해결**: 문서 피드백 위젯이나 사내 대시보드가 리포트를 올리면 Claude가 해당 리포에 세션을 열어 이슈 컨텍스트로 변경 초안을 작성한다

### GitHub
- **라이브러리 포트**: Python SDK에 PR이 머지될 때마다 병렬 Go SDK로 변경을 포트하고 매칭 PR을 연다
- **맞춤 코드 리뷰**: PR이 열릴 때마다 팀 체크리스트(보안·성능)를 돌려 사람 리뷰어가 보기 전에 인라인 코멘트를 남긴다

## 시작하기

루틴은 Claude Code on the web이 활성화된 Pro, Max, Team, Enterprise 플랜에서 바로 쓸 수 있습니다. claude.ai/code에서 첫 루틴을 만들거나 CLI에서 `/schedule`을 치면 됩니다.

루틴은 인터랙티브 세션과 동일하게 구독 사용량을 소비합니다. 일일 한도:

- Pro: 하루 최대 5개
- Max: 하루 최대 15개
- Team / Enterprise: 하루 최대 25개

초과분은 extra usage로 실행할 수 있습니다. 자세한 내용은 공식 문서 참고.

## 출처

- [Introducing routines in Claude Code](https://claude.com/blog/introducing-routines-in-claude-code) — 2026년 4월 14일.
