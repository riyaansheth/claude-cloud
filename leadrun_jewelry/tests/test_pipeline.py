"""Offline tests. All fixtures are synthetic (*.test domains, 555-01xx numbers)
and live only here; they never reach the output CSVs, which the real run writes
to leadrun_jewelry/."""
import csv
import json
import shutil
from pathlib import Path

import pytest

from pipeline import build, config, db, scope
from pipeline import crawl_sites, discover_osm, discover_web, linkedin, util

WORK = Path(__file__).parent / "_work"


@pytest.fixture()
def tmpdb(monkeypatch):
    shutil.rmtree(WORK, ignore_errors=True)
    WORK.mkdir()
    monkeypatch.setattr(config, "DB_PATH", WORK / "p.sqlite3")
    monkeypatch.setattr(config, "ALL_CSV", WORK / "all.csv")
    monkeypatch.setattr(config, "QUALIFIED_CSV", WORK / "q.csv")
    monkeypatch.setattr(config, "REPORT_MD", WORK / "REPORT.md")
    monkeypatch.setattr(config, "QUALIFIED_XLSX", WORK / "q.xlsx")
    db._local.__dict__.clear()
    yield db.connect()
    db._local.__dict__.clear()
    shutil.rmtree(WORK, ignore_errors=True)


# ------------------------------------------------------------------ scope
@pytest.mark.parametrize("name,cat,reason", [
    ("EZPawn #12", "Pawn Shop", "pawn"),
    ("Midtown Pawn & Jewelry", "Jewelers", "pawn"),
    ("Cash For Gold USA", "Jewelers", "gold-buyer"),
    ("Liberty Coin & Jewelry", "Jewelers", "coin-currency"),
    ("Bead World", "Jewelry Supplies", "beads-craft"),
    ("Claire's", "Jewelry store", "costume-fashion"),
    ("Ink & Steel Piercing", "Jewelry store", "piercing-tattoo"),
    ("Watch Battery Kiosk", "Watch repair", "kiosk-battery"),
    ("Moissanite Masters", "Jewelry store", "simulants"),
    ("Kay Jewelers", "Jewelry store", "chain"),
    ("Zales", "Jewelry store", "chain"),
    ("Second Act Consignment", "Consignment shop", "thrift-consignment"),
    ("Metro Appraisal Services", "Jewelry appraiser", "appraiser-lab-insurer"),
    ("Empire Diamond Wholesalers", "Jewelers", "diamond-trade"),
    ("Loose Diamonds NYC", "Diamond dealer", "diamond-trade"),
])
def test_kill_list(name, cat, reason):
    assert scope.kill_reason(name, cat) == reason


@pytest.mark.parametrize("name,cat", [
    ("Smith Jewelers & Appraisals", "Jewelers"),
    ("Hartwell Goldsmith Studio", "Jewelry designer"),
    ("Old Town Estate Jewelry", "Jewelry store"),
    ("Cartwright Fine Jewelry", "Jewelry store"),   # 'cart' must not match inside a word
    ("Kaye & Sons Jewelers", "Jeweler"),             # 'kay' must not match 'kaye'
])
def test_in_scope(name, cat):
    assert scope.kill_reason(name, cat) is None


def test_diamond_district_trade_office():
    assert scope.kill_reason("Gem Trade Co", "Jewelers", "10 W 47th St Suite 1204, New York, NY 10036",
                             "New York, NY") == "diamond-trade"
    assert scope.kill_reason("Gem Trade Co", "Jewelers", "10 Main St, Chicago, IL 60601",
                             "Chicago, IL") is None


def test_osm_brand_is_chain():
    assert scope.kill_reason("Some Store", "shop=jewelry", osm_tags={"brand": "Kay"}) == "chain"


def test_site_kill_uses_only_headline_text():
    assert scope.site_kill_reason("Best Pawn Shop in Houston", "", "") == "pawn"
    assert scope.site_kill_reason("Smith Jewelers | Custom Engagement Rings", "We also buy gold", "") is None


@pytest.mark.parametrize("name,cat,tags,seg", [
    ("Old Town Estate Jewelry", "Jewelry store", None, "Estate & antique jewelry"),
    ("Main St Jewelry Repair", "Jewelry repair", None, "Jewelry repair / goldsmith"),
    ("Hartwell Goldsmith", "", {"craft": "jeweller"}, "Jewelry repair / goldsmith"),
    ("Lumen Custom Jewelry Design", "Jewelry designer", None, "Custom / bespoke jeweler"),
    ("Smith Jewelers", "Jewelry store", None, "Jewelry retailer"),
    ("Tick Tock Shop", "shop=watches", {"shop": "watches"}, None),
    ("Acme Hardware", "Hardware store", None, None),
])
def test_segments(name, cat, tags, seg):
    assert scope.classify_segment(name, cat, "", tags) == seg


# ------------------------------------------------------------------ util
def test_email_rules():
    assert util.email_status("youremail@gmail.com") == "placeholder"
    assert util.email_status("name@domain.com") == "placeholder"
    assert util.email_status("example@smith.test") == "placeholder"
    assert util.email_status("info@smithjewelers.test") == "ok"
    assert util.email_status("logo@2x.png") == "invalid"
    assert util.is_role_email("info@x.test") and not util.is_role_email("sarah@x.test")
    assert util.email_relates("sarah@smithjewelers.test", "smithjewelers.test", "Smith Jewelers")
    assert util.email_relates("smithjewels@gmail.com", "", "Smith Jewelers")
    assert not util.email_relates("hello@webagency.test", "smithjewelers.test", "Smith Jewelers")


def test_phone_rules():
    assert util.phone_digits("tel:+1-312-555-0142") == "3125550142"
    assert util.is_toll_free("(888) 555-0100")
    assert util.phone_digits("12345") == ""


def test_people_extraction():
    t = ("Owner: Sarah Goldberg has 30 years at the bench. Michael Chen, Master Jeweler. "
         "Founded by Anna Klein in 1979. Read More about Custom Design.")
    names = [p[0] for p in util.extract_people(t, "Goldberg Fine Jewelry")]
    assert names[:3] == ["Sarah Goldberg", "Michael Chen", "Anna Klein"]
    assert "Read More" not in names and "Custom Design" not in names


# ------------------------------------------------------------------ parsers
OSM_EL = {"type": "node", "id": 42, "tags": {
    "shop": "jewelry", "name": "Hartwell Jewelers", "addr:housenumber": "12",
    "addr:street": "Main Street", "addr:city": "Evanston", "addr:postcode": "60201",
    "phone": "+1 312 555 0142", "website": "https://www.hartwell.test/home",
    "contact:instagram": "https://instagram.com/hartwell.test"}}


def test_osm_parse():
    r = discover_osm.element_to_listing(OSM_EL, "Chicago, IL")
    assert r["bkey"] == "osm:node/42"
    assert r["address"] == "12 Main Street, Evanston, IL 60201"
    assert (r["city"], r["state"]) == ("Evanston", "IL")
    assert r["website"] == "https://www.hartwell.test"
    assert r["source_url"] == "https://www.openstreetmap.org/node/42"
    assert r["category"] == "shop=jewelry"


SITE_HTML = """<html><head><title>Hartwell Jewelers | Custom Engagement Rings</title>
<script type="application/ld+json">{"@type":"JewelryStore","name":"Hartwell","founder":{"name":"Dana Hartwell"}}</script>
</head><body><h1>Fine jewelry since 1962</h1>
<a href="mailto:dana@hartwell.test">Email Dana</a>
<a href="tel:+13125550142">Store</a> <a href="tel:3125550199">Dana's cell</a>
<span>Fax: <a href="tel:3125550111">312-555-0111</a></span>
<a href="https://www.facebook.com/hartwelljewelers">fb</a>
<a href="https://www.facebook.com/sharer.php?u=x">share</a>
<a href="/meet-our-team">Meet the team</a>
<p>Owner Dana Hartwell is a GIA Graduate Gemologist with an on-site bench jeweler.</p>
<span data-cfemail="1d7e72736979627e5d75687e797366683369786e69"></span>
</body></html>"""


def test_parse_page():
    p = crawl_sites.parse_page(SITE_HTML, "https://hartwell.test/")
    assert "dana@hartwell.test" in p["emails"]
    assert p["tels"] == ["3125550142", "3125550199"]          # fax excluded
    assert p["socials"] == ["https://facebook.com/hartwelljewelers"]
    assert any("meet-our-team" in l for l in p["links"])
    assert crawl_sites.SINCE_RX.search(p["text"]).group(1) == "1962"
    assert crawl_sites.SIGNAL_RX["gia"].search(p["text"])
    assert crawl_sites.SIGNAL_RX["bench"].search(p["text"])


def test_linkedin_judge():
    j = linkedin.judge
    assert j("Dana Hartwell", "Hartwell Jewelers", "Evanston",
             "https://www.linkedin.com/in/dana-hartwell-123", "Dana Hartwell - Owner - Hartwell Jewelers | LinkedIn", "") == "match"
    assert j("Dana Hartwell", "Hartwell Jewelers", "Evanston",
             "https://www.linkedin.com/in/hartwelljewelers", "Hartwell Jewelers | LinkedIn", "") == "reject"
    assert j("Dana Hartwell", "Hartwell Jewelers", "Evanston",
             "https://www.linkedin.com/in/dana-hartwell", "Dana Hartwell | LinkedIn", "Accountant in Ohio") == "ambiguous"


YP_HTML = """<div class="result"><a class="business-name" href="/chicago-il/mip/hartwell-jewelers-1?lid=1">Hartwell Jewelers</a>
<div class="categories"><a>Jewelers</a><a>Jewelry Repairing</a></div><div class="phones">(312) 555-0142</div>
<div class="street-address">12 Main St</div><div class="locality">Evanston, IL 60201</div>
<a class="track-visit-website" href="https://hartwell.test/">Website</a>
<div class="result-rating four half"></div><span class="count">(33)</span></div>"""


def test_yp_parse():
    rows, has_next = discover_web.parse_yp(YP_HTML, "Chicago, IL", "u")
    r = rows[0]
    assert r["category"] == "Jewelers, Jewelry Repairing"
    assert (r["city"], r["state"], r["rating"], r["reviews"]) == ("Evanston", "IL", "4.5", "33")
    assert r["source_url"] == "https://www.yellowpages.com/chicago-il/mip/hartwell-jewelers-1"


BBB_HTML = """<html><script type="application/ld+json">{"@type":"LocalBusiness","name":"Hartwell Jewelers",
"telephone":"(312) 555-0142","url":"https://hartwell.test",
"address":{"streetAddress":"12 Main St","addressLocality":"Evanston","addressRegion":"IL","postalCode":"60201"}}</script>
<body><h1>Hartwell Jewelers</h1><a href="/us/category/jewelry-stores">Jewelry Stores</a>
<h3>Business Management</h3>
Ms. Dana Hartwell, Owner
Business Started:
3/1/1962
</body></html>"""


def test_bbb_profile_parse():
    r = discover_web.parse_bbb_profile(BBB_HTML, "https://www.bbb.org/us/il/evanston/profile/jewelry-stores/hartwell-0654-1", "Chicago, IL")
    assert r["name"] == "Hartwell Jewelers" and r["category"] == "Jewelry Stores"
    assert r["extra"]["bbb_people"] == [{"name": "Dana Hartwell", "role": "Owner"}]
    assert r["extra"]["bbb_years"] == "1962"


# ------------------------------------------------------------------ builder
def _listing(con, **kw):
    base = {"category": "Jewelry store", "phone": "", "website": "", "address": "",
            "city": "", "state": "", "zip": "", "origin": "Google Maps", "rating": "",
            "reviews": "", "discovered_at": "2026-10-13T14:22:07+05:30"}
    base.update(kw)
    db.upsert_listing(con, base)


def _seed(con):
    # Business A: two listings (Chicago Maps + Evanston-market YP) sharing a phone.
    _listing(con, bkey="gmaps:a1", name="Hartwell Jewelers", phone="(312) 555-0142",
             website="https://hartwell.test", address="12 Main St, Evanston, IL 60201",
             market="Chicago, IL", source_url="https://www.google.com/maps/place/a1",
             rating="4.8", reviews="33")
    _listing(con, bkey="yp:a2", name="Hartwell Jewelers Inc", phone="312.555.0142",
             market="Boston, MA", origin="YellowPages",
             source_url="https://www.yellowpages.com/x/mip/a2")
    # Business B: toll-free, no address, email only.
    _listing(con, bkey="osm:node/7", name="Lumen Custom Jewelry", category="shop=jewelry",
             phone="(888) 555-0100", website="https://lumen.test", market="Chicago, IL",
             origin="OpenStreetMap", source_url="https://www.openstreetmap.org/node/7")
    # A pawn shop that slipped past discovery — builder must drop it.
    _listing(con, bkey="gmaps:p", name="Loop Pawn & Gold", phone="(312) 555-0177",
             market="Chicago, IL", source_url="https://www.google.com/maps/place/p")
    crawl_a = {"emails": {"dana@hartwell.test": "https://hartwell.test/contact"},
               "placeholder_emails": [], "tels": {"3125550142": "https://hartwell.test/",
                                                  "3125550199": "https://hartwell.test/contact"},
               "socials": ["https://facebook.com/hartwelljewelers"], "signals": ["gia", "bench"],
               "since": "1962", "meta": {"title": "Hartwell Jewelers", "desc": "", "h1": ""},
               "about_text": "", "jsonld": []}
    crawl_b = {"emails": {"info@lumen.test": "https://lumen.test/contact"},
               "placeholder_emails": ["youremail@lumen.test"], "tels": {}, "socials": [],
               "signals": ["custom-design"], "since": "", "meta": {"title": "Lumen", "desc": "", "h1": ""},
               "about_text": "", "jsonld": []}
    for root, res in (("https://hartwell.test", crawl_a), ("https://lumen.test", crawl_b)):
        con.execute("INSERT OR REPLACE INTO crawls VALUES (?,?,?,?,?,?)",
                    (root, root, "ok", "{}", json.dumps(res), "2026-10-13T14:30:00+05:30"))
    db.add_person(con, "gmaps:a1", "Dana Hartwell", "Owner",
                  "https://www.bbb.org/us/il/evanston/profile/x", "bbb-profile")


def _read(p):
    with open(p, newline="") as f:
        return list(csv.DictReader(f))


def test_builder_end_to_end(tmpdb):
    _seed(tmpdb)
    build.build(log=lambda *a: None)
    rows = _read(config.ALL_CSV)
    q = _read(config.QUALIFIED_CSV)
    assert list(rows[0].keys()) == config.COLUMNS
    names = {r["Business"] for r in rows}
    assert "Loop Pawn & Gold" not in names                       # killed by builder pass
    assert tmpdb.execute("SELECT reason FROM dropped WHERE bkey='gmaps:p'").fetchone()[0] == "pawn"
    a = next(r for r in rows if r["Business"] == "Hartwell Jewelers")
    assert a["Merged Listings"] == "1" and a["Also Listed As"] == "Hartwell Jewelers Inc"
    assert a["Other Markets"] == "Boston, MA"
    assert a["Mobile Candidates"] == "(312) 555-0199"            # main number excluded
    assert a["Signals"].startswith("2 of 3") and "direct-line" in a["Signals"]
    assert "gia" in a["Signals"] and "since-1962" in a["Signals"]
    assert a["Match Type"] == "Email" and a["Email Source"] == "https://hartwell.test/contact"
    assert a["Contact Person"] == "Dana Hartwell" and a["Role"] == "Owner"
    assert a["Real City"] == "Evanston" and a["Real State"] == "IL"
    assert a["Segment"] == "Jewelry retailer"
    b = next(r for r in rows if r["Business"] == "Lumen Custom Jewelry")
    assert b["Flags"] == "no-address, toll-free"                 # Flags actually populated
    assert "role-email" in b["Signals"] and b["Signals"].startswith("1 of 3")
    assert b["Segment"] == "Custom / bespoke jeweler"
    assert [r["Business"] for r in q] == ["Hartwell Jewelers"]
    from openpyxl import load_workbook
    ws = load_workbook(config.QUALIFIED_XLSX)["Qualified Leads"]
    assert [c.value for c in ws[1]] == config.COLUMNS and ws.cell(2, 1).value == "Hartwell Jewelers"
    report = config.REPORT_MD.read_text()
    assert "dropped_out_of_scope" in report and "| pawn |" in report


def test_builder_idempotent(tmpdb):
    _seed(tmpdb)
    build.build(log=lambda *a: None)
    first = config.ALL_CSV.read_bytes()
    _seed(tmpdb)          # re-running discovery inserts nothing new
    build.build(log=lambda *a: None)
    assert config.ALL_CSV.read_bytes() == first


def test_shared_switchboard_not_merged(tmpdb):
    for i, nm in enumerate(["Aurum Jewelers", "Bellini Jewelry", "Castor Goldsmith"]):
        _listing(tmpdb, bkey=f"yp:s{i}", name=nm, phone="(212) 555-0100",
                 website=f"https://site{i}.test", address=f"{i} Mall Way, Miami, FL 33101",
                 market="Miami, FL", origin="YellowPages", source_url=f"https://www.yellowpages.com/s{i}")
    build.build(log=lambda *a: None)
    rows = _read(config.ALL_CSV)
    assert len(rows) == 3
    assert all("shared-switchboard" in r["Flags"] for r in rows)


def test_cache_key_accepts_post_dict():
    from pipeline.http import cache_path
    a = cache_path("https://overpass.test/api", {"data": "q1"})
    assert a == cache_path("https://overpass.test/api", {"data": "q1"})
    assert a != cache_path("https://overpass.test/api", {"data": "q2"})


def test_wholesale_category_alone_does_not_drop():
    cat = "Jewelers, Jewelers-Wholesale & Manufacturers, Jewelry Designers"
    assert scope.kill_reason("Unusual Wedding Rings", cat) is None
    assert scope.kill_reason("Gold Star Jewelry Wholesale Inc", cat) == "wholesale-manufacturer"
    assert scope.kill_reason("Jewelers Of America", cat) == "trade-association"
    assert scope.site_kill_reason("ABC Jewelry | Wholesale only, to the trade only") == "wholesale-manufacturer"


def test_live_run_regressions():
    assert scope.kill_reason("Buyers Of NYC Gold Selling Of Midtown NYC", "Jewelers") == "gold-buyer"
    assert scope.kill_reason("Folli Follie", "Jewelers") == "chain"
    assert util.phone_digits("tel:+30 210 624 1140") == ""
    assert util.phone_digits("tel:+1 (312) 555-0142") == "3125550142"
    assert "Period Signed" not in [p[0] for p in util.extract_people("Period Signed pieces by Cartier.")]
    crawl = {"meta": {"title": "The Plumb Club | Members", "h1": ""}}
    assert not build.site_is_business({"name": "Ema Jewelry Inc", "website": "https://plumbclub.test"}, crawl)
    assert build.site_is_business({"name": "Hartwell Jewelers", "website": "https://hartwell.test"}, crawl)


def test_buyer_category_alone_does_not_drop():
    assert scope.kill_reason("Hartwell Jewelers", "Jewelers, Jewelry Buyers, Diamond Buyers") is None
    assert scope.kill_reason("Fairfield Estate Buyers", "Jewelers") == "gold-buyer"


def test_regex_names_need_given_name():
    t = "Emeritus Board member. Focus Tiffany pieces. Assistant Sales: Page. Owner: Mish Tworkowski."
    assert [p[0] for p in util.extract_people(t)] == []          # 'Mish' not a common given name
    assert [p[0] for p in util.extract_people("Owner: Dana Hartwell")] == ["Dana Hartwell"]
    assert util.is_role_email("careers@x.test") and util.is_role_email("concierge@x.test")


def test_street_is_not_a_person():
    assert not util.plausible_name("Madison Ave", need_given=True)
    assert util.plausible_name("Madison Clarke", need_given=True)


def test_foreign_site_contacts_rejected():
    agta = {"meta": {"title": "AGTA - American Gem Trade Association", "h1": "New York"}}
    assert not build.site_is_business({"name": "New York Jewelry Mart", "website": "https://agta.org"}, agta)
    lst = {"name": "Peggy Skemp Jewelry", "website": "https://laurelelliott.test", "extra": "{}",
           "source_url": "https://www.yellowpages.com/x"}
    crawl = {"emails": {"customerservice@laurelelliott.test": "https://laurelelliott.test/"}}
    assert build._pick_email(lst, crawl, [], "laurelelliott.test")[0] == ""
    lst2 = dict(lst, name="Lewis Jewelers", website="https://lewisusa.test")
    crawl2 = {"emails": {"info@lewisusa.test": "https://lewisusa.test/"}}
    assert build._pick_email(lst2, crawl2, [], "lewisusa.test")[0] == "info@lewisusa.test"


def test_more_scope_rules():
    assert scope.kill_reason("Graff Diamonds Chicago", "Jewelers") == "chain"
    assert scope.classify_segment("Mintz & Gold", "Jewelers", "A litigation law firm "
                                  "representing clients in commercial disputes, employment matters " * 3) is None
    assert scope.classify_segment("Hartwell Jewelers", "Jewelers", "Engagement rings and fine jewelry " * 10)
    assert not util.is_us_number("(647) 537-8336") and util.is_us_number("(312) 555-0142")


def test_directory_self_links_are_not_websites():
    assert util.root_url("https://www.yellowpages.com/new-york-ny/mip/x") == ""
    assert util.root_url("https://www.bbb.org/us/x") == ""
    assert util.root_url("https://lanejewelersny.localsearch.com/") == "https://lanejewelersny.localsearch.com"
    assert scope.classify_segment("Sister Jewelry", "Jewelers",
                                  "Facebook Email or phone Password You're Temporarily Blocked " * 8) is not None


def test_strong_jewelry_name_survives_thin_site():
    js_shell = "Please enable JavaScript to view this site. Loading... Cookies policy accept " * 5
    assert scope.classify_segment("Paul's Jewelry", "Jewelers", js_shell) == "Jewelry retailer"
    assert scope.classify_segment("Loft", "Jewelers, Clothing Stores", "Women's clothing, dresses, pants and tops " * 8) is None
