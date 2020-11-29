
all: build

build: venv

VENV_DIR := .virtualenv
PYTHON := $(VENV_DIR)/bin/python3

PY_REQUIREMENTS := $(wildcard requirements*.txt)
$(VENV_DIR)/marker: $(PY_REQUIREMENTS)
	python3 -m venv $(@D)
	./$(@D)/bin/pip install --upgrade setuptools pip
	echo "$(PY_REQUIREMENTS)" | xargs -n 1 ./$(@D)/bin/pip install -r
	touch $@
venv: $(VENV_DIR)/marker

clean:
	rm -rf $(VENV_DIR)
	find apps -type d -name '__pycache__' -delete
	rm -f db.sqlite3

migrate:
	$(PYTHON) manage.py migrate

runserver: venv migrate
	$(PYTHON) manage.py runserver

format: venv
	find apps -type f -name '*.py' | xargs ./$(VENV_DIR)/bin/yapf -i


.PHONY: all build venv clean migrate runserver

