[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Evaluate prompts in the developer console

## 이 글이 뭔가요
이 글은 Anthropic Console의 Evaluate 기능을 소개하며, 프롬프트 생성·테스트 케이스 생성·버전 간 출력 비교로 프롬프트를 개선하는 흐름을 설명합니다.

## 언제 유용한가요
배포 전에 프롬프트 변경을 반복적으로 검증하고, 배치 테스트와 평가를 통해 품질을 확인해야 할 때 유용합니다.

## 핵심 포인트
- Console의 프롬프트 생성기로 작업 설명에서 초기 프롬프트를 생성할 수 있습니다.
- CSV로 테스트 케이스를 가져오거나, 변수별 생성 요구사항을 바탕으로 테스트 케이스를 자동 생성할 수 있습니다.
- 테스트 스위트를 한 번에 실행하고, 프롬프트 버전 간 출력을 나란히 비교하며 반복 개선할 수 있습니다.
- 필요하면 SME가 5점 척도로 응답 품질을 채점해 개선 여부를 추적할 수 있습니다.

## 번들 리소스
- 스킬: `console-prompt-evaluation-workflow` (Agent Skills)

## 출처
- https://claude.com/blog/evaluate-prompts
