# ADR-003: Use SQLAlchemy for Database Access

---

## 1. Document Information

| Field         | Value                |
| ------------- | -------------------- |
| ADR Number    | ADR-003              |
| Status        | Accepted             |
| Decision Date | 2026-07-26           |
| Author        | Raja Rangarao Moturi |

---

## 2. Context

The FastAPI backend requires a reliable way to interact with PostgreSQL.

The data-access approach should support:

* model definition
* database queries
* transactions
* filtering
* pagination
* testing
* repository abstraction
* migration integration

The developer is familiar with JPA and Hibernate concepts from Spring Boot.

---

## 3. Decision Drivers

* PostgreSQL compatibility
* mature Python ecosystem
* transaction support
* ORM capability
* query flexibility
* testability
* migration compatibility
* familiarity with ORM concepts
* suitability for layered architecture

---

## 4. Options Considered

### Option 1: SQLAlchemy

Advantages:

* mature and widely adopted
* supports ORM and SQL expression approaches
* strong transaction support
* compatible with Alembic
* suitable for repository patterns
* supports both synchronous and asynchronous access

Disadvantages:

* learning curve
* session lifecycle must be managed correctly
* incorrect loading strategies may affect performance

### Option 2: Raw SQL

Advantages:

* complete control over queries
* direct understanding of SQL behavior
* no ORM abstraction overhead

Disadvantages:

* more repetitive code
* manual mapping
* harder maintainability
* greater risk of inconsistent transaction handling
* less suitable for a beginner-friendly layered application

### Option 3: SQLModel

Advantages:

* designed to work with FastAPI
* combines validation and database models
* less boilerplate

Disadvantages:

* can tightly couple API schemas and database models
* less architectural separation
* smaller ecosystem than SQLAlchemy
* hides concepts the project intends to practise

### Option 4: Django ORM

Advantages:

* mature ORM
* easy model definitions

Disadvantages:

* primarily designed for Django
* unnecessary framework dependency
* poor fit for a FastAPI-focused project

---

## 5. Decision

The project will use **SQLAlchemy** for ORM-based database access.

The application will keep:

* SQLAlchemy database models
* Pydantic API schemas

as separate model types.

Alembic will be used for schema migrations.

---

## 6. Rationale

SQLAlchemy provides production-relevant ORM experience and maps well to concepts already familiar from Hibernate and JPA.

| JPA or Hibernate    | SQLAlchemy                   |
| ------------------- | ---------------------------- |
| Entity              | ORM model                    |
| Entity manager      | Session                      |
| Repository          | Repository module or class   |
| Transaction         | Session transaction          |
| JPQL or Criteria    | SQLAlchemy query expressions |
| Flyway or Liquibase | Alembic                      |

Separating API schemas from database models improves maintainability and prevents accidental exposure of internal database fields.

---

## 7. Positive Consequences

* strong PostgreSQL integration
* clear entity modelling
* controlled transactions
* reusable queries
* easier repository testing
* compatibility with Alembic
* reduced repetitive data mapping
* production-relevant ORM knowledge

---

## 8. Negative Consequences

* requires session-management discipline
* ORM queries can hide inefficient database behavior
* additional model definitions may be needed
* developers must understand commits, rollbacks, and object lifecycles

---

## 9. Risks and Mitigations

| Risk                               | Mitigation                                                          |
| ---------------------------------- | ------------------------------------------------------------------- |
| Database sessions are not closed   | Manage sessions through FastAPI dependencies                        |
| Transactions remain incomplete     | Define commit and rollback boundaries                               |
| API schemas become database models | Keep Pydantic and SQLAlchemy models separate                        |
| N+1 query problems appear          | Review relationship-loading strategies when relationships are added |
| Complex queries become difficult   | Use SQLAlchemy expressions or carefully controlled SQL              |

---

## 10. Review Conditions

Review this decision if:

* SQLAlchemy creates unacceptable complexity
* the project adopts a different database architecture
* direct SQL becomes necessary for specific high-performance operations

---

## 11. Related Documents

* `docs/LLD.md`
* `docs/API_SPEC.md`
* ADR-002
