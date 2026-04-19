# Scripts

## list_pending.py
아직 처리되지 않은 블로그 글 URL을 출력합니다.

```bash
python scripts/list_pending.py --limit 3
```

## mark_processed.py
SKILL.md 생성이 끝난 글을 `state/processed.json`에 기록합니다.

```bash
python scripts/mark_processed.py \
  https://claude.com/blog/skills \
  skills \
  --source-date 2025-10-16
```

## 배치 흐름 (Perplexity Computer cron)

매시간 실행되는 에이전트는 다음을 수행합니다.

1. `scripts/list_pending.py --limit 2` 로 처리 대기 중인 URL 1~2개를 가져옵니다.
2. 각 URL을 fetch하여 본문을 분석합니다.
3. `skills/<slug>/SKILL.md` 와 `skills/<slug>/source.json` 을 생성합니다.
4. `scripts/mark_processed.py` 로 상태 파일을 갱신합니다.
5. `git add . && git commit -m "skill: <slug>" && git push` 로 반영합니다.

한 번에 1~2개만 처리하여 과부하를 방지합니다. 블로그 업데이트는 느리므로 시간이 지나면 자연스럽게 전체가 정리됩니다.
