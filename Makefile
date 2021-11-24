# Makefile.
#
# This is intended for convenience.
# All commands should be usable even without make.

# --- Variables

ROOT := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))

PROJECT := vanadium

PIP_REQ_MAIN := requirements.txt
PIP_REQ_DEV  := requirements-dev.txt

DOCKER_TAG  := $(PROJECT)
DOCKER_APP  := $(PROJECT)-app
DOCKER_HOST := localhost
DOCKER_PORT := 8080

MKDOCS_SITE_PATH      := $(ROOT)/build/docs
MKDOCS_SERVER_HOST    := localhost
MKDOCS_SERVER_PORT    := 8001
MKDOCS_SERVER_ADDRESS := $(MKDOCS_SERVER_HOST):$(MKDOCS_SERVER_PORT)

SERVER_APP_PATH   := $(ROOT)
SERVER_APP_NAME   := $(PROJECT).app.main:application
SERVER_HOST       := 127.0.0.1
SERVER_PORT       := 8080
SERVER_MAIN_FLAGS := --host $(SERVER_HOST) --port $(SERVER_PORT) $(SERVER_APP_NAME)
SERVER_TEST_FLAGS := --reload $(SERVER_MAIN_FLAGS)

SERVER_APP_PATH   := $(ROOT)
SERVER_APP_ENTRY  := $(PROJECT).app.main:application
SERVER_HOST       := 127.0.0.1
SERVER_PORT       := 8080
# Note: '--factory' needed because app entry is a factory function not an instance/
SERVER_MAIN_FLAGS := --host $(SERVER_HOST) --port $(SERVER_PORT) --factory
SERVER_TEST_FLAGS := $(SERVER_MAIN_FLAGS) --reload

COVERAGE_CONF := $(ROOT)/.coveragerc
COVERAGE_DATA := $(shell grep -E "datafile =" $(COVERAGE_CONF) | cut -d ' ' -f 3)

# --- Rules

help:
	@echo "Make targets:"
	@echo ""
	@echo "Project builds:"
	@echo ""
	@echo "  Notes:"
	@echo "  - These commands need an active virtualenv and use Poetry."
	@echo "    There are Pip equivalents but they are not make targets."
	@echo ""
	@echo "  install     - Install non-dev dependencies and main package"
	@echo "  develop     - Install all dependencies and main package"
	@echo "  depends     - Install all dependencies without the main package"
	@echo ""
	@echo "  build       - Build all distributable Python packages"
	@echo "  build-sdist - Build project as source tarball"
	@echo "  build-wheel - Build project as wheel"
	@echo ""
	@echo "  clean       - Remove all built Python packages"
	@echo "  clean-sdist - Remove built tarballs"
	@echo "  clean-wheel - Remove built wheels"
	@echo ""
	@echo "  docs         - Rebuild all documentation"
	@echo "  docs-changed - Rebuild only changed documentation"
	@echo "  docs-clean   - Remove built documentation"
	@echo "  docs-serve   - Run a local mkdocs server"
	@echo ""
	@echo "Pip requirements:"
	@echo ""
	@echo "  pip-requirements      - Export Pip requirements files with hashes"
	@echo "  pip-requirements-base - Export Pip requirements files without hashes"
	@echo ""
	@echo "Docker image:"
	@echo ""
	@echo "  docker-build       - Build Docker image from Dockerfile"
	@echo "  docker-run         - Run Docker container"
	@echo ""
	@echo "PyTest: common commands"
	@echo ""
	@echo "  test-all           - Run all test cases"
	@echo "  test-one           - Run until first failing case"
	@echo "  test-debug         - Run debugger if any cases fail"
	@echo ""
	@echo "Coverage:"
	@echo ""
	@echo "  cover-test         - Run coverage over pytest"
	@echo "  cover-report       - Generate text report of coverage"
	@echo "                       Skips files with complete coverage"
	@echo "  cover-report-full  - Generate full text report of coverage"
	@echo "  cover-html         - Generate HTML report of coverage"
	@echo "                       Skips files with complete coverage"
	@echo "  cover-html-full    - Generate full HTML report of coverage"
	@echo "  cover-clean        - Clear out existing coverage data"
	@echo "  cover-redo         - Clear out existing data and run tests again"
	@echo ""
	@echo "Uvicorn server"
	@echo ""
	@echo "  serve              - Run uvicorn server, simulating prodction"
	@echo "  serve-test         - Run uvicorn server for development"
	@echo "                       Automatically reloads when source changes"
	@echo ""


# Project builds

install:
	poetry install --no-dev

develop:
	poetry install

depends:
	poetry install --no-root

build: build-sdist build-wheel

clean: clean-sdist clean-wheel

build-sdist:
	poetry build -f sdist

clean-sdist:
	rm -f dist/$(PROJECT)*.tar.gz
	rmdir --ignore-fail-on-non-empty dist

build-wheel:
	poetry build -f wheel

clean-wheel:
	rm -f dist/$(PROJECT)*.whl
	rmdir --ignore-fail-on-non-empty dist


# Doc builds

docs: $(MKDOCS_SITE_PATH)
	poetry run mkdocs build -d $(MKDOCS_SITE_PATH)

docs-changed: $(MKDOCS_SITE_PATH)
	poetry run mkdocs build --dirty -d $(MKDOCS_SITE_PATH)

docs-clean:
	rm -rf $(MKDOCS_SITE_PATH)

docs-serve:
	poetry run mkdocs serve -a $(MKDOCS_SERVER_ADDRESS)

$(MKDOCS_SITE_PATH):
	mkdir -p $@

.PHONY: docs docs-changed docs-clean


# Pip requirements

pip-requirements:
	poetry export -f requirements.txt > $(PIP_REQ_MAIN)
	poetry export --dev -f requirements.txt > $(PIP_REQ_DEV)

pip-requirements-base:
	poetry export --without-hashes -f requirements.txt > $(PIP_REQ_MAIN)
	poetry export --without-hashes --dev -f requirements.txt > $(PIP_REQ_DEV)


# Docker

docker-build:
	docker build -t "$(DOCKER_TAG)" .

docker-run:
	docker run -it --rm --name "$(DOCKER_APP)" -p "$(DOCKER_PORT):$(DOCKER_PORT)" "$(DOCKER_TAG)"


# PyTest

test-all:
	poetry run pytest

test-one:
	poetry run pytest -x

test-debug:
	poetry run pytest -x --pdb


# PyTest + Coverage

cover-test:
	poetry run coverage run -m pytest

cover-report: $(COVERAGE_DATA)
	poetry run coverage report --skip-covered --skip-empty

cover-report-full: $(COVERAGE_DATA)
	poetry run coverage report

cover-html: $(COVERAGE_DATA)
	poetry run coverage html --skip-covered --skip-empty

cover-html-full: $(COVERAGE_DATA)
	poetry run coverage html

cover-clean:
	poetry run coverage erase

cover-redo: cover-clean cover-test


# Uvicorn

serve:
	poetry run uvicorn $(SERVER_MAIN_FLAGS) $(SERVER_APP_ENTRY)

serve-test:
	poetry run uvicorn $(SERVER_TEST_FLAGS) $(SERVER_APP_ENTRY)
