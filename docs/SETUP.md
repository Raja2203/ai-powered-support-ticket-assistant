# AI-Powered Support Ticket Assistant

## Development Setup Guide

---

## 1. Document Information

| Field           | Value                               |
| --------------- | ----------------------------------- |
| Project Name    | AI-Powered Support Ticket Assistant |
| Document Type   | Development Setup Guide             |
| Document Status | Draft                               |
| Version         | 1.0                                 |
| Author          | Raja Rangarao Moturi                |
| Last Updated    | 2026-07-26                          |

---

## 2. Purpose

This document explains how a developer can prepare, configure, and verify the AI-Powered Support Ticket Assistant in a local development environment.

It covers:

* required software
* repository setup
* project directory structure
* environment-variable configuration
* backend setup
* frontend setup
* PostgreSQL setup
* AI-provider configuration
* Docker setup
* local verification
* common setup problems
* cleanup and reset procedures

This guide should allow another developer to run the project without relying on undocumented local knowledge.

---

## 3. Supported Development Environment

The project is designed to support:

* Windows
* macOS
* Linux

The primary development environment may use Windows, but project setup should remain portable across supported operating systems.

Docker-based setup is the recommended approach for consistent multi-service execution.

Direct local execution should also remain available for learning and debugging.

---

## 4. Required Software

Before setting up the project, install the following tools.

| Tool                            | Purpose                              |    Required |
| ------------------------------- | ------------------------------------ | ----------: |
| Git                             | Source control                       |         Yes |
| Python                          | Backend development                  |         Yes |
| Node.js                         | React frontend development           |         Yes |
| npm                             | Frontend package management          |         Yes |
| PostgreSQL                      | Local database when not using Docker |    Optional |
| Docker Desktop or Docker Engine | Container execution                  | Recommended |
| Docker Compose                  | Multi-service local environment      | Recommended |
| Code editor                     | Development                          |         Yes |
| Postman                         | Manual API testing                   |    Optional |
| PostgreSQL client               | Database inspection                  |    Optional |

Recommended editors include:

* Visual Studio Code
* PyCharm
* IntelliJ IDEA with Python support

---

## 5. Recommended Versions

The project should define supported versions before implementation.

Suggested baseline:

| Tool           | Recommended Version                      |
| -------------- | ---------------------------------------- |
| Python         | 3.12 or later supported project version  |
| Node.js        | Current active Long-Term Support version |
| npm            | Version included with selected Node.js   |
| PostgreSQL     | 16 or later supported project version    |
| Docker         | Recent stable release                    |
| Docker Compose | Compose V2                               |
| Git            | Recent stable release                    |

Exact versions should later be pinned in:

* backend dependency configuration
* frontend package configuration
* Dockerfiles
* CI workflows

---

## 6. Repository Structure

The planned repository structure is:

```text
ai-powered-support-ticket-assistant/
├── .github/
│   ├── workflows/
│   ├── ISSUE_TEMPLATE/
│   └── pull_request_template.md
│
├── docs/
│   ├── adr/
│   ├── README.md
│   ├── PROBLEM_DEFINITION.md
│   ├── REQUIREMENTS.md
│   ├── HLD.md
│   ├── LLD.md
│   ├── API_SPEC.md
│   ├── TESTING.md
│   ├── SECURITY.md
│   ├── SETUP.md
│   └── DEPLOYMENT.md
│
├── src/
│   ├── backend/
│   └── frontend/
│
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Makefile
├── README.md
└── LICENSE
```

The structure may evolve during implementation, but documentation, backend, frontend, tests, and automation should remain clearly separated.

---

## 7. Repository Setup

### 7.1 Clone the Repository

The developer should:

1. Copy the repository URL from GitHub.
2. Clone the repository to a local workspace.
3. Open the project root directory.
4. confirm that the correct default branch is checked out.

### 7.2 Branch Strategy

The project uses:

* `main` for stable code
* `develop` for integrated development
* `feature/*` for individual features
* `bugfix/*` for defect corrections
* `docs/*` for larger documentation changes when needed

New application features should normally begin from the latest `develop` branch.

### 7.3 Repository Verification

After cloning, verify that the repository contains:

* root `README.md`
* `docs/`
* `src/backend/`
* `src/frontend/`
* `.env.example`
* `.gitignore`
* `docker-compose.yml`
* `.github/workflows/`

Some implementation files may not exist during the documentation phase.

---

## 8. Environment Configuration Strategy

The project uses environment variables for runtime configuration.

Environment-specific configuration must not be hardcoded into application source files.

### 8.1 Root Environment Template

The root `.env.example` may describe shared Docker Compose values such as:

* application environment
* backend port
* frontend port
* PostgreSQL host
* PostgreSQL port
* PostgreSQL database name
* PostgreSQL username
* PostgreSQL password placeholder

### 8.2 Backend Environment Template

The backend `.env.example` may include:

* application name
* application version
* environment
* debug setting
* API prefix
* backend host
* backend port
* database URL
* database pool configuration
* AI provider name
* AI API key placeholder
* AI model name
* AI timeout
* AI retry limit
* prompt version
* allowed frontend origins
* log level
* default page size
* maximum page size

### 8.3 Frontend Environment Template

The frontend `.env.example` may include:

* backend API base URL
* frontend environment
* application display name
* optional public feature flags

Frontend environment variables must not contain private credentials.

---

## 9. Local Environment File Rules

Each developer may create local environment files based on the provided examples.

Local environment files:

* must not be committed
* must contain development-only values
* must not contain production secrets
* must not be shared through screenshots or chat
* should use different credentials from production

The `.gitignore` file should exclude local environment files.

---

# 10. Backend Setup

## 10.1 Backend Location

The backend application will be located under:

```text
src/backend/
```

## 10.2 Virtual Environment

A dedicated Python virtual environment should be created for the backend.

The virtual environment should:

* isolate project dependencies
* avoid using global Python packages
* use the project-supported Python version
* remain excluded from Git

Common virtual-environment directory names include:

* `.venv`
* `venv`

The project should select one naming convention and use it consistently.

## 10.3 Backend Dependencies

Backend dependencies will be defined in the backend dependency file.

Expected dependency categories include:

* FastAPI framework
* ASGI server
* SQLAlchemy
* PostgreSQL driver
* Pydantic settings
* AI-provider client
* database migration tool
* testing tools
* linting and formatting tools

Dependencies should be added only when required.

## 10.4 Backend Application Configuration

Before starting the backend, verify:

* Python virtual environment is active
* dependencies are installed
* backend environment file exists
* database configuration is valid
* AI configuration is available when AI endpoints are tested
* frontend origin is configured
* required directories exist

## 10.5 Backend Startup Expectations

The backend should eventually expose:

* health endpoint
* readiness endpoint
* OpenAPI specification
* Swagger UI
* ReDoc
* versioned ticket APIs

The health endpoint should work even when the database is unavailable.

The readiness endpoint should confirm database connectivity.

---

# 11. Frontend Setup

## 11.1 Frontend Location

The React application will be located under:

```text
src/frontend/
```

## 11.2 Frontend Tooling

The frontend will use:

* React.js
* a lightweight development build tool such as Vite
* npm for dependency management

The exact frontend test and styling tools will be selected during frontend implementation.

## 11.3 Frontend Dependencies

Expected dependency categories include:

* React
* React DOM
* client-side routing
* API communication
* frontend testing
* linting
* optional UI styling tools

A global state-management library should not be added during the initial setup unless a real requirement exists.

## 11.4 Frontend Environment Configuration

The frontend should know only the backend API base URL and other non-secret public configuration.

The frontend must not receive:

* database credentials
* AI API keys
* backend secrets
* cloud credentials

## 11.5 Frontend Startup Expectations

The frontend should eventually provide:

* ticket-creation page
* ticket-list page
* ticket-details page
* AI-analysis panel
* error page
* loading and empty states

During initial setup, a placeholder page is sufficient to confirm the application starts successfully.

---

# 12. PostgreSQL Setup

The project supports two PostgreSQL setup approaches:

1. Docker-based PostgreSQL
2. Locally installed PostgreSQL

The Docker-based approach is recommended for consistency.

---

## 13. Docker-Based PostgreSQL

Docker Compose should define a PostgreSQL service with:

* database name
* database user
* database password
* internal service hostname
* port mapping
* named data volume
* health check

The backend container should connect using the Docker service name rather than `localhost`.

The host machine may connect using the exposed local PostgreSQL port.

---

## 14. Locally Installed PostgreSQL

When PostgreSQL is installed directly on the developer machine, verify:

* PostgreSQL service is running
* required database exists
* required user exists
* password is correct
* local port is available
* application user has required permissions
* backend connection URL uses the correct host

A separate database should be used for:

* local development
* automated testing

The development database must not also serve as the test database.

---

## 15. Database Naming Convention

Suggested database names:

| Environment               | Database Name                |
| ------------------------- | ---------------------------- |
| Local development         | `support_ticket_dev`         |
| Automated testing         | `support_ticket_test`        |
| Future shared development | `support_ticket_development` |
| Future production         | Environment-managed name     |

The exact names may change, but each environment should remain isolated.

---

## 16. Database Schema Management

The project will use Alembic as the authoritative migration mechanism.

Database setup should eventually include:

1. Confirm PostgreSQL is running.
2. Confirm the target database exists.
3. Load backend environment settings.
4. Apply all pending migrations.
5. Verify the tickets table and required indexes exist.

The project may also contain `schema.sql` as a learning reference, but migration files should control actual schema evolution.

---

# 17. AI Provider Setup

## 17.1 AI Provider Selection

The exact AI provider will be selected through a separate architecture decision.

The MVP will use one external provider.

## 17.2 Required AI Configuration

Expected AI settings include:

* provider name
* API key
* model name
* request timeout
* retry limit
* prompt version

## 17.3 AI Key Rules

The AI API key:

* belongs only in backend configuration
* must not be committed
* must not be included in frontend files
* must not be printed in logs
* should be rotated if exposed

## 17.4 Running Without AI Configuration

Basic ticket-management functionality should remain usable without an AI provider.

Without valid AI configuration:

* health check should still work
* ticket creation should still work
* ticket retrieval should still work
* ticket updates should still work
* AI-analysis requests should return a controlled configuration error

---

# 18. Docker Setup

## 18.1 Docker Services

The planned Docker Compose environment includes:

* PostgreSQL
* FastAPI backend
* React frontend

Redis is not part of the MVP.

## 18.2 Expected Local Ports

| Service    | Default Local Port |
| ---------- | -----------------: |
| Frontend   |             `3000` |
| Backend    |             `8000` |
| PostgreSQL |             `5432` |

Port values should remain configurable.

## 18.3 Docker Volumes

A named volume should be used for PostgreSQL data.

This allows database data to remain available after containers stop or restart.

Source-code mounts may be used for local development where appropriate.

## 18.4 Docker Networking

Docker Compose should create an internal network where:

* frontend communicates with backend
* backend communicates with PostgreSQL
* PostgreSQL is not treated as an external public service

The backend should use the PostgreSQL service name as the host inside the Docker network.

## 18.5 Service Readiness

Container startup order does not guarantee service readiness.

The setup should include:

* PostgreSQL health check
* backend connection retry handling
* backend readiness endpoint
* frontend error handling when backend is unavailable

---

# 19. Local Setup Approaches

The project should support two development approaches.

## 19.1 Fully Containerized Setup

Services run through Docker Compose:

* frontend container
* backend container
* PostgreSQL container

Recommended for:

* reproducible setup
* onboarding
* environment verification
* portfolio demonstration

## 19.2 Hybrid Local Setup

Possible hybrid approach:

* frontend runs locally
* backend runs locally
* PostgreSQL runs in Docker

Recommended for:

* faster debugging
* easier hot reload
* learning individual tools

Both approaches should use consistent environment values and database migrations.

---

# 20. Initial Setup Sequence

The recommended first-time setup sequence is:

1. Install required tools.
2. Clone the repository.
3. Review root documentation.
4. Create local environment files from examples.
5. Configure development database credentials.
6. Configure optional AI credentials.
7. Prepare backend virtual environment.
8. Install backend dependencies.
9. Install frontend dependencies.
10. Start PostgreSQL.
11. Apply database migrations.
12. Start the backend.
13. verify the health endpoint.
14. Verify the readiness endpoint.
15. Start the frontend.
16. Verify frontend-to-backend communication.
17. Run automated tests.
18. Run lint checks.

---

# 21. Backend Verification

The backend setup is successful when:

* the application starts without configuration errors
* health endpoint returns `200`
* readiness endpoint returns `200`
* Swagger UI is available
* OpenAPI specification is generated
* application logs show successful startup
* no secrets are printed
* database connectivity succeeds

Expected local backend URL:

```text
http://localhost:8000
```

Expected development documentation locations:

```text
http://localhost:8000/docs
http://localhost:8000/redoc
http://localhost:8000/openapi.json
```

---

# 22. Frontend Verification

The frontend setup is successful when:

* development server starts
* application loads in the browser
* no build errors appear
* backend URL is loaded from environment configuration
* frontend can call the health or ticket API
* errors are displayed clearly when backend is unavailable
* browser console contains no exposed secrets

Expected local frontend URL:

```text
http://localhost:3000
```

---

# 23. PostgreSQL Verification

Database setup is successful when:

* PostgreSQL service is running
* development database exists
* application user can connect
* migrations complete successfully
* expected tables exist
* backend readiness check reports database as ready
* ticket records can be persisted later

A database client may be used for verification, but application migrations remain the source of truth.

---

# 24. AI Integration Verification

AI setup is successful when:

* backend recognizes the selected provider
* API key is available only to the backend
* configured model exists
* analysis request completes
* structured response is returned
* invalid output is rejected
* model and prompt version are recorded
* no secret appears in logs or responses

Live AI verification should use synthetic ticket content.

---

# 25. Automated Test Verification

The setup should support:

* backend unit tests
* backend integration tests
* repository tests
* mocked AI tests
* frontend component tests
* frontend integration tests

Before using the test suite, verify:

* test database configuration is separate
* test environment variables are available
* live AI calls are disabled by default
* test data is synthetic
* test cleanup works correctly

---

# 26. Linting and Formatting Verification

The project should define automated checks for:

* Python linting
* Python formatting
* import organization
* optional Python type checking
* JavaScript or TypeScript linting
* frontend formatting

The same checks should run:

* locally
* in CI

Developers should run checks before opening a pull request.

---

# 27. Makefile or Command Shortcut Strategy

The root Makefile may provide shortcuts for common tasks such as:

* setup
* start
* stop
* restart
* test
* lint
* format
* migrate
* create migration
* view logs
* clean

Makefile commands are convenience wrappers.

The underlying setup process should still be documented so developers understand what each command performs.

On Windows, developers may use compatible tooling or equivalent task scripts when traditional Make is unavailable.

---

# 28. Git Hooks

Local Git hooks are optional for the MVP.

Future hooks may run:

* formatting
* linting
* selected unit tests
* secret scanning

Git hooks should not replace CI because developers can bypass local hooks.

---

# 29. Common Setup Problems

## 29.1 Python Command Uses the Wrong Installation

Symptoms:

* package imports fail
* virtual environment is not active
* dependencies install globally
* editor reports unresolved imports

Checks:

* verify active Python path
* confirm virtual environment activation
* confirm editor interpreter selection
* reinstall dependencies inside the virtual environment

## 29.2 Backend Cannot Connect to PostgreSQL

Possible causes:

* PostgreSQL is not running
* incorrect host
* incorrect port
* invalid credentials
* database does not exist
* Docker service is not healthy
* backend uses `localhost` from inside a container

Checks:

* confirm database service status
* confirm environment values
* verify database name and user
* verify Docker service hostname
* review readiness response
* review sanitized backend logs

## 29.3 Frontend Cannot Reach Backend

Possible causes:

* backend is not running
* incorrect API base URL
* CORS is not configured
* wrong backend port
* Docker network configuration is incorrect

Checks:

* open backend health endpoint directly
* review frontend environment file
* verify allowed frontend origin
* inspect browser network requests
* review backend logs

## 29.4 AI Analysis Fails

Possible causes:

* missing API key
* invalid API key
* model unavailable
* provider rate limit
* provider outage
* timeout
* invalid structured output

Checks:

* verify backend AI configuration
* confirm selected model
* review controlled error code
* review sanitized logs
* retry using synthetic ticket data

## 29.5 Docker Container Stops Immediately

Possible causes:

* missing environment variable
* startup command failure
* dependency installation failure
* port conflict
* database connection failure

Checks:

* inspect container logs
* confirm environment file
* verify ports
* verify Dockerfile configuration
* confirm database health

## 29.6 Port Already in Use

Potential conflicts:

* frontend port `3000`
* backend port `8000`
* PostgreSQL port `5432`

Resolution:

* stop the conflicting process
* change the local port mapping
* update environment configuration
* keep internal service ports consistent where practical

## 29.7 Database Migration Fails

Possible causes:

* incorrect database URL
* missing database
* migration history mismatch
* insufficient database permissions
* conflicting manual schema changes

Checks:

* confirm target database
* inspect migration status
* avoid manually editing migration-managed tables
* restore the local database when safe
* create a corrective migration instead of editing applied history

---

# 30. Resetting the Local Environment

Resetting may be required when:

* database schema becomes inconsistent
* local test data is no longer useful
* Docker volumes contain invalid development state
* migrations are being tested from a clean environment

A reset may involve:

* stopping services
* removing development containers
* removing the local development database volume
* recreating the database
* applying migrations again
* reinstalling dependencies when necessary

Resetting the database permanently deletes local development data.

Only synthetic or disposable development data should be present.

---

# 31. Cleaning Generated Files

Generated or local-only files may include:

* Python cache directories
* test coverage output
* frontend build output
* frontend dependency directory
* local virtual environment
* local logs
* local environment files
* temporary database data
* editor-specific settings

The project should ignore these files where appropriate.

Cleanup should not remove:

* migration files
* source code
* documentation
* committed configuration templates
* test fixtures required by the project

---

# 32. Developer Workflow After Setup

A normal development workflow should be:

1. Update the local `develop` branch.
2. Create a feature branch.
3. Start required local services.
4. Apply pending migrations.
5. Implement one focused change.
6. Add or update tests.
7. Run tests locally.
8. Run lint and formatting checks.
9. Update documentation.
10. Commit with a meaningful message.
11. Push the branch.
12. Open a pull request.
13. Resolve CI failures.
14. Review the change.
15. Merge only after required checks pass.

---

# 33. Setup Security Checklist

Before running the application:

* [ ] Local `.env` files are excluded from Git
* [ ] AI key is not present in frontend configuration
* [ ] Database password is not hardcoded
* [ ] Production credentials are not used locally
* [ ] Only synthetic test data is used
* [ ] CORS allows only required local origins
* [ ] Debug settings are appropriate for local development
* [ ] Logs do not print credentials
* [ ] Docker Compose does not contain real secrets
* [ ] Repository history contains no exposed credentials

---

# 34. Setup Completion Checklist

## Repository

* [ ] Repository cloned
* [ ] Correct branch checked out
* [ ] Documentation reviewed
* [ ] Local environment files created
* [ ] Secrets remain uncommitted

## Backend

* [ ] Supported Python version installed
* [ ] Virtual environment created
* [ ] Virtual environment activated
* [ ] Backend dependencies installed
* [ ] Backend environment configured
* [ ] Backend application starts
* [ ] Health endpoint returns `200`
* [ ] Swagger UI loads

## Database

* [ ] PostgreSQL starts
* [ ] Development database exists
* [ ] Test database exists
* [ ] Application user can connect
* [ ] Migrations complete
* [ ] Readiness endpoint returns `200`

## Frontend

* [ ] Supported Node.js version installed
* [ ] Frontend dependencies installed
* [ ] Frontend environment configured
* [ ] Frontend starts
* [ ] Browser application loads
* [ ] Frontend reaches backend

## AI

* [ ] AI provider selected
* [ ] AI key configured in backend only
* [ ] AI model configured
* [ ] Synthetic analysis request succeeds
* [ ] Invalid AI output is handled safely

## Quality

* [ ] Backend tests pass
* [ ] Frontend tests pass
* [ ] Backend lint checks pass
* [ ] Frontend lint checks pass
* [ ] Docker Compose starts all required services
* [ ] No secrets are committed

---

# 35. Open Setup Decisions

The following items should be finalized during implementation:

* Exact supported Python version
* Exact supported Node.js version
* Exact PostgreSQL version
* Backend dependency-management format
* Frontend package manager
* Selected AI provider
* Selected AI model
* Backend linting tools
* Frontend testing tools
* End-to-end testing tool
* Whether Makefile support is sufficient for Windows
* Whether local HTTPS is required
* Whether the frontend runs in Docker during normal development
* Whether PostgreSQL is exposed to the host by default

---

# 36. Related Documents

| Document               | Location                     |
| ---------------------- | ---------------------------- |
| Problem Definition     | `docs/PROBLEM_DEFINITION.md` |
| Requirements           | `docs/REQUIREMENTS.md`       |
| High-Level Design      | `docs/HLD.md`                |
| Low-Level Design       | `docs/LLD.md`                |
| API Specification      | `docs/API_SPEC.md`           |
| Testing Strategy       | `docs/TESTING.md`            |
| Security Guidelines    | `docs/SECURITY.md`           |
| Architecture Decisions | `docs/adr/`                  |
| Deployment Guide       | `docs/DEPLOYMENT.md`         |
| Root Project Overview  | `README.md`                  |

---

# 37. Document History

| Version | Date       | Author               | Description                     |
| ------- | ---------- | -------------------- | ------------------------------- |
| 1.0     | 2026-07-26 | Raja Rangarao Moturi | Initial development setup guide |
