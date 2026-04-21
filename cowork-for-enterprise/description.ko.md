[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
이 글은 Claude Cowork가 모든 유료 플랜에서 정식 제공(GA)되었음을 알리고, 엔터프라이즈 운영에 필요한 관리/거버넌스 기능과 커넥터를 소개합니다.

## 언제 유용한가요
회사에서 Claude Cowork를 운영·관리하는 입장에서 역할 기반 접근 제어, 팀별 예산(지출 한도), 사용량 분석, 도구/커넥터 활동에 대한 관측 가능성(Observability)이 필요할 때 유용합니다.

## 핵심 포인트
- Enterprise용 역할 기반 접근 제어(RBAC): 사용자를 그룹(예: SCIM 연동 포함)으로 구성하고, Claude 기능을 정의하는 커스텀 역할을 할당.
- 그룹(팀) 단위 지출 한도: 팀별 예산 설정.
- 사용량 분석: 관리자 대시보드 + Analytics API(사용자별 활동, 스킬/커넥터 호출 등).
- OpenTelemetry 이벤트 확장: 도구/커넥터 호출, 파일 읽기/수정, 사용된 스킬, AI-initiated 액션 승인 여부 등.
- Zoom MCP 커넥터: 회의 요약/액션 아이템/전사/녹화 등을 Cowork 워크플로에 연결.
- 커넥터별 액션 제어: 조직 전체에서 특정 커넥터의 쓰기 동작을 비활성화하고 읽기만 허용하는 식의 제한.

## 번들 리소스
- 글에서 소개한 엔터프라이즈 관리 기능을 정리한 스킬: `skills/cowork-enterprise-admin-controls/SKILL.md`.

## 출처
- https://claude.com/blog/cowork-for-enterprise
