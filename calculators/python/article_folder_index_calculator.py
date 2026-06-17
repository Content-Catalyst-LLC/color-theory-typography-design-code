#!/usr/bin/env python3
import csv
from pathlib import Path
root = Path(__file__).resolve().parents[2]
rows = list(csv.DictReader((root / "data" / "article_inventory.csv").open("r", encoding="utf-8")))
out = root / "calculators" / "outputs" / "article_folder_links.md"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text("\n".join(["# Article Folder Links", ""] + [f"- [{r['title']}](../../articles/{r['slug']}/) — [website]({r['website_url']})" for r in rows]) + "\n", encoding="utf-8")
print(f"Wrote {out}")
