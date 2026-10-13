#!/usr/bin/env bash
# Reproduce the run: ingest research-worker JSON (raw/*/*.json) -> progress.sqlite3,
# crawl own websites (needs egress to business sites; resumable), then build CSVs + REPORT.md.
# Every stage is idempotent; re-running never duplicates rows.
#   ./run.sh                       # normal
#   ./run.sh --retry-unreachable   # re-crawl sites that were blocked last time
set -euo pipefail
cd "$(dirname "$0")"
python3 scripts/ingest.py
python3 scripts/crawl.py "$@" || echo "crawl stage failed (network?) — building from what is in the DB"
python3 scripts/build.py
