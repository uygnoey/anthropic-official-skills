[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요

이 글은 Claude를 위한 Skills를 실무적으로 작성하는 방법을 다룹니다. Skill이 잘 트리거되도록 name/description을 쓰는 법, SKILL.md 구조화, 테스트와 반복 개선까지 포함합니다.

## 언제 유용한가요

Claude 앱(claude.ai), Claude Code, 또는 Skills API로 재사용 가능한 Skill을 만들고 싶을 때, 이름/설명(트리거링), 지시문 구조, 테스트 전략, 컨텍스트 크기 관리에 대한 가이드가 필요하면 유용합니다.

## 핵심 포인트

- Skill의 핵심 구성요소는 name, description(트리거링에 가장 중요), instructions입니다.
- description은 무엇을 할 수 있는지, 언제 활성화되어야 하는지, 어디까지가 범위 밖인지까지 구체적으로 써야 합니다.
- SKILL.md는 단계/전제조건/에러 처리/예시를 포함해 스캔 가능한 구조로 작성합니다.
- 컨텍스트가 비대해지지 않도록 컴패니언 파일을 링크하는 “메뉴” 접근을 권장합니다.
- 정상/엣지/범위 밖 요청으로 테스트 매트릭스를 만들고, 실제 사용 결과를 기반으로 반복 개선합니다.

## 번들 리소스

- 바로 적용 가능한 Skill 작성 템플릿: `skills/skill-authoring-guide/templates/skill-template.md`
- Skill 검증용 테스트 매트릭스 템플릿: `skills/skill-authoring-guide/templates/test-matrix.md`
- 글의 SKILL.md 예시를 기반으로 정리한 발췌 모음: `skills/skill-authoring-guide/examples/skill-examples.md`

## 출처

- https://claude.com/blog/how-to-create-skills-key-steps-limitations-and-examples
