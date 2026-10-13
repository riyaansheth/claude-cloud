"""Push run outputs to a separate results branch, without touching the working
tree or the code branch.

Builds a commit with git plumbing (hash-object -> mktree -> commit-tree) whose
tree holds only leadrun_jewelry/{jewelry_all.csv, jewelry_qualified.csv,
REPORT.md}, parented on the remote results branch tip, and pushes it to
refs/heads/<RESULTS_BRANCH>. No-op when the outputs have not changed.
"""
import subprocess
import time

from . import config

RESULTS_BRANCH = "claude/jewelry-leads-results"
FILES = [config.ALL_CSV, config.QUALIFIED_CSV, config.REPORT_MD,
         config.QUALIFIED_XLSX]
TRAILER = ("Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n"
           "Claude-Session: https://claude.ai/code/session_011EVb4KaNaj6AQ86xbNTbBs")


def _git(*args, input=None):
    r = subprocess.run(["git", *args], cwd=config.ROOT, input=input, text=True,
                       capture_output=True)
    if r.returncode:
        raise RuntimeError(f"git {' '.join(args)}: {r.stderr.strip()}")
    return r.stdout.strip()


def _retry(fn, tries=5):
    for i in range(tries):
        try:
            return fn()
        except RuntimeError:
            if i == tries - 1:
                raise
            time.sleep(2 ** (i + 1))   # 2, 4, 8, 16s


def push(summary="", log=print):
    files = [f for f in FILES if f.exists()]
    if not files:
        log("[autopush] no outputs yet")
        return None
    parent = None
    try:
        _retry(lambda: _git("fetch", "-q", "origin", f"+refs/heads/{RESULTS_BRANCH}:refs/remotes/origin/{RESULTS_BRANCH}"), tries=2)
        parent = _git("rev-parse", f"refs/remotes/origin/{RESULTS_BRANCH}")
    except RuntimeError:
        pass  # branch does not exist yet: first commit is a root commit
    entries = "".join(f"100644 blob {_git('hash-object', '-w', str(f))}\t{f.name}\n" for f in files)
    sub = _git("mktree", input=entries)
    tree = _git("mktree", input=f"040000 tree {sub}\t{config.ROOT.name}\n")
    if parent and _git("rev-parse", f"{parent}^{{tree}}") == tree:
        log("[autopush] outputs unchanged; nothing to push")
        return parent
    msg = f"Jewelry lead run results{': ' + summary if summary else ''}\n\n{TRAILER}\n"
    commit = _git("commit-tree", tree, *(["-p", parent] if parent else []), "-m", msg)
    _retry(lambda: _git("push", "-q", "origin", f"{commit}:refs/heads/{RESULTS_BRANCH}"))
    log(f"[autopush] pushed {commit[:9]} to {RESULTS_BRANCH}")
    return commit
