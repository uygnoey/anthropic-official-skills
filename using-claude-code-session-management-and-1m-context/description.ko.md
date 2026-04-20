[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude Code: 세션 관리와 1M 컨텍스트 활용

## 이 글이 뭔가요

Claude Code 팀이 세션과 컨텍스트 윈도(이제 최대 100만 토큰)를 어떻게 관리해야 결과가 좋아지는지 정리한 실용 가이드입니다. 새 슬래시 명령 `/usage`를 소개하고, 컨텍스트 로트(context rot)와 컴팩션(compaction)을 설명하며, 매 턴을 continue / `/rewind` / `/clear` / `/compact` / 서브에이전트 다섯 가지로 분기할 수 있는 결정점으로 제시합니다.

## 언제 유용한가요

- Claude Code 세션을 오래 쓸수록 결과 품질이 떨어진다고 느낄 때
- `/compact`, `/clear`, 되돌리기(rewind), 서브에이전트 중 무엇을 쓸지 고민될 때
- 컨텍스트가 아직 "쓸모 있는" 상태인지, 덜어내야 하는 상태인지 판단 기준이 필요할 때
- 자동 컴팩션이 잘못돼 결과가 망가진 경험이 있을 때
- 작업 위임용 서브에이전트 프롬프트 예시가 필요할 때

## 핵심 포인트

- 컨텍스트 윈도는 시스템 프롬프트, 대화 전체, 모든 도구 호출/출력, 읽은 파일까지 전부 포함하며 하드 컷오프입니다.
- **Context rot**: 컨텍스트가 커질수록 어텐션이 분산되고 오래된 내용이 현재 작업을 방해하면서 성능이 저하됩니다.
- **컴팩션**은 윈도가 차면 히스토리를 모델이 쓴 요약으로 대체합니다. `/compact <hint>`로 직접 트리거할 수도 있습니다.
- 매 턴은 분기점: Continue, `/rewind`(Esc 두 번), `/clear`, `/compact`, 서브에이전트.
- 원칙: **새 작업 = 새 세션**. 단, 방금 구현한 기능의 문서화처럼 이어지는 작업은 컨텍스트를 유지하는 편이 빠르고 저렴합니다.
- **수정보다 되돌리기**: Claude가 잘못된 방향으로 갔을 때 "안 됐어"라고 지시하지 말고, 유용한 파일 읽기 직후로 `/rewind` 한 뒤 배운 내용을 담아 다시 프롬프트하세요.
- **Compact vs Clear**: compact는 손실이 있지만 쉽고, clear는 수작업이 더 들지만 무엇을 이월할지 내가 정합니다.
- **나쁜 자동 컴팩션**은 모델이 당신의 다음 방향을 예측하지 못할 때 발생합니다. 윈도가 차기 전에 힌트를 담아 선제적으로 compact 하세요.
- **서브에이전트**: 다음 단계가 최종 결론만 필요할 만큼 중간 출력이 많을 때 최적. 판단 기준: *도구 출력을 또 쓸 건가, 결론만 필요한가?*

## 번들 리소스

- `skills/context-window-management/SKILL.md` — continue/rewind/compact/clear/서브에이전트 선택 프레임워크
- `skills/context-window-management/references/decision-table.md` — 본문의 상황 → 도구 결정표
- `skills/context-window-management/examples/subagent-prompts.md` — 본문에 인용된 서브에이전트 위임 프롬프트
- `guides/session-management-1m-context.{en,ko,es,ja}.md` — 네 언어 서술형 가이드

## 출처

- [Using Claude Code: session management and 1M context](https://claude.com/blog/using-claude-code-session-management-and-1m-context) — 2026년 4월 15일 게시.
