all: build

install:
	pip install -r requirements.txt

build: install
	pip install -r test-requirements.txt
	python -m build

test:
	pandoc -o test/test_pdf.pdf test/test_pdf.md
	python -m pytest

regenerate:
	openapi-generator-cli generate -i ../openapi.yaml -g python -o . --additional-properties=packageName=bsubio,packageVersion=1.0.0,projectName=bsubio

examples: install
	cd examples && pip install -r requirements.txt

clean:
	rm -rf dist build *.egg-info
	rm -rf .pytest_cache
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

publish: build test
	python -m twine upload dist/*

.PHONY: all install build test regenerate examples clean publish
