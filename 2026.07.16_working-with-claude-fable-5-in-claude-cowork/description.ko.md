[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Anthropic Education 팀의 Josefina Albert가, 길고 복잡하고 비동기적인 작업을 다룰 때 Claude Cowork — 지식 노동을 위한 Anthropic의 에이전트형 AI 시스템 — 안에서 Claude Fable 5와 함께 일하는 방법을 설명한다.

전제는 더 유능한 모델이 다른 작업 방식을 요구한다는 것이다. Cowork는 이미 큰 작업을 동시에 실행되는 여러 부분으로 쪼개고, 각 부분마다 별도의 서브에이전트를 붙이며, 시작 시점에 계획을 세운 뒤 그 계획에 자기 결과를 대조한다. 길고 다단계인 작업에서 Fable 5가 가진 우위는 바로 그 형태에 들어맞는다. 올해 실적을 바탕으로 내년 예산을 짜는 작업이라면, 시작 전에 워크플로를 계획하고 잘못 읽은 런레이트를 실행 도중에 잡아내 그 오류가 이후 모든 추정치로 흘러가기 전에 고친다. 이 모델과 일하는 것은 유능한 동료와 일하는 것에 가깝다. 상황을 설명하고, 좋은 결과물이 어떤 모습인지 합의한 뒤, 일하게 두면 된다.

## 언제 유용한가요
- Cowork 작업이 수십 단계에 걸치거나 며칠이 걸리고, 각 단계가 앞 단계 위에 쌓일 때.
- Sonnet 5, Opus, Fable 5 중 무엇을 고를지, 또는 어떤 effort 수준을 설정할지 판단할 때.
- 아직 정리되지 않은 아이디어에서 출발하면서, 내 파일과 도구에 접근할 수 있는 사고 파트너가 필요할 때.
- 결과만 중요한 작업인데도 계속 단계별 프롬프트를 쓰고 있을 때.
- 긴 대화가 예상보다 많은 사용량을 소모하고 있을 때.
- 예전 모델을 위해 쓴 스킬이나 메모리 파일이 새 모델을 제약하고 있을 수 있을 때.

## 핵심 포인트
- **Fable 5는 Cowork의 기본값이 아니다** — 직접 선택해야 한다. 기본값은 Sonnet 5이고 일상적인 작업에 맞는다. Opus는 형태가 분명한 깊은 작업에 적합하다. Fable 5는 가장 복잡하거나 모호한 프로젝트, 특히 여러 도구를 쓰고 일련의 판단이 필요한 작업을 위한 것이다.
- **effort 설정으로 선택을 더 다듬는다.** 높은 effort는 사전 계획과 실행 중 점검을 늘린다. Anthropic의 테스트에서 낮은 effort의 Fable 5는 이전 모델의 최고 effort와 대등하거나 그 이상인 경우가 많았다.
- **새 분류기가 Claude Opus 4.8로 라우팅한다.** 사이버보안 또는 생물·화학과 관련된 요청이 분류기를 발동시킬 수 있다. 발동 시 사용자에게 알려주며, 새 대화를 시작하기 전까지 대화는 Opus에 머문다. 보수적으로 조정되어 있어 오탐이 발생한다.
- **아이디어 하나만 있어도 시작할 수 있다.** Cowork에서의 브레인스토밍은 모델에게 실제 파일과 연결된 도구를 사고 재료로 준다. 두 가지 프롬프트: *"시작하기 전에, 이걸 제대로 하려면 알아야 할 걸 전부 나에게 물어봐."* 그리고 *"내가 원하는 건 대략 이거야. 가져갈 수 있는 방향 세 가지와 각각의 간단한 샘플을 줘."*
- **제약보다 맥락이 낫다.** 제약은 하지 말아야 할 것만 알려주지만, 맥락은 이 작업이 무엇을 위한 것인지 알려주므로 제약이 예상하지 못한 상황에서도 제대로 판단할 수 있다. 초안과 최종본을 함께 주면 그 차이에서 당신의 기준을 알아낸다.
- **긴 대화는 비용이 크다.** Claude는 메시지마다 대화 전체를 다시 읽는다. 새 작업은 새 대화에서 시작하고, 더 이상 필요 없는 예약 작업은 꺼두자.
- **접근 방식, 절차, 타이밍을 위임하라** — 방법론, 어떤 스킬을 쓸지, 일정. 단계를 직접 적는 것은 과정 자체가 중요할 때뿐이다.
- **계획 패널이 방향을 바꾸는 지점이다.** 무엇을 하려는지, 그리고 어떤 파일과 도구를 쓰는지 보여준다. 계획 속 잘못된 한 단계는 완성된 잘못된 결과물보다 고치기 싸다. 한 문장이면 처음부터 다시 하지 않고 수정된다.
- **셋업에 투자하라:** 매일 쓰는 도구를 연결하고, 글쓰기를 자기 목소리에 맞추고(Fable 5는 긴 세션에서 더 간결해지는 경향이 있다), 예전 모델용으로 쓴 스킬과 메모리를 점검하라.

## 번들 리소스
- `skills/delegating-complex-work-in-cowork/SKILL.md` — 전체 작업 방법: 모델과 effort 선택, 아이디어에서 출발, 맥락으로 브리핑, 결정 위임, 계획 관찰, 셋업 투자.
- `skills/delegating-complex-work-in-cowork/references/model-and-effort-selection.md` — 모델 선택표, 높은/낮은 effort가 바꾸는 것, Opus 4.8 폴백 작동 방식.
- `skills/delegating-complex-work-in-cowork/references/setup-checklist.md` — 도구 연결, 목소리 조정, 예전 모델용 설정 재점검.
- `skills/delegating-complex-work-in-cowork/templates/kickoff-prompts.md` — 원문에 나온 모든 프롬프트를 용도별로 정리.
- `skills/delegating-complex-work-in-cowork/examples/delegation-patterns.md` — 세 가지 위임 패턴과 예산·대시보드 사례 상세.
- `guides/working-with-a-frontier-model-in-cowork.{en,ko,es,ja}.md` — 4개 언어 전체 워크스루.

## 출처
[Working with Claude Fable 5 in Claude Cowork](https://claude.com/blog/working-with-claude-fable-5-in-claude-cowork) — Josefina Albert, 2026년 7월 16일.
