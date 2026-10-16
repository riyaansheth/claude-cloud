"""Person-level leads: LinkedIn profiles of people at diamond-trade firms (owners, buyers, sales, partners).

Reads raw_people/*/*.json (one file per person, written by "People" workers), dedupes on the LinkedIn
slug, keeps only real linkedin.com/in/ URLs of named humans, and writes diamonds_people.csv plus a
'People' sheet in diamond_leads_people.xlsx. Never mixes with the 1-lead-per-business sheets.
"""
import csv, json, re, sys
from collections import Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import RUN_DIR, clean_linkedin, kill_reason, now_iso

COLS = ["Person", "Title", "Company", "Company Website", "City", "State", "Market", "LinkedIn Profile",
        "LinkedIn Source", "Company Email", "Company Phone", "Seniority", "Trade Signals", "Source", "Found At"]

def main():
    best = {}
    dropped = Counter()
    for f in sorted((RUN_DIR / "raw_people").glob("*/*.json")):
        try:
            p = json.loads(f.read_text())
        except Exception:
            dropped["malformed"] += 1; continue
        li = clean_linkedin(p.get("linkedin_url", ""))
        name = " ".join((p.get("person") or "").split())
        if not li or len(name.split()) < 2:
            dropped["no-personal-linkedin"] += 1; continue
        if kill_reason(p.get("company", "")):
            dropped["kill-list"] += 1; continue
        if p.get("is_diamond_trade") is False:
            dropped["not-diamond-trade"] += 1; continue
        slug = li.rsplit("/in/", 1)[1].lower().rstrip("/")
        row = {"Person": name, "Title": p.get("title", ""), "Company": p.get("company", ""),
               "Company Website": p.get("company_website", ""), "City": p.get("city", ""),
               "State": (p.get("state") or "")[:2].upper(), "Market": p.get("market", ""),
               "LinkedIn Profile": li, "LinkedIn Source": p.get("linkedin_source", ""),
               "Company Email": p.get("company_email", ""), "Company Phone": p.get("company_phone", ""),
               "Seniority": p.get("seniority", ""), "Trade Signals": ", ".join(p.get("signals", []) or []),
               "Source": p.get("source_url") or p.get("linkedin_source", ""), "Found At": p.get("found_at") or now_iso()}
        score = sum(bool(v) for v in row.values())
        if slug not in best or score > best[slug][0]:
            best[slug] = (score, row)
    rows = sorted((r for _, r in best.values()), key=lambda r: (r["Market"], r["Company"].lower(), r["Person"]))
    with open(RUN_DIR / "diamonds_people.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS); w.writeheader(); w.writerows(rows)
    from export_xlsx import sheet
    from openpyxl import Workbook
    wb = Workbook(); wb.remove(wb.active)
    sheet(wb, "People", COLS, rows, {"Person": 24, "Title": 30, "Company": 32, "LinkedIn Profile": 44, "Market": 18})
    ws = wb.create_sheet("By Market"); ws.append(["Market", "People with LinkedIn", "Companies"])
    for m, n in Counter(r["Market"] for r in rows).most_common():
        ws.append([m, n, len({r["Company"] for r in rows if r["Market"] == m})])
    wb.save(RUN_DIR / "diamond_leads_people.xlsx")
    print(f"people={len(rows)} markets={len({r['Market'] for r in rows})} dropped={dict(dropped)}")

if __name__ == "__main__":
    main()
