[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Skills로 프론트엔드 디자인 품질을 끌어올리기

## 이 글이 뭔가요
이 글은 Claude **Skills**를 재사용 가능한 “디자인 지침 번들”로 만들어, 프론트엔드/UI 생성 결과가 흔한 ‘AI 기본값’(예: 특정 폰트/예측 가능한 그라디언트)으로 수렴하는 문제를 줄이는 방법을 설명합니다.

## 언제 유용한가요
- 랜딩 페이지, 대시보드, 앱 등 고객 노출 UI를 브랜드답게 만들고 싶을 때
- 디자인 규칙을 한 번 정리해두고 필요할 때만 불러와 쓰고 싶을 때(기본 프롬프트 비대화 방지)
- 단일 HTML 장난감 예제가 아니라 React + Tailwind + 컴포넌트 라이브러리 같은 현대적 스택으로 웹 산출물을 만들고 싶을 때

## 핵심 포인트
- Skills는 파일로 보관해 두었다가 작업에 맞춰 **필요할 때만** 불러오게 해서, 전문 지침을 시스템 프롬프트에 상시로 넣지 않아도 됩니다.
- 지침은 너무 추상적이어도, 반대로 픽셀/헥스 코드 수준으로 과도하게 고정해도 문제가 되므로 ‘적절한 고도’의 지시가 중요합니다.
- 타이포그래피/테마/모션/배경에서 흔한 기본값을 피하도록 구체적인 대안을 제시하면 결과 품질이 좋아집니다.
- 글에는 타이포그래피 선택 블록, RPG 테마 블록, 더 포괄적인 `frontend_aesthetics` 블록 예시가 포함됩니다.

## 번들 리소스
- Skill: `skills/frontend-design-aesthetics/SKILL.md`
- Guide (en/ko): `guides/frontend-design-skills-playbook.*.md`

## 출처
Claude 공식 블로그 글: https://claude.com/blog/improving-frontend-design-through-skills (게시 2025-11-12)
