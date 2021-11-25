# Build System

Building Vanadium requires that you have Poetry installed.
See: <https://python-poetry.org/docs/#installation>

If you cannot or do not want to install Poetry you can use `pip install -e` and `virtualenv` with the provided `requirements.txt` files.

- Note that the `requirements*.txt` files are provided for production builds that cannot run with Poetry for some reason. They are not intended for development and edits made to them can be overridden by future changes to the Poetry files. The authoritative list of dependencies are in the `[poetry.dependencies]` and `[poetry.dev-dependencies]` sections of `pyproject.toml`.

A `Makefile` is provided for with targets for convenient access to common tasks. If you have `make` installed you may find using it to be simpler but there is no requirement to use it instead of the associated commands directly.`

To see all available commands type `make help`.

## Building

| Action | Make | Poetry |
| ------ | ---- | ------ |
| Create production environment + install dependencies | `make install` | `poetry install --no-dev` |
| Create development environment + install dependencies | `make develop` | `poetry install` |
| Activate virtual environment | N/A | `poetry shell` [^poetry-shell]|
| Deactivate virtual environment | N/A | `exit` |

[^poetry-shell]: Unlike `source .venv/bin/activate` use of `poetry shell` creates a subshell. There is no `deactivate`.


## Testing

Unit testing is done with `pytest`.

- If you activate the virtual environment you can use `pytest` commands directly.
- If you want to run tests without activating the virtual environment use `poetry run pytest ` with the same arguments you pass to `pytest`.

| Action | Make | Poetry |
| ------ | ---- | ------ |
| Run all tests showing all failures | `make test-all` | `poetry run pytest` |
| Run all tests stopping on first failure | `make test-one` | `poetry run pytest -x` |
| Run all tests dropping into debugger on failure | `make test-debug` | `poetry run pytest -x --pdb` |


## Coverage

- If you activate the virtual environment you can use `coverage` commands directly.
- If you want to run tests without activating the virtual environment use `poetry run coverage ` with the same arguments you pass to `coverage`.

| Action | Make | Poetry |
| ------ | ---- | ------ |
| Run tests with coverage | `make cover-test` | `poetry run coverage run -m pytest ` |
| Print coverage report | `make cover-report-full` | `poetry run coverage report` |
| Print minimal coverage report | `make cover-report` | `poetry run coverage report --skip--covered --skip-empty` |
| Generate HTML coverage | `make cover-html-full` | `poetry run coverage html` |
| Generate HTML minimal coverage | `make cover-html` | `poetry run coverage html --skip--covered --skip-empty` |


## Documentation

- If you activate the virtual environment you can use `mkdocs` commands directly.
- If you want to run tests without activating the virtual environment use `poetry run mkdocs ` with the same arguments you pass to `mkdocs`.
- The port for the Mkdocs server can be overriden with:

    ```
    make docs-serve MKDOCS_SERVER_PORT={port}
    ```

| Action | Make | Poetry |
| ------ | ---- | ------ |
| Build static documentation | `make docs` | `poetry run mkdocs build -d build/docs` |
| Run live docs server. Live updates as you edit the docs | `make docs-serve` | `poetry run mkdocs serve -a localhost:{port}` |
