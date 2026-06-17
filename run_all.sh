#!/usr/bin/env bash
set -euo pipefail
PYTHONPATH=python python3 python/run_workflow.py
if command -v Rscript >/dev/null 2>&1; then Rscript r/article_summary.R; else echo "Rscript not found; skipping R workflow."; fi
bash calculators/run_calculator_smoke_tests.sh
if command -v pytest >/dev/null 2>&1; then PYTHONPATH=python pytest python/tests; else echo "pytest not found; skipping Python tests."; fi
echo "All smoke workflows complete."
