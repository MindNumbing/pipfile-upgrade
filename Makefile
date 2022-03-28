.PHONY: help

default: help

run: ## run the python program
	python -m pipfile_upgrade

dry-run: ## run the python program without making changes
	python -m pipfile_upgrade --dry-run

test: ## test the python program
	python -m pytest

lint: ## lint the python program
	black . && isort . && mypy . && flake8 . && vulture .

build: ## build the program
	python setup.py build sdist bdist_wheel

clean: ## removes builds and caches
	rm -rf .mypy_cache build/ dist/ *pipfile_upgrade.egg-info*

help: ## show this help
	@echo
	@fgrep -h " ## " $(MAKEFILE_LIST) | fgrep -v fgrep | sed -Ee 's/([a-z.]*):[^#]*##(.*)/\1##\2/' | column -t -s "##"
	@echo
