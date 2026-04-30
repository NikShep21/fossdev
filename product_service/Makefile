APP = app.main:app
APP_DIR = src
HOST ?= 127.0.0.1
PORT ?= 8001

.PHONY: install dev run health

install:
	poetry install

dev:
	poetry run uvicorn $(APP) --app-dir $(APP_DIR) --reload --host $(HOST) --port $(PORT)

run:
	poetry run uvicorn $(APP) --app-dir $(APP_DIR) --host $(HOST) --port $(PORT)

health:
	curl http://$(HOST):$(PORT)/health
