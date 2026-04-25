[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요

이 글은 Claude Code hooks를 설정해 반복 작업을 자동화하고, 프로젝트 규칙을 강제하며, 코딩 세션에 필요한 컨텍스트를 주입하는 방법을 설명합니다.

## 언제 유용한가요

도구 실행 전/후, 세션 시작/종료, 컴팩션 전/후, 중단(Stop) 등의 라이프사이클 이벤트에서 자동으로 커맨드 실행이나 프롬프트 기반 점검을 수행하고 싶을 때 유용합니다.

## 핵심 포인트

- hooks는 JSON으로 설정하며, 라이프사이클 이벤트(예: PreToolUse, PostToolUse, SessionStart, Stop)에 하나 이상의 동작을 매핑합니다.
- hook 동작은 커맨드를 실행하거나(prompt 타입) 점검 프롬프트를 삽입할 수 있습니다.
- matcher는 대소문자를 구분하며, 여러 규칙이 매칭되면 병렬로 실행될 수 있습니다.
- hooks는 사용자 권한으로 임의의 셸 커맨드를 실행하므로, stdin 입력을 검증/정제하고 민감한 파일(.env, 자격증명 등)을 다룰 때 주의해야 합니다.
- 기본 타임아웃은 60초이며, hook별로 설정할 수 있습니다.

## 번들 리소스

- hook 입력/출력을 로깅하기 위한 재사용 래퍼 스크립트: `hooks/log-wrapper.sh`
- 자주 쓰는 패턴을 위한 예시 hook 설정:
  - Write 전에 파일 경로를 검증 (`hooks/pretooluse-validate-write-path.json`)
  - PermissionRequest로 테스트 커맨드 제한 (`hooks/permissionrequest-validate-tests.json`)
  - Write/Edit 뒤 자동 포매팅 (`hooks/posttooluse-format-written-files.json`)
  - 컴팩션 전에 트랜스크립트 백업 (`hooks/precompact-backup-transcript.json`)
  - SessionStart에 프로젝트 컨텍스트 표시 (`hooks/sessionstart-show-context.json`)
  - SessionStart에 세션 로그 기록 (`hooks/sessionstart-log-session.json`)
  - Stop 시 완료 여부 점검 강제 (`hooks/stop-completion-check.json`)
  - SubagentStop에서 서브에이전트 결과 검토 (`hooks/subagentstop-review.json`)
  - UserPromptSubmit에서 스프린트 컨텍스트 주입 (`hooks/userpromptsubmit-inject-context.json`)

## 출처

- https://claude.com/blog/how-to-configure-hooks
