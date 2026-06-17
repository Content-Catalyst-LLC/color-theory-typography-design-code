#!/usr/bin/env bash
set -euo pipefail
python3 calculators/python/article_folder_index_calculator.py
if command -v Rscript >/dev/null 2>&1; then Rscript calculators/r/section_count_summary.R; else echo "Rscript not found; skipping R calculator."; fi
echo "Calculator smoke tests complete."
