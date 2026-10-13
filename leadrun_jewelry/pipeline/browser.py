"""Headless Chromium with a real desktop UA (YellowPages / BBB 403 plain curl).

One Browser per worker process. `get_html()` caches page HTML on disk so a
re-run re-parses instead of re-fetching.
"""
import os
import random
import time

from . import config
from .http import cache_path, Blocked

_BLOCK_MARKERS = ("captcha", "unusual traffic", "are you a robot", "access denied",
                  "/sorry/index", "px-captcha", "cf-chl", "request blocked")


class Browser:
    def __init__(self, headless=True):
        from playwright.sync_api import sync_playwright
        self._pw = sync_playwright().start()
        kw = {"headless": headless, "args": ["--disable-blink-features=AutomationControlled"]}
        if os.path.exists(config.CHROMIUM_PATH):
            kw["executable_path"] = config.CHROMIUM_PATH
        proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
        if proxy:
            kw["proxy"] = {"server": proxy}
        self.browser = self._pw.chromium.launch(**kw)
        self.ctx = self.browser.new_context(user_agent=config.UA, locale="en-US",
                                            viewport={"width": 1366, "height": 900},
                                            ignore_https_errors=False)
        self.page = self.ctx.new_page()

    def get_html(self, url, *, wait_selector=None, min_gap=2.5, use_cache=True,
                 scroll=0, timeout=45000):
        cp = cache_path("browser:" + url)
        if use_cache and cp.exists():
            self.last_status = 200
            return cp.read_text("utf-8", "replace")
        time.sleep(min_gap + random.uniform(0, min_gap * 0.5))
        try:
            resp = self.page.goto(url, wait_until="domcontentloaded", timeout=timeout)
        except Exception as e:  # noqa: BLE001
            msg = str(e)
            if "ERR_TUNNEL_CONNECTION_FAILED" in msg or "ERR_PROXY" in msg:
                raise Blocked(f"egress-blocked {url}") from e
            raise
        if wait_selector:
            try:
                self.page.wait_for_selector(wait_selector, timeout=15000)
            except Exception:  # noqa: BLE001 — selector may legitimately be absent
                pass
        if scroll:
            # Google Maps results live in a scrollable feed panel; hover it first
            # so wheel events scroll the list rather than the map.
            feed = self.page.query_selector("div[role='feed']")
            if feed:
                box = feed.bounding_box()
                if box:
                    self.page.mouse.move(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
            last = -1
            for _ in range(scroll):
                self.page.mouse.wheel(0, 5000)
                time.sleep(1.5)
                n = self.page.locator("a.hfpxzc").count() if feed else 0
                if feed and n == last and "end of the list" in (self.page.content()[-200000:]).lower():
                    break
                last = n
        html = self.page.content()
        status = resp.status if resp else 0
        self.last_status = status
        # Real pages often mention "recaptcha" in scripts; only a challenge page
        # carries the marker in its title or is a tiny interstitial.
        title = (self.page.title() or "").lower()
        small = len(html) < 15000
        if status in (403, 429) or any(m in title or (small and m in html.lower())
                                       for m in _BLOCK_MARKERS):
            raise Blocked(f"http-{status} or challenge page at {url}")
        if status == 200 and use_cache:
            cp.write_text(html, "utf-8")
        return html

    def close(self):
        try:
            self.browser.close()
        finally:
            self._pw.stop()
