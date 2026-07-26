# ADR-007: Use Docker Compose for Local Development

---

## 1. Document Information

| Field         | Value                |
| ------------- | -------------------- |
| ADR Number    | ADR-007              |
| Status        | Accepted             |
| Decision Date | 2026-07-26           |
| Author        | Raja Rangarao Moturi |

---

## 2. Context

The application requires multiple local components:

* FastAPI backend
* PostgreSQL database
* frontend application
* environment configuration

Developers should be able to run these services consistently without manually installing and configuring every dependency.

The project also needs a reproducible environment for setup, testing, and portfolio demonstration.

---

## 3. Decision Drivers

* reproducible local setup
* environment consistency
* simplified database startup
* service isolation
* beginner Docker exposure
* easy project onboarding
* one-command startup
* future deployment preparation

---

## 4. Options Considered

### Option 1: Docker Compose

Advantages:

* starts multiple services together
* reproducible configuration
* built-in service networking
* persistent database volumes
* easier onboarding
* useful production-related experience

Disadvantages:

* requires Docker
* volume and networking concepts must be learned
* container startup may hide local debugging details
* Windows file mounting may require attention

### Option 2: Fully Manual Local Setup

Advantages:

* simple application debugging
* no container knowledge required
* direct use of local tools

Disadvantages:

* environment inconsistencies
* PostgreSQL must be installed manually
* setup instructions become longer
* harder for another developer to reproduce

### Option 3: Kubernetes

Advantages:

* advanced orchestration
* production scaling concepts
* health and deployment management

Disadvantages:

* excessive complexity for MVP
* high learning overhead
* unnecessary infrastructure
* not suitable for local beginner setup

### Option 4: Separate Docker Commands

Advantages:

* individual control over containers
* fewer Compose concepts

Disadvantages:

* manual networking
* manual environment coordination
* inconvenient multi-service startup
* harder documentation

---

## 5. Decision

The project will use **Docker Compose** for the local multi-service environment.

The initial Compose environment will include:

* backend
* PostgreSQL
* frontend when frontend development begins

Redis will not be included until the system has a justified caching, rate-limiting, or background-processing requirement.

---

## 6. Rationale

Docker Compose gives the project a repeatable local environment without introducing Kubernetes-level complexity.

Developers will still be allowed to run the backend or frontend directly outside Docker for debugging and learning.

Docker Compose is a supported execution method, not the only possible development method.

---

## 7. Positive Consequences

* consistent service configuration
* easy PostgreSQL startup
* simplified networking
* easier onboarding
* persistent local database storage
* fewer machine-specific setup differences
* practical Docker experience
* foundation for future deployment

---

## 8. Negative Consequences

* Docker must be installed
* container troubleshooting is required
* local file permissions may differ by operating system
* startup order does not guarantee service readiness
* volume behavior must be understood

---

## 9. Compose Design Rules

* PostgreSQL data should use a named volume.
* Secrets must not be embedded in the Compose file.
* Environment variables should come from local environment files or placeholders.
* Backend readiness should consider database availability.
* Service names should be stable.
* Ports should be configurable.
* `depends_on` must not be treated as a complete readiness solution.
* Health checks should be used where appropriate.
* Production secrets must not use development values.

---

## 10. Risks and Mitigations

| Risk                                         | Mitigation                                            |
| -------------------------------------------- | ----------------------------------------------------- |
| Backend starts before PostgreSQL is ready    | Use health checks and connection retry handling       |
| Database data disappears                     | Use named volumes                                     |
| Secrets are committed                        | Use `.env.example` and ignore local `.env` files      |
| Docker setup blocks learning                 | Support direct local execution                        |
| Development and production containers differ | Document environment differences                      |
| Unnecessary services are added               | Require a real use case before adding Redis or queues |

---

## 11. Review Conditions

Review this decision if:

* the application no longer requires multiple local services
* the project adopts a different local development platform
* production orchestration requirements need a separate decision
* Docker becomes unavailable in the target environment

---

## 12. Related Documents

* `docs/HLD.md`
* `docs/SETUP.md`
* `docs/DEPLOYMENT.md`
* `docker-compose.yml`
