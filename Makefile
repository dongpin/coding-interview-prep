VENV    = venv
PYTHON  = $(VENV)/bin/python3
PIP     = $(VENV)/bin/pip
SRC_DIR = python

.PHONY: venv test lint fix check

venv:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip --quiet
	$(PIP) install -r requirements.txt --quiet

test:
	$(PYTHON) -m pytest $(SRC_DIR)/tests/ -v

lint:
	$(PYTHON) -m flake8 $(SRC_DIR) --max-line-length=100

fix:
	$(PYTHON) -m autoflake --in-place --remove-all-unused-imports --remove-unused-variables -r $(SRC_DIR)
	$(PYTHON) -m autopep8 --in-place --aggressive --recursive $(SRC_DIR)

check: lint test
