.DEFAULT_GOAL := create-structure

ifeq ($(OS),Windows_NT)
	PYTHON := python
else
	PYTHON := python3
endif

create-structure:
	mkdir -p src tests docs
	touch README.md setup.py requirements.txt
	touch docs/DOMAIN.md
	touch src/.gitkeep tests/.gitkeep

install-dep:
	$(PYTHON) -m pip install -r requirements.txt

install:
	$(PYTHON) -m pip install -e .

test-pytest:
	$(PYTHON) -m pytest
