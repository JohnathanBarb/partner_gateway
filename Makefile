SHELL := /bin/sh

.PHONY: venv
venv:
	if [ ! -d .venv ]; then virtualenv -p python3.10.3 .venv; fi
	. .venv/bin/activate

.PHONY: install
install: venv
	pip install --upgrade pip poetry
	poetry install --no-root

.PHONY: tests
tests:
	poetry run pytest --junitxml report.xml

.PHONY: test
test: tests

.PHONY: tests-report
tests-report:
	poetry run pytest --cov=. --cov-report html
