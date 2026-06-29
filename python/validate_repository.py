from __future__ import annotations

from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "LICENSE",
    "CITATION.cff",
    "repository_manifest.json",
    "docs/meaning_not_reduction.md",
    "docs/interpretive_cautions.md",
    "data/article_registry.csv",
    "sql/schema.sql",
]

def main() -> int:
    missing = [path for path in REQUIRED if not (ROOT / path).exists()]
    if missing:
        print("Missing required files:")
        for path in missing:
            print(f" - {path}")
        return 1

    registry = ROOT / "data" / "article_registry.csv"
    with registry.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    if not rows:
        print("article_registry.csv has no rows.")
        return 1

    required_columns = {"article_id", "title", "section", "sequence_order", "slug", "status"}
    missing_columns = required_columns - set(rows[0].keys())
    if missing_columns:
        print(f"article_registry.csv missing columns: {sorted(missing_columns)}")
        return 1

    print("Repository validation passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
