[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# 반응형 웹 레이아웃 만들기

## 이 글이 뭔가요
이 글은 Claude(특히 Claude Code)를 사용해 반응형 웹 레이아웃을 생성하거나 기존 CSS를 리팩터링하여 다양한 뷰포트 크기에서 안정적으로 동작하게 만드는 방법을 다룹니다.

## 언제 유용한가요
- 고정 폭(fixed width)과 경직된 레이아웃 규칙 때문에 모바일/태블릿에서 오버플로우가 발생하거나 가독성이 떨어질 때.
- 수동으로 브레이크포인트를 반복 수정하는 방식 대신, 테스트 기반으로 체계적인 반응형 리팩터링을 하고 싶을 때.

## 핵심 포인트
- Claude Code가 스타일시트를 읽고 경직된 제약을 찾아 `max-width`, `flex-basis`, `auto-fit` 그리드 같은 유연한 대안으로 바꾸는 데 도움을 줄 수 있습니다.
- 브레이크포인트별 미디어 쿼리를 추가하고, 320px·512px 같은 작은 뷰포트에서 가로 오버플로우가 없는지 확인합니다.
- Playwright 테스트를 생성해 iPhone/iPad/데스크톱 등 다양한 디바이스 크기에서 동작을 검증할 수 있습니다.

## 번들 리소스
- Skill: `responsive-layout-refactor` (지침, 프롬프트 예시, 스니펫 예시)

## 출처
- https://claude.com/blog/build-responsive-web-layouts
