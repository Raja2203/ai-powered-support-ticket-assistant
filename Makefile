# --------------------------------------------------
# Project Configuration
# --------------------------------------------------

PROJECT_NAME=ai-powered-support-ticket-assistant
BACKEND_DIR=src/backend
FRONTEND_DIR=src/frontend

PYTHON=python
PIP=pip
NPM=npm
DOCKER_COMPOSE=docker compose

# --------------------------------------------------
# Help
# --------------------------------------------------

.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make setup-backend       Install backend dependencies"
	@echo "  make setup-frontend      Install frontend dependencies"
	@echo "  make setup               Install backend and frontend dependencies"
	@echo "  make backend             Start FastAPI backend locally"
	@echo "  make frontend            Start React frontend locally"
	@echo "  make up                  Start all Docker services"
	@echo "  make down                Stop all Docker services"
	@echo "  make restart             Restart all Docker services"
	@echo "  make build               Build Docker images"
	@echo "  make logs                Display Docker service logs"
	@echo "  make ps                  Display Docker service status"
	@echo "  make test-backend        Run backend tests"
	@echo "  make test-frontend       Run frontend tests"
	@echo "  make test                Run all tests"
	@echo "  make lint-backend        Run backend lint checks"
	@echo "  make lint-frontend       Run frontend lint checks"
	@echo "  make lint                Run all lint checks"
	@echo "  make format-backend      Format backend files"
	@echo "  make format-frontend     Format frontend files"
	@echo "  make format              Format backend and frontend files"
	@echo "  make migrate             Apply database migrations"
	@echo "  make migration           Create a database migration"
	@echo "  make clean               Remove generated files"
	@echo "  make reset               Stop services and delete local volumes"

# --------------------------------------------------
# Setup
# --------------------------------------------------

.PHONY: setup-backend
setup-backend:
	cd $(BACKEND_DIR) && $(PIP) install -r requirements.txt

.PHONY: setup-frontend
setup-frontend:
	cd $(FRONTEND_DIR) && $(NPM) install

.PHONY: setup
setup: setup-backend setup-frontend

# --------------------------------------------------
# Local Development
# --------------------------------------------------

.PHONY: backend
backend:
	cd $(BACKEND_DIR) && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

.PHONY: frontend
frontend:
	cd $(FRONTEND_DIR) && $(NPM) run dev

# --------------------------------------------------
# Docker
# --------------------------------------------------

.PHONY: up
up:
	$(DOCKER_COMPOSE) up -d

.PHONY: down
down:
	$(DOCKER_COMPOSE) down

.PHONY: restart
restart:
	$(DOCKER_COMPOSE) down
	$(DOCKER_COMPOSE) up -d

.PHONY: build
build:
	$(DOCKER_COMPOSE) build

.PHONY: logs
logs:
	$(DOCKER_COMPOSE) logs -f

.PHONY: ps
ps:
	$(DOCKER_COMPOSE) ps

# --------------------------------------------------
# Backend Testing
# --------------------------------------------------

.PHONY: test-backend
test-backend:
	cd $(BACKEND_DIR) && pytest

# --------------------------------------------------
# Frontend Testing
# --------------------------------------------------

.PHONY: test-frontend
test-frontend:
	cd $(FRONTEND_DIR) && $(NPM) test -- --run

.PHONY: test
test: test-backend test-frontend

# --------------------------------------------------
# Backend Linting and Formatting
# --------------------------------------------------

.PHONY: lint-backend
lint-backend:
	cd $(BACKEND_DIR) && ruff check .

.PHONY: format-backend
format-backend:
	cd $(BACKEND_DIR) && ruff format .
	cd $(BACKEND_DIR) && ruff check . --fix

# --------------------------------------------------
# Frontend Linting and Formatting
# --------------------------------------------------

.PHONY: lint-frontend
lint-frontend:
	cd $(FRONTEND_DIR) && $(NPM) run lint

.PHONY: format-frontend
format-frontend:
	cd $(FRONTEND_DIR) && $(NPM) run format

.PHONY: lint
lint: lint-backend lint-frontend

.PHONY: format
format: format-backend format-frontend

# --------------------------------------------------
# Database Migrations
# --------------------------------------------------

.PHONY: migrate
migrate:
	cd $(BACKEND_DIR) && alembic upgrade head

.PHONY: migration
migration:
	@test -n "$(name)" || (echo "Usage: make migration name=\"migration description\"" && exit 1)
	cd $(BACKEND_DIR) && alembic revision --autogenerate -m "$(name)"

# --------------------------------------------------
# Cleanup
# --------------------------------------------------

.PHONY: clean
clean:
	@echo "Removing generated backend files..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type f -name ".coverage" -delete

	@echo "Removing generated frontend files..."
	rm -rf $(FRONTEND_DIR)/dist
	rm -rf $(FRONTEND_DIR)/coverage
	rm -rf $(FRONTEND_DIR)/test-results

# --------------------------------------------------
# Full Local Reset
# --------------------------------------------------

.PHONY: reset
reset:
	$(DOCKER_COMPOSE) down -v --remove-orphans