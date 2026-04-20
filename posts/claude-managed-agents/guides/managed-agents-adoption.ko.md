[English](./managed-agents-adoption.en.md) · **한국어** · [Español](./managed-agents-adoption.es.md) · [日本語](./managed-agents-adoption.ja.md)

# Claude Managed Agents 도입 플레이북

[Claude Managed Agents](https://claude.com/blog/claude-managed-agents) 2026년 4월 8일 출시 발표를 바탕으로 정리했습니다. 원문은 제품 발표 글이므로, 이 가이드는 그 내용을 의사결정 및 도입 플레이북 형태로 재구성한 것입니다. 원문에 없는 재사용 가능한 개발자 패턴은 포함하지 않습니다.

## 관리형 하네스가 필요한 이유

Managed Agents 이전에는 프로덕션용 에이전트를 출시하려면 엔지니어링 팀이 최소한 다음 항목을 직접 구축하거나 통합해야 했습니다.

- 샌드박스 코드 실행 환경
- 장기 실행 작업을 재개할 수 있는 체크포인팅
- 자격 증명 관리
- 실제 시스템에 대한 범위 지정 권한 관리
- 엔드투엔드 트레이싱
- 모델 업그레이드마다 재작성해야 하는 에이전트 루프

Managed Agents는 **오케스트레이션 하네스**(도구 호출 시점 결정, 컨텍스트 관리, 오류 복구 방법을 처리)와 운영 인프라를 함께 제공함으로써, 팀이 플랫폼 구축이 아닌 제품 출시에 집중할 수 있게 합니다.

## 제공 기능 요약

| 기능 | 설명 | 제공 현황 |
|---|---|---|
| 프로덕션급 에이전트 | 보안 샌드박싱, 인증, 도구 실행을 자동으로 처리 | 퍼블릭 베타 |
| 장기 실행 세션 | 몇 시간씩 자율 운영 가능; 연결이 끊겨도 진행 상황과 결과물이 유지됨 | 퍼블릭 베타 |
| 멀티 에이전트 조율 | 에이전트가 다른 에이전트를 생성·지시하여 복잡한 작업을 병렬 처리 | 리서치 프리뷰 (액세스 요청 필요) |
| 신뢰 기반 거버넌스 | 범위 지정 권한, 신원 관리, 실제 시스템에 대한 실행 트레이싱 | 퍼블릭 베타 |
| 결과 기반 모드 | 원하는 결과와 성공 기준을 정의하면 Claude가 자체 평가하며 반복 수행 | 리서치 프리뷰 (액세스 요청 필요) |
| 기존 프롬프트-응답 방식 | 더 세밀한 제어 흐름이 필요할 때 선택 | 퍼블릭 베타 |

## 의사결정 체크리스트: 직접 구축 vs. 도입

자체 에이전트 런타임을 작성하기 전에 아래 항목을 검토하세요. 각 항목은 Managed Agents가 이미 처리하는 사항과 대응됩니다.

- [ ] 샌드박스 격리, 커널 강화, 탈출 모니터링을 전담할 팀이 있는가?
- [ ] Claude 모델이 업그레이드될 때마다 에이전트 루프를 재구축할 준비가 되어 있는가?
- [ ] 연결 끊김, 배포, 장애 조치 상황에서도 장기 실행 세션을 안정적으로 유지할 수 있는가?
- [ ] 모든 도구 호출, 결정, 장애를 감사 가능한 형태로 추적할 방법이 있는가?
- [ ] 에이전트를 실제 시스템에 대한 1급 신원(first-class identity)으로 취급하는 범위 지정 권한 인프라가 있는가?
- [ ] 위 항목을 모두 구축한 뒤에도 몇 달이 아닌 몇 주 안에 제품 가치를 제공할 수 있는가?

하나라도 "아니오"라면 관리형 런타임을 선택하는 근거가 됩니다.

## Managed Agents 위에서 출시된 팀들

원문은 출시 시점의 실제 통합 사례를 열거합니다. 규범적인 패턴이 아닌 도입 참고 사례로 활용하세요.

| 팀 | 사용 사례 | 출처 |
|---|---|---|
| Notion | Notion 워크스페이스 안에서 Claude에게 작업을 위임; 수십 개의 작업을 병렬로 처리하고 팀이 결과물을 함께 검토 | Eric Liu, PM — [기사](https://claude.com/blog/claude-managed-agents) |
| Rakuten | 제품·영업·마케팅·재무 분야의 엔터프라이즈 에이전트를 Slack과 Teams에 연결; 각 전문 에이전트를 1주일 내에 배포 | Yusuke Kaji, GM of AI for Business — [기사](https://claude.com/blog/claude-managed-agents) |
| Asana | AI Teammates — Asana 프로젝트 내에서 작업을 맡아 결과물 초안을 작성하는 협업 에이전트 | Amritansh Raghav, CTO — [기사](https://claude.com/blog/claude-managed-agents) |
| Vibecode | 프롬프트 한 줄로 앱을 배포하는 플랫폼; 고객이 인프라를 최소 10배 빠르게 구성 | Ansh Nanda, Co-founder — [기사](https://claude.com/blog/claude-managed-agents) |
| Sentry | Seer(디버깅 에이전트)와 패치를 작성하고 PR을 여는 Claude 기반 에이전트를 결합 | Indragie Karunaratne, Sr Director Eng AI/ML — [기사](https://claude.com/blog/claude-managed-agents) |
| Atlassian | Jira 워크플로에 내장된 개발자 에이전트; Jira에서 직접 작업을 할당 | Sanchan Saxena, SVP Teamwork Collection — [기사](https://claude.com/blog/claude-managed-agents) |
| Casetext | 사용자의 문서와 서신에서 모든 질문에 답하기 위해 커스텀 도구를 즉석에서 코딩하는 시스템 | Javed Qadrud-Din, CTO — [기사](https://claude.com/blog/claude-managed-agents) |
| Rewatch | MCP를 통해 캘린더·연락처 도구를 갖춘 회의 준비 에이전트; 수일 만에 출시 | John Han, Co-founder — [기사](https://claude.com/blog/claude-managed-agents) |

## 도입 경로

원문에서 언급된 기능에 맞춰 단계별 도입 방법을 정리했습니다.

1. **먼저 단일 작업 실행기를 선택하세요.** 원문의 공통 패턴은 "1주일 내에 배포된 전문 에이전트"입니다. 멀티 에이전트 조율보다 여기서 시작하세요.
2. **작업, 도구, 가드레일을 정의하세요.** 이것이 여러분의 입력값이며, 하네스가 오케스트레이션, 컨텍스트 관리, 오류 복구를 담당합니다.
3. **Claude Platform에서 실행하세요.** Claude Console, 새 CLI, 또는 내장 `claude-api` Skill이 있는 Claude Code를 사용하세요 (`"start onboarding for managed agents in Claude API"`).
4. **계측하고 검사하세요.** Claude Console의 세션 트레이싱, 통합 분석, 문제 해결 기능을 활용해 모든 도구 호출과 장애 유형을 검토하세요.
5. **결과 기반 모드 도입 여부를 결정하세요.** 작업에 확인 가능한 성공 기준이 있다면 결과 모드 리서치 프리뷰 액세스를 요청하세요. 그렇지 않으면 프롬프트-응답 방식을 유지하세요.
6. **멀티 에이전트 조율은 필요할 때만 추가하세요.** 병렬 전문 에이전트가 측정 가능한 가치를 더할 때 리서치 프리뷰 액세스를 요청하세요.

## 비용 모델 계획

- 표준 Claude Platform 토큰 요금
- 활성 런타임에 대해 **세션 시간당 $0.08** 추가

계획에 반영해야 할 비용 변수는 두 가지입니다: 의사결정당 토큰 소비량과 에이전트가 활성 상태로 유지되는 실제 시간. 장기 자율 실행 세션은 단기 집중 실행보다 세션 시간 비용이 더 많이 발생하므로, 용량 계획 시 이 트레이드오프를 고려하세요.

## 이 포스트가 **다루지 않는 것**

- 자체 에이전트 하네스를 구축하는 방법에 대한 레퍼런스가 아닙니다
- 운영 규칙이 있는 명명된 에이전트 역할을 정의하지 않습니다
- 훅, 출력 스타일, 플러그인 번들링을 규정하지 않습니다

이 포스트는 도입 및 범위 설정 참고 자료로 활용하세요. 재사용 가능한 Claude Code 패턴은 이 리포지토리의 Skills와 Subagents를 참고하세요.

## 출처

[Claude Managed Agents: get to production 10x faster](https://claude.com/blog/claude-managed-agents) (게시일 2026-04-08).
