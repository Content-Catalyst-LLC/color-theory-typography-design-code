from pathlib import Path
import csv
def test_article_inventory_has_36_rows():
    rows = list(csv.DictReader(Path("data/article_inventory.csv").open("r", encoding="utf-8")))
    assert len(rows) == 36
def test_article_folders_exist():
    rows = list(csv.DictReader(Path("data/article_inventory.csv").open("r", encoding="utf-8")))
    assert not [row["slug"] for row in rows if not Path("articles", row["slug"], "README.md").exists()]
