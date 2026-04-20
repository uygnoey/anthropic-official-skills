[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Claude Code의 Auto mode(자동 모드)를 소개합니다. Claude가 많은 도구 실행을 자동으로 승인하되, 위험한 행동을 막기 위한 안전장치를 함께 적용하는 권한 모드입니다.

## 언제 유용한가요
승인 팝업을 줄이면서도 장시간 작업을 돌리고 싶지만, --dangerously-skip-permissions처럼 권한 체크를 완전히 건너뛰기는 부담스러울 때 유용합니다.

## 핵심 포인트
- 기본 권한 모드는 파일 쓰기와 bash 실행마다 승인 요청이 발생하며, Auto mode는 이런 중단을 줄이기 위해 설계되었습니다.
- 각 도구 호출 전 분류기(classifier)가 대량 삭제, 민감 데이터 반출, 악성 코드 실행 등 파괴적 행동 가능성을 점검합니다.
- 안전하다고 판단된 작업은 자동 진행되고, 위험 작업은 차단되어 다른 접근을 시도하도록 유도되며, 반복 차단 시 최종적으로 사용자 승인 프롬프트가 뜹니다.
- --dangerously-skip-permissions보다 위험을 낮추지만, 위험이 완전히 사라지는 것은 아니므로 격리된 환경 사용을 권장합니다.
- 개발자는 `claude --enable-auto-mode`로 켠 뒤 Shift+Tab으로 모드를 전환할 수 있고, 관리자는 관리 설정의 `disableAutoMode`로 비활성화할 수 있습니다.

## 번들 리소스
- 1 skill (auto-mode-permissions)

## 출처
- Auto mode for Claude Code (2026-03-24): https://claude.com/blog/auto-mode
