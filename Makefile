# Makefile for GRETL Jobs Analyzer Python

.PHONY: help test coverage lint format clean install dev-install run

# Default target
help:
	@echo "GRETL Jobs Analyzer - Python Version"
	@echo "======================================"
	@echo ""
	@echo "Available targets:"
	@echo "  help        - Show this help message"
	@echo "  test        - Run unit tests"
	@echo "  syntax-check - Basic syntax check (no external deps)"
	@echo "  coverage    - Run tests with coverage report (requires coverage)"
	@echo "  lint        - Run linting checks (requires flake8)"
	@echo "  format      - Format code with black (requires black)"
	@echo "  typecheck   - Run type checking with mypy (requires mypy)"
	@echo "  check       - Run all available quality checks"
	@echo "  check-full  - Run all quality checks (requires dev tools)"
	@echo "  code-review - Manual code review checklist"
	@echo "  clean       - Remove generated files"
	@echo "  setup-dev   - Install development dependencies"
	@echo "  install     - Install package"
	@echo "  dev-install - Install package in development mode"
	@echo "  run         - Run analyzer with default settings"
	@echo "  run-debug   - Run analyzer with debug output"

# Run tests
test:
	@echo "Running unit tests..."
	python3 -m unittest test_gretl_analyzer.py -v

# Run tests with coverage
coverage:
	@echo "Running tests with coverage..."
	@if command -v coverage >/dev/null 2>&1; then \
		python3 -m coverage run -m unittest test_gretl_analyzer.py; \
		python3 -m coverage report -m; \
		python3 -m coverage html; \
		echo "Coverage report generated in htmlcov/"; \
	else \
		echo "coverage not installed. Install with: pip3 install coverage"; \
		echo "Running tests without coverage..."; \
		python3 -m unittest test_gretl_analyzer.py -v; \
	fi

# Lint code
lint:
	@echo "Running linting checks..."
	@if command -v flake8 >/dev/null 2>&1; then \
		python3 -m flake8 gretl_analyzer.py test_gretl_analyzer.py --max-line-length=88 --extend-ignore=E203,W503; \
	else \
		echo "flake8 not installed. Install with: pip3 install flake8"; \
		echo "Alternative: Basic syntax check with python3 -m py_compile"; \
		python3 -m py_compile gretl_analyzer.py test_gretl_analyzer.py; \
	fi

# Format code
format:
	@echo "Formatting code..."
	@if command -v black >/dev/null 2>&1; then \
		python3 -m black gretl_analyzer.py test_gretl_analyzer.py --line-length=88; \
	else \
		echo "black not installed. Install with: pip3 install black"; \
		echo "Code formatting skipped."; \
	fi

# Type checking
typecheck:
	@echo "Running type checks..."
	@if command -v mypy >/dev/null 2>&1; then \
		python3 -m mypy gretl_analyzer.py --ignore-missing-imports; \
	else \
		echo "mypy not installed. Install with: pip3 install mypy"; \
		echo "Type checking skipped."; \
	fi

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	rm -rf __pycache__/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf *.egg-info/
	rm -rf build/
	rm -rf dist/
	rm -f GRETL_Jobs_Overview.md

# Install package
install:
	@echo "Installing package..."
	pip3 install .

# Uninstall package
uninstall:
	@echo "Uninstalling package..."
	pip3 uninstall gretl-jobs-analyzer

# Install package in development mode
dev-install:
	@echo "Installing package in development mode..."
	pip3 install -e .
	pip3 install -r requirements.txt

# Run analyzer
run:
	@echo "Running GRETL Jobs Analyzer..."
	python3 gretl_analyzer.py

# Run analyzer with debug
run-debug:
	@echo "Running GRETL Jobs Analyzer with debug output..."
	python3 gretl_analyzer.py --debug

# Create example job structure for testing
create-example:
	@echo "Creating example job structure..."
	mkdir -p example_jobs/test_job1
	mkdir -p example_jobs/test_job2
	echo "triggers.cron=0 2 * * *" > example_jobs/test_job1/job.properties
	echo "triggers.upstream=test_job1" > example_jobs/test_job2/job.properties
	echo "INSERT INTO target.table1 SELECT * FROM source.table1;" > example_jobs/test_job1/main.sql
	echo "INSERT INTO target.table2 SELECT * FROM source.table2;" > example_jobs/test_job2/main.sql
	@echo "Example jobs created in example_jobs/"

# Run analyzer on example
run-example: create-example
	@echo "Running analyzer on example jobs..."
	python3 gretl_analyzer.py --gretl-jobs-dir example_jobs --output-file example_output.md
	@echo "Example output generated in example_output.md"

# Basic syntax check (no external dependencies)
syntax-check:
	@echo "Running basic syntax check..."
	python3 -m py_compile gretl_analyzer.py test_gretl_analyzer.py
	@echo "Syntax check passed!"

# Manual code review checklist
code-review:
	@echo "Manual Code Review Checklist:"
	@echo "=============================="
	@echo "✓ Run tests: make test"
	@echo "✓ Check syntax: make syntax-check"
	@echo "✓ Review TODO/FIXME comments:"
	@grep -n "TODO\|FIXME\|XXX" *.py || echo "  No TODO/FIXME found"
	@echo "✓ Check line length manually (max 88 chars)"
	@echo "✓ Verify type hints are present"
	@echo "✓ Check docstrings are complete"

# All quality checks (with fallbacks)
check:
	@echo "Running all available quality checks..."
	@make syntax-check
	@make test
	@make lint
	@make typecheck
	@echo "All available quality checks completed!"

# Quality checks with external tools (requires dev dependencies)
check-full: lint typecheck test coverage
	@echo "All quality checks with external tools passed!"

# Development setup
setup-dev:
	@echo "Setting up development environment..."
	pip3 install -r requirements.txt
	@echo "Development environment ready!"
	@echo "Now you can use: make lint, make format, make coverage, make typecheck"

# Upload to PyPI (requires credentials)
#upload:
#	@echo "Uploading to PyPI..."
#	python3 -m twine upload dist/*

# Show project info
info:
	@echo "Project Information:"
	@echo "==================="
	@echo "Name: GRETL Jobs Analyzer"
	@echo "Language: Python 3.7+"
	@echo "Dependencies: None (stdlib only)"
	@echo "License: MIT"
	@echo ""
	@echo "Files:"
	@ls -la *.py *.md *.txt Makefile 2>/dev/null || true
