[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Fine-tune Claude 3 Haiku in Amazon Bedrock

## 이 글이 뭔가요
이 글은 Amazon Bedrock에서 Claude 3 Haiku를 파인튜닝할 수 있게 된 소식을 소개하고, 무엇을 할 수 있는지와 시작 방법(액세스 요청 포함)을 설명합니다.

## 언제 유용한가요
분류, 도메인 특화 해석, 구조화된 출력 등 특정 업무에 더 잘 맞도록 Claude 3 Haiku를 커스터마이즈하면서도 지연과 비용을 낮게 유지하고 싶을 때 유용합니다.

## 핵심 포인트
- 파인튜닝은 고품질 프롬프트-완성(prompt–completion) 쌍 데이터로 Claude 3 Haiku를 특정 작업에 특화합니다.
- 파인튜닝은 AWS 환경 내부에서 진행되며 학습 데이터는 고객의 AWS 계정에 유지됩니다.
- Amazon Bedrock 콘솔 또는 API로 테스트/반복/배포 흐름을 구성할 수 있습니다.

## 번들 리소스
- Agent Skill: 프롬프트-완성 데이터 준비와 파인튜닝 결과 평가를 위한 체크리스트

## 출처
- https://claude.com/blog/fine-tune-claude-3-haiku
