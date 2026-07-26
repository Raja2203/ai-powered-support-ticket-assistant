# AI-Powered Support Ticket Assistant

## Security Guidelines

---

## 1. Document Information

| Field           | Value                               |
| --------------- | ----------------------------------- |
| Project Name    | AI-Powered Support Ticket Assistant |
| Document Type   | Security Guidelines                 |
| Document Status | Draft                               |
| Version         | 1.0                                 |
| Author          | Raja Rangarao Moturi                |
| Last Updated    | 2026-07-26                          |

---

## 2. Purpose

This document defines the security requirements and practices for the AI-Powered Support Ticket Assistant.

It covers:

* secret management
* customer-data protection
* input validation
* API security
* AI security
* prompt-injection protection
* logging protection
* database security
* frontend security
* Docker security
* dependency security
* CI security
* incident handling
* future authentication and authorization

The purpose is to reduce avoidable security risks while keeping the MVP beginner-friendly and realistic.

---

## 3. Security Objectives

The system should protect:

* customer names
* customer email addresses
* ticket descriptions
* AI-generated responses
* AI-provider API keys
* database credentials
* application configuration
* source code
* deployment credentials
* system logs

The primary security objectives are:

* confidentiality
* integrity
* availability
* traceability
* least privilege
* secure failure handling

---

## 4. Security Scope

This document applies to:

* React frontend
* FastAPI backend
* PostgreSQL database
* AI-provider integration
* Docker containers
* Docker Compose
* GitHub repository
* GitHub Actions
* environment files
* application logs
* API requests and responses

---

## 5. MVP Security Limitations

Authentication and authorization are outside the initial MVP.

Therefore:

* the MVP must use synthetic test data
* it must not process real customer-sensitive information
* it must not be publicly exposed without additional protection
* it must not be treated as production-ready
* it must not allow unrestricted internet access to ticket data

Before real users or real customer data are introduced, the system must add:

* authentication
* authorization
* HTTPS
* rate limiting
* audit logging
* secure secret storage
* stronger deployment controls

---

# 6. Threat Model

## 6.1 Main Assets

Important assets include:

* ticket records
* customer information
* AI API credentials
* database credentials
* application configuration
* source code
* AI prompts
* AI-generated output
* build and deployment workflows

## 6.2 Potential Threat Actors

Possible threat actors include:

* unauthenticated external users
* malicious API clients
* users submitting harmful ticket content
* compromised dependencies
* accidental developer mistakes
* leaked credentials
* malicious prompt content
* unauthorized repository users

## 6.3 Main Threats

The MVP should consider:

* secret leakage
* unauthorized API access
* SQL injection
* prompt injection
* cross-site scripting
* excessive input size
* sensitive data in logs
* dependency vulnerabilities
* insecure CORS
* exposed database ports
* container misconfiguration
* AI-generated misinformation
* denial-of-service through repeated AI calls
* accidental data deletion

---

# 7. Secret Management

## 7.1 Secrets

The following values are secrets:

* AI-provider API key
* database password
* database connection string containing credentials
* future JWT secret
* future email-provider credentials
* future deployment credentials
* future cloud-access keys

## 7.2 Storage Rules

Secrets must:

* be stored outside source code
* be loaded through environment variables
* never appear in committed files
* never appear in screenshots
* never appear in documentation examples
* never appear in frontend code
* never be returned in API responses
* never be written to logs

## 7.3 Environment Files

Local secret values may be stored in a local `.env` file.

The repository should include only:

```text
.env.example
```

The `.env.example` file should contain:

* variable names
* placeholder values
* short descriptions where helpful

It must not contain real credentials.

## 7.4 Git Ignore Rules

The repository must ignore:

* `.env`
* `.env.local`
* `.env.development`
* `.env.production`
* secret JSON files
* local certificates
* credential files

## 7.5 Secret Rotation

A secret must be rotated when:

* it is accidentally committed
* it appears in logs
* it is shared publicly
* a developer loses control of it
* a repository collaborator should no longer have access
* compromise is suspected

Deleting the secret from Git history is not sufficient. The secret itself must also be invalidated and replaced.

---

# 8. Frontend Secret Protection

The React frontend is delivered to the user's browser.

Therefore, any value included in the frontend build must be considered public.

The frontend must not contain:

* AI-provider API keys
* database credentials
* backend private keys
* JWT signing secrets
* cloud-access keys
* private service tokens

The frontend may contain non-secret configuration such as:

* backend API base URL
* application environment name
* public feature flags

All AI-provider calls must pass through the FastAPI backend.

---

# 9. Customer Data Protection

## 9.1 Customer Data in MVP

The ticket may include:

* customer name
* customer email
* issue description
* transaction-related information entered by the user

Even in a learning project, this information should be treated carefully.

## 9.2 Data-Minimization Principle

The system should collect only information required to process the ticket.

The MVP should not request:

* payment-card numbers
* banking credentials
* account passwords
* government identifiers
* authentication tokens
* unnecessary personal details

## 9.3 Test Data

Development and testing must use synthetic data.

Do not use:

* real customer tickets
* real email addresses without permission
* production issue descriptions
* real transaction numbers
* confidential company information

## 9.4 Sensitive Ticket Content

Users may accidentally enter sensitive information.

The application should display guidance such as:

> Do not include passwords, full payment-card numbers, or other sensitive credentials.

Future versions may introduce automatic redaction.

---

# 10. Data Sent to the AI Provider

## 10.1 Minimum Necessary Data

The backend should send only the data necessary for analysis.

Typical AI input may include:

* ticket subject
* ticket description
* supported categories
* supported priorities
* output-format instructions

The system should avoid sending:

* internal database IDs
* database credentials
* customer passwords
* API keys
* unrelated tickets
* infrastructure details
* application logs
* hidden configuration

## 10.2 Customer Identifiers

Customer name and email should not be sent to the AI provider unless required.

For classification and summarization, the subject and description should normally be sufficient.

## 10.3 Provider Data Policies

Before using real customer data, the project must review:

* provider data-retention policy
* provider training-data policy
* regional data processing
* enterprise privacy controls
* data-deletion options
* legal and contractual requirements

---

# 11. Input Validation

All client input must be treated as untrusted.

Validation must occur in the backend even when the frontend already validates the fields.

## 11.1 Required Validation

The backend should validate:

* required fields
* field types
* email format
* minimum lengths
* maximum lengths
* enum values
* page numbers
* page sizes
* sort fields
* sort direction
* date ranges
* ticket identifiers
* status transitions

## 11.2 Whitespace Handling

Text fields should:

* remove unnecessary leading and trailing whitespace
* reject whitespace-only input
* preserve meaningful internal spacing

## 11.3 Input-Length Limits

Maximum lengths should be enforced for:

* customer name
* email
* subject
* description
* search query
* AI summary
* suggested response

This helps reduce:

* excessive memory usage
* oversized requests
* logging problems
* unnecessary AI cost
* denial-of-service risk

---

# 12. SQL Injection Protection

The application should use:

* SQLAlchemy parameterized queries
* controlled repository methods
* validated filter values
* controlled sorting fields

The system must not create database queries by directly joining untrusted user input into SQL strings.

Special attention is required for:

* search
* sorting
* filtering
* dynamic query construction

Clients must not be allowed to provide arbitrary column names or SQL fragments.

---

# 13. Cross-Site Scripting Protection

Ticket descriptions and AI-generated responses may contain HTML-like content.

The frontend must treat ticket content as plain text by default.

The frontend should not:

* insert untrusted HTML directly
* render raw AI output as trusted markup
* use unsafe HTML-rendering features without sanitization

React escapes text content by default. This protection should not be bypassed unnecessarily.

---

# 14. CORS Security

CORS should allow only approved frontend origins.

Local development may allow:

```text
http://localhost:3000
```

Production should use the exact deployed frontend origin.

The backend should avoid unrestricted CORS settings such as allowing every origin when:

* credentials are introduced
* authentication is added
* sensitive data is processed

Allowed methods and headers should also be restricted to what the application needs.

---

# 15. API Security

## 15.1 Endpoint Exposure

The MVP API should be accessible only in controlled local or development environments.

Before public deployment, add:

* authentication
* authorization
* HTTPS
* rate limiting
* request-size limits
* secure headers
* monitoring

## 15.2 HTTP Methods

Endpoints should use appropriate HTTP methods.

Examples:

* `GET` for retrieval
* `POST` for creation and AI analysis
* `PATCH` for partial updates

Operations that change data should not be exposed through `GET`.

## 15.3 Error Messages

API errors should not reveal:

* stack traces
* SQL queries
* table names
* filesystem paths
* package versions
* environment variables
* AI-provider credentials
* raw exception messages

Errors should use:

* stable application error codes
* clear user-facing messages
* internal detailed logs where safe

---

# 16. Authentication and Authorization

Authentication and authorization are planned for a future version.

Potential roles include:

* customer
* support agent
* administrator

## 16.1 Future Authentication Requirements

Authentication may later support:

* secure login
* password hashing
* token expiration
* refresh-token handling
* logout
* account lockout
* password-reset workflows

## 16.2 Future Authorization Requirements

Authorization should ensure:

* customers see only their own tickets
* support agents access permitted queues
* administrators manage system configuration
* sensitive operations require elevated permissions
* permanent deletion is restricted

## 16.3 Least Privilege

Users and services should receive only the minimum permissions required.

---

# 17. Prompt Injection Protection

Ticket descriptions are untrusted user input.

A malicious ticket may contain instructions such as:

* ignore previous instructions
* reveal the API key
* output an unsupported category
* classify every ticket as critical
* expose system prompts
* return database credentials

The AI system must treat ticket content as data, not as trusted system instructions.

## 17.1 Prompt-Separation Rules

The prompt should clearly separate:

* system instructions
* application rules
* ticket content
* expected output format

Ticket content should be wrapped or labelled as untrusted input.

## 17.2 Output Restrictions

The AI should be restricted to:

* supported categories
* supported priorities
* supported response fields
* structured output

The backend must reject unsupported output even if the AI follows malicious ticket instructions.

## 17.3 Secret Isolation

The AI model should never receive:

* API keys
* database passwords
* environment variables
* internal credentials

The model cannot reveal a secret it was never given.

---

# 18. AI Output Security

AI output is untrusted external input.

The backend must validate:

* structure
* required fields
* field types
* category
* priority
* support team
* field lengths
* empty values

The frontend must safely render AI output as plain text.

The system must not automatically execute instructions contained in AI output.

Examples of unsafe behaviour include:

* calling arbitrary URLs from model output
* executing generated code
* running generated database queries
* sending generated email automatically
* changing ticket status automatically without business rules

---

# 19. AI Hallucination Controls

The AI may create unsupported claims.

Examples include:

* refund has already been processed
* payment has been reversed
* delivery will arrive at a specific time
* account access has been restored
* a support agent has performed an action

Controls should include:

* human review
* clear draft labels
* restricted prompts
* content validation
* no automatic sending
* no automatic irreversible action
* agent-edit capability

---

# 20. AI Abuse and Cost Protection

AI endpoints may create cost and rate-limit risk.

Future security controls should include:

* authentication
* rate limiting
* per-user usage limits
* duplicate-request prevention
* request-size limits
* analysis cooldown
* cost monitoring
* token-usage monitoring

For the MVP:

* block duplicate analysis while one is running
* limit ticket-description length
* require explicit analysis requests
* avoid automatic repeated regeneration

---

# 21. Logging Security

## 21.1 Safe Logging

Logs may include:

* request ID
* operation name
* ticket public ID
* event type
* success or failure
* response status
* execution duration
* exception category

## 21.2 Prohibited Logging

Logs must not include:

* AI API key
* database password
* complete environment variables
* full connection strings with credentials
* full ticket descriptions
* raw prompts containing customer data
* full AI responses containing sensitive information
* access tokens
* private keys

## 21.3 Error Logging

Internal errors should be logged with enough detail for debugging while avoiding sensitive data.

User-facing responses must remain generic.

## 21.4 Log Access

In future environments:

* log access should be restricted
* log retention should be defined
* sensitive logs should be deleted appropriately
* access should be auditable

---

# 22. Database Security

## 22.1 Database Credentials

Database credentials should:

* be stored in environment variables
* use separate values per environment
* not be committed
* be rotated when exposed

## 22.2 Database User Permissions

The application database user should have only required permissions.

It should not have unnecessary administrative permissions.

For production, separate roles may be used for:

* application runtime
* migrations
* administration
* backups

## 22.3 Network Exposure

In production, PostgreSQL should not be directly accessible from the public internet.

Only authorized backend services and administrators should reach it.

## 22.4 Backups

Production planning should include:

* automated backups
* backup encryption
* restore testing
* retention policy
* access restrictions

Backups are outside the MVP but required for real deployment.

---

# 23. Data Retention and Deletion

The MVP uses ticket closure instead of public permanent deletion.

Future data-retention policy should define:

* how long tickets are retained
* when closed tickets are archived
* when customer data is deleted
* how deletion requests are handled
* whether AI-provider data must also be deleted
* how backups are affected

Permanent deletion should require:

* authorization
* confirmation
* audit logging
* clear business justification

---

# 24. Frontend Security

The frontend should:

* validate forms for user experience
* rely on backend validation for enforcement
* escape user-generated content
* avoid unsafe HTML rendering
* avoid storing secrets
* avoid exposing internal errors
* avoid logging sensitive data in the browser console
* handle API errors safely
* use secure HTTPS endpoints in production

## 24.1 Browser Storage

Sensitive ticket data should not be stored unnecessarily in:

* local storage
* session storage
* browser cookies

Future authentication tokens should be handled using a carefully selected secure strategy.

---

# 25. Secure HTTP and HTTPS

Local development may use HTTP.

Production must use HTTPS.

HTTPS protects:

* login credentials
* ticket content
* API responses
* authentication tokens
* AI-related requests between frontend and backend

The system should redirect insecure production traffic to HTTPS where supported.

---

# 26. Security Headers

Future production deployment should configure security headers such as:

* Content Security Policy
* X-Content-Type-Options
* Referrer-Policy
* Permissions-Policy
* Strict-Transport-Security
* frame protection

The exact implementation may be handled by:

* backend middleware
* reverse proxy
* hosting platform
* CDN

---

# 27. Docker Security

Docker images should:

* use trusted official base images
* use pinned major or minor versions where practical
* install only required packages
* avoid embedding secrets
* avoid running as root where practical
* keep image size minimal
* remove unnecessary build files
* expose only required ports

## 27.1 Docker Compose Security

Docker Compose should:

* use environment variables
* avoid hardcoded production credentials
* avoid exposing unnecessary ports
* use named volumes
* keep development settings separate from production
* avoid privileged containers
* avoid mounting sensitive host directories

---

# 28. Dependency Security

The project depends on Python and JavaScript packages.

Risks include:

* known vulnerabilities
* malicious packages
* abandoned packages
* dependency confusion
* unreviewed updates

Controls should include:

* use well-known packages
* review dependency purpose
* pin compatible versions
* update dependencies regularly
* remove unused dependencies
* run dependency scanning
* review major-version upgrades
* avoid copying untrusted installation commands

---

# 29. GitHub Security

## 29.1 Repository Access

Repository write access should be limited.

Use:

* protected `main` branch
* required pull requests
* required CI checks
* restricted force pushes
* restricted branch deletion

## 29.2 Secret Scanning

GitHub secret scanning or equivalent checks should be enabled where available.

## 29.3 Dependency Alerts

Dependency alerts should be reviewed and addressed based on severity and exploitability.

## 29.4 Pull Request Review

Security-sensitive changes should receive additional attention.

Examples include:

* authentication
* authorization
* secret handling
* CORS
* database queries
* AI prompt construction
* file handling
* deployment configuration

---

# 30. CI Security

GitHub Actions should follow least privilege.

Workflows should:

* request only required permissions
* avoid printing secrets
* use repository secrets for protected values
* avoid running untrusted scripts with secrets
* pin trusted actions where practical
* separate live AI tests from normal CI
* fail when critical checks fail

Pull requests from untrusted sources should not automatically receive sensitive credentials.

---

# 31. Security Testing

Security testing should include:

* invalid-input tests
* oversized-input tests
* SQL-injection attempts
* prompt-injection attempts
* unsupported enum tests
* error-information exposure tests
* CORS checks
* secret-leak checks
* dependency scans
* Docker image scans where practical

Future testing may include:

* penetration testing
* dynamic application security testing
* authenticated authorization testing
* threat-model reviews
* security code review

---

# 32. Rate Limiting

Rate limiting is not included in the initial MVP.

It should be added before public exposure.

High-priority endpoints for future rate limiting:

* ticket creation
* ticket search
* AI analysis
* AI regeneration
* authentication endpoints

Rate limits should balance:

* legitimate use
* denial-of-service protection
* AI-provider cost
* user experience

---

# 33. Denial-of-Service Protection

Potential denial-of-service risks include:

* very large request bodies
* excessive ticket creation
* repeated AI-analysis requests
* expensive search queries
* excessive pagination size

MVP protections include:

* field-length limits
* page-size limits
* controlled sort fields
* duplicate-analysis prevention
* AI timeouts

Future protections include:

* authentication
* rate limiting
* gateway limits
* request-body limits
* monitoring
* blocking abusive clients

---

# 34. File Upload Security

File attachments are outside the MVP.

Before file uploads are introduced, the project must define:

* allowed file types
* maximum file size
* malware scanning
* storage location
* filename sanitization
* content-type verification
* download authorization
* retention and deletion
* protection against executable uploads

---

# 35. Error and Failure Security

The system should fail securely.

Examples:

* invalid AI output should not be stored
* database failure should roll back the transaction
* missing configuration should prevent unsafe startup
* unavailable AI should not block ticket retrieval
* unauthorized future actions should be rejected by default
* unknown exceptions should return generic errors

---

# 36. Security Incident Handling

A future production system should define an incident process.

Basic incident steps:

1. Identify the issue.
2. Contain the exposure.
3. Revoke affected secrets.
4. Preserve relevant evidence.
5. Assess impacted data.
6. Fix the root cause.
7. Validate the fix.
8. Communicate with affected stakeholders where required.
9. Document lessons learned.
10. Add regression tests.

For a learning project, any exposed credential should be revoked immediately.

---

# 37. Vulnerability Severity

| Severity | Description                                                   |
| -------- | ------------------------------------------------------------- |
| Critical | Credential exposure, remote code execution, major data breach |
| High     | Unauthorized data access or major security-control bypass     |
| Medium   | Limited exposure or exploit requiring specific conditions     |
| Low      | Minor weakness with limited impact                            |

Critical and high vulnerabilities should block deployment.

---

# 38. Security Review Before Merge

A security review is especially important when a change includes:

* new external API integration
* new environment variables
* new database queries
* raw HTML rendering
* file uploads
* authentication
* authorization
* new CORS settings
* new Docker permissions
* new GitHub Actions permissions
* user-controlled URLs
* AI prompt changes

---

# 39. Security Review Before Deployment

Before a public or shared deployment:

* [ ] HTTPS is enabled
* [ ] Authentication is implemented
* [ ] Authorization is implemented
* [ ] Production secrets are securely stored
* [ ] Development credentials are removed
* [ ] CORS is restricted
* [ ] Database is not publicly exposed
* [ ] Debug mode is disabled
* [ ] API documentation exposure is reviewed
* [ ] Rate limiting is enabled
* [ ] Input-size limits are enforced
* [ ] Logs do not expose sensitive data
* [ ] Dependency scans pass
* [ ] Docker image scans pass where available
* [ ] Database backups are configured
* [ ] Restore process is tested
* [ ] Monitoring and alerts are configured
* [ ] Incident-response contacts are defined
* [ ] Only synthetic or approved data is present

---

# 40. Secure Development Checklist

* [ ] No secrets are hardcoded
* [ ] `.env` files are ignored
* [ ] `.env.example` contains placeholders only
* [ ] All inputs are validated
* [ ] Maximum lengths are enforced
* [ ] SQLAlchemy parameterization is used
* [ ] User content is rendered as plain text
* [ ] AI output is validated
* [ ] AI output is not executed
* [ ] AI responses remain drafts
* [ ] Logs exclude sensitive content
* [ ] CORS is configured explicitly
* [ ] Error responses hide internal details
* [ ] Dependencies are reviewed
* [ ] Security-related tests are included
* [ ] Documentation is updated

---

# 41. Open Security Decisions

The following decisions should be addressed before production use:

* Which authentication mechanism will be used?
* How will access tokens be stored?
* Which authorization roles will exist?
* What ticket data may be sent to the AI provider?
* What is the data-retention period?
* How will customer-deletion requests be handled?
* Which rate-limiting strategy will be used?
* Which secrets manager will be used?
* How will audit logs be stored?
* Which production security headers will be enabled?
* How will dependency scanning be enforced?
* How will Docker image scanning be performed?
* Which monitoring and alerting platform will be used?
* Should sensitive ticket text be automatically redacted?

---

# 42. Related Documents

| Document               | Location                     |
| ---------------------- | ---------------------------- |
| Problem Definition     | `docs/PROBLEM_DEFINITION.md` |
| Requirements           | `docs/REQUIREMENTS.md`       |
| High-Level Design      | `docs/HLD.md`                |
| Low-Level Design       | `docs/LLD.md`                |
| API Specification      | `docs/API_SPEC.md`           |
| Testing Strategy       | `docs/TESTING.md`            |
| Architecture Decisions | `docs/adr/`                  |
| Setup Guide            | `docs/SETUP.md`              |
| Deployment Guide       | `docs/DEPLOYMENT.md`         |

---

# 43. Document History

| Version | Date       | Author               | Description                 |
| ------- | ---------- | -------------------- | --------------------------- |
| 1.0     | 2026-07-26 | Raja Rangarao Moturi | Initial Security Guidelines |
