from __future__ import annotations
import csv, json
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
def read_csv(path):
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))
def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
def write_markdown(path, lines):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
def build_article_outputs(root=ROOT):
    inventory = read_csv(root / "data" / "article_inventory.csv")
    siblings = read_csv(root / "data" / "sibling_article_maps.csv")
    counts = Counter(row["section"] for row in inventory)
    records = [{"title": r["title"], "slug": r["slug"], "section": r["section"], "status": r["status"], "website_url": r["website_url"], "folder": f"articles/{r['slug']}/"} for r in inventory]
    summary = {"article_count": len(inventory), "section_count": len(counts), "sections": dict(counts), "sibling_article_maps": siblings}
    write_json(root / "outputs" / "article_inventory.json", records)
    write_json(root / "outputs" / "repo_summary.json", summary)
    write_markdown(root / "outputs" / "article_folder_index.md", ["# Article Folder Index", ""] + [f"- [{r['title']}](../{r['folder']}) — {r['section']}" for r in records])
    write_markdown(root / "outputs" / "meaning_article_map_crosswalk.md", ["# Meaning Article Map Crosswalk", ""] + [f"- [{r['article_map']}]({r['website_url']}) — `{r['repo']}`" for r in siblings])
    return summary
def build_canvas_cards(root=ROOT):
    for row in read_csv(root / "data" / "article_inventory.csv"):
        write_markdown(root / "canvas" / "cards" / f"{row['slug']}.md", [f"# Canvas Card: {row['title']}", "", f"- Section: {row['section']}", f"- Status: {row['status']}", f"- Website URL: {row['website_url']}", "", "## Guardrail", "", "Use computation to support clarity, documentation, and exploration. Do not replace interpretation with automation."])
