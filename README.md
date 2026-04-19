# Anthropic Official Skills

> Auto-generated `SKILL.md` files distilled from official [Anthropic / Claude blog posts](https://www.claude.com/blog).
> Each skill is written in **Korean and English**, with runnable examples.

이 저장소는 **Anthropic 공식 블로그 글**을 기반으로, Claude를 더 잘 사용하기 위한 실용 스킬(프롬프트·패턴·예제)을 자동으로 정리합니다.
매시간 배치가 돌면서 신규 글 또는 아직 정리되지 않은 글을 찾아 `SKILL.md`로 변환하여 커밋합니다.

## 구조 / Structure

```
skills/
  <slug>/
    SKILL.md          # KR + EN, examples included
    source.json       # 원 글 URL, 날짜, 처리 메타데이터
scripts/
  process_blog.py     # 배치 스크립트 (Perplexity Computer가 호출)
state/
  processed.json      # 이미 처리된 글 목록 (중복 방지)
```

## 원칙 / Principles

1. **출처 명시**: 모든 SKILL.md 상단에 원본 블로그 URL과 게시일을 명시합니다.
2. **한국어 + 영어 병기**: 각 섹션을 KR / EN 순으로 제공합니다.
3. **실행 가능한 예시**: 프롬프트 샘플, 코드 스니펫 등 바로 복사해서 쓸 수 있는 예시를 포함합니다.
4. **근거 없는 확장 금지**: 원 글에 명시된 내용만 요약·정리합니다. 추측이나 보강은 하지 않습니다.

## 배치 동작 / Batch behavior

- 매시간 1회 Perplexity Computer가 `scripts/process_blog.py`의 실행 로직을 수행합니다.
- `https://www.claude.com/sitemap.xml` 에서 `/blog/` URL 목록을 수집합니다.
- `state/processed.json`에 없는 URL이 있으면 본문을 가져와 SKILL.md를 생성합니다.
- 한 번 실행 시 최대 몇 개의 새 글을 처리하여 과도한 API 호출을 방지합니다.

## 라이선스 / License

- 원문(Anthropic 블로그 글)의 저작권은 Anthropic에 있습니다. 이 저장소는 학습·참고 목적의 요약·인용만 포함합니다.
- 저장소 자체 코드(스크립트, 구조)는 MIT License.
