[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
이 글은 Claude Managed Agents에서 파일시스템 기반의 내장 메모리를 퍼블릭 베타로 제공한다는 소식을 소개합니다.

## 언제 유용한가요
별도의 메모리 인프라를 직접 구축·운영하지 않고도, 세션을 거치며 개선되는 프로덕션 에이전트를 만들고 싶을 때 유용합니다.

## 핵심 포인트
- 메모리는 세션을 가로질러 학습하고, 여러 에이전트 간에 학습 내용을 공유하는 장기 실행 에이전트를 염두에 두고 설계되었습니다.
- 메모리는 파일시스템에 직접 마운트되므로, 에이전트가 익숙한 도구(bash 및 코드 실행)를 활용해 메모리를 다룰 수 있습니다.
- 메모리는 파일 형태로 휴대 가능하며, 엔터프라이즈 운영에 필요한 제어(권한 스코프, 감사 로그, 내보내기/롤백/삭제(레닥션), API 기반 관리)를 제공합니다.
- 변경 사항은 Claude Console에서 세션 이벤트로도 표시되어 추적성을 높입니다.

## 번들 리소스
- Skill: managed-agents-memory-overview (개념 요약 및 구현 고려사항)
- Guide: managed-agents-memory (배포/운영 체크리스트)

## 출처
https://claude.com/blog/claude-managed-agents-memory
