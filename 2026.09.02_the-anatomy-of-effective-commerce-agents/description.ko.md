[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# 효과적인 커머스 에이전트의 해부학 가이드

## 이 글이 뭔가요

Ali Shazal과 Matthew Koen이 쓴 긴 엔지니어링 가이드로, Anthropic이 리테일·마켓플레이스·여행·
엔터테인먼트·통신 분야의 엔터프라이즈 팀들과 일하며 얻은 것을 정리했다. 프로덕션 커머스 에이전트를
만드는 과정을 네 부분으로 짚는다. 아키텍처, 빠르고 저렴하게 만들기, 프로덕션 운영, 그리고 모델이
바뀌어도 남는 것.

핵심 주장은 아키텍처에 관한 것이다. 커머스 에이전트는 **표준 에이전트 루프 안의 모델 하나**여야 하며,
모듈성은 서브에이전트 부대가 아니라 에이전트 스킬로 얻어야 한다. 커머스 대화는 의도와 턴을 넘나들며
강하게 결합되어 있어서, 서브에이전트 핸드오프마다 상태를 잃고 토큰 비용이 배가되고 지연이 붙는다.
스킬을 갖춘 단일 에이전트는 하나의 프롬프트로 전부 처리하는 설계와 서브에이전트 설계를 품질에서
일관되게 앞질렀고, 태스크당 비용과 지연도 대체로 더 낮았다.

## 언제 유용한가요

- 쇼핑 에이전트나 머천트 에이전트를 설계하면서 어떻게 분해할지 정해야 할 때.
- 에이전트가 동작은 하는데 너무 느리거나 태스크당 비용이 과해서, 어느 레버를 먼저 당길지 알아야 할 때.
- 매 턴 지연 비용을 치르지 않으면서 세션을 넘어가는 장기 메모리가 필요할 때.
- 에이전트가 장바구니·주문·가격·환불·예산을 건드릴 수 있어서, 모델의 선의에 의존하지 않는 강제가
  필요할 때.
- 여러 팀이 동시에 바꾸는 비결정적 시스템의 eval 스위트를 만들 때.

## 핵심 포인트

- **서브에이전트가 아니라 스킬.** 핸드오프는 상태를 잃고 비용을 배가하고 지연을 더하며, 커머스 도메인
  경계는 깔끔하게 나뉘지 않는다. 서브에이전트는 딥 리서치처럼 좁고 자기완결적인 작업이나, 이미 자체
  컴플라이언스를 가진 전용 에이전트를 운영하는 도메인에만 남긴다.
- **배치는 빈도로 결정한다.** 대부분의 턴에서 필요한 내용(대략 트래픽의 3분의 1 이상)은 시스템
  프롬프트, 롱테일은 스킬. 안전·법률·브랜드·사용자 안전 내용은 빈도와 무관하게 시스템 프롬프트다.
- **툴은 이미 운영 중인 시스템을 호출한다.** 툴 경계가 그 시스템의 로직이 끝나고 모델의 판단이
  시작되는 지점이다. 원본 응답은 툴 내부에서 재구성하고, 오류에는 에러 코드 대신 행동 가능한 안내를
  반환한다.
- **UI 컴포넌트는 툴이다.** `present_products`, `present_itinerary` — messages 배열에 네이티브 저장,
  타입 안전성, 참조 가능한 레이아웃("세 번째 것"), 점진적 스트리밍. 인자는 서버에서 버퍼링되며,
  `eager_input_streaming: true`는 스키마 보장 일부를 토큰 단위 스트리밍과 맞바꾼다.
- **지연 = (턴 수 × 마지막 토큰까지의 시간) + 툴 시간.** 더 적은 턴, 더 빠른 툴, 더 빠른 토큰.
  컨텍스트를 미리 적재하고, 지능으로 턴을 되사고, 병렬 툴 호출을 켜고, 조기 디스패치한다.
- **체감 지연은 별개의 문제다.** 컴포넌트를 점진적으로 스트리밍하고, 툴 인자나 `user_facing_message`
  파라미터로 만든 짧은 진행 문구를 보여준다.
- **프롬프트 캐싱이 최대의 비용 레버다.** 변경 빈도순 세 구간 — 글로벌(바이트 단위 동일), 세션,
  휘발성(맨 끝). 스킬은 툴 결과로 적재하고 브레이크포인트는 앞으로 굴린다. 최고의 배포는 90~99%
  히트율로 돌아간다.
- **모델은 스윕으로 고른다.** 품질·지연·비용 지표를 정의하고, 모델과 effort 레벨 전반에 전체 eval
  스위트를 돌리고, 모델별로 프롬프트를 다시 튜닝하고, 태스크당 비용을 측정한다. 비슷하면 지능을
  택한다.
- **메모리는 에이전트 밖에서 비동기로 쓴다.** 별도 프로세스가 대화를 읽고 타입이 있는 사실을 생성·
  갱신·삭제한다. 지연 비용이 없고 내부 eval에서 사실 회수율이 13% 높았다. 추출기는 사용자와
  어시스턴트 텍스트만 읽고 툴 결과는 읽지 않는다.
- **메모리는 세 레이어로 읽는다.** 항상 컨텍스트에, 턴마다 프리페치, 그리고 조회 툴 뒤에.
- **안전 강제는 하네스에 산다.** 모델은 준비하고 사람이나 정책이 적용한다. 쓰기와 렌더는 서버 발급
  ID만 받는다. 상한은 결과 상태에 대해 강제하고 세션별 쓰기를 직렬화한다. 모든 서드파티 콘텐츠는
  소독하며, 펜스 안의 텍스트는 보고 대상일 뿐 실행 대상이 아니다.
- **대화 시뮬레이션이 아니라 스냅샷 eval.** 상태를 직접 구성해 최종 상태와 응답을 채점한다.
  시뮬레이션 사용자 실행은 커버리지 발견용일 뿐이다. 길고 지저분하고 모순적인 이력에서 시작하라.
  창발적 실패는 거기 있다.
- **소유권과 선별 CI 스위트로 출시한다.** 핵심 고트래픽 케이스 + 안전 케이스 전부 + 변경이 건드리는
  케이스. 에이전트는 단일 배포 단위이므로 카나리로 내보내고 릴리스 캘린더에 올린다.

## 번들 리소스

- `skills/commerce-agent-architecture/SKILL.md` — 단일 에이전트 + 스킬 설계, 배치 규칙, 툴 설계,
  UI 컴포넌트를 툴로.
- `skills/commerce-agent-architecture/references/skills-vs-subagents.md` — 전체 트레이드오프와
  서브에이전트가 여전히 맞는 두 경우.
- `skills/commerce-agent-architecture/references/capability-map.md` — 레퍼런스 구현의 쇼핑·머천트
  에이전트 프롬프트/스킬 분배.
- `skills/commerce-agent-architecture/references/ui-components-as-tools.md` — 이점, 버퍼링
  트레이드오프, `eager_input_streaming`.
- `skills/commerce-agent-latency-and-cost/SKILL.md` — 세 개의 지연 레버, 체감 지연, 캐싱, 모델 선택.
- `skills/commerce-agent-latency-and-cost/references/prompt-cache-segments.md` — 세 구간 레이아웃과
  체크리스트.
- `skills/commerce-agent-latency-and-cost/references/model-selection-sweep.md` — 스윕 절차와
  타이브레이커.
- `skills/commerce-agent-memory/SKILL.md` — 타입 레코드, 비동기 추출, 세 개의 읽기 레이어.
- `skills/commerce-agent-memory/templates/memory-fact-record.json` — 사실 레코드 형태.
- `skills/commerce-agent-memory/references/memory-data-handling.md` — 보존, 수정, 삭제, 배포 단위
  토글.
- `skills/commerce-agent-safety-harness/SKILL.md` — 네 가지 강제 원칙.
- `skills/commerce-agent-safety-harness/references/safety-principles.md` — 각 원칙의 전문.
- `skills/commerce-agent-safety-harness/scripts/sanitize_untrusted_content.py` — 리스팅, 리뷰,
  정책, 판매자 메시지, 저장된 메모리를 위한 실행 가능한 새니타이저.
- `skills/commerce-agent-evals/SKILL.md` — 스냅샷 테스트와 다섯 개의 커버리지 영역.
- `skills/commerce-agent-evals/references/eval-coverage-matrix.md` — 전체 케이스 매트릭스.
- `skills/commerce-agent-evals/references/ci-suite-selection.md` — 소유권, CI 선별, 릴리스 캘린더
  실천.
- `skills/commerce-agent-evals/templates/snapshot-case.md` — 채워 넣는 스냅샷 케이스.
- `guides/anatomy-of-a-commerce-agent.{en,ko,es,ja}.md` — 가이드 전문 4개 언어.

## 출처

- https://claude.com/blog/the-anatomy-of-effective-commerce-agents (게시일 2026-09-02)
