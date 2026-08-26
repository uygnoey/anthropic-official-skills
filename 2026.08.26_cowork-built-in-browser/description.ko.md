[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Cowork에 자체 브라우저가 생겼습니다

## 이 글이 뭔가요

제품 공지입니다. 데스크톱 앱의 Claude Cowork에 전용 브라우저가 내장되었습니다. 작업에 웹사이트가
필요하면 사이드 패널에 브라우저가 열리고, Claude가 페이지를 이동하며 읽고 클릭하고 입력합니다. 이
브라우저가 Claude in Chrome과 어떻게 다른지, 어떤 상황에서 무엇을 골라야 하는지, 로그인을 사이트
단위로 어떻게 가져오는지, 프롬프트 인젝션으로부터 세션을 무엇이 지키는지, 유료 플랜과 엔터프라이즈
관리자에게 어떻게 배포되는지를 다룹니다.

## 언제 유용한가요

- 다른 창에서 계속 일하는 동안 웹 작업을 따로 돌리고 싶을 때.
- 특정 작업에 내장 브라우저와 Claude in Chrome 중 무엇을 쓸지 정해야 할 때.
- 개인 탭·북마크·비밀번호를 노출하지 않고 에이전트가 사이트에 접근하게 하고 싶을 때.
- 조직에 내장 브라우저를 켜야 하는 엔터프라이즈 관리자일 때.

## 핵심 포인트

- **데스크톱 앱 안의 브라우저.** 작업에 웹사이트가 필요하면 사이드 패널에 브라우저가 열리고,
  Claude가 웹페이지를 이동하며 읽고 클릭하고 입력합니다.
- **개인 브라우징과 분리되어 있습니다.** Claude는 사용자의 탭, 북마크, 비밀번호를 절대 보지
  않습니다.
- **로그인은 사이트 단위로 가져옵니다.** macOS에서는 Chrome, Edge, Firefox에서, Windows와
  Linux에서는 Firefox에서 가져올 수 있습니다. 금융, 이메일, SSO 사이트는 명시적으로 포함하지 않는
  한 기본적으로 제외됩니다.
- **내장 브라우저는** 다른 일을 계속하는 동안 돌아가야 하는 웹 작업에 씁니다 — 리서치 수집, 공급업체
  포털에서 청구서 모으기 같은 일.
- **Claude in Chrome은** 이미 열어 두고 로그인해 둔 페이지에 씁니다 — CRM 업데이트, 받은편지함
  처리, 문서 편집.
- **기본값은 사용 이력에 따라 달라집니다.** 이미 Claude in Chrome을 쓰고 있는지에 따라 전환되며,
  Settings → Cowork → Preferred browser에서 직접 선택할 수 있습니다.
- **위험은 프롬프트 인젝션입니다.** 페이지에 숨겨진 지시문이 Claude의 방향을 틀려고 합니다. 내장
  브라우저에는 Claude in Chrome과 동일한 안전장치가 적용되며, 여기에는 사용자가 요청한 내용과 실제
  동작이 맞는지 검사하는 절차가 포함됩니다. 이런 장치는 위험을 유의미하게 줄이지만 완전히 없애지는
  못하므로, 신뢰할 수 있는 사이트부터 시작하세요.
- **배포.** Pro, Max, Team 플랜에 한 주에 걸쳐 macOS, Windows, Linux(베타)로 배포됩니다. Claude에게
  웹 작업을 맡기는 것 외에 별도 설정은 필요 없습니다. 엔터프라이즈 관리자는 Organization settings →
  Cowork → Built-in browser에서 바로 켤 수 있습니다.
- **브라우저는 데스크톱에 있습니다.** 데스크톱 앱이 열려 있고 연결되어 있으면 웹과 모바일에서도 쓸
  수 있고, 데스크톱 앱 없이 웹만 쓰는 경우에는 계속 Claude in Chrome을 사용합니다.

## 번들 리소스

- `skills/desktop-browser-routing/SKILL.md` — 내장 브라우저와 Claude in Chrome 중 무엇을 고를지,
  그리고 어느 쪽이든 안전하게 쓰는 법.
- `skills/desktop-browser-routing/references/browser-choice.md` — 두 브라우저 비교.
- `skills/desktop-browser-routing/references/logins-and-safety.md` — 로그인 가져오기 범위와
  프롬프트 인젝션 대응 태세.
- `guides/built-in-browser-rollout.{en,ko,es,ja}.md` — 배포, 관리자 활성화, 설정.

## 출처

<https://claude.com/blog/cowork-built-in-browser> (2026-08-26)
