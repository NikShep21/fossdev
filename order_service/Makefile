APP = app.main:app
APP_DIR = src
HOST ?= 127.0.0.1
PORT ?= 8000

PRODUCT_HOST ?= 127.0.0.1
PRODUCT_PORT ?= 8001
PRODUCT_SERVICE_URL ?= http://$(PRODUCT_HOST):$(PRODUCT_PORT)

.PHONY: install dev run health

install:
	poetry install

dev:
	PRODUCT_SERVICE_URL=$(PRODUCT_SERVICE_URL) poetry run uvicorn $(APP) --app-dir $(APP_DIR) --reload --host $(HOST) --port $(PORT)

run:
	PRODUCT_SERVICE_URL=$(PRODUCT_SERVICE_URL) poetry run uvicorn $(APP) --app-dir $(APP_DIR) --host $(HOST) --port $(PORT)

health:
	curl http://$(HOST):$(PORT)/health
