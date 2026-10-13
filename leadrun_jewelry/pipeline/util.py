"""Normalisers and extractors shared by every stage."""
import hashlib
import html
import json
import re
from datetime import datetime
from urllib.parse import urljoin, urlparse, unquote
from zoneinfo import ZoneInfo

from . import config

# ------------------------------------------------------------------ time
def now_iso():
    return datetime.now(ZoneInfo(config.FOUND_AT_TZ)).isoformat(timespec="seconds")


def sha(s):
    return hashlib.sha1(s.encode("utf-8")).hexdigest()[:16]


# ------------------------------------------------------------------ phones
TOLL_FREE = {"800", "833", "844", "855", "866", "877", "888"}
_PHONE_RX = re.compile(r"(?:\+?1[\s.\-]?)?\(?([2-9]\d{2})\)?[\s.\-]?([2-9]\d{2})[\s.\-]?(\d{4})\b")


def phone_digits(s):
    """10-digit US number or '' — accepts '+1 (212) 555-0100', 'tel:2125550100'."""
    if not s:
        return ""
    raw = unquote(str(s)).strip()
    if raw.lower().startswith("tel:"):
        raw = raw[4:].strip()
    # An explicit non-US country code (+30 210…) is never a US number.
    if raw.startswith("+") and not raw.lstrip("+ ").startswith("1"):
        return ""
    d = re.sub(r"\D", "", raw)
    if len(d) == 11 and d.startswith("1"):
        d = d[1:]
    if len(d) != 10 or d[0] in "01" or d[3] in "01":
        return ""
    return d


def is_toll_free(s):
    d = phone_digits(s)
    return bool(d) and d[:3] in TOLL_FREE


def fmt_phone(d):
    d = phone_digits(d)
    return f"({d[:3]}) {d[3:6]}-{d[6:]}" if d else ""


# ------------------------------------------------------------------ urls
def domain_of(url):
    if not url:
        return ""
    if "://" not in url:
        url = "https://" + url
    host = (urlparse(url).hostname or "").lower()
    return host[4:] if host.startswith("www.") else host


def is_shared_host(dom):
    return any(dom == h or dom.endswith("." + h) for h in config.SHARED_HOSTS)


def root_url(url):
    dom = domain_of(url)
    if not dom:
        return ""
    host = (urlparse(url if "://" in url else "https://" + url).hostname or "").lower()
    if is_shared_host(dom):
        # Keep the path for hosted pages (wixsite.com/<site>), otherwise the
        # root would point at the platform, not the business.
        p = urlparse(url if "://" in url else "https://" + url)
        path = p.path.rstrip("/")
        return f"https://{host}{path}"
    return f"https://{host}"


# ------------------------------------------------------------------ emails
EMAIL_RX = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,24}")
ROLE_LOCALS = {"info", "sales", "hello", "contact", "office", "admin", "support",
               "service", "inquiries", "inquiry", "enquiries", "team", "store",
               "shop", "orders", "help", "mail", "customerservice", "appointments",
               "jewelry", "jewelers", "repairs", "custom", "design", "studio",
               "careers", "jobs", "pr", "press", "media", "concierge", "clientservices",
               "clientservice", "client", "clients", "customercare", "care", "marketing",
               "events", "reservations", "billing", "accounts", "returns", "privacy",
               "wholesale", "webmaster", "hr", "bookings", "showroom", "boutique"}
LOW_VALUE_LOCALS = {"careers", "jobs", "pr", "press", "media", "privacy", "billing",
                    "accounts", "returns", "webmaster", "hr", "wholesale"}
PLACEHOLDER_LOCALS = {"youremail", "your.email", "yourname", "your", "email",
                      "name", "user", "username", "test", "example", "someone",
                      "john", "johndoe", "john.doe", "jane", "janedoe", "first.last",
                      "firstname", "firstname.lastname", "you", "me", "noreply",
                      "no-reply", "donotreply", "xxx", "abc"}
PLACEHOLDER_DOMAINS = {"example.com", "example.org", "domain.com", "email.com",
                       "yourdomain.com", "yoursite.com", "website.com", "company.com",
                       "mysite.com", "test.com", "sentry.io", "sentry.wixpress.com",
                       "wixpress.com", "sentry-next.wixpress.com", "address.com",
                       "yourcompany.com", "mail.com", "godaddy.com", "squarespace.com",
                       "shopify.com", "wix.com", "schema.org", "w3.org"}
CONSUMER_DOMAINS = {"gmail.com", "yahoo.com", "hotmail.com", "aol.com", "outlook.com",
                    "icloud.com", "me.com", "mac.com", "msn.com", "live.com",
                    "comcast.net", "att.net", "sbcglobal.net", "verizon.net",
                    "bellsouth.net", "cox.net", "charter.net", "earthlink.net",
                    "optonline.net", "protonmail.com", "ymail.com", "rocketmail.com"}
_ASSET_EXT = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".css", ".js")


def clean_email(e):
    e = unquote(e or "").strip().strip(".,;:<>()[]\"'").lower()
    e = e.split("?")[0]
    if e.startswith("mailto:"):
        e = e[7:]
    return e


def email_status(e):
    """'ok' | 'placeholder' | 'invalid'."""
    e = clean_email(e)
    if not EMAIL_RX.fullmatch(e) or e.endswith(_ASSET_EXT) or "@2x" in e:
        return "invalid"
    local, dom = e.rsplit("@", 1)
    if (local in PLACEHOLDER_LOCALS or dom in PLACEHOLDER_DOMAINS
            or local.startswith("your") or "example" in dom
            or re.fullmatch(r"[0-9a-f]{20,}", local)):
        return "placeholder"
    return "ok"


def is_role_email(e):
    local = clean_email(e).split("@")[0]
    return local in ROLE_LOCALS or local.split(".")[0] in ROLE_LOCALS


def name_tokens(s):
    s = re.sub(r"[^a-z0-9 ]", " ", (s or "").lower())
    stop = {"the", "and", "of", "co", "inc", "llc", "ltd", "jewelers", "jeweler",
            "jewelry", "jewellery", "jewellers", "fine", "company", "store",
            "shop", "designs", "design", "studio", "gallery", "custom", "diamonds",
            "diamond", "gold", "gems", "estate", "watches", "watch", "repair", "by"}
    return [t for t in s.split() if len(t) > 2 and t not in stop]


def email_relates(e, site_domain, business_name):
    """Accept own-domain, consumer-domain (found on the business's own pages) or
    a domain that shares a distinctive token with the business name."""
    dom = clean_email(e).rsplit("@", 1)[-1]
    if site_domain and (dom == site_domain or dom.endswith("." + site_domain)
                        or site_domain.endswith("." + dom)):
        return True
    if dom in CONSUMER_DOMAINS:
        return True
    label = dom.split(".")[0]
    return any(t in label for t in name_tokens(business_name))


# ------------------------------------------------------------------ html
def decode_cfemail(hexstr):
    """Cloudflare email obfuscation: data-cfemail="..."."""
    try:
        key = int(hexstr[:2], 16)
        return "".join(chr(int(hexstr[i:i + 2], 16) ^ key) for i in range(2, len(hexstr), 2))
    except ValueError:
        return ""


def visible_text(soup):
    for t in soup(["script", "style", "noscript", "svg"]):
        t.decompose()
    return re.sub(r"\s+", " ", soup.get_text(" ")).strip()


def jsonld_blocks(soup):
    out = []
    for s in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(s.string or s.get_text() or "")
        except (ValueError, TypeError):
            continue
        stack = [data]
        while stack:
            d = stack.pop()
            if isinstance(d, list):
                stack.extend(d)
            elif isinstance(d, dict):
                out.append(d)
                if "@graph" in d:
                    stack.append(d["@graph"])
    return out


def abs_url(base, href):
    return urljoin(base, html.unescape(href or ""))


# ------------------------------------------------------------------ socials
SOCIAL_RX = re.compile(
    r"https?://(?:www\.|m\.|mbasic\.)?(facebook\.com|instagram\.com|twitter\.com|x\.com)"
    r"/(?!sharer|share|intent|dialog|plugins|tr\b|tr\?|hashtag|p/|reel/|explore|"
    r"policies|privacy|help|login|home\.php|watch|events|groups/|pages/create)"
    r"[A-Za-z0-9_.\-/%?=]+", re.I)


def norm_social(u):
    u = u.split("#")[0].rstrip("/")
    u = re.sub(r"https?://(?:www\.|m\.|mbasic\.)", "https://", u, flags=re.I)
    u = re.sub(r"^http://", "https://", u, flags=re.I)
    u = re.sub(r"\?(?!id=).*$", "", u)
    return u


# ------------------------------------------------------------------ names
_NAME = r"([A-Z][a-z]+(?:[-'][A-Z][a-z]+)?(?:\s+[A-Z]\.)?\s+(?:Mc|Mac|O')?[A-Z][a-z]+(?:-[A-Z][a-z]+)?)"
ROLE_WORDS = {
    "owner": "Owner", "co-owner": "Owner", "proprietor": "Owner",
    "president": "President", "ceo": "President", "founder": "Founder",
    "co-founder": "Founder", "founded by": "Founder", "manager": "Manager",
    "general manager": "Manager", "store manager": "Manager", "partner": "Partner",
    "principal": "Owner", "member": "Member", "managing member": "Member",
    "master jeweler": "Owner", "bench jeweler": "Featured On About Page",
    "goldsmith": "Featured On About Page", "gemologist": "Featured On About Page",
    "graduate gemologist": "Featured On About Page", "designer": "Featured On About Page",
}
NOT_NAMES = set("""jewelry jewelers jeweler fine custom design designs diamond diamonds gold
silver platinum engagement wedding rings ring estate antique street avenue suite road
boulevard drive our the about contact team story meet store shop gallery studio
graduate gemologist gemological institute america american society master bench
jeweler owner president founder manager monday tuesday wednesday thursday friday
saturday sunday january february march april may june july august september october
november december new york los angeles chicago houston dallas miami atlanta
philadelphia san francisco boston seattle las vegas phoenix diego denver washington
detroit minneapolis charlotte nashville scottsdale naples greenwich palm beach beverly
hills privacy policy terms service read more learn view all shop now book appointment
family owned since years google maps facebook instagram customer reviews free
shipping gift card watch watches repair repairs bridal collection collections
home page click here call us email us period signed vintage art deco nouveau
victorian edwardian georgian retro mid century rare important unique handmade sterling
yellow white rose karat carat sapphire ruby emerald pearl pearls opal topaz piece pieces
heritage legacy quality service services welcome visit located location hours open
contact appointment book schedule shop online""".split())

STREET_WORDS = {"ave", "avenue", "st", "street", "blvd", "boulevard", "rd", "road", "dr",
                "drive", "ln", "lane", "way", "pl", "place", "plaza", "sq", "square", "park",
                "center", "centre", "mall", "ct", "court", "pkwy", "parkway", "hwy", "highway",
                "village", "heights", "hills", "beach", "city", "county", "district"}
_ROLE_ALT = "|".join(sorted((re.escape(k) for k in ROLE_WORDS), key=len, reverse=True))
_NAME_THEN_ROLE = re.compile(_NAME + r"\s*(?:,|-|–|—|\||is the|is our|,? our)?\s*(?i:the\s+)?((?i:" + _ROLE_ALT + r"))\b")
_ROLE_THEN_NAME = re.compile(r"\b((?i:" + _ROLE_ALT + r"))\s*(?::|,|-|–|—|\bis\b|\bby\b)?\s*" + _NAME)
_MEET = re.compile(r"\b(?i:meet)\s+(?:(?i:the\s+\w+\s*[:\-–]?\s*))?" + _NAME)


def plausible_name(n, business_name="", need_given=False):
    """need_given=True (regex finds on free text) requires the first word to be a
    known given name; structured sources (BBB principal block) don't."""
    parts = n.replace(".", " ").split()
    if need_given:
        from .firstnames import FIRST_NAMES
        if not parts or parts[0].lower() not in FIRST_NAMES:
            return False
    if len(parts) < 2 or len(parts) > 4:
        return False
    if parts[-1].lower() in STREET_WORDS:      # "Madison Ave", "Lincoln Park"
        return False
    if any(p.lower().strip("'") in NOT_NAMES for p in parts):
        return False
    btoks = set(name_tokens(business_name))
    # A "name" that is the business name (e.g. "Sterling Silver") is not a human.
    if btoks and all(p.lower() in btoks for p in parts):
        return False
    return all(p[0].isupper() for p in parts)


def extract_people(text, business_name=""):
    """Return [(name, role, snippet)] for names adjacent to owner-ish role words.
    Regex only; ambiguous pages are handed to subagents (agent_queue)."""
    found = []
    seen = set()

    def add(name, role_raw, m):
        name = re.sub(r"\s+", " ", name).strip()
        # _NAME is case-sensitive in spirit; the IGNORECASE role pattern can
        # let lowercase words in, so re-check capitalisation here.
        if not plausible_name(name, business_name, need_given=True) or name.lower() in seen:
            return
        seen.add(name.lower())
        role = ROLE_WORDS.get(role_raw.lower().strip(), "Featured On About Page")
        found.append((name, role, text[max(0, m.start() - 60): m.end() + 60]))

    for m in _ROLE_THEN_NAME.finditer(text):
        add(m.group(2), m.group(1), m)
    for m in _NAME_THEN_ROLE.finditer(text):
        add(m.group(1), m.group(2), m)
    for m in _MEET.finditer(text):
        add(m.group(1), "featured", m)
    order = ["Owner", "President", "Founder", "Partner", "Member", "Manager",
             "Featured On About Page"]
    found.sort(key=lambda x: order.index(x[1]))
    return found


# ------------------------------------------------------------------ zip -> state
_ZIP3 = [(5, 5, "NY"), (6, 9, "PR"), (10, 27, "MA"), (28, 29, "RI"), (30, 38, "NH"),
         (39, 49, "ME"), (50, 59, "VT"), (60, 69, "CT"), (70, 89, "NJ"), (100, 149, "NY"),
         (150, 196, "PA"), (197, 199, "DE"), (200, 200, "DC"), (201, 201, "VA"),
         (202, 205, "DC"), (206, 219, "MD"), (220, 246, "VA"), (247, 268, "WV"),
         (270, 289, "NC"), (290, 299, "SC"), (300, 319, "GA"), (320, 349, "FL"),
         (350, 369, "AL"), (370, 385, "TN"), (386, 397, "MS"), (398, 399, "GA"),
         (400, 427, "KY"), (430, 459, "OH"), (460, 479, "IN"), (480, 499, "MI"),
         (500, 528, "IA"), (530, 549, "WI"), (550, 567, "MN"), (570, 577, "SD"),
         (580, 588, "ND"), (590, 599, "MT"), (600, 629, "IL"), (630, 658, "MO"),
         (660, 679, "KS"), (680, 693, "NE"), (700, 714, "LA"), (716, 729, "AR"),
         (730, 749, "OK"), (750, 799, "TX"), (800, 816, "CO"), (820, 831, "WY"),
         (832, 838, "ID"), (840, 847, "UT"), (850, 865, "AZ"), (870, 884, "NM"),
         (885, 885, "TX"), (889, 898, "NV"), (900, 961, "CA"), (967, 968, "HI"),
         (970, 979, "OR"), (980, 994, "WA"), (995, 999, "AK")]
STATES = {"AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID",
          "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO",
          "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA",
          "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "PR"}


def state_from_zip(z):
    m = re.match(r"\s*(\d{5})", z or "")
    if not m:
        return ""
    p = int(m.group(1)[:3])
    for lo, hi, st in _ZIP3:
        if lo <= p <= hi:
            return st
    return ""


_ADDR_TAIL = re.compile(r",\s*([A-Za-z .'\-]+?),?\s+([A-Z]{2})\s+(\d{5})(?:-\d{4})?\s*$")


def parse_city_state(address):
    """'123 Main St, Evanston, IL 60201' -> ('Evanston', 'IL')."""
    m = _ADDR_TAIL.search((address or "").strip())
    if m and m.group(2) in STATES:
        return m.group(1).strip(), m.group(2)
    return "", ""
