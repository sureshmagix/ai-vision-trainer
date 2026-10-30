.PHONY: help install dev-backend dev-frontend dev-worker test test-backend test-frontend test-worker lint format migrate docker-up docker-down

PYTHON ?= python3
NPM ?= npm
export PYTHONPATH := $(CURDIR):$(CURDIR)/backend:$(CURDIR)/worker:$(CURDIR)/shared

help:
	@echo "AI Vision Trainer — Command Automation"
	@echo "---------------------------------------"
	@echo "make install         - Install backend, worker, and frontend dependencies"
	@echo "make dev-backend     - Start FastAPI backend with live reload"
	@echo "make dev-frontend    - Start React Vite frontend"
	@echo "make dev-worker      - Start isolated background worker"
	@echo "make test            - Run all test suites (backend, worker, frontend)"
	@echo "make test-backend    - Run backend pytest suite"
	@echo "make test-worker     - Run worker pytest suite"
	@echo "make test-frontend   - Run frontend vitest suite"
	@echo "make lint            - Run code quality and static checks"
	@echo "make migrate         - Apply database migrations via Alembic"
	@echo "make docker-up       - Launch full stack via Docker Compose"
	@echo "make docker-down     - Stop Docker Compose services"

install:
	@echo "Installing backend and worker dependencies..."
	$(PYTHON) -m pip install -r backend/requirements.txt
	@echo "Installing frontend dependencies..."
	cd frontend && $(NPM) install

dev-backend:
	cd backend && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

dev-frontend:
	cd frontend && $(NPM) run dev

dev-worker:
	cd worker && $(PYTHON) -m tasks.runner

test-backend:
	cd backend && pytest tests/ -v

test-worker:
	cd worker && pytest tests/ -v

test-frontend:
	cd frontend && $(NPM) run test:run

test-monorepo:
	pytest tests/ -v

test: test-backend test-worker test-frontend test-monorepo

lint:
	cd backend && $(PYTHON) -m ruff check app tests || true
	cd frontend && $(NPM) run lint || true

migrate:
	cd backend && alembic upgrade head

docker-up:
	docker compose -f infrastructure/docker-compose.yml up -d --build

docker-down:
	docker compose -f infrastructure/docker-compose.yml down
