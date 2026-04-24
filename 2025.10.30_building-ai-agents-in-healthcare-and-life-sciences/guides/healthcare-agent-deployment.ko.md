[English](./healthcare-agent-deployment.en.md) · **한국어** · [Español](./healthcare-agent-deployment.es.md) · [日本語](./healthcare-agent-deployment.ja.md)

# 헬스케어/생명과학 AI 에이전트 배포 가이드

이 가이드는 원문을 배포 관점의 의사결정 흐름으로 압축 정리합니다.

## 1) 상호운용성 결정
1. 연결 방식(직접 연동, API/MCP 등 커스텀 커넥터, 미들웨어)을 선택합니다.
2. 데이터 수집/변환을 표준화합니다.
3. 임상적 긴급도에 따라 실시간 vs 배치 동기화를 정의합니다.

## 2) 안전/컴플라이언스 통제
- 거버넌스, 감사 추적, 운영 모니터링을 수립합니다.
- 임상적 효과 주장에는 근거 기반 검증을 요구합니다.

## 3) 사람 감독 모델
- 에스컬레이션/오버라이드 경로를 명확히 합니다.
- 안전 우선의 기본 동작을 채택합니다.

## 출처
- https://claude.com/blog/building-ai-agents-in-healthcare-and-life-sciences
