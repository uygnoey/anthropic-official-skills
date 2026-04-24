[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
이 글은 “어드바이저 전략(advisor strategy)”을 소개합니다. 더 강한 모델(Opus)을 어드바이저로, 더 저렴한 모델(Sonnet 또는 Haiku)을 실행자(executor)로 짝지어, 전체 비용을 낮추면서도 고난도 판단에서는 프런티어급 조언을 얻는 방식입니다.

## 언제 유용한가요
대부분의 구간에서는 도구를 사용해 끝까지 실행하면서도, 어려운 의사결정 순간에만 더 높은 추론 품질이 필요할 때 유용합니다. 가장 강한 모델을 모든 토큰에 쓰지 않고도 성능과 비용의 균형을 잡을 수 있습니다.

## 핵심 포인트
- 실행자(Sonnet/Haiku)가 작업을 끝까지 수행합니다(도구 호출, 결과 읽기, 반복 실행).
- 필요할 때 실행자가 어드바이저(Opus)에게 상담하고, 어드바이저는 계획/수정/중단 신호를 반환하지만 도구 호출이나 사용자-facing 출력은 하지 않습니다.
- Claude Platform의 “advisor tool”을 사용하면 Messages API 요청에 소폭 변경만으로 단일 요청 내부에서 모델 전환이 이뤄집니다.
- `max_uses`로 어드바이저 호출 횟수를 제한할 수 있고, 사용량(토큰)은 별도로 보고됩니다.

## 번들 리소스
- 어드바이저 전략을 정리하고 원문 API 스니펫을 포함한 스킬: `skills/advisor-strategy-playbook/SKILL.md`.
- 원문 API 스니펫을 그대로 담은 실행 가능한 예시 파일: `skills/advisor-strategy-playbook/examples/messages_api_example.py`.

## 출처
- https://claude.com/blog/the-advisor-strategy
