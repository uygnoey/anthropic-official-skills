[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
이 글은 Claude Code에서 보안 리뷰를 자동화하는 방법을 소개합니다. 터미널에서 즉시 실행하는 `/security-review` 명령과, Pull Request를 자동으로 검사하는 GitHub Actions 연동이 포함됩니다.

## 언제 유용한가요
- 커밋 전에 주요 취약점을 빠르게 점검하고 싶을 때
- PR마다 자동으로 보안 이슈를 찾아내고 수정 제안을 남기는 CI 워크플로우를 만들고 싶을 때

## 핵심 포인트
- `/security-review` 명령은 SQL 인젝션, XSS, 인증/인가 결함, 안전하지 않은 데이터 처리, 의존성 취약점 등을 점검할 수 있습니다.
- GitHub Action은 PR diff에 코멘트를 남기며, 커스텀 규칙으로 오탐을 줄이도록 설정할 수 있습니다.
- 이슈를 찾은 뒤 Claude Code에게 수정 구현까지 요청할 수 있습니다.

## 번들 리소스
- Skill: `skills/security-review-automation/SKILL.md`

## 출처
- https://claude.com/blog/automate-security-reviews-with-claude-code
