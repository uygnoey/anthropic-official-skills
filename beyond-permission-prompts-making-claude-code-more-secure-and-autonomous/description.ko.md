[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
이 글은 에이전트형 코딩을 더 안전하고 더 자율적으로 만들기 위해 Claude Code에 추가된 **네이티브 샌드박싱** 기반 기능 2가지를 소개합니다. 연구 프리뷰 형태의 샌드박스된 bash 도구와, 클라우드 샌드박스에서 실행되는 웹용 Claude Code가 핵심입니다.

## 언제 유용한가요
반복적인 권한 승인 프롬프트 없이도 Claude Code(또는 다른 코딩 에이전트)가 더 많은 작업을 수행하도록 하되, 프롬프트 인젝션 등으로 인한 의도치 않은 도구 사용 위험을 낮추고 싶을 때 유용합니다.

## 핵심 포인트
- Claude Code는 기본적으로 권한 기반(기본 read-only)으로 동작하지만, 잦은 승인은 ‘승인 피로(approval fatigue)’를 유발할 수 있습니다.
- 글은 작업마다 권한을 묻는 방식보다 샌드박싱이 더 안전하면서도 더 자율적이라고 주장합니다.
- 효과적인 샌드박싱에는 **파일시스템 격리**(읽기/쓰기 가능한 디렉터리 제한)와 **네트워크 격리**(접속 가능한 호스트 제한)가 모두 필요합니다.
- 샌드박스된 bash 도구는 OS 수준 프리미티브(예: Linux bubblewrap, macOS seatbelt)를 사용해 제한을 강제합니다.
- 웹용 Claude Code는 각 세션을 격리된 클라우드 샌드박스에서 실행하되, 민감한 자격 증명은 샌드박스 밖에 두고 git 작업은 프록시로 처리합니다.

## 번들 리소스
- 이 글은 개념과 제품 기능 설명이 중심이며, 즉시 실행 가능한 정책 파일·hook 설정·스크립트 등은 제공하지 않습니다.

## 출처
- https://claude.com/blog/beyond-permission-prompts-making-claude-code-more-secure-and-autonomous
