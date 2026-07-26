# ADR-004: Use a Layered Backend Architecture

---

## 1. Document Information

| Field         | Value                |
| ------------- | -------------------- |
| ADR Number    | ADR-004              |
| Status        | Accepted             |
| Decision Date | 2026-07-26           |
| Author        | Raja Rangarao Moturi |

---

## 2. Context

The backend contains multiple responsibilities:

* HTTP request handling
* request validation
* business rules
* database access
* AI-provider communication
* AI-output parsing
* exception handling
* configuration
* logging

Placing all responsibilities inside FastAPI route functions would make the application difficult to test and maintain.

---

## 3. Decision Drivers

* separation of concerns
* testability
* maintainability
* Spring Boot familiarity
* controlled dependency direction
* AI-provider isolation
* database-access isolation
* future extensibility
* beginner learning value

---

## 4. Options Considered

### Option 1: Layered Architecture

Proposed layers:

* router
* service
* repository
* model
* schema
* AI integration
* configuration
* exception handling

Advantages:

* clear responsibilities
* easy unit testing
* familiar enterprise structure
* supports provider replacement
* supports future feature growth

Disadvantages:

* more files
* some boilerplate
* unnecessary abstraction is possible

### Option 2: Route-Centric Architecture

Routes directly perform validation, database operations, and AI calls.

Advantages:

* fast initial development
* fewer files
* easy for a very small demo

Disadvantages:

* routes become large
* hard to test business logic
* database and AI logic become tightly coupled
* difficult to maintain

### Option 3: Microservices

Separate ticket, AI, and analytics services.

Advantages:

* independent deployment
* component isolation
* independent scaling

Disadvantages:

* excessive complexity for MVP
* distributed transactions and networking
* more deployment and monitoring work
* inappropriate for a beginner project

---

## 5. Decision

The backend will use a **layered modular monolith architecture**.

The main dependency flow will be:

```text
Router
→ Service
→ Repository
→ PostgreSQL
```

AI operations will use:

```text
Service
→ AI Service
→ AI Client
→ External AI Provider
```

---

## 6. Layer Responsibilities

### Router Layer

* accepts HTTP requests
* applies schemas
* calls services
* returns HTTP responses

### Service Layer

* applies business rules
* coordinates repositories and AI services
* validates state transitions

### Repository Layer

* performs database operations
* isolates query logic

### Schema Layer

* validates request, response, and AI data

### AI Integration Layer

* communicates with the provider
* parses and validates responses
* maps provider failures

### Exception Layer

* defines application errors
* converts errors into consistent API responses

---

## 7. Rationale

A modular monolith provides enough structure to practise professional design without introducing distributed-system complexity.

This approach is also familiar to a Spring Boot developer:

| Spring Boot              | Proposed FastAPI Architecture |
| ------------------------ | ----------------------------- |
| Controller               | Router                        |
| Service                  | Service                       |
| Repository               | Repository                    |
| Entity                   | SQLAlchemy model              |
| DTO                      | Pydantic schema               |
| Controller advice        | Exception handler             |
| Configuration properties | Settings module               |

---

## 8. Positive Consequences

* easier testing
* clear ownership of responsibilities
* smaller route functions
* easier database replacement
* easier AI-provider replacement
* improved code readability
* supports gradual project growth
* teaches enterprise backend structure

---

## 9. Negative Consequences

* more files and directories
* small operations may pass through several layers
* poor abstractions may create unnecessary boilerplate
* developers must avoid circular dependencies

---

## 10. Risks and Mitigations

| Risk                                | Mitigation                                        |
| ----------------------------------- | ------------------------------------------------- |
| Too many unnecessary classes        | Add abstractions only where responsibility exists |
| Business logic leaks into routes    | Enforce service-layer ownership                   |
| Database logic leaks into services  | Use repositories consistently                     |
| Circular imports                    | Maintain one-directional dependency flow          |
| Architecture becomes overengineered | Keep the application as one deployable backend    |

---

## 11. Review Conditions

Review this decision if:

* the application becomes too small to justify existing layers
* a component requires independent scaling and deployment
* module boundaries become unclear
* repeated cross-module coupling appears

---

## 12. Related Documents

* `docs/HLD.md`
* `docs/LLD.md`
