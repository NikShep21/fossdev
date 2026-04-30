APP = src.main:app
HOST = 127.0.0.1
PORT = 8000

.PHONY: install dev run test health

install:
	poetry install

dev:
	poetry run uvicorn $(APP) --reload --host $(HOST) --port $(PORT)

run:
	poetry run uvicorn $(APP) --host $(HOST) --port $(PORT)

test:
	poetry run pytest

health:
	curl http://$(HOST):$(PORT)/health
