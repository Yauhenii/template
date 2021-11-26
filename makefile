.DEFAULT_GOAL := help

venv_path = .venv
activate_path = $(venv_path)/bin/activate
python_path = $(venv_path)/bin/python3.8
black_path = $(venv_path)/bin/black
isort_path = $(venv_path)/bin/isort
app_path = app
main_path = $(app_path)/main.py

.PHONY: help
help:
	@(\
	echo 'use make sync|update|start'; \
	)

.PHONY: sync
sync:
	@(\
	python3.8 -m venv $(venv_path); \
	source $(activate_path); \
	pip install -r requirements.txt; \
	)

.PHONY: update
update:
	@(\
	source $(activate_path); \
	pip install -r requirements.txt; \
	)

.PHONY: start
start:
	@(\
	$(python_path) $(main_path); \
	)

.PHONY: format
format:
	@(\
	$(black_path) $(app_path); \
	$(isort_path) $(app_path); \
	)
