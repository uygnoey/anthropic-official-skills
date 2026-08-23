[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Thomson Reuters는 175년 역사의 콘텐츠·기술 기업으로, 법률·세무·회계·컴플라이언스 등 정밀함을 요구하는 전문 업무 흐름에 AI를 적용하고 있다. 이 글은 CTO Joel Hron이 들려주는 이야기다. 법정에서 버텨야 하는 일에 모델이 적합한지를 회사가 어떻게 판단하는지, 그리고 적합하다고 판단한 뒤 제품에서 무엇을 바꿨는지에 대한 기록이다.

이야기를 조직하는 축은 책임의 소재다. "최종 결과물에 대해 책임을 지는 것은 여전히 그 인간 전문가"이고, 그래서 모델에 적용되는 시험은 벤치마크 점수가 아니라 그 결과물이 전문가의 법률 검토를 견디는가이다. 이렇게 나온 접근에 회사가 붙인 이름이 Fiduciary-Grade AI™다. 권위 있는 콘텐츠에 접지하고, 도메인 전문성으로 다듬고, 전문 업무 흐름 안에 심는다.

후반부는 아키텍처 이야기다. 더 똑똑한 챗봇을 만드는 대신 Thomson Reuters는 제품을 에이전트 기반 시스템으로 다시 만들었다. CoCounsel Legal은 별개의 스킬을 순차 실행하던 구조에서, Claude Agent SDK 위의 단일 에이전트가 실시간으로 수백 개 도구를 가로질러 계획하고 조율하는 구조로 옮겨 갔다.

## 언제 유용한가요
- 결과물이 책임지는 사람의 검토를 견뎌야 하고, "대체로 맞음"이 곧 실패일 때.
- 규제 대상이거나 이해관계가 큰 업무를 모델에 맡기기 전에 무엇을 요구할지 정할 때.
- 제품이 별개 기능들의 모음이고, 사용자가 직접 순서를 짜고 있을 때.
- 넓은 도구 표면을 가로질러 계획하는 에이전트를 위해 모델을 평가할 때.
- 인용 검증을 사람의 검토를 기준으로 어디에 둘지 설계할 때.
- AI 이니셔티브를 보고하는데 태스크당 비용만 요구받고 있을 때.

## 핵심 포인트
- **시험은 벤치마크가 아니라 전문가 검토다.** Thomson Reuters는 모델의 결과물이 전문가의 법률 검토를 견딜 수 있는지를 물어 평가한다.
- **AI가 책임을 대신 지지 않는다.** "최종 결과물에 대해 책임을 지는 것은 여전히 그 인간 전문가입니다." — Joel Hron
- **세 가지 강점, 하나의 시스템.** 권위 있는 콘텐츠, 깊은 도메인 전문성, 워크플로 통합. Anthropic의 프런티어 모델을 큐레이션된 콘텐츠, 2,700명 이상의 도메인 전문가, 평가 인프라와 결합한다.
- **Fiduciary-Grade AI™**는 결과물이 "이해관계가 클 때에도 투명하고, 검증 가능하며, 방어 가능"함을 뜻한다.
- **법률 리서치는 검증을 축으로 다시 만들어졌다.** 단순 검색·조회가 아니라 인용 검증과 확인에 맞춰 조정된 에이전트 덕분에, 전문가는 확신을 가지고 검토하고 검증하고 판단할 수 있다.
- **모델을 신뢰하기 전 네 가지 요구 사항:** 사람 검토 이전의 인용 검증, 긴 도구 사용 사슬 전반의 컨텍스트 관리, 에이전트에 의존하는 대신 결과물을 만들어 가는 과정에 사람을 끌어들이는 협업, 그리고 전문가가 며칠~몇 주 다듬을 신청서·제출 문서까지 포함하는 고급 초안 작성으로의 역량 확장.
- **더 똑똑한 챗봇이 아니라 에이전트 우선.** 이제 하나의 에이전트가 수백 개의 사내 도구에 동시에 접근한다.
- **CoCounsel Legal의 재구축:** 별개 스킬의 순차 실행에서 Claude Agent SDK 위의 실시간 계획·조율로. 고객 데이터는 보호되며 서드파티 모델 학습에 쓰이지 않는다.
- **무엇을 시험하는가:** "Claude에 대한 우리의 큰 시험은 계획을 세우는 능력과 도구를 효과적으로 쓰는 능력이 얼마나 좋은지를 평가하는 것입니다."
- **왜 Anthropic인가:** 투명성, 안전성, 책임 있는 AI 개발에 대한 접근 방식. 초기의 확신은 함께 만든 딥 리서치 역량에서 나왔다.
- **ROI에 대한 통념 반대 입장.** "수익률 계산을 너무 최적화하려 들면 나무를 보다 숲을 놓칩니다." 태스크당 비용 지표보다 문화적 사고방식 전환이 먼저다. 다만 DORA와 프로덕션 투입 시간은 여전히 추적한다.
- **구체적인 수치 하나:** Claude 위에 만든 사내 오류 대응 도구가 근본 원인 분석을 3시간에서 4분으로 줄였다.
- **일 자체가 달라졌다.** "코드를 한 줄 한 줄 쓰는 행위는 더 이상 그 직무가 아니다." 이제는 시스템적 사고, 판단력, 안목이 가장 중요하고, 같은 패턴이 사람들을 제품·디자인·재무를 가로지르는 더 "T자형"으로 만든다.
- **다음 단계:** 더 긴 호흡의 작업, 더 나은 컨텍스트 관리, 에이전트 작업 사슬 전반에서 믿을 수 있는 도구 호출. Hron 본인은 코드베이스 파악에 Claude Code를, 전략 분석에 Claude Cowork를 쓴다.
- **기준선:** 전문가용 AI는 "거의 맞는 것으로는 충분하지 않은" 환경에서 작동해야 한다.

## 번들 리소스
- `skills/defensible-ai-outputs/SKILL.md` — 권위 있는 콘텐츠에 접지하고, 검토 전에 인용을 검증하고, 네 가지 요구 사항을 충족하고, 투명성·검증 가능성·방어 가능성을 점검한다.
- `skills/defensible-ai-outputs/references/four-requirements.md` — 각 요구 사항이 실무에서 뜻하는 바와, 원문이 명시하지 않은 부분.
- `skills/defensible-ai-outputs/templates/citation-validation-checklist.md` — 주장 단위·산출물 단위 게이트, 그리고 책임지는 전문가에게 넘길 때의 인계 양식.
- `skills/defensible-ai-outputs/examples/professional-workflows.md` — 검증을 축으로 다시 만든 법률 리서치, 고급 초안 작성, 오류 대응 도구.
- `skills/agent-first-product-rebuild/SKILL.md` — 사용자가 하던 순서 짜기를 계획하는 에이전트로 대체하고, 도구를 넓게 노출하고, 계획과 도구 사용으로 모델을 시험한다.
- `skills/agent-first-product-rebuild/references/agent-architecture.md` — 전후 비교, 아키텍처가 모델에 요구하는 것, 그리고 남은 질문들.
- `skills/agent-first-product-rebuild/references/measuring-the-shift.md` — ROI에 대한 입장, 여전히 추적하는 지표, 그리고 일에 일어난 더 깊은 변화.
- `skills/agent-first-product-rebuild/templates/agent-readiness-review.md` — 계획, 도구 사용, 컨텍스트 관리, 그리고 네 가지 전문가 요구 사항을 기록으로.
- `skills/agent-first-product-rebuild/examples/cocounsel-rebuild.md` — CoCounsel Legal 재구축의 상세.
- `guides/building-ai-for-high-stakes-work.{en,ko,es,ja}.md` — 4개 언어로 정리한 전체 이야기.

## 출처
[Working at the Frontier: How Thomson Reuters Builds AI for High-Stakes Professional Work](https://claude.com/blog/working-at-the-frontier-how-thomson-reuters-builds-ai-for-high--stakes-professional-work) — Claude 블로그, 2026년 7월 8일.
