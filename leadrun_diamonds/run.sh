#!/usr/bin/env bash
# Reproduce the build: ingest research-worker JSON (raw/*/*.json) into progress.sqlite3, then build outputs.
# Both stages are idempotent; re-running never duplicates rows.
set -euo pipefail
cd "$(dirname "$0")"
python3 scripts/ingest.py
python3 scripts/build.py
