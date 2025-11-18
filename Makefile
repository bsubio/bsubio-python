.PHONY: all build test examples clean install dev fmt lint typecheck check docs publish help

# Python interpreter to use
PYTHON := python3

# Virtual environment directory
VENV := .venv

# Detect OS for virtual environment activation
ifeq ($(OS),Windows_NT)
	VENV_BIN := $(VENV)/Scripts
	PYTHON_VENV := $(VENV_BIN)/python.exe
else
	VENV_BIN := $(VENV)/bin
	PYTHON_VENV := $(VENV_BIN)/python
endif

all: build

# Create virtual environment and install dependencies
$(VENV):
	$(PYTHON) -m venv $(VENV)
	$(PYTHON_VENV) -m pip install --upgrade pip setuptools wheel

# Install package in development mode with all dependencies
dev: $(VENV)
	$(PYTHON_VENV) -m pip install -e ".[dev]"
	@echo "Development environment ready. Activate with: source $(VENV_BIN)/activate"

# Install package in production mode
install: $(VENV)
	$(PYTHON_VENV) -m pip install .

# Build distribution packages
build: $(VENV)
	$(PYTHON_VENV) -m pip install --upgrade build
	$(PYTHON_VENV) -m build

# Run tests with coverage
test: $(VENV)
	$(PYTHON_VENV) -m pytest

# Run specific test file
test-file: $(VENV)
	@test -n "$(FILE)" || (echo "Usage: make test-file FILE=tests/test_client.py" && exit 1)
	$(PYTHON_VENV) -m pytest $(FILE)

# Run tests with verbose output
test-verbose: $(VENV)
	$(PYTHON_VENV) -m pytest -vv

# Format code with black
fmt: $(VENV)
	$(PYTHON_VENV) -m black src/ tests/ examples/

# Check code formatting without modifying files
fmt-check: $(VENV)
	$(PYTHON_VENV) -m black --check src/ tests/ examples/

# Lint code with ruff
lint: $(VENV)
	$(PYTHON_VENV) -m ruff check src/ tests/ examples/

# Fix linting issues automatically
lint-fix: $(VENV)
	$(PYTHON_VENV) -m ruff check --fix src/ tests/ examples/

# Type check with mypy
typecheck: $(VENV)
	$(PYTHON_VENV) -m mypy src/bsubio

# Run all checks (format, lint, typecheck, test)
check: fmt-check lint typecheck test

# Build and run example scripts
examples: $(VENV)
	@echo "Running basic example..."
	$(PYTHON_VENV) examples/basic.py || true
	@echo "\nRunning comprehensive example..."
	$(PYTHON_VENV) examples/comprehensive.py || true
	@echo "\nRunning batch example..."
	$(PYTHON_VENV) examples/batch.py || true

# Run specific example
example: $(VENV)
	@test -n "$(NAME)" || (echo "Usage: make example NAME=basic" && exit 1)
	$(PYTHON_VENV) examples/$(NAME).py

# Clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf src/*.egg-info
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

# Clean everything including virtual environment
distclean: clean
	rm -rf $(VENV)

# Publish to PyPI (requires authentication)
publish: build
	@echo "Publishing to PyPI..."
	@echo "Make sure you have configured your PyPI credentials (~/.pypirc or environment variables)"
	$(PYTHON_VENV) -m pip install --upgrade twine
	$(PYTHON_VENV) -m twine check dist/*
	$(PYTHON_VENV) -m twine upload dist/*

# Publish to Test PyPI
publish-test: build
	@echo "Publishing to Test PyPI..."
	$(PYTHON_VENV) -m pip install --upgrade twine
	$(PYTHON_VENV) -m twine check dist/*
	$(PYTHON_VENV) -m twine upload --repository testpypi dist/*

# Generate documentation (placeholder for future sphinx docs)
docs:
	@echo "Documentation generation not yet implemented"
	@echo "Consider adding Sphinx or mkdocs in the future"

# Download OpenAPI specification
openapi:
	curl -s https://app.bsub.io/static/openapi.yaml -o openapi.yaml
	@echo "OpenAPI spec downloaded to openapi.yaml"

# Show help
help:
	@echo "BSUB.IO Python SDK - Makefile targets:"
	@echo ""
	@echo "  make dev              - Set up development environment with all dependencies"
	@echo "  make install          - Install package in production mode"
	@echo "  make build            - Build distribution packages for PyPI"
	@echo "  make test             - Run tests with coverage"
	@echo "  make test-verbose     - Run tests with verbose output"
	@echo "  make fmt              - Format code with black"
	@echo "  make fmt-check        - Check code formatting"
	@echo "  make lint             - Lint code with ruff"
	@echo "  make lint-fix         - Fix linting issues automatically"
	@echo "  make typecheck        - Type check with mypy"
	@echo "  make check            - Run all checks (format, lint, typecheck, test)"
	@echo "  make examples         - Run all example scripts"
	@echo "  make example NAME=x   - Run specific example (e.g., make example NAME=basic)"
	@echo "  make clean            - Clean build artifacts"
	@echo "  make distclean        - Clean everything including virtual environment"
	@echo "  make publish          - Publish to PyPI"
	@echo "  make publish-test     - Publish to Test PyPI"
	@echo "  make openapi          - Download OpenAPI specification"
	@echo "  make help             - Show this help message"
	@echo ""
	@echo "Quick start:"
	@echo "  1. make dev           - Set up development environment"
	@echo "  2. source .venv/bin/activate  - Activate virtual environment"
	@echo "  3. make check         - Run all checks"
	@echo ""
