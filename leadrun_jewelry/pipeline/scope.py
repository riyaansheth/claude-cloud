"""Scope rules: the HARD EXCLUSION KILL-LIST, the diamond-trade carve-out, and
segment classification.

`kill_reason()` is applied twice: at discovery (before any crawl is spent) and
again in the builder immediately before a row is written. A non-None return
means the business is dropped — never relabelled, never shipped flagged.
"""
import re

def _rx(*terms):
    return re.compile(r"(?<![a-z0-9])(?:" + "|".join(terms) + r")(?![a-z0-9])", re.I)

# reason -> pattern, matched against business name and source category.
KILL_NAME_CATEGORY = [
    ("pawn", _rx(r"pawn", r"pawns", r"pawnbrokers?", r"pawn ?shops?", r"ez ?pawn",
                 r"cash america", r"loans? on jewelry", r"collateral loans?")),
    ("gold-buyer", _rx(r"cash for gold", r"we buy gold", r"gold exchange",
                       r"scrap gold", r"bullion", r"precious metals? buyers?",
                       r"refinery", r"refiners?", r"gold buyers?",
                       r"buyers? of [\w ]{0,20}gold", r"gold (?:selling|buying)",
                       r"we buy", r"cash for (?:gold|diamonds|jewelry)",
                       r"sell (?:your )?gold")),
    ("coin-currency", _rx(r"coins?", r"numismatics?", r"rare coins",
                          r"currency exchange", r"stamps? and coins?",
                          r"stamps? & coins?")),
    ("beads-craft", _rx(r"beads?", r"bead stores?", r"bead shops?", r"beading",
                        r"findings", r"jewelry suppl(?:y|ies)",
                        r"jewellery suppl(?:y|ies)", r"crafts?", r"hobby",
                        r"hobbies", r"wire wrapping", r"charm bar")),
    ("costume-fashion", _rx(r"costume jewelry", r"fashion jewelry",
                            r"fashion jewellery", r"claire'?s", r"icing",
                            r"accessories store", r"accessories", r"handbags?")),
    ("piercing-tattoo", _rx(r"piercings?", r"tattoos?", r"body jewelry",
                            r"permanent jewelry", r"permanent bracelets?")),
    ("kiosk-battery", _rx(r"kiosks?", r"battery", r"batteries", r"watch battery",
                          r"carts?", r"mall cart", r"phone cases?",
                          r"cell phone")),
    ("simulants", _rx(r"moissanite", r"cubic zirconia", r"cz", r"lab simulants?",
                      r"diamond alternatives?", r"simulated diamonds?")),
    ("chain", _rx(r"kay", r"kay jewelers", r"jared", r"zales", r"pandora",
                  r"tiffany ?& ?co\.?", r"tiffany and co", r"tiffany",
                  r"blue nile", r"james allen", r"brilliant earth", r"signet",
                  r"shane co\.?", r"shane company", r"helzberg",
                  r"ben bridge", r"daniel'?s jewelers", r"rogers ?& ?hollands",
                  r"rogers and hollands", r"swarovski", r"macy'?s",
                  r"jc ?penney", r"nordstrom", r"piercing pagoda", r"peoples jewellers",
                  r"banter", r"diamonds direct", r"kendra scott", r"david yurman",
                  r"alex and ani", r"cartier", r"bvlgari", r"bulgari",
                  r"van cleef", r"harry winston", r"chopard", r"tourneau",
                  r"bucherer", r"mayors jewelers", r"fred meyer jewelers",
                  r"charm diamond centres", r"jewelry exchange", r"walmart",
                  r"costco", r"sam'?s club", r"target", r"dillard'?s",
                  r"saks", r"neiman marcus", r"bloomingdale'?s", r"sears",
                  r"kohl'?s", r"jcp", r"boscov'?s", r"belk", r"folli follie",
                  r"swatch", r"fossil", r"lovisa", r"mejuri", r"chow tai fook",
                  r"links of london", r"thomas sabo", r"michael kors",
                  r"james avery", r"jostens?", r"gorjana", r"ross[- ]simons",
                  r"reeds jewelers", r"kirk freeport", r"graff", r"de beers",
                  r"mikimoto", r"chanel", r"boucheron", r"piaget", r"chaumet",
                  r"buccellati", r"messika", r"pomellato", r"damiani", r"hermes",
                  r"herm[eè]s", r"louis vuitton", r"dior", r"gucci", r"rolex boutique",
                  r"omega boutique", r"john hardy", r"david morris", r"fabergé|faberge")),
    ("thrift-consignment", _rx(r"thrift", r"consignment", r"resale",
                               r"goodwill", r"second ?hand", r"salvation army",
                               r"flea market", r"swap meet")),
    ("appraiser-lab-insurer", _rx(r"appraisals?", r"appraisers?",
                                  r"gemological (?:lab|laboratory|institute)",
                                  r"gem lab", r"gia lab", r"igi", r"insurance",
                                  r"insurers?")),
]

# These two reasons are dropped only when the business name carries no jewelry
# retail word — "Smith Jewelers & Appraisals" is a jeweler, "Smith Appraisals" is not.
SOFT_REASONS = {"thrift-consignment", "appraiser-lab-insurer", "costume-fashion"}
# Except these phrases, which kill regardless.
HARD_COSTUME = _rx(r"costume jewelry", r"fashion jewelry", r"fashion jewellery",
                   r"claire'?s", r"icing")

JEWELRY_WORD = _rx(r"jewel\w*", r"goldsmiths?", r"silversmiths?", r"gems?",
                   r"diamonds?", r"bench jewelers?", r"engraving", r"rings?",
                   r"watch(?:es)?", r"horolog\w*", r"orfèvre")

BUYER_NAME = _rx(r"jewelry buyers?", r"diamond buyers?", r"estate buyers?", r"gold buyers?")

# Diamond wholesale / trade — out of scope for this run (separate diamonds run).
DIAMOND_TRADE = _rx(r"diamond wholesalers?", r"wholesale diamonds?",
                    r"diamond brokers?", r"loose diamonds?", r"diamond dealers?",
                    r"diamond cutters?", r"diamond cutting", r"diamond district",
                    r"diamond exchange", r"diamond trading", r"diamond importers?",
                    r"diamond manufacturers?", r"diamonds? wholesale")
# Generic jewelry wholesale/manufacturing: YellowPages tags many retailers with
# "Jewelers-Wholesale & Manufacturers", so the category alone never drops a row;
# the name or the site's own headline has to say it.
WHOLESALE_NAME = _rx(r"wholesalers?", r"wholesale", r"manufacturers?", r"mfg",
                     r"trade only", r"to the trade")
DIAMOND_DISTRICT_ADDR = re.compile(
    r"\b(?:4[67]th|forty[- ]?(?:sixth|seventh))\s+st", re.I)
TRADE_OFFICE = re.compile(r"\b(?:suite|ste\.?|fl(?:oor)?\.?|room|rm\.?|booth|#)\s*\w+", re.I)

# What a site plainly sells: only <title>, meta description and <h1> are checked,
# so a jeweler that mentions "we also buy gold" in a footer is not killed.
SITE_KILL = [
    ("pawn", _rx(r"pawn", r"pawnbrokers?", r"pawn ?shop", r"collateral loans?",
                 r"loans? on jewelry")),
    ("gold-buyer", _rx(r"cash for gold", r"gold buyers?", r"scrap gold",
                       r"bullion", r"refinery")),
    ("coin-currency", _rx(r"rare coins", r"numismatics?", r"coin dealers?",
                          r"coin shop")),
    ("beads-craft", _rx(r"bead stores?", r"bead shop", r"beads", r"jewelry supplies",
                        r"jewelry making supplies", r"findings")),
    ("costume-fashion", _rx(r"costume jewelry", r"fashion jewelry",
                            r"fashion accessories", r"handbags")),
    ("piercing-tattoo", _rx(r"body piercing", r"piercing studio", r"tattoo",
                            r"permanent jewelry")),
    ("simulants", _rx(r"moissanite", r"cubic zirconia", r"lab simulants?",
                      r"diamond alternatives?", r"simulated diamonds?")),
    ("wholesale-manufacturer", _rx(r"wholesale only", r"to the trade only",
                                   r"jewelry manufacturer", r"wholesale jewelry manufacturer")),
    ("diamond-trade", _rx(r"diamond wholesalers?", r"wholesale diamonds?",
                          r"loose diamond (?:dealer|wholesaler)s?",
                          r"diamond brokers?", r"to the trade only", r"trade only")),
]


def kill_reason(name, category="", address="", market="", osm_tags=None):
    """Return the drop reason, or None if the business may proceed."""
    name = name or ""
    category = category or ""
    hay = f"{name} | {category}"
    has_jewel = bool(JEWELRY_WORD.search(name))
    for reason, rx in KILL_NAME_CATEGORY:
        if not rx.search(hay):
            continue
        if reason in SOFT_REASONS and has_jewel and not (
                reason == "costume-fashion" and HARD_COSTUME.search(hay)):
            continue
        return reason
    # YP tags many retailers "Jewelry Buyers"/"Diamond Buyers" as a side category;
    # only a business *named* as a buyer is dropped for it.
    if BUYER_NAME.search(name):
        return "gold-buyer"
    if DIAMOND_TRADE.search(hay):
        return "diamond-trade"
    if WHOLESALE_NAME.search(name):
        return "wholesale-manufacturer"
    if re.search(r"\bjewel+ers of america\b|\bjewelers board of trade\b|\bgemological institute\b",
                 name, re.I):
        return "trade-association"
    if (market.startswith("New York") and DIAMOND_DISTRICT_ADDR.search(address or "")
            and TRADE_OFFICE.search(address or "")):
        return "diamond-trade"
    if osm_tags:
        # OSM brand tags are only put on chain stores.
        if osm_tags.get("brand") or osm_tags.get("brand:wikidata"):
            return "chain"
        shop = osm_tags.get("shop", "")
        if shop in ("pawnbroker", "money_lender", "craft", "beads",
                    "tattoo", "fashion_accessories", "second_hand",
                    "charity", "department_store", "variety_store", "mall"):
            return {"pawnbroker": "pawn", "money_lender": "pawn",
                    "craft": "beads-craft", "beads": "beads-craft",
                    "tattoo": "piercing-tattoo",
                    "fashion_accessories": "costume-fashion",
                    "second_hand": "thrift-consignment",
                    "charity": "thrift-consignment"}.get(shop, "chain")
    return None


def site_kill_reason(title="", description="", h1=""):
    hay = " | ".join(x for x in (title, description, h1) if x)
    for reason, rx in SITE_KILL:
        if rx.search(hay):
            return reason
    return None


# ---------------------------------------------------------------- segments
_EST = _rx(r"estate", r"antiques?", r"vintage", r"heirlooms?", r"period jewelry",
           r"victorian", r"art deco", r"edwardian")
_REP = _rx(r"repairs?", r"restoration", r"goldsmiths?", r"silversmiths?",
           r"bench jewelers?", r"engraving", r"engravers?", r"jewelry service")
_CUS = _rx(r"custom", r"bespoke", r"designs?", r"designers?", r"handmade",
           r"hand[- ]?crafted", r"atelier", r"studio", r"made to order",
           r"metalsmiths?")
_RET = _rx(r"jewel\w*", r"fine jewelry", r"watch(?:es)?", r"diamonds?",
           r"gems?", r"gold", r"bridal", r"engagement rings?")


SITE_JEWELRY = _rx(r"jewel\w*", r"rings?", r"diamonds?", r"gold", r"silver", r"gems?",
                   r"bracelets?", r"necklaces?", r"earrings?", r"watch(?:es)?",
                   r"pendants?", r"engagement", r"goldsmith", r"platinum", r"pearls?")


def classify_segment(name, category="", site_text="", osm_tags=None):
    """Return one of config.SEGMENTS, or None (= out of scope, drop)."""
    head = f"{name} | {category}"
    osm_tags = osm_tags or {}
    # A crawled site with no jewelry vocabulary at all is not a jeweler's site
    # (e.g. a law firm "Mintz & Gold" filed under Jewelers by a directory).
    strong_name = _rx(r"jewel\w*", r"gems?", r"diamonds?", r"goldsmiths?", r"silversmiths?",
                      r"watch(?:es)?", r"jewell?ery").search(name or "")
    if (not strong_name and site_text and len(site_text) > 200
            and not SITE_JEWELRY.search(site_text)
            and not re.search(r"facebook|instagram|log in|sign in|temporarily blocked",
                              site_text[:400], re.I)):
        return None
    if _EST.search(head):
        return "Estate & antique jewelry"
    if _REP.search(head) or osm_tags.get("craft") in ("jeweller", "goldsmith",
                                                      "silversmith"):
        if not _RET.search(name) or _REP.search(name):
            return "Jewelry repair / goldsmith"
    if _CUS.search(head):
        if _RET.search(head) or osm_tags.get("shop") == "jewelry":
            return "Custom / bespoke jeweler"
    if osm_tags.get("craft") in ("jeweller", "goldsmith", "silversmith"):
        return "Jewelry repair / goldsmith"
    shop = osm_tags.get("shop")
    if shop == "watches":
        # Watch-only shops are in scope only as fine watch & jewelry boutiques.
        if _rx(r"jewel\w*", r"diamonds?", r"fine", r"gems?").search(
                f"{head} {site_text[:3000]}"):
            return "Jewelry retailer"
        return None
    if shop == "jewelry" or _RET.search(head):
        if site_text and _EST.search(site_text[:3000]) and _rx(
                r"estate jewelry", r"antique jewelry").search(site_text[:3000]):
            return "Estate & antique jewelry"
        if site_text and _rx(r"custom design", r"custom jewelry",
                             r"bespoke").search(site_text[:3000]):
            return "Custom / bespoke jeweler"
        return "Jewelry retailer"
    return None
