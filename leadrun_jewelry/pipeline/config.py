"""Static run configuration: markets, search terms, output schema.

Bounding boxes are search parameters only (south, west, north, east). They
decide where Overpass looks; the Real City / Real State columns always come from
the listing itself, never from the market.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # ./leadrun_jewelry
DB_PATH = ROOT / "progress.sqlite3"
CACHE_DIR = ROOT / "cache"                             # raw HTML/JSON cache
AGENT_DIR = ROOT / "agent_queue"                       # narrow-end subagent work
LOG_DIR = ROOT / "logs"
QUALIFIED_CSV = ROOT / "jewelry_qualified.csv"
ALL_CSV = ROOT / "jewelry_all.csv"
REPORT_MD = ROOT / "REPORT.md"

# Timestamps in Found At are written in this zone (matches the production sheet).
FOUND_AT_TZ = "Asia/Kolkata"

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")
CHROMIUM_PATH = "/opt/pw-browsers/chromium"

# (market label, state, bbox) — first 10 are worked first.
MARKETS = [
    ("New York", "NY", (40.4774, -74.2591, 40.9176, -73.7004)),
    ("Los Angeles", "CA", (33.7037, -118.6682, 34.3373, -118.1553)),
    ("Chicago", "IL", (41.6445, -87.9401, 42.0230, -87.5240)),
    ("Houston", "TX", (29.5370, -95.9097, 30.1105, -95.0146)),
    ("Dallas", "TX", (32.6175, -96.9989, 33.0237, -96.4637)),
    ("Miami", "FL", (25.6000, -80.4500, 25.9800, -80.1200)),
    ("Atlanta", "GA", (33.6478, -84.5519, 33.8868, -84.2896)),
    ("Philadelphia", "PA", (39.8670, -75.2803, 40.1379, -74.9558)),
    ("San Francisco", "CA", (37.7081, -122.5149, 37.8324, -122.3570)),
    ("Boston", "MA", (42.2279, -71.1912, 42.3969, -70.9860)),
    ("Seattle", "WA", (47.4955, -122.4359, 47.7341, -122.2359)),
    ("Las Vegas", "NV", (36.0000, -115.3500, 36.3300, -115.0500)),
    ("Phoenix", "AZ", (33.2900, -112.3200, 33.9200, -111.9200)),
    ("San Diego", "CA", (32.5300, -117.2800, 33.1100, -116.9000)),
    ("Denver", "CO", (39.6100, -105.1100, 39.9100, -104.6000)),
    ("Washington", "DC", (38.7900, -77.1200, 38.9960, -76.9100)),
    ("Detroit", "MI", (42.2550, -83.2900, 42.4500, -82.9100)),
    ("Minneapolis", "MN", (44.8900, -93.3300, 45.0500, -93.1900)),
    ("Charlotte", "NC", (35.0100, -81.0100, 35.4000, -80.6500)),
    ("Nashville", "TN", (35.9700, -87.0500, 36.4100, -86.5100)),
    ("Scottsdale", "AZ", (33.4500, -111.9600, 33.8900, -111.7500)),
    ("Naples", "FL", (26.0800, -81.8300, 26.3000, -81.7000)),
    ("Greenwich", "CT", (40.9800, -73.7300, 41.1100, -73.5700)),
    ("Palm Beach", "FL", (26.6300, -80.1200, 26.8000, -80.0300)),
    ("Beverly Hills", "CA", (34.0500, -118.4300, 34.1000, -118.3800)),
]


def market_label(city, st):
    return f"{city}, {st}"


GMAPS_QUERIES = ["jewelry store", "custom jewelry", "jewelry repair",
                 "estate jewelry", "goldsmith jeweler"]
# (bare "goldsmith <city>" makes Maps jump straight to a business named "The Goldsmith")
YP_TERMS = ["jewelers"]
BBB_CATEGORIES = ["Jewelry Stores", "Jewelry Repair"]

# Pages fetched per site during the crawl.
CRAWL_PATHS = ["/", "/about", "/about-us", "/contact", "/team", "/our-story",
               "/meet-the-jeweler", "/contact-us"]

# Domains never used as a dedupe key (many unrelated businesses share them).
SHARED_HOSTS = {
    "linktr.ee", "wixsite.com", "square.site", "business.site", "facebook.com",
    "instagram.com", "squarespace.com", "godaddysites.com", "weebly.com",
    "myshopify.com", "google.com", "sites.google.com", "yelp.com", "x.com",
    "twitter.com", "tiktok.com", "etsy.com", "wordpress.com", "blogspot.com",
}

# Exact output schema. 1-26 match usaENRICHEDleads.xlsx (minus the two legacy
# verification columns); 27-28 are working columns appended after.
COLUMNS = [
    "Business", "Segment", "Category (as listed)", "Phone", "Email",
    "LinkedIn Profile", "Contact Person", "Role", "Website", "Address",
    "Real City", "Real State", "Market", "Lead Origin", "Rating", "Reviews",
    "Source", "Signals", "Match Type", "Email Source", "LinkedIn Source",
    "Found At", "Also Listed As", "Other Markets", "Merged Listings", "Flags",
    "Mobile Candidates", "Socials",
]
assert len(COLUMNS) == 28

SEGMENTS = ("Jewelry retailer", "Custom / bespoke jeweler",
            "Estate & antique jewelry", "Jewelry repair / goldsmith")
ORIGINS = ("Google Maps", "YellowPages", "Bing Maps", "BBB", "OpenStreetMap",
           "LinkedIn", "Trade Directory", "Building Directory")
FLAG_VALUES = ("no-address", "toll-free", "chain", "placeholder-email",
               "shared-switchboard", "out-of-scope")
