# to-do-exercise Makefile


SHELL := /bin/bash
HIDE ?= @
VENV ?= env
BIN_DIR ?= $(VENV)/bin/

PYTHON := $(BIN_DIR)python
PYTHON_VER := python3.10

.PHONY: prepare-venv
prepare-venv $(VENV):
	$(HIDE)$(PYTHON_VER) -m venv $(VENV)
	$(HIDE)$(BIN_DIR)pip install --upgrade pip wheel
	$(HIDE)$(BIN_DIR)pip install --upgrade --requirement requirements.txt

.PHONY: run
run:
	$(HIDE)$(PYTHON) main.py

.PHONY: test
test:
	$(HIDE)$(PYTHON) test_main.py
