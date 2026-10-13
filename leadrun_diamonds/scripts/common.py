"""Shared constants and normalisers for the diamond-trade lead run."""
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

RUN_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = RUN_DIR / "raw"
DB_PATH = RUN_DIR / "progress.sqlite3"

SEGMENT = "Diamond wholesaler / trade"

# 26 core columns (production order) + 4 working columns appended after.
CORE_COLUMNS = [
    "Business", "Segment", "Category (as listed)", "Phone", "Email", "LinkedIn Profile",
    "Contact Person", "Role", "Website", "Address", "Real City", "Real State", "Market",
    "Lead Origin", "Rating", "Reviews", "Source", "Signals", "Match Type", "Email Source",
    "LinkedIn Source", "Found At", "Also Listed As", "Other Markets", "Merged Listings", "Flags",
]
WORK_COLUMNS = ["Mobile Candidates", "Socials", "Building / Suite", "Trade Memberships"]
COLUMNS = CORE_COLUMNS + WORK_COLUMNS
assert len(CORE_COLUMNS) == 26 and len(COLUMNS) == 30

LEAD_ORIGINS = {"LinkedIn", "Trade Directory", "Building Directory", "Google Maps", "YellowPages",
                "Bing Maps", "BBB", "OpenStreetMap", "Web Search", "Trade Show"}

# Hosts that many unrelated businesses share; never a dedupe key.
PLATFORM_HOSTS = ("linktr.ee", "wixsite.com", "square.site", "business.site", "facebook.com",
                  "instagram.com", "godaddysites.com", "weebly.com", "squarespace.com",
                  "shopify.com", "myshopify.com", "sites.google.com", "yelp.com", "x.com",
                  "twitter.com", "linkedin.com")

# ---------------------------------------------------------------- kill-list
# (reason, regex) — matched against business name and source category.
KILL_LIST = [
    ("pawn", r"\bpawn|pawnbroker|ezpawn|cash america|loans? on jewelry|collateral loan"),
    ("cash-for-gold", r"cash for gold|we buy gold|gold exchange|scrap gold|\bbullion\b|precious metals? buyer|\brefinery\b|\brefiners?\b|gold buyers?\b"),
    ("coin", r"\bcoins?\b|numismatic|currency exchange|stamp and coin"),
    ("beads-craft", r"\bbeads?\b|bead (store|shop)|\bfindings\b|jewelry suppl(y|ies)|\bcraft(s)?\b|\bhobby\b|wire wrapping|charm bar"),
    ("costume-fashion", r"costume jewelry|fashion jewelry|claire'?s|\bicing\b|accessories store|\bhandbags?\b"),
    ("piercing", r"piercing|tattoo|body jewelry|permanent jewelry"),
    ("kiosk", r"\bkiosk\b|watch battery|\bbattery\b|mall cart|\bcart\b|phone case"),
    ("simulant", r"moissanite|cubic zirconia|\bcz\b|lab simulant|diamond alternative|simulated diamond"),
    ("chain", r"\bkay jewelers\b|^kay$|\bjared (the galleria|jewel)|^jared$|\bzales\b|\bpandora\b|\btiffany ?(&|and) ?co|^tiffany$|blue nile|james allen|brilliant earth|\bsignet\b|shane co\b|helzberg|ben bridge|daniel'?s jewelers|rogers (&|and) hollands|swarovski|macy'?s|jcpenney|j\.c\. penney|nordstrom|\britani\b|with clarity|clean origin|\bvrai\b"),
    ("thrift", r"\bthrift\b|consignment|resale shop"),
]
_KILL = [(r, re.compile(p, re.I)) for r, p in KILL_LIST]

# Agent drop reasons that are judgement calls (not regex-detectable) but still out of scope.
JUDGEMENT_DROPS = {"retail-only", "gemstone-only", "appraiser-lab", "other", "pawn", "cash-for-gold",
                   "coin", "beads-craft", "costume-fashion", "piercing", "kiosk", "simulant",
                   "chain", "thrift", "unverified"}


def kill_reason(name: str, category: str = "") -> str:
    """Return kill-list reason for a business name / source category, or ''."""
    for text in (name or "", category or ""):
        for reason, rx in _KILL:
            if rx.search(text):
                return reason
    return ""


# ---------------------------------------------------------------- normalisers
LEGAL = r"\b(inc|incorporated|llc|l\.l\.c|ltd|limited|corp|corporation|co|company|the|usa|us|ny|nyc)\b"


def norm_name(name: str) -> str:
    s = (name or "").lower().replace("&", " and ")
    s = re.sub(r"[^\w\s]", " ", s)
    s = re.sub(LEGAL, " ", s)
    return re.sub(r"\s+", " ", s).strip()


def phone_digits(p: str) -> str:
    d = re.sub(r"\D", "", p or "")
    if len(d) == 11 and d.startswith("1"):
        d = d[1:]
    return d if len(d) == 10 and d[0] not in "01" else ""


TOLL_FREE = ("800", "833", "844", "855", "866", "877", "888")


def is_toll_free(digits: str) -> bool:
    return digits[:3] in TOLL_FREE


def host_of(url: str) -> str:
    if not url:
        return ""
    if "://" not in url:
        url = "https://" + url
    h = (urlparse(url).hostname or "").lower()
    return h[4:] if h.startswith("www.") else h


def site_domain(url: str) -> str:
    """Root domain usable as a dedupe key; '' for shared platform hosts."""
    h = host_of(url)
    if not h or any(h == p or h.endswith("." + p) for p in PLATFORM_HOSTS):
        return ""
    parts = h.split(".")
    return ".".join(parts[-2:]) if len(parts) >= 2 else h


def root_url(url: str) -> str:
    h = host_of(url)
    return f"https://{'www.' if url and '//www.' in url else ''}{h}" if h else ""


EMAIL_RX = re.compile(r"^[a-z0-9._%+'-]+@[a-z0-9.-]+\.[a-z]{2,}$", re.I)
PLACEHOLDER_LOCAL = {"youremail", "your", "example", "name", "email", "user", "username", "test",
                     "someone", "john", "johndoe", "jane", "yourname", "first", "firstname"}
PLACEHOLDER_DOMAIN = ("example.com", "domain.com", "email.com", "yourdomain.com", "yoursite.com",
                      "website.com", "sentry.io", "wixpress.com", "sentry-next.wixpress.com")
ROLE_LOCAL = {"info", "sales", "trade", "contact", "office", "hello", "admin", "support", "orders",
              "inquiries", "inquiry", "service", "team", "mail", "enquiries", "customerservice",
              "wholesale", "diamonds", "help", "store", "shop", "general", "accounts", "billing"}


def classify_email(e: str):
    """-> (clean_email, status) where status in ok|placeholder|invalid|''."""
    e = (e or "").strip().lower().removeprefix("mailto:").split("?")[0]
    if not e:
        return "", ""
    if not EMAIL_RX.match(e) or e.endswith((".png", ".jpg", ".gif", ".webp")):
        return e, "invalid"
    local, dom = e.split("@", 1)
    if local in PLACEHOLDER_LOCAL or dom in PLACEHOLDER_DOMAIN or dom.endswith("wixpress.com"):
        return e, "placeholder"
    return e, "ok"


def is_role_email(e: str) -> bool:
    return e.split("@", 1)[0] in ROLE_LOCAL if "@" in e else False


LI_RX = re.compile(r"^https?://([a-z]{2,3}\.)?linkedin\.com/in/([^/?#\s]+)/?", re.I)


def clean_linkedin(url: str) -> str:
    m = LI_RX.match((url or "").strip())
    return f"https://www.linkedin.com/in/{m.group(2)}" if m else ""


def linkedin_is_personal(url: str, business: str, person: str) -> bool:
    """Personal = /in/ URL, named human with first+last, slug does not restate the business."""
    if not url or len((person or "").split()) < 2:
        return False
    slug = re.sub(r"[^a-z]", "", url.rsplit("/in/", 1)[1].lower())
    biz = re.sub(r"[^a-z]", "", norm_name(business))
    biz_core = re.sub(r"(diamonds?|jewel(ry|ers?)|gems?|international|group|trading)", "", biz)
    if not slug:
        return False
    if len(biz) >= 5 and biz in slug:          # slug restates the whole business name
        return False
    if len(slug) >= 5 and slug in biz:         # slug is just a piece of the business name
        return False
    toks = [re.sub(r"[^a-z]", "", t.lower()) for t in person.split()]
    names_in_slug = any(len(t) >= 3 and t in slug for t in (toks[0], toks[-1]))
    if not names_in_slug and len(biz_core) >= 5 and biz_core in slug:
        return False
    return True


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
