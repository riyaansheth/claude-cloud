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
QUALIFIED_XLSX = ROOT / "jewelry_qualified.xlsx"
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
    # --- run 2: next 20 markets (positions 26-45) ---
    ("Austin", "TX", (30.1000, -97.9500, 30.5200, -97.5600)),
    ("San Antonio", "TX", (29.2500, -98.7500, 29.7000, -98.3000)),
    ("Fort Worth", "TX", (32.5500, -97.5500, 32.9900, -97.1000)),
    ("San Jose", "CA", (37.2000, -122.0500, 37.4700, -121.7500)),
    ("Sacramento", "CA", (38.4300, -121.6000, 38.7000, -121.3000)),
    ("Portland", "OR", (45.4300, -122.8400, 45.6500, -122.4700)),
    ("Salt Lake City", "UT", (40.6000, -112.0500, 40.8500, -111.7500)),
    ("Kansas City", "MO", (38.8500, -94.7500, 39.2500, -94.4000)),
    ("St. Louis", "MO", (38.5000, -90.5000, 38.8000, -90.1500)),
    ("Columbus", "OH", (39.8500, -83.2000, 40.1500, -82.8000)),
    ("Cleveland", "OH", (41.3800, -81.9000, 41.6000, -81.5000)),
    ("Cincinnati", "OH", (39.0500, -84.7000, 39.2500, -84.3500)),
    ("Indianapolis", "IN", (39.6300, -86.3300, 39.9300, -85.9500)),
    ("Pittsburgh", "PA", (40.3600, -80.1000, 40.5200, -79.8500)),
    ("Baltimore", "MD", (39.2000, -76.7200, 39.3800, -76.5200)),
    ("Orlando", "FL", (28.3500, -81.5500, 28.6500, -81.2000)),
    ("Tampa", "FL", (27.8500, -82.6500, 28.1500, -82.3500)),
    ("Fort Lauderdale", "FL", (26.0500, -80.2500, 26.2500, -80.0800)),
    ("Raleigh", "NC", (35.7000, -78.8000, 35.9500, -78.5000)),
    ("New Orleans", "LA", (29.8800, -90.2000, 30.0500, -89.9000)),
    # Run 3: 20 more US metros (bounding boxes = south, west, north, east).
    ("Jacksonville", "FL", (30.1000, -81.8500, 30.5000, -81.4000)),
    ("Memphis", "TN", (35.0000, -90.1000, 35.2800, -89.7500)),
    ("Louisville", "KY", (38.1000, -85.9000, 38.3200, -85.5500)),
    ("Milwaukee", "WI", (42.9200, -88.0700, 43.1900, -87.8600)),
    ("Albuquerque", "NM", (35.0000, -106.7500, 35.2200, -106.4700)),
    ("Tucson", "AZ", (32.1000, -111.0500, 32.3500, -110.7800)),
    ("Oklahoma City", "OK", (35.3500, -97.7000, 35.6500, -97.3500)),
    ("Tulsa", "OK", (36.0000, -96.0500, 36.2500, -95.8000)),
    ("Omaha", "NE", (41.1800, -96.2000, 41.3500, -95.9200)),
    ("Richmond", "VA", (37.4500, -77.6000, 37.6500, -77.3800)),
    ("Virginia Beach", "VA", (36.7000, -76.2000, 36.9500, -75.9500)),
    ("Birmingham", "AL", (33.4000, -86.9500, 33.6200, -86.6500)),
    ("Buffalo", "NY", (42.8200, -78.9200, 43.0000, -78.7500)),
    ("Hartford", "CT", (41.7000, -72.7800, 41.8200, -72.6200)),
    ("Providence", "RI", (41.7700, -71.4800, 41.8800, -71.3700)),
    ("El Paso", "TX", (31.7000, -106.5500, 31.9500, -106.2000)),
    ("Honolulu", "HI", (21.2500, -157.9500, 21.4000, -157.6500)),
    ("Boise", "ID", (43.5200, -116.3500, 43.7000, -116.1000)),
    ("Charleston", "SC", (32.7000, -80.1000, 32.9200, -79.8500)),
    ("Grand Rapids", "MI", (42.8500, -85.7800, 43.0500, -85.5500)),
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
    "yellowpages.com", "yp.com", "bbb.org", "yelp.com", "mapquest.com",
}
# Directory hosts are never a business's own website.
DIRECTORY_HOSTS = {"yellowpages.com", "yp.com", "bbb.org", "yelp.com", "google.com",
                   "mapquest.com", "superpages.com", "manta.com", "bing.com"}

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
