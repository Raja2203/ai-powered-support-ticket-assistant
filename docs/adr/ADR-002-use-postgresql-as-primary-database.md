# ADR-002: Use PostgreSQL as the Primary Database

---

## 1. Document Information

| Field         | Value                |
| ------------- | -------------------- |
| ADR Number    | ADR-002              |
| Status        | Accepted             |
| Decision Date | 2026-07-26           |
| Author        | Raja Rangarao Moturi |

---

## 2. Context

The application requires persistent storage for customer-support tickets and validated AI-generated results.

The data includes:

* customer details
* ticket subject and description
* ticket status
* category
* priority
* assigned support team
* AI-generated summary
* suggested response
* analysis metadata
* timestamps

The project also requires filtering, sorting, pagination, constraints, indexing, and reliable transactional updates.

---

## 3. Decision Drivers

* relational ticket structure
* transactional consistency
* filtering and reporting support
* production relevance
* compatibility with SQLAlchemy
* support for indexes and constraints
* Docker availability
* strong community support
* future analytics capability

---

## 4. Options Considered

### Option 1: PostgreSQL

Advantages:

* mature relational database
* strong transaction support
* advanced indexing
* reliable constraint enforcement
* good SQL capabilities
* strong Python ecosystem support
* suitable for future analytics

Disadvantages:

* requires database setup
* more complex than SQLite
* schema migrations must be managed

### Option 2: SQLite

Advantages:

* very easy local setup
* no separate database server
* useful for small prototypes

Disadvantages:

* limited concurrency compared with PostgreSQL
* local behavior can differ from production
* less useful for learning production database setup
* fewer operational concepts to practise

### Option 3: MySQL

Advantages:

* mature relational database
* widely used
* good ORM support

Disadvantages:

* the developer already plans to gain deeper PostgreSQL experience
* PostgreSQL offers strong support for advanced querying and data types
* no meaningful advantage for this MVP

### Option 4: MongoDB

Advantages:

* flexible document model
* natural JSON-like records
* easy schema evolution

Disadvantages:

* ticket data has a clear relational structure
* relational constraints are valuable
* filtering and transactional updates fit PostgreSQL well
* introduces unnecessary database-model differences

---

## 5. Decision

The system will use **PostgreSQL** as its primary persistent database.

PostgreSQL will be the source of truth for:

* ticket information
* ticket status
* validated AI analysis
* AI-analysis state
* analysis metadata
* timestamps

---

## 6. Rationale

Ticket data has a predictable structure and benefits from:

* required fields
* controlled values
* transactions
* indexes
* reliable updates
* filtering
* pagination

PostgreSQL is well suited to these requirements and provides production-relevant database experience.

---

## 7. Positive Consequences

* strong data integrity
* reliable transactions
* efficient filtering and pagination
* support for controlled schema evolution
* compatibility with Docker Compose
* compatibility with SQLAlchemy and Alembic
* future support for reporting and analytics

---

## 8. Negative Consequences

* local setup requires a running database
* credentials and connections must be configured
* migrations must be maintained
* connection failures must be handled
* testing requires a database strategy

---

## 9. Risks and Mitigations

| Risk                                | Mitigation                                     |
| ----------------------------------- | ---------------------------------------------- |
| Database setup becomes difficult    | Provide Docker Compose and setup documentation |
| Schema differs between environments | Use Alembic migrations                         |
| Credentials are committed           | Use `.env.example` and Git ignore rules        |
| Queries become slow                 | Add justified indexes and inspect query plans  |
| Tests affect development data       | Use a separate test database                   |

---

## 10. Review Conditions

Review this decision if:

* the application requires a fundamentally non-relational data model
* another database provides a clear operational requirement
* the project moves to a platform with strict database constraints

---

## 11. Related Documents

* `docs/HLD.md`
* `docs/LLD.md`
* `docs/API_SPEC.md`
