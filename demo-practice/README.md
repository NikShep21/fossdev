# Demo Practice

## Description of the work

This work implements automation of typical development tasks for a Python project using a `Makefile`.

`Make` is used as a single entry point for the main operations: creating a virtual environment, installing dependencies, running the application, testing, type checking, formatting, linting, and dependency validation.

The main idea of the solution is not to run commands manually one by one and not to rely on an activated shell environment, but to execute everything through explicit commands defined in the `Makefile`.

## What is implemented

The project includes the following parts of the assignment:

- creation of a local virtual environment in `.venv`;
- installation of dependencies from `requirements.txt` into that environment;
- running the application through the interpreter from `.venv`;
- test execution;
- static type checking;
- code formatting;
- style checking;
- automated validation of imports against declared dependencies;
- a composite `check` target that combines several checks.

## Project structure

```text
demo-practice/
├── docs/
│   └── DOMAIN.md
├── scripts/
│   └── check_requirements.py
├── src/
│   ├── app.py
│   ├── calc.py
│   └── service.py
├── tests/
│   └── test_calc.py
├── .gitignore
├── Makefile
├── README.md
└── requirements.txt
```

## Make targets

The project uses the following targets:

- `make venv` — create the local virtual environment;
- `make install` — install dependencies into `.venv`;
- `make run` — run the application;
- `make test` — run tests;
- `make typecheck` — run static type checking;
- `make format` — format the code;
- `make lint` — run style checks;
- `make check-requirements` — validate imports against declared dependencies;
- `make check` — run the main validation chain.

## Dependency validation

Dependency validation is implemented through `scripts/check_requirements.py`.

The script analyzes imports used in the source code and compares them with dependencies listed in `requirements.txt`. It reports missing packages and also shows possibly unused declared dependencies.

## How to run

Typical workflow:

```bash
make venv
make install
make check
```
