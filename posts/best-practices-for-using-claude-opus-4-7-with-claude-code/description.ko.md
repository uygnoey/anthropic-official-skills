[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Claude Code에서 Opus 4.7의 동작 특성과, 프롬프트·설정(노력도/effort, adaptive thinking, 세션 구성)을 조정해 품질과 토큰 효율을 높이는 방법을 설명합니다.

## 언제 유용한가요
Opus 4.6에서 4.7로 업그레이드(또는 신규 설정)하면서, 동작을 예측 가능하게 만들고 토큰 사용량을 관리하며 effort 레벨별 활용 기준이 필요할 때 유용합니다.

## 핵심 포인트
- 첫 턴에 의도·제약·수용 기준·관련 파일 위치를 한 번에 제공하면, 턴이 늘어나며 발생하는 추가 추론을 줄이고 품질을 높일 수 있습니다.
- 대화형 세션에서 사용자 턴이 늘어날수록 추론 오버헤드가 커지므로, 질문을 묶고 필요한 상호작용을 줄이는 것이 유리합니다.
- Claude Code에서 Opus 4.7의 기본 effort는 `xhigh`( `high`와 `max` 사이)이며 대부분의 에이전트 코딩 작업에 권장됩니다. 작업 중에도 effort를 바꿔 비용/지연과 성능을 조절할 수 있습니다.
- Opus 4.7은 고정 예산의 Extended Thinking이 아니라 adaptive thinking을 사용하며, 더/덜 생각하도록 프롬프트로 직접 요청할 수 있습니다.
- 행동 변화: 작업 난이도에 따라 답변 길이가 조정되고, 도구 호출은 줄고 추론은 늘며, 기본적으로 subagent 생성이 줄었습니다. 더 많은 도구 사용이나 병렬 subagent가 필요하면 명시해야 합니다.

## 번들 리소스
- 1 skill (opus-4-7-claude-code-best-practices)
- 1 guide set (opus-4-7-claude-code-best-practices)

## 출처
- Best practices for using Claude Opus 4.7 with Claude Code (2026-04-16): https://claude.com/blog/best-practices-for-using-claude-opus-4-7-with-claude-code
