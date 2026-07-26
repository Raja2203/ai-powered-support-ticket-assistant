# AI-Powered Support Ticket Assistant

## Testing Strategy

---

## 1. Document Information

| Field           | Value                               |
| --------------- | ----------------------------------- |
| Project Name    | AI-Powered Support Ticket Assistant |
| Document Type   | Testing Strategy                    |
| Document Status | Draft                               |
| Version         | 1.0                                 |
| Author          | Raja Rangarao Moturi                |
| Last Updated    | 2026-07-26                          |

---

## 2. Purpose

This document defines the testing approach for the AI-Powered Support Ticket Assistant.

It explains:

* testing objectives
* testing levels
* backend testing
* frontend testing
* database testing
* AI integration testing
* API contract testing
* failure testing
* test environments
* test data strategy
* mocking strategy
* coverage expectations
* CI test execution
* release-quality checks

The goal is to verify that the application behaves correctly, handles failures safely, and remains maintainable as new features are added.

---

## 3. Testing Objectives

The testing strategy should ensure that:

* ticket operations behave correctly
* invalid input is rejected
* status transitions follow business rules
* database operations are reliable
* AI output is validated
* AI failures do not crash the application
* frontend workflows behave correctly
* API responses match the documented contracts
* errors use consistent response formats
* application changes do not break existing features
* CI detects problems before code is merged

---

## 4. Testing Principles

The project will follow these testing principles.

### 4.1 Test Business Behaviour

Tests should verify business outcomes rather than only checking internal implementation details.

For example, tests should verify that:

* a closed ticket cannot be updated
* an unsupported AI category is rejected
* invalid status transitions return a conflict
* AI failure does not delete an existing ticket

### 4.2 Keep Tests Deterministic

Automated tests should produce the same result each time.

Tests should avoid depending on:

* live AI-provider behaviour
* unstable network services
* shared production data
* execution order
* current local machine configuration

### 4.3 Isolate External Dependencies

External systems should be mocked or replaced during most automated tests.

These systems include:

* AI provider
* external APIs
* email services
* future payment services
* future notification services

### 4.4 Test Failures Intentionally

Failure conditions are part of expected system behaviour.

Tests should cover:

* invalid requests
* missing tickets
* database failures
* AI timeouts
* invalid AI responses
* unsupported status transitions
* stale AI analysis

### 4.5 Maintain Test Readability

A test should clearly communicate:

* what condition is being tested
* what action occurs
* what result is expected

Test names should describe behaviour instead of implementation details.

---

## 5. Testing Scope

The testing strategy covers:

* FastAPI routes
* request and response schemas
* ticket business rules
* repository operations
* PostgreSQL integration
* AI-service behaviour
* AI-output parsing
* AI-output validation
* exception handling
* health and readiness endpoints
* React components
* frontend API communication
* frontend workflows
* Docker-based application startup
* CI workflows

---

## 6. Out-of-Scope Testing for MVP

The following testing areas are outside the initial MVP:

* large-scale load testing
* penetration testing
* production disaster-recovery testing
* multi-region failover testing
* chaos engineering
* mobile application testing
* accessibility certification
* multilingual AI evaluation
* advanced security red-team testing
* large-scale AI benchmarking
* Kubernetes deployment testing

These can be added when the application grows.

---

## 7. Testing Pyramid

The project will use a testing pyramid.

```text
               End-to-End Tests
             Frontend Integration
           API Integration Tests
        Service and Repository Tests
              Unit Tests
```

Most tests should be unit and service-level tests.

Fewer tests should depend on:

* real databases
* complete frontend-backend execution
* browser automation
* live external services

This keeps the test suite fast and reliable.

---

## 8. Testing Levels

The project will include:

1. Unit testing
2. Service-layer testing
3. Repository integration testing
4. API integration testing
5. AI integration testing
6. Frontend component testing
7. Frontend integration testing
8. End-to-end testing
9. Docker smoke testing
10. CI verification

---

# 9. Unit Testing

## 9.1 Purpose

Unit tests verify small pieces of logic in isolation.

They should not require:

* PostgreSQL
* live AI provider
* frontend server
* network access

## 9.2 Backend Unit Test Areas

Backend unit tests should cover:

* ticket-status transition rules
* category validation
* priority validation
* support-team validation
* pagination calculations
* sorting validation
* date-range validation
* ticket input normalization
* AI-output parsing
* AI-output schema validation
* stale-analysis detection
* business exception creation
* error-code mapping

## 9.3 Example Behavioural Scenarios

Examples of unit-test scenarios include:

* `OPEN` can move to `IN_PROGRESS`
* `OPEN` cannot move directly to `RESOLVED`
* `CLOSED` cannot move to another state
* unsupported priority values are rejected
* unsupported category values are rejected
* page number below one is rejected
* AI output missing a required field is rejected
* AI output with unsupported category is rejected
* blank customer name is rejected
* date-from later than date-to is rejected

---

# 10. Service-Layer Testing

## 10.1 Purpose

Service tests verify business workflows while isolating database and AI implementation details.

Repositories and AI clients should be replaced with mocks or test doubles.

## 10.2 Ticket Service Scenarios

The ticket service should be tested for:

* successful ticket creation
* ticket lookup
* ticket update
* ticket status update
* ticket closure
* closed-ticket modification rejection
* missing-ticket handling
* invalid-status transition handling
* filtering input validation
* stale-analysis protection
* analysis regeneration rules

## 10.3 AI Workflow Scenarios

The service layer should be tested for:

* successful analysis
* analysis already in progress
* ticket not found
* closed ticket
* invalid ticket content
* AI timeout
* AI provider unavailable
* malformed AI response
* unsupported AI category
* unsupported AI priority
* successful regeneration
* failed regeneration preserving previous valid output

---

# 11. Repository Integration Testing

## 11.1 Purpose

Repository tests verify real interaction with PostgreSQL.

These tests should use a dedicated test database.

They should not use:

* development database
* production database
* shared personal database

## 11.2 Repository Scenarios

Repository integration tests should cover:

* creating a ticket
* retrieving by internal ID
* retrieving by public ID
* listing tickets
* filtering by status
* filtering by category
* filtering by priority
* filtering by customer email
* filtering by AI-analysis status
* sorting by creation date
* pagination
* ticket updates
* ticket status changes
* storing validated AI results
* preserving previous analysis
* transaction rollback
* unique public ID constraints

## 11.3 Database Constraint Tests

Database tests should verify:

* required fields cannot be null
* public IDs are unique
* unsupported status values are rejected
* unsupported priority values are rejected
* invalid transactions are rolled back
* indexes exist where defined
* closed timestamps are stored correctly

---

# 12. API Integration Testing

## 12.1 Purpose

API integration tests verify the complete request path:

```text
HTTP Request
→ FastAPI Router
→ Request Validation
→ Service Layer
→ Repository
→ Database
→ Response
```

## 12.2 Health API Tests

Test scenarios:

* health endpoint returns `200`
* health endpoint returns expected service name
* health endpoint does not require the database
* health response includes timestamp and version

## 12.3 Readiness API Tests

Test scenarios:

* readiness returns `200` when the database is available
* readiness returns `503` when the database is unavailable
* readiness does not call the AI provider
* readiness response uses the documented structure

## 12.4 Ticket Creation API Tests

Test scenarios:

* valid ticket returns `201`
* missing customer name returns validation error
* invalid email returns validation error
* short subject returns validation error
* blank description returns validation error
* default status is `OPEN`
* default priority is `MEDIUM`
* default analysis status is `NOT_REQUESTED`

## 12.5 Ticket Retrieval API Tests

Test scenarios:

* existing ticket returns `200`
* unknown ticket returns `404`
* invalid public ID format returns validation error
* returned fields match the API contract

## 12.6 Ticket List API Tests

Test scenarios:

* default pagination works
* status filter works
* priority filter works
* category filter works
* customer email filter works
* multiple filters work together
* invalid page is rejected
* excessive page size is rejected
* unsupported sort field is rejected
* default sorting returns newest tickets first

## 12.7 Ticket Update API Tests

Test scenarios:

* editable fields can be updated
* restricted fields cannot be updated
* missing ticket returns `404`
* closed ticket returns conflict
* ticket text changes mark analysis as outdated
* empty update request is handled consistently

## 12.8 Ticket Status API Tests

Test scenarios:

* valid transition succeeds
* invalid transition returns `409`
* unsupported status returns validation error
* repeated current status behaves consistently
* closing a ticket sets `closed_at`
* closed ticket cannot transition again

## 12.9 AI Analysis API Tests

Test scenarios:

* valid analysis returns `200`
* missing ticket returns `404`
* closed ticket returns conflict
* duplicate in-progress request returns conflict
* AI timeout returns `504`
* AI unavailable returns `503`
* invalid AI output returns `502`
* validated output is stored
* previous valid result remains when regeneration fails

## 12.10 AI Correction API Tests

Test scenarios:

* valid correction succeeds
* unsupported category is rejected
* unsupported priority is rejected
* empty correction request is rejected
* ticket without analysis returns `404`
* closed ticket cannot be corrected
* correction does not change ticket status

---

# 13. AI Integration Testing

## 13.1 Purpose

AI integration tests verify that the application safely handles model output.

The main automated test suite should not depend on live AI calls.

## 13.2 Mocked AI Responses

Mocked responses should cover:

### Valid Responses

* valid payment ticket
* valid delivery ticket
* valid account ticket
* valid refund ticket
* valid technical ticket
* valid other-category ticket

### Invalid Structure

* malformed JSON
* empty response
* missing category
* missing priority
* missing summary
* missing recommended team
* missing suggested response
* unexpected top-level structure

### Invalid Values

* unsupported category
* unsupported priority
* invalid support team
* empty summary
* overly long summary
* overly long response
* non-string values

### Provider Failures

* timeout
* network error
* authentication error
* rate-limit error
* service unavailable
* malformed provider response

## 13.3 AI Safety Tests

AI-generated response validation should check that the response does not:

* claim that a refund was completed without confirmation
* claim that payment was reversed without confirmation
* promise a specific resolution time without support
* expose internal system information
* contain unsupported sensitive instructions
* automatically close the ticket
* instruct the system to ignore validation rules

## 13.4 Prompt Injection Scenarios

Test tickets may include malicious or misleading text such as:

* instructions to ignore the system prompt
* requests to reveal API keys
* requests to expose database credentials
* embedded fake JSON
* instructions to assign unsupported categories
* instructions to mark all tickets as critical

Expected behaviour:

* the AI output must still follow the application schema
* secrets must never be returned
* unsupported values must be rejected
* ticket text must be treated as data, not system instructions

---

# 14. Live AI Testing

## 14.1 Purpose

Live AI testing verifies real provider integration.

It should not run during every CI execution.

## 14.2 Execution Conditions

Live AI tests should run only when:

* explicitly enabled
* valid test credentials are available
* test data contains no sensitive customer information
* cost and rate limits are understood
* provider availability is acceptable

## 14.3 Live AI Test Scenarios

A small live test suite may verify:

* provider authentication
* selected model availability
* expected structured output
* valid category generation
* valid priority generation
* timeout configuration
* prompt-version compatibility

## 14.4 Limitations

Live AI tests may be:

* slower
* non-deterministic
* costly
* rate-limited
* affected by provider changes

Therefore, they should supplement mocked tests rather than replace them.

---

# 15. Frontend Unit Testing

Frontend unit tests should cover:

* date formatting
* ticket-status formatting
* category labels
* priority labels
* query-parameter construction
* form-validation helpers
* API error-code mapping
* pagination calculations

---

# 16. Frontend Component Testing

Component tests should cover:

* ticket form
* ticket table
* ticket filters
* pagination controls
* status badge
* priority badge
* category badge
* error alert
* loading indicator
* AI-analysis panel
* suggested-response editor

## 16.1 Ticket Form Scenarios

* fields render correctly
* required-field messages appear
* invalid email is rejected
* submit is disabled during request
* successful submission shows confirmation
* backend validation errors are displayed

## 16.2 Ticket List Scenarios

* tickets are displayed
* empty state is displayed
* loading state is displayed
* filters update the request
* pagination controls work
* API errors are displayed

## 16.3 Ticket Details Scenarios

* ticket information is displayed
* status update control is available
* invalid transitions are prevented where appropriate
* AI-analysis button triggers request
* analysis loading state is displayed
* AI suggestions are displayed
* suggested response can be edited

---

# 17. Frontend Integration Testing

Frontend integration tests should verify interaction between multiple components and mocked backend APIs.

Test scenarios include:

* ticket form submission
* ticket list loading
* ticket filtering
* ticket-detail loading
* ticket-status update
* AI-analysis request
* AI timeout display
* AI invalid-output display
* human correction submission

---

# 18. End-to-End Testing

## 18.1 Purpose

End-to-end tests verify the complete user workflow through the browser.

They may include:

```text
Browser
→ React Frontend
→ FastAPI Backend
→ PostgreSQL
```

The AI provider should normally remain mocked in end-to-end tests.

## 18.2 Initial End-to-End Scenarios

### Scenario 1: Create and View Ticket

1. Open the ticket-creation page.
2. Enter valid ticket data.
3. Submit the ticket.
4. Verify confirmation.
5. Open the ticket-details page.
6. Verify saved data.

### Scenario 2: Analyze Ticket

1. Open an existing ticket.
2. Request AI analysis.
3. Verify loading state.
4. Receive mocked valid analysis.
5. Verify category, priority, summary, and response.

### Scenario 3: Update Status

1. Open an `OPEN` ticket.
2. Change status to `IN_PROGRESS`.
3. Verify updated status.
4. Change status to `RESOLVED`.
5. Verify updated status.

### Scenario 4: Handle AI Failure

1. Open a ticket.
2. Request AI analysis.
3. Simulate provider timeout.
4. Verify user-friendly error.
5. Verify ticket remains available.
6. Verify retry is possible.

---

# 19. Docker Smoke Testing

Docker smoke testing verifies that the local environment starts correctly.

Checks include:

* backend container starts
* PostgreSQL container starts
* frontend container starts
* backend connects to PostgreSQL
* frontend reaches backend
* health endpoint returns success
* readiness endpoint returns success
* database volume persists data
* services use the expected ports

The smoke test does not replace unit or integration tests.

---

# 20. Test Environment Strategy

## 20.1 Local Environment

Used for:

* developer testing
* debugging
* manual API testing
* frontend testing
* Docker Compose testing

## 20.2 Test Environment

Used for:

* automated tests
* isolated PostgreSQL database
* mocked AI provider
* temporary test data

## 20.3 Future Development Environment

May be used for:

* shared integration testing
* deployment verification
* live AI-provider testing
* stakeholder demonstrations

## 20.4 Future Production Environment

Production testing should focus on:

* smoke checks
* monitoring
* health verification
* safe post-deployment validation

Production must not be used for destructive testing.

---

# 21. Test Database Strategy

The project should use a separate database for automated tests.

The test database should:

* be isolated from development
* be reset between test runs
* use the same schema as the application
* support transaction rollback where practical
* use migrations for schema setup
* contain only generated test data

Possible approaches include:

* dedicated PostgreSQL test database
* temporary PostgreSQL container
* transaction-based test isolation

SQLite should not replace PostgreSQL for integration tests because database behaviour may differ.

---

# 22. Test Data Strategy

Test data should be:

* synthetic
* predictable
* isolated
* reusable where appropriate
* free of real customer information

## 22.1 Example Ticket Categories

Test tickets should cover:

* payment failure
* delayed delivery
* account login issue
* refund delay
* technical error
* uncategorized issue

## 22.2 Boundary Test Data

Test data should include:

* minimum valid lengths
* maximum valid lengths
* values just below the minimum
* values just above the maximum
* whitespace-only values
* unusual but valid email addresses
* special characters in ticket descriptions
* very long AI responses

## 22.3 Sensitive Data Rule

Do not use:

* real customer names
* real customer emails
* production ticket descriptions
* real payment data
* real account credentials

---

# 23. Mocking Strategy

Mocks should be used for:

* AI provider
* external network calls
* future email provider
* future notification services
* time-dependent behaviour where needed

Mocks should not be overused for repository integration tests.

A repository test should verify real PostgreSQL interaction rather than mocking every database operation.

---

# 24. Test Fixtures

Reusable fixtures may include:

* test application
* test client
* database session
* clean database
* valid ticket request
* stored open ticket
* stored closed ticket
* completed AI analysis
* mocked valid AI response
* mocked invalid AI response
* mocked timeout
* mocked provider outage

Fixtures should remain small and understandable.

---

# 25. Coverage Expectations

Coverage is a quality indicator, not the only measure of test quality.

Recommended initial targets:

| Area                      |        Target |
| ------------------------- | ------------: |
| Business rules            | 90% or higher |
| Service layer             | 85% or higher |
| AI parsing and validation | 90% or higher |
| API routes                | 80% or higher |
| Repository layer          | 75% or higher |
| Frontend utilities        | 80% or higher |
| Overall backend           | 80% or higher |

Coverage targets should not encourage meaningless tests.

Critical failure paths should be tested even if overall coverage is already high.

---

# 26. Manual Testing

Manual testing remains useful for:

* Swagger UI verification
* Postman testing
* frontend usability
* error-message clarity
* responsive layout
* accessibility review
* live AI-output review
* Docker setup verification

Manual test results should not replace automated tests.

---

# 27. API Contract Verification

The implemented OpenAPI specification should be compared against `docs/API_SPEC.md`.

Verify:

* endpoint paths
* HTTP methods
* request fields
* response fields
* status codes
* validation rules
* enum values
* error formats
* pagination behaviour
* filtering behaviour

Documentation and implementation must remain synchronized.

---

# 28. Regression Testing

Every bug fix should include a test that fails before the fix and passes after the fix.

Regression tests should be added for:

* invalid state transitions
* incorrect filtering
* pagination errors
* AI-output parsing defects
* lost previous analysis
* incorrect error mapping
* frontend API-error handling
* database rollback failures

---

# 29. Performance Testing

Large-scale performance testing is outside the MVP.

Basic performance checks may verify:

* ticket listing uses pagination
* database queries do not retrieve all records
* AI requests use timeouts
* duplicate analysis requests are blocked
* common filters use indexes
* frontend does not repeatedly call the same endpoint unnecessarily

Future performance testing may measure:

* requests per second
* response latency
* database query time
* AI-analysis latency
* concurrent users
* frontend rendering performance

---

# 30. Security Testing

Basic security tests should verify:

* missing secrets are detected
* API keys are not returned
* database passwords are not logged
* unsupported input is rejected
* overly long input is rejected
* raw exceptions are not exposed
* CORS is restricted
* SQL injection attempts do not bypass ORM parameterization
* prompt injection does not control system behaviour

Detailed security testing is documented in `docs/SECURITY.md`.

---

# 31. CI Testing Workflow

The CI pipeline should run on:

* pull requests
* pushes to `develop`
* pushes to `main`

The backend CI workflow should:

1. check out the repository
2. configure the required Python version
3. install dependencies
4. start or configure the test database
5. run database migrations
6. run lint checks
7. run unit tests
8. run integration tests
9. generate coverage results
10. fail when required checks fail

The frontend CI workflow should later:

1. configure Node.js
2. install dependencies
3. run lint checks
4. run component tests
5. build the frontend
6. fail when required checks fail

Live AI tests should not run in the normal CI pipeline.

---

# 32. CI Quality Gates

A pull request should not be merged when:

* tests fail
* lint checks fail
* required build fails
* database migrations fail
* coverage falls below the agreed threshold
* API contracts are intentionally changed without documentation updates
* secrets are detected
* critical security checks fail

---

# 33. Test Naming Convention

Test names should describe the expected behaviour.

Recommended style:

```text
test_<operation>_<condition>_<expected_result>
```

Examples:

* `test_create_ticket_with_valid_data_returns_created_ticket`
* `test_update_closed_ticket_returns_conflict`
* `test_ai_timeout_preserves_existing_analysis`
* `test_invalid_priority_is_rejected`
* `test_list_tickets_with_status_filter_returns_matching_items`

The names should remain readable even without opening the test body.

---

# 34. Test Organization

Recommended backend test structure:

```text
src/backend/tests/
├── unit/
│   ├── services/
│   ├── schemas/
│   ├── ai/
│   └── business_rules/
├── integration/
│   ├── api/
│   ├── repositories/
│   └── database/
├── fixtures/
└── conftest
```

Recommended frontend test organization:

```text
src/frontend/src/
├── components/
├── pages/
├── services/
└── tests/
```

The exact organization may evolve, but test responsibilities should remain clear.

---

# 35. Bug Severity Levels

| Severity | Description                                                |
| -------- | ---------------------------------------------------------- |
| Critical | Data loss, security exposure, or total application failure |
| High     | Core ticket or AI workflow cannot complete                 |
| Medium   | Feature works incorrectly but a workaround exists          |
| Low      | Minor user-interface or documentation issue                |

Critical and high-severity defects should block release.

---

# 36. Entry Criteria for Testing

Testing for a feature can begin when:

* requirements are understood
* API contract is defined
* acceptance criteria are available
* implementation is available
* required test environment is ready
* dependencies can be mocked or accessed
* database migrations are available when needed

---

# 37. Exit Criteria for a Feature

A feature is ready for merge when:

* planned tests are implemented
* unit tests pass
* integration tests pass where required
* lint checks pass
* no critical or high defects remain
* expected error paths are tested
* documentation is updated
* test coverage remains acceptable
* no secrets or real customer data are included

---

# 38. Release Testing Checklist

Before a release:

* [ ] Backend tests pass
* [ ] Frontend tests pass
* [ ] Lint checks pass
* [ ] Frontend build succeeds
* [ ] Database migrations succeed
* [ ] Docker Compose starts successfully
* [ ] Health endpoint returns `200`
* [ ] Readiness endpoint returns `200`
* [ ] Ticket creation works
* [ ] Ticket retrieval works
* [ ] Ticket listing works
* [ ] Ticket status updates work
* [ ] AI analysis works with mocked response
* [ ] AI failure is handled safely
* [ ] No secrets are committed
* [ ] Documentation matches implementation
* [ ] No critical or high defects remain

---

# 39. Open Testing Decisions

The following decisions should be finalized during setup:

* Which backend coverage tool will be used?
* Which frontend testing framework will be used?
* Which browser automation tool will be used?
* Will integration tests use a local test database or container?
* What exact coverage threshold will block pull requests?
* Should API contract tests compare generated OpenAPI automatically?
* How often should live AI tests run?
* Should accessibility testing be automated?
* Should performance smoke tests run in CI?
* Should security scanning run on every pull request?

---

# 40. Testing Review Checklist

* [ ] Testing objectives are clear
* [ ] Testing pyramid is defined
* [ ] Unit-test scope is defined
* [ ] Service-test scope is defined
* [ ] Repository integration scope is defined
* [ ] API-test scope is defined
* [ ] AI mocking strategy is defined
* [ ] Live AI testing is separated
* [ ] Frontend testing is defined
* [ ] End-to-end workflows are defined
* [ ] Test database strategy is defined
* [ ] Test data contains no real customer information
* [ ] Failure scenarios are included
* [ ] Coverage expectations are documented
* [ ] CI execution is defined
* [ ] Release checks are documented
* [ ] Open decisions are identified

---

# 41. Related Documents

| Document               | Location                     |
| ---------------------- | ---------------------------- |
| Problem Definition     | `docs/PROBLEM_DEFINITION.md` |
| Requirements           | `docs/REQUIREMENTS.md`       |
| High-Level Design      | `docs/HLD.md`                |
| Low-Level Design       | `docs/LLD.md`                |
| API Specification      | `docs/API_SPEC.md`           |
| Security Guidelines    | `docs/SECURITY.md`           |
| Architecture Decisions | `docs/adr/`                  |
| Setup Guide            | `docs/SETUP.md`              |
| Deployment Guide       | `docs/DEPLOYMENT.md`         |

---

# 42. Document History

| Version | Date       | Author               | Description              |
| ------- | ---------- | -------------------- | ------------------------ |
| 1.0     | 2026-07-26 | Raja Rangarao Moturi | Initial Testing Strategy |
