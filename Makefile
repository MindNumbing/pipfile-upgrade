.PHONY: help

default: help

run: ## run the python program
	python -m pipfile_upgrade

dry-run: ## run the python program without making changes
	python -m pipfile_upgrade --dry-run

test: ## test the python program
	python -m pytest

lint: ## lint the python program
	black . && isort . && mypy --strict . && flake8 . && vulture .

help: ## show this help
	@echo
	@fgrep -h " ## " $(MAKEFILE_LIST) | fgrep -v fgrep | sed -Ee 's/([a-z.]*):[^#]*##(.*)/\1##\2/' | column -t -s "##"
	@echo
