[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# AI 가속 공격 시대의 보안 프로그램 준비

## 이 글이 뭔가요

AI 모델이 취약점을 빠르게 찾고 체이닝·공격에 활용하는 환경에 맞춰 보안 프로그램을 어떻게 조정해야 하는지에 대한 Anthropic 보안팀의 가이드입니다. 7개 영역("지금 할 일": 패치 갭, 취약점 리포트 물량, 출시 전 버그 찾기, 기존 코드 감사, 침해 가정 설계, 노출 축소, 사고 대응)과 함께 AI가 관여한 취약점 리포트를 어떻게 작성할지, 보안팀이 없는 소규모 조직용 간소화 체크리스트, 그리고 CISA KEV·EPSS·NIST SSDF·OWASP ASVS·SLSA·OpenSSF Scorecard·CISA Zero Trust·MITRE ATT&CK·NIST CSF 2.0 등 표준으로 이어지는 참조 테이블을 담고 있습니다.

## 언제 유용한가요

- AI 기반 공격 속도에 맞춰 기존 보안 프로그램을 재정비할 때
- 패치 갭·취약점 관리·사고 대응 정책 업데이트 초안을 쓸 때
- CI에 AI 보조 코드 리뷰(SAST 인접)를 도입하는 책임 있는 롤아웃 경로가 필요할 때
- AI 보조 취약점 리포트를 제출하거나 받을 때 품질 기준이 필요할 때
- 소규모 조직이나 오픈소스 프로젝트의 간소화된 실행 목록이 필요할 때

## 핵심 포인트

- 패치 갭 닫기: CISA KEV 즉시, 나머지는 EPSS 기준, 인터넷 노출 시스템 24시간 목표, 안전한 범위에서 자동화
- 취약점 리포트 물량이 한 자릿수가 아닌 두 자릿수 배 증가한다고 전제하고, AI로 트리아지·중복 제거·패치 초안 생성
- 출시 전 버그 찾기: CI에 SAST + AI 리뷰, CD에 자동 펜테스트, 빌드 체인 보호(SLSA), Secure by Design, 신규 코드는 메모리 안전 언어 우선
- 기존 코드 감사: 비신뢰 입력 파서, 인증·인가 경계, 인터넷에서 접근 가능한 경로, 레거시 코드부터
- 침해 가정 설계: 제로 트러스트, 하드웨어 기반 신원, 짧은 수명 토큰, 마찰만 주는 통제 대신 실질적 장벽 도입
- 노출 축소·인벤토리, 주인 없는 서비스 폐기, 자체 외부 자동 레드팀 운영
- 사고 대응 시간 단축: 큐 맨 앞에 트리아지 에이전트, dwell time 지표, AI 스크라이브, 사전 합의된 긴급 변경 절차
- AI 보조 취약점 리포트는 사람이 검증하고 본인 이름을 걸 수 있을 때만 보낼 것
- 모두 SOC 2 / ISO 27001 통제에 자연스럽게 매핑

## 번들 리소스

- `skills/closing-the-patch-gap/SKILL.md` — 패치 갭 관리의 우선순위·롤아웃 재사용 패턴
- `skills/writing-quality-vuln-reports/SKILL.md` — AI 보조 취약점 리포트 체크리스트와 자가 점검
- `agents/security-triage-agent.md` — SIEM 질의 도구를 갖춘 트리아지 에이전트 (원문 명시)
- `agents/vulnerability-scanning-agent.md` — 파서·인증·외부 도달 경로를 스캔하는 격리 에이전트 (원문 명시)
- `agents/external-red-team-agent.md` — 자사 perimeter에 대한 자율 외부 레드팀 에이전트 (원문 명시)
- `guides/security-program-playbook.{en,ko,es,ja}.md` — 7개 영역 전체 롤아웃 플레이북 + 표준 참조를 4개 언어로

## 출처

[Preparing your security program for AI-accelerated offense](https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense) (게시 2026-04-10)를 바탕으로 정리했습니다.
