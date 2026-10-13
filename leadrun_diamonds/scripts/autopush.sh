#!/usr/bin/env bash
# Commit the current lead outputs to a separate branch and push it, without touching the
# working tree or the checked-out branch (uses a private index + commit-tree).
# Skips the commit when outputs are unchanged. Retries the push on network errors.
set -euo pipefail
BR="${AUTOPUSH_BRANCH:-leadrun/diamonds-output}"
cd "$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
FILES=(leadrun_diamonds/diamond_leads.xlsx leadrun_diamonds/diamonds_qualified.csv
       leadrun_diamonds/diamonds_all.csv leadrun_diamonds/dropped_out_of_scope.csv
       leadrun_diamonds/REPORT.md)
export GIT_INDEX_FILE="$(git rev-parse --git-dir)/autopush.index"
rm -f "$GIT_INDEX_FILE"
git fetch -q origin "$BR" 2>/dev/null || true
PARENT="$(git rev-parse -q --verify "refs/remotes/origin/$BR" || git rev-parse -q --verify "refs/heads/$BR" || true)"
[ -n "$PARENT" ] && git read-tree "$PARENT"
git add -f -- "${FILES[@]}"
TREE="$(git write-tree)"
if [ -n "$PARENT" ] && [ "$TREE" = "$(git rev-parse "$PARENT^{tree}")" ]; then
  echo "autopush: outputs unchanged, nothing to push"; exit 0
fi
MSG="Diamond leads output $(date -u +%FT%TZ): $(python3 - <<'PY'
import csv
a=list(csv.DictReader(open('leadrun_diamonds/diamonds_all.csv')))
q=list(csv.DictReader(open('leadrun_diamonds/diamonds_qualified.csv')))
print(f"{len(a)} researched, {len(q)} qualified")
PY
)"
COMMIT="$(git commit-tree "$TREE" ${PARENT:+-p "$PARENT"} -m "$MSG")"
git update-ref "refs/heads/$BR" "$COMMIT"
for d in 0 2 4 8 16; do
  sleep "$d"; git push -q origin "refs/heads/$BR:refs/heads/$BR" && { echo "autopush: $MSG -> $BR"; exit 0; }
done
echo "autopush: push failed after retries" >&2; exit 1
