# Scripts

## list_pending.py
처리 대기 중인 블로그 글 URL을 **3-tier 우선순위**로 출력합니다.

출력 형식: `<url>\t<YYYY-MM-DD | unknown>\t<NEW|BACKLOG|UNKNOWN>`

| Tier | 설명 | 정렬 |
|---|---|---|
| NEW | `meta.last_run_at` 이후 게시된 글 | 최신 → 과거 |
| BACKLOG | `meta.last_run_at` 이전 게시된 글 | 오래된 → 최신 |
| UNKNOWN | 게시일을 못 찾은 글 (sitemap-only 포함) | 알파벳 |

```bash
python scripts/list_pending.py --limit 2
python scripts/list_pending.py --urls-only  # URL만
```

## mark_processed.py
SKILL.md 생성이 끝난 글을 `state/processed.json`의 `entries`에 기록합니다.

```bash
python scripts/mark_processed.py \
  https://claude.com/blog/skills \
  skills \
  --source-date 2025-10-16
```

## update_last_run.py
배치 실행이 끝날 때 한 번 호출하여 `state/processed.json`의 `meta.last_run_at`을 오늘 날짜(UTC)로 갱신합니다. 다음 실행에서 NEW/BACKLOG 경계를 정하는 기준이 됩니다.

```bash
python scripts/update_last_run.py
```

## 배치 흐름 (Perplexity Computer cron, 4시간 간격)

1. `python scripts/list_pending.py --limit 2` — 우선순위가 높은 글 1~2개 선정
2. 각 URL을 fetch → 본문 분석 → `skills/<slug>/SKILL.md`, `source.json` 생성
3. `python scripts/mark_processed.py <url> <slug> --source-date YYYY-MM-DD`
4. `skills/README.md` 인덱스 갱신 (최신이 위)
5. `python scripts/update_last_run.py` — 처리 건수와 무관하게 실행
6. `git add . && git commit -m "skill: <slug>" && git push`

NEW 글이 있으면 자동으로 먼저 잡히고, 없으면 BACKLOG의 가장 오래된 글부터 처리됩니다.
