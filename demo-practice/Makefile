.DEFAULT_GOAL := check

VENV := .venv

ifeq ($(OS),Windows_NT)
	PYTHON := $(VENV)/Scripts/python.exe
	PIP := $(VENV)/Scripts/pip.exe
else
	PYTHON := $(VENV)/bin/python
	PIP := $(VENV)/bin/pip
endif

.PHONY: install run test typecheck format lint check-requirements check

venv:
	python -m venv $(VENV)

install: venv
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

run: install
	$(PYTHON) src/app.py

test: install
	PYTHONPATH=src $(PYTHON) -m pytest tests

typecheck: install
	PYTHONPATH=src $(PYTHON) -m mypy src tests

format: install
	$(PYTHON) -m ruff format src tests scripts

lint: install
	$(PYTHON) -m ruff check src tests scripts

check-requirements: install
	$(PYTHON) scripts/check_requirements.py

check: typecheck lint check-requirements test
