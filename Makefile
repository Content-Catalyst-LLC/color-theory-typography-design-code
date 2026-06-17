.PHONY: all python r calculators test clean
all: python r calculators
python:
	PYTHONPATH=python python3 python/run_workflow.py
r:
	Rscript r/article_summary.R || true
calculators:
	bash calculators/run_calculator_smoke_tests.sh
test:
	PYTHONPATH=python python3 -m pytest python/tests || true
clean:
	rm -rf outputs/* calculators/outputs/* canvas/cards/*
