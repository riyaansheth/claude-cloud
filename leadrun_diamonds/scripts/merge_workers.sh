#!/usr/bin/env bash
# Pull every cloud worker's raw/ records into this checkout, then rebuild (ingest -> crawl -> build -> xlsx -> autopush).
# Workers push only leadrun_diamonds/raw/** to leadrun/worker-N / leadrun/verify-X, so checking those paths out
# of each branch is conflict-free. Safe to re-run.
set -uo pipefail
cd "$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
BRANCHES=(leadrun/worker-1 leadrun/worker-2 leadrun/worker-3 leadrun/worker-4 leadrun/worker-5 leadrun/worker-6
          leadrun/verify-a leadrun/verify-b)
for b in "${BRANCHES[@]}"; do
  if git fetch -q origin "$b" 2>/dev/null; then
    n=$(git diff --name-only HEAD "origin/$b" -- leadrun_diamonds/raw | wc -l)
    git checkout "origin/$b" -- leadrun_diamonds/raw 2>/dev/null && echo "merged $b ($n raw files differ)"
  else
    echo "no branch yet: $b"
  fi
done
./leadrun_diamonds/run.sh 2>&1 | grep -v '^unreachable\|^ok '
