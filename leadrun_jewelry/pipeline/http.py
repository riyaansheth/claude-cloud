"""Polite HTTP: shared session, per-host throttle, retries, disk cache.

Network failures are recorded, not hidden: a 403 from the sandbox egress proxy
(CONNECT refused) is reported as kind='egress-blocked' so REPORT.md can say
exactly which host stopped the run.
"""
import json
import os
import random
import threading
import time
from urllib.parse import urlparse

import requests

from . import config
from .util import sha

_lock = threading.Lock()
_last_hit = {}
_session_local = threading.local()


class Blocked(Exception):
    """The host refused us (egress policy, 403/429 after retries, captcha)."""


def session():
    s = getattr(_session_local, "s", None)
    if s is None:
        s = requests.Session()
        s.headers.update({"User-Agent": config.UA,
                          "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
                          "Accept-Language": "en-US,en;q=0.9"})
        ca = os.environ.get("REQUESTS_CA_BUNDLE") or os.environ.get("SSL_CERT_FILE")
        if ca:
            s.verify = ca
        _session_local.s = s
    return s


def _throttle(host, min_gap):
    with _lock:
        wait = _last_hit.get(host, 0) + min_gap - time.time()
        _last_hit[host] = max(time.time(), _last_hit.get(host, 0) + min_gap)
    if wait > 0:
        time.sleep(wait + random.uniform(0, min_gap * 0.3))


def cache_path(url, data=None):
    config.CACHE_DIR.mkdir(parents=True, exist_ok=True)
    if isinstance(data, dict):
        data = json.dumps(data, sort_keys=True)
    return config.CACHE_DIR / f"{sha(url + (data or ''))}.bin"


def fetch(url, *, data=None, min_gap=1.0, timeout=25, retries=2, use_cache=True,
          max_bytes=3_000_000):
    """Return (status, final_url, text). Raises Blocked on egress/policy refusal."""
    cp = cache_path(url, data)
    if use_cache and cp.exists():
        raw = cp.read_bytes()
        status, final, body = raw.split(b"\n", 2)
        return int(status), final.decode(), body.decode("utf-8", "replace")
    host = urlparse(url).hostname or ""
    last_exc = None
    for attempt in range(retries + 1):
        _throttle(host, min_gap)
        try:
            if data is not None:
                r = session().post(url, data=data, timeout=timeout)
            else:
                r = session().get(url, timeout=timeout, allow_redirects=True, stream=True)
            body = r.raw.read(max_bytes, decode_content=True) if data is None else r.content
            text = body.decode(r.encoding or "utf-8", "replace")
            if r.status_code in (429, 503) and attempt < retries:
                time.sleep(5 * (attempt + 1))
                continue
            if r.status_code < 500 or attempt == retries:
                if r.status_code == 200 and use_cache:
                    cp.write_bytes(f"{r.status_code}\n{r.url}\n".encode() + text.encode())
                return r.status_code, r.url, text
        except requests.exceptions.ProxyError as e:
            # Only a 403 on CONNECT is an egress-policy refusal. A 502 or a dropped
            # tunnel means the destination itself is down: an ordinary failure.
            if "403" in str(e):
                raise Blocked(f"egress-blocked {host}: {e}") from e
            last_exc = e
            break
        except requests.RequestException as e:
            last_exc = e
            time.sleep(2 ** attempt)
    raise requests.RequestException(f"{url}: {last_exc}")
