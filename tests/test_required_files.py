from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_required_files_exist():
    required = [
        "README.md",
        "LICENSE",
        "CITATION.cff",
        "repository_manifest.json",
        "docs/meaning_not_reduction.md",
        "docs/interpretive_cautions.md",
        "data/article_registry.csv",
        "sql/schema.sql",
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel
