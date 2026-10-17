#!/usr/bin/env bash
# Pull every cloud worker's raw/ records into this checkout, then rebuild (ingest -> crawl -> build -> xlsx -> autopush).
# Workers push only leadrun_diamonds/raw/** to leadrun/worker-N / leadrun/verify-X, so checking those paths out
# of each branch is conflict-free. Safe to re-run.
set -uo pipefail
cd "$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
BRANCHES=(leadrun/worker-1 leadrun/worker-2 leadrun/worker-3 leadrun/worker-4 leadrun/worker-5 leadrun/worker-6
          leadrun/verify-a leadrun/verify-b leadrun/enrich-0 leadrun/enrich-1 leadrun/enrich-2 leadrun/enrich-3 leadrun/enrich-4 leadrun/r3-0 leadrun/r3-1 leadrun/r3-2 leadrun/r3-3 leadrun/r3-4 leadrun/r4-0 leadrun/r4-1 leadrun/r4-2 leadrun/r4-3 leadrun/r4-4
          leadrun/r5-0 leadrun/r5-1 leadrun/r5-2 leadrun/r5-3 leadrun/r5-4
          leadrun/people-0 leadrun/people-1 leadrun/people-2 leadrun/people-3
          leadrun/li-0 leadrun/li-1 leadrun/li-2 leadrun/li-3
          leadrun/r6-0 leadrun/r6-1 leadrun/r6-2 leadrun/r6-3 leadrun/r6-4 \
          leadrun/r7-0 leadrun/r7-1 leadrun/r7-2 leadrun/r7-3 leadrun/r7-4 \
          leadrun/r8-0 leadrun/r8-1 leadrun/r8-2 leadrun/r8-3 leadrun/r8-4)
for b in "${BRANCHES[@]}"; do
  if git fetch -q origin "$b" 2>/dev/null; then
    # only the files this worker itself changed since it forked — never its stale copies of others' files
    base=$(git merge-base HEAD "origin/$b")
    mapfile -t files < <(git diff --name-only --diff-filter=AM "$base" "origin/$b" -- leadrun_diamonds/raw leadrun_diamonds/raw_people)
    if [ ${#files[@]} -gt 0 ]; then
      printf '%s\0' "${files[@]}" | xargs -0 git checkout "origin/$b" --
    fi
    echo "merged $b (${#files[@]} files it changed)"
  else
    echo "no branch yet: $b"
  fi
done
./leadrun_diamonds/run.sh 2>&1 | grep -v '^unreachable\|^ok '
python3 leadrun_diamonds/scripts/build_people.py
