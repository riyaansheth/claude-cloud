#!/usr/bin/env bash
# Reproduce the run: ingest research-worker JSON (raw/*/*.json) -> progress.sqlite3,
# crawl own websites (needs egress to business sites; resumable), build CSVs + REPORT.md,
# compile diamond_leads.xlsx, then autopush the outputs to the leadrun/diamonds-output branch.
# Every stage is idempotent; re-running never duplicates rows.
#   ./run.sh                       # normal
#   ./run.sh --retry-unreachable   # re-crawl sites that were blocked last time
#   NO_AUTOPUSH=1 ./run.sh         # skip the push
set -euo pipefail
cd "$(dirname "$0")"
python3 scripts/ingest.py
python3 scripts/crawl.py "$@" || echo "crawl stage failed (network?) — building from what is in the DB"
python3 scripts/build.py
python3 scripts/export_xlsx.py
[ -n "${NO_AUTOPUSH:-}" ] || scripts/autopush.sh || echo "autopush failed — outputs are still on disk"
