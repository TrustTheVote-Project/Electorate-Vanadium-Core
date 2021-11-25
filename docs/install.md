# Installation

## Requirements

You will need the following software installed:

- [Git](https://git-scm.com). This is part of almost every Linux distribution, but if you don't have it you can [download it for any platform](https://git-scm.com/downloads).
- [Poetry](https://python-poetry.org). Follow the [installations instructions](https://python-poetry.org/docs/#installation) and get the [installation script](https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py). Read about[how to use Poetry](https://python-poetry.org/docs/basic-usage/)

    Note: It is recommended that you **not** pipe the installation script directly to a shell. Download and verify it, and then run it.

- [Docker](https://docs.docker.com). You can [download it for any platform](https://docs.docker.com/get-docker).

### Optional

- [Make](https://gnu.org/software/make) comes with almost every Linux distribution, and MacOS. You don't strictly needed it: it's used for conveniently invoking common build steps. If you don't have it, you can explicitly run each command it calls by looking in the Makefile. You can also see what the most common commands under [Build System](development/build-system.md).

## Initial Setup

Clone the repository

```bash
    git clone https://github.com/TrustTheVote-Project/electorate-vanadium-core
    cd electorate-vanadium-core
```

Create a virtual environment.

```bash
    poetry shell
```

## Deployment

Vanadium is intended to be deployed as as Docker image. To run it:

Start the virtual environment if you haven't already:

```bash
    poetry shell
```

Install the production environment (no development dependencies):

```bash
    make install
```

Create the Docker image

```bash
    make build-docker
```

Run the Docker image

```bash
    make run-docker
```

## Development

For development you can install the development environment (with development dependencies):

```bash
    make develop
```

You can rebuild the Docker image but you may want to test things out without going through the step of using Docker. In that case you can run a local server:

```bash
    make serve
```

Run the server with live updates for incremental testing:

```bash
    make serve-test
```

## Testing

Run the unit tests:

```bash
    make test-all
```

Run the unit tests stopping on the first error.

```bash
    make test-one
```

Run the unit tests dropping into the debugger on the first error.

```bash
    make test-debug
```

## Documentation

Rebuild all the documentation. This generates all the documentation in `build/docs`.

```bash
    make docs
```

View the documentation from a local server, with live updates.

```bash
    make docs-serve
```
