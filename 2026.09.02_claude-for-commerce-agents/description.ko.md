[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude로 커머스 에이전트 만들기

## 이 글이 뭔가요

제품 발표다. Anthropic이 커머스 에이전트를 만들기 위한 공개 블루프린트를 내놓았다. **쇼핑
에이전트**와 **머천트 에이전트**의 레퍼런스 구현, 그리고 리테일·여행·통신·티케팅 예제가 함께 들어
있다. 헤드라인 수치는 이렇다. Claude로 쇼핑 에이전트를 운영한 리테일러들은 장바구니가 최대 35% 커지고,
구매 완료 확률이 60% 높아지는 것을 확인했다.

쇼핑 에이전트는 애플리케이션이나 웹사이트 안에 들어가 카탈로그 검색, 다중 상품 구성, 선호 반영, 상품
비교, 체크아웃 핸드오프를 위한 장바구니 구성, 고객 서비스 질문을 처리한다. 머천트 에이전트는 매출
성과 질문에 답하고, 재고를 추적하고, 가격과 프로모션을 추천하고, 캠페인을 초안한다. 언제나 사람이
배포 전에 승인하는 제안의 형태로.

Shopify, Priceline, Wix, Zomato, Fetch, Square가 이 위에서 만들고 있는 곳으로 언급되며, Accenture,
Mastercard, Visa가 파트너로 참여한다.

## 언제 유용한가요

- 커머스 에이전트 프로젝트를 시작하면서 빈 리포지토리가 아니라 동작하는 레퍼런스에서 출발하고 싶을 때.
- 카탈로그, 장바구니, 체크아웃, 선호, 주문 이력 중 에이전트가 호출해야 할 기존 시스템의 범위를 잡을 때.
- 구매자 쪽과 판매자 쪽 중 어디를 먼저 만들지 정할 때.
- 배포 위치를 알아야 할 때. Claude API, Amazon Bedrock, Microsoft Foundry, Google Cloud Vertex AI.

## 핵심 포인트

- **레퍼런스 에이전트 둘, 블루프린트 하나.** 쇼핑(소비자용)과 머천트(사업자용).
  [github.com/anthropics/commerce-agents](https://github.com/anthropics/commerce-agents)에 있다.
- **쇼핑 에이전트의 통합 지점**은 카탈로그 검색, 장바구니 관리, 체크아웃, 고객 선호, 주문 이력이다.
  에이전트는 이미 운영 중인 시스템을 호출한다.
- **쇼핑 가드레일이 함께 온다.** 가격과 상품은 카탈로그 데이터로 제한되고, 조작적 업셀 패턴은 배제된다.
- **머천트 원칙:** 에이전트는 변경을 제안하고, 사람이 배포 전에 승인한다.
- **Claude가 도는 곳이면 어디든 배포한다** — Claude API, Amazon Bedrock, Microsoft Foundry, Google
  Cloud Vertex AI.
- **셋업이 빠르다고 보고된다.** Wix 엔지니어들은 15분 만에 동작하는 커머스 에이전트를 얻었고, Fetch는
  두 에이전트를 한 시간 안에 로컬에서 돌렸으며 라이브 대화가 첫 시도에 동작했다.
- **신뢰가 명시된 제약이다.** 두 결제 파트너 모두 같은 틀로 말한다. Visa: *"AI는 커머스를 근본적으로
  재편할 것이다. 그러나 신뢰는 모든 거래의 중심에 남아야 한다."*
- **엔지니어링 상세는 별도의 글이다.** 아키텍처, 지연, 캐싱, 메모리, 안전, eval은 짝이 되는 심화 글
  *효과적인 커머스 에이전트의 해부학 가이드*에 있다.

## 번들 리소스

- `agents/shopping-agent.md` — 소비자용 에이전트. 통합 지점, 역량, 그리고 카탈로그 그라운딩과 조작적
  업셀 금지 가드레일.
- `agents/merchant-agent.md` — 사업자용 에이전트. 역량과 "적용하지 말고 제안하라" 운영 원칙.
- `skills/commerce-agent-blueprint/SKILL.md` — 블루프린트에서 배포를 스코핑하고 띄우는 방법.
- `skills/commerce-agent-blueprint/references/blueprint-contents.md` — 리포지토리에 들어 있는 것,
  역량별 정리.
- `skills/commerce-agent-blueprint/references/deployment-options.md` — 배포 위치, 파트너 생태계,
  이 위에서 만들고 있는 곳들.

## 출처

- https://claude.com/blog/claude-for-commerce-agents (게시일 2026-09-02)
- 엔지니어링 심화: https://claude.com/blog/the-anatomy-of-effective-commerce-agents
