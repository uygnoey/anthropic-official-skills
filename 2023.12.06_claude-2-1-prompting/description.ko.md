[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
이 글은 Claude 2.1에서 긴 컨텍스트(needle-in-a-haystack 유형) 검색 정확도를 높이는 간단한 프롬프트 수정 방법을 설명합니다.

## 언제 유용한가요
긴 문서(최대 약 200K 토큰)를 제공하고, 문서 안의 특정 문장(특히 문맥에서 벗어나 있거나 삽입된 문장)을 근거로 답을 받아야 할 때 유용합니다.

## 핵심 포인트
- Claude 2.1은 200K 토큰 컨텍스트 윈도우와 강한 장문 검색 성능을 제공합니다.
- 모델이 단일 문장(특히 문맥에서 벗어난 문장)에 근거해 답변하기를 주저할 수 있습니다.
- 답변을 “Here is the most relevant sentence in the context:”로 시작하라는 짧은 지시를 추가하면 정확도가 크게 향상됩니다.

## 번들 리소스
- Skill: long-context-needle-finding
- 프롬프트 템플릿: needle 찾기용 응답 선두 문장

## 출처
- https://claude.com/blog/claude-2-1-prompting
