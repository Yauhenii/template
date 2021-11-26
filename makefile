.DEFAULT_GOAL := help

venv_path = .venv
activate_path = $(venv_path)/bin/activate
python_path = $(venv_path)/bin/python3.8
main_path = app/main.py

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

