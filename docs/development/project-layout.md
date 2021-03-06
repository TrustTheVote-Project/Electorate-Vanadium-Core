# Project Structure

This is the layout of the source.

### Source files

```plaintext
bin/                    # User commands and top-level scripts
docs/
    index.md            # The documentation homepage.
    ...                 # Other markdown pages, images and other files.
src/                    # Source code
    electos/vanadium    # Vanadium package
test/                   # Test code
    vanadium/tests      # Root of Python tests
```

### Generated files

Files and directories generated by the build process, as defined in the `Makefile`. These can be safely deleted, though their contents are not under version control.

```plaintext
build/docs/             # Generated MkDocs documentation
dist/                   # Generated Python build files
```

### Configuration files

```plaintext
Makefile                # High-level interface to other commands

coverage.json           # Coverage configuration
Dockerfile              # Docker startup
mkdocs.yml              # MkDocs configuration
pyproject.toml          # Build system and tool configuration
  poetry.lock           # Pinned list of Python dependencies
pytest.ini              # PyTest configuration
tox.ini                 # Tox configuration
```
