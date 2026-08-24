[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Anthropic 필드 마케터가 Claude Code로 모든 세일즈 담당자에게 주간 맞춤 업데이트를 보내는 방법

## 이 글이 뭔가요

Anthropic의 필드 마케터 Adam Ward가, 일요일 저녁마다 손으로 만들던 슬라이드를 대체해 자신이 지원하는 모든 세일즈 담당자에게 월요일 아침 맞춤 다이제스트를 자동으로 보내는 시스템을 어떻게 만들었는지 설명한다. 마케팅 해커톤에서 약 한 시간 만에 초안을 만들고, 이후 몇 주간의 파일럿 피드백으로 다듬었다.

Ward의 핵심 주장은, 마케터에게 필요한 것은 코딩 실력이 아니라 자신의 비즈니스 문제를 명확히 설명하는 능력이라는 것이다. 그는 스스로를 기술자가 아닌 프로덕트 매니저로 규정하는 프롬프트로 시작했고, 문제 설명을 음성으로 녹음해 Claude에 비즈니스 맥락을 전달했으며, 원하는 출력 형식을 보여주는 템플릿 예시를 제공했다.

## 언제 유용한가요

- 주간·월간처럼 반복되는 업데이트를 손으로 개인화하느라 시간이 많이 들 때
- 여러 팀을 지원하면서 같은 브리핑을 대상별로 다시 잘라내야 할 때
- CRM, 이벤트, 콘텐츠 데이터가 여러 시스템에 흩어져 있고 이를 담당자별로 매칭해야 할 때
- 처음에는 자기 검토 루프로 시작해 나중에 자율 발송으로 넘어가는 롤아웃 경로가 필요할 때

## 핵심 포인트

- **비즈니스 문제부터 말한다.** 새로 온 동료에게 인수인계하듯 Claude에 브리핑한다. Ward는 자신을 기술자가 아닌 프로덕트 매니저로 규정했고, 문제 설명을 음성으로 녹음해 비즈니스 맥락을 전달했다.
- **원하는 형식을 보여준다.** "이번 주의 top three things" 구조로 실행 가능한 항목을 우선하는 출력 템플릿 예시가, 추상적인 지시보다 효과가 컸다.
- **실제 데이터를 연결한다.** Claude를 MCP로 BigQuery에 연결했다. BigQuery는 HubSpot, Clay, Salesforce에서 데이터를 끌어오는 Anthropic 마케팅 데이터 소스다. 개인화는 CRM의 담당 영역, Slack의 관련 어카운트 업데이트, 그리고 마케팅 이니셔티브와의 매칭에서 나온다.
- **모든 수정 요청을 명시적 규칙으로 바꾼다.** 첫 주가 지난 뒤 프롬프트에는 각각 특정 피드백에서 유래한 아홉 개의 명시적 콘텐츠 규칙이 담겼다. URL을 절대 지어내지 말고 정확한 원본 데이터에 있는 링크만 렌더링할 것, 컨택의 직함을 이벤트 대상과 대조해 검증할 것, 산업 게이트를 두어 리테일 어카운트에 금융 중심 이벤트가 가지 않게 할 것, 아직 담당 어카운트가 없는 신규 셀러에게는 별도의 환영 메시지를 쓸 것 등이다.
- **스키마 변경에도 견디게 만든다.** 필드 이벤트 시트의 열 순서가 6주 동안 세 번 바뀌었다. 해법은 Claude가 먼저 헤더 행을 읽고 열 매핑을 검증하게 하는 것이었다. 열 번호를 하드코딩하는 대신 "이벤트 URL이 있는 열을 보라" 같은 의미 기반 지시를 사용했다.
- **의욕 있는 소그룹으로 파일럿한다.** 피드백을 주기로 약속한 10명 규모의 세일즈 팀 하나가, 더 넓은 롤아웃 전에 데이터 품질과 관련성 문제를 드러내 주었다.
- **확장은 복사 + 필드 하나 수정이다.** BDR들이 자기 버전을 요청했을 때 Ward는 프롬프트를 복제하고, BDR이 CRM에서 어카운트에 매핑되는 방식을 나타내는 필드 하나만 바꿨다. 이틀 만에 출시됐다. 이어서 고객 성공, 얼라이언스, 세일즈 외부의 크로스펑셔널 파트너 버전이 나왔다.
- **측정 가능한 효과.** 다이제스트 도입 후 일주일 만에 임원 디너 등록자가 두 배가 됐다. 월요일 발송분은 감사와 책임 추적을 위해 매번 아카이브되고, 매니저는 팀 단위 롤업을 받으며, Ward가 휴가 중일 때도 시스템은 스스로 돌아갔다.

## 번들 리소스

- `skills/personalized-weekly-digests/SKILL.md` — Claude Code로 반복 맞춤 다이제스트를 구축하고 운영하기
- `skills/personalized-weekly-digests/templates/kickoff-prompt.md` — 비즈니스 문제를 규정하는 첫 브리핑
- `skills/personalized-weekly-digests/templates/digest-message-template.md` — "top three things" 메시지 구조
- `skills/personalized-weekly-digests/references/content-rules.md` — 파일럿 피드백에서 도출된 규칙 목록
- `skills/personalized-weekly-digests/references/data-sources.md` — 데이터 연결과 스키마 변동 대응
- `skills/personalized-weekly-digests/examples/feedback-to-rule.md` — 피드백을 규칙으로 바꾼 실제 예시
- `guides/automating-a-recurring-personalized-briefing.{en,ko,es,ja}.md` — 4개 언어 롤아웃 방법론

## 출처

- https://claude.com/blog/how-an-anthropic-field-marketer-uses-claude-code-to-send-weekly-personalized-updates-to-every-sales-rep (2026-08-24 게시, Adam Ward)
