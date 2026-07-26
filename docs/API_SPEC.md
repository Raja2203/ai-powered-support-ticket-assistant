# AI-Powered Support Ticket Assistant

## API Specification

---

## 1. Document Information

| Field           | Value                               |
| --------------- | ----------------------------------- |
| Project Name    | AI-Powered Support Ticket Assistant |
| Document Type   | API Specification                   |
| Document Status | Draft                               |
| Version         | 1.0                                 |
| Author          | Raja Rangarao Moturi                |
| Last Updated    | 2026-07-26                          |

---

## 2. Purpose

This document defines the REST API contracts for the AI-Powered Support Ticket Assistant.

It describes:

* API naming conventions
* API versioning
* endpoint responsibilities
* request fields
* response fields
* validation rules
* HTTP status codes
* pagination
* filtering
* sorting
* standard error responses
* AI-analysis operations

This document defines the expected external behavior of the backend. It does not contain implementation details.

---

## 3. API Overview

The backend exposes REST APIs for:

* application health checks
* application readiness checks
* ticket creation
* ticket retrieval
* ticket listing
* ticket updates
* ticket status changes
* AI ticket analysis
* manual correction of AI-generated values

The frontend and external API clients communicate with the backend using JSON.

---

## 4. Base URL

### 4.1 Local Development

```text
http://localhost:8000
```

### 4.2 API Version Prefix

```text
/api/v1
```

### 4.3 Complete Local API Base URL

```text
http://localhost:8000/api/v1
```

All MVP business APIs should use the `/api/v1` prefix.

---

## 5. API Design Principles

The API will follow these principles:

* use nouns for resource paths
* use standard HTTP methods
* use JSON request and response bodies
* use consistent error structures
* use stable application error codes
* validate all client input
* avoid exposing database details
* avoid exposing AI-provider details
* use pagination for collection endpoints
* use ISO 8601 timestamps
* use uppercase controlled values for enums
* keep AI operations explicit
* prevent automatic sending of AI-generated responses

---

## 6. Content Type

Requests containing a body should use:

```text
Content-Type: application/json
```

Responses will use:

```text
Content-Type: application/json
```

File uploads are outside the MVP scope.

---

## 7. Date and Time Format

All timestamps should use ISO 8601 format in UTC.

Example:

```text
2026-07-26T15:30:45Z
```

The backend should store timestamps consistently and avoid returning server-local time without timezone information.

---

## 8. Controlled Values

## 8.1 Ticket Status

Supported ticket statuses:

* `OPEN`
* `IN_PROGRESS`
* `RESOLVED`
* `CLOSED`

## 8.2 Ticket Category

Supported ticket categories:

* `PAYMENT`
* `DELIVERY`
* `ACCOUNT`
* `REFUND`
* `TECHNICAL`
* `OTHER`

## 8.3 Ticket Priority

Supported ticket priorities:

* `LOW`
* `MEDIUM`
* `HIGH`
* `CRITICAL`

## 8.4 AI Analysis Status

Supported AI-analysis statuses:

* `NOT_REQUESTED`
* `IN_PROGRESS`
* `COMPLETED`
* `FAILED`
* `INVALID_OUTPUT`

## 8.5 Support Team

Initial supported teams:

* `PAYMENTS_SUPPORT`
* `DELIVERY_SUPPORT`
* `ACCOUNT_SUPPORT`
* `REFUND_SUPPORT`
* `TECHNICAL_SUPPORT`
* `GENERAL_SUPPORT`

Human-readable team names may be displayed by the frontend.

---

## 9. Common Ticket Resource

A ticket resource may contain the following fields:

| Field                | Type              | Description                                   |
| -------------------- | ----------------- | --------------------------------------------- |
| `id`                 | Integer           | Internal ticket identifier                    |
| `public_id`          | String            | User-facing ticket identifier                 |
| `customer_name`      | String            | Customer name                                 |
| `customer_email`     | String            | Customer email address                        |
| `subject`            | String            | Short issue title                             |
| `description`        | String            | Detailed customer issue                       |
| `status`             | String            | Current ticket status                         |
| `category`           | String or null    | Ticket category                               |
| `priority`           | String            | Ticket priority                               |
| `assigned_team`      | String or null    | Recommended or selected support team          |
| `ai_summary`         | String or null    | AI-generated ticket summary                   |
| `suggested_response` | String or null    | AI-generated response draft                   |
| `ai_analysis_status` | String            | Current AI-analysis state                     |
| `ai_model`           | String or null    | Model used for the latest successful analysis |
| `prompt_version`     | String or null    | Prompt version used for analysis              |
| `ai_analyzed_at`     | Timestamp or null | Time of the latest successful analysis        |
| `created_at`         | Timestamp         | Ticket creation time                          |
| `updated_at`         | Timestamp         | Ticket last modification time                 |
| `closed_at`          | Timestamp or null | Ticket closure time                           |

The final response may hide internal fields that are not useful to API consumers.

---

# 10. Operational APIs

## 10.1 Health Check

### Endpoint

```text
GET /health
```

### Purpose

Confirms that the FastAPI application process is running.

This endpoint should not depend on:

* PostgreSQL
* the AI provider
* frontend availability
* external services

### Request Parameters

None.

### Successful Response

**HTTP status:** `200 OK`

Example:

```json
{
  "status": "healthy",
  "service": "ai-support-ticket-assistant",
  "version": "1.0.0",
  "timestamp": "2026-07-26T15:30:45Z"
}
```

### Possible Errors

| Status                      | Scenario                                     |
| --------------------------- | -------------------------------------------- |
| `500 Internal Server Error` | Application cannot produce a health response |

---

## 10.2 Readiness Check

### Endpoint

```text
GET /ready
```

### Purpose

Confirms that the application is ready to handle ticket requests.

The readiness check should verify:

* required application configuration is available
* PostgreSQL is reachable
* a lightweight database query can be completed

The readiness check should not make an AI request.

### Request Parameters

None.

### Successful Response

**HTTP status:** `200 OK`

```json
{
  "status": "ready",
  "components": {
    "application": "ready",
    "database": "ready"
  },
  "timestamp": "2026-07-26T15:30:45Z"
}
```

### Failure Response

**HTTP status:** `503 Service Unavailable`

```json
{
  "status": "not_ready",
  "components": {
    "application": "ready",
    "database": "unavailable"
  },
  "timestamp": "2026-07-26T15:30:45Z"
}
```

---

# 11. Ticket APIs

## 11.1 Create Ticket

### Endpoint

```text
POST /api/v1/tickets
```

### Purpose

Creates a new customer-support ticket.

AI analysis will not run automatically during ticket creation in the MVP.

### Request Body

| Field            | Required | Type   | Description                |
| ---------------- | -------: | ------ | -------------------------- |
| `customer_name`  |      Yes | String | Name of the customer       |
| `customer_email` |      Yes | String | Valid customer email       |
| `subject`        |      Yes | String | Short issue title          |
| `description`    |      Yes | String | Detailed issue description |

### Example Request

```json
{
  "customer_name": "Raja Moturi",
  "customer_email": "raja@example.com",
  "subject": "Payment deducted but order failed",
  "description": "The payment was deducted from my account, but the order is showing as failed."
}
```

### Backend-Assigned Defaults

The client cannot provide these values during creation:

| Field                | Default         |
| -------------------- | --------------- |
| `status`             | `OPEN`          |
| `priority`           | `MEDIUM`        |
| `category`           | `null`          |
| `assigned_team`      | `null`          |
| `ai_analysis_status` | `NOT_REQUESTED` |
| `ai_summary`         | `null`          |
| `suggested_response` | `null`          |

### Successful Response

**HTTP status:** `201 Created`

```json
{
  "id": 1,
  "public_id": "TKT-20260726-000001",
  "customer_name": "Raja Moturi",
  "customer_email": "raja@example.com",
  "subject": "Payment deducted but order failed",
  "description": "The payment was deducted from my account, but the order is showing as failed.",
  "status": "OPEN",
  "category": null,
  "priority": "MEDIUM",
  "assigned_team": null,
  "ai_summary": null,
  "suggested_response": null,
  "ai_analysis_status": "NOT_REQUESTED",
  "ai_model": null,
  "prompt_version": null,
  "ai_analyzed_at": null,
  "created_at": "2026-07-26T15:30:45Z",
  "updated_at": "2026-07-26T15:30:45Z",
  "closed_at": null
}
```

### Possible Errors

| Status                      | Error Code              | Scenario                              |
| --------------------------- | ----------------------- | ------------------------------------- |
| `422 Unprocessable Entity`  | `VALIDATION_ERROR`      | Request fields are missing or invalid |
| `503 Service Unavailable`   | `DATABASE_UNAVAILABLE`  | Ticket cannot be stored               |
| `500 Internal Server Error` | `INTERNAL_SERVER_ERROR` | Unexpected failure                    |

---

## 11.2 Get Ticket by Public ID

### Endpoint

```text
GET /api/v1/tickets/{ticket_id}
```

### Purpose

Retrieves one ticket using its public identifier.

### Path Parameter

| Parameter   | Type   | Description              |
| ----------- | ------ | ------------------------ |
| `ticket_id` | String | Public ticket identifier |

Example:

```text
GET /api/v1/tickets/TKT-20260726-000001
```

### Successful Response

**HTTP status:** `200 OK`

The response contains the complete ticket resource.

### Possible Errors

| Status                      | Error Code              | Scenario                            |
| --------------------------- | ----------------------- | ----------------------------------- |
| `404 Not Found`             | `TICKET_NOT_FOUND`      | Ticket does not exist               |
| `422 Unprocessable Entity`  | `VALIDATION_ERROR`      | Ticket identifier format is invalid |
| `503 Service Unavailable`   | `DATABASE_UNAVAILABLE`  | Database is unavailable             |
| `500 Internal Server Error` | `INTERNAL_SERVER_ERROR` | Unexpected failure                  |

---

## 11.3 List Tickets

### Endpoint

```text
GET /api/v1/tickets
```

### Purpose

Returns a filtered, sorted, and paginated list of tickets.

### Query Parameters

| Parameter            | Required | Type    | Default      | Description                       |
| -------------------- | -------: | ------- | ------------ | --------------------------------- |
| `page`               |       No | Integer | `1`          | Requested page                    |
| `page_size`          |       No | Integer | `20`         | Number of records per page        |
| `status`             |       No | String  | None         | Filter by ticket status           |
| `category`           |       No | String  | None         | Filter by category                |
| `priority`           |       No | String  | None         | Filter by priority                |
| `assigned_team`      |       No | String  | None         | Filter by assigned team           |
| `customer_email`     |       No | String  | None         | Filter by customer email          |
| `ai_analysis_status` |       No | String  | None         | Filter by AI-analysis status      |
| `created_from`       |       No | Date    | None         | Tickets created on or after date  |
| `created_to`         |       No | Date    | None         | Tickets created on or before date |
| `search`             |       No | String  | None         | Search selected text fields       |
| `sort_by`            |       No | String  | `created_at` | Field used for sorting            |
| `sort_order`         |       No | String  | `desc`       | Sort direction                    |

### Pagination Rules

* minimum page value: `1`
* default page size: `20`
* maximum page size: `100`
* values outside the supported range should be rejected consistently

### Supported Sort Fields

* `created_at`
* `updated_at`
* `priority`
* `status`

### Supported Sort Orders

* `asc`
* `desc`

### Example Request

```text
GET /api/v1/tickets?status=OPEN&priority=HIGH&page=1&page_size=20&sort_by=created_at&sort_order=desc
```

### Successful Response

**HTTP status:** `200 OK`

```json
{
  "items": [
    {
      "id": 1,
      "public_id": "TKT-20260726-000001",
      "customer_name": "Raja Moturi",
      "customer_email": "raja@example.com",
      "subject": "Payment deducted but order failed",
      "status": "OPEN",
      "category": "PAYMENT",
      "priority": "HIGH",
      "assigned_team": "PAYMENTS_SUPPORT",
      "ai_analysis_status": "COMPLETED",
      "created_at": "2026-07-26T15:30:45Z",
      "updated_at": "2026-07-26T15:35:12Z"
    }
  ],
  "pagination": {
    "page": 1,
    "page_size": 20,
    "total_items": 1,
    "total_pages": 1,
    "has_next": false,
    "has_previous": false
  },
  "sorting": {
    "sort_by": "created_at",
    "sort_order": "desc"
  }
}
```

### Possible Errors

| Status                      | Error Code              | Scenario                                         |
| --------------------------- | ----------------------- | ------------------------------------------------ |
| `422 Unprocessable Entity`  | `VALIDATION_ERROR`      | Unsupported filter, pagination, or sorting value |
| `503 Service Unavailable`   | `DATABASE_UNAVAILABLE`  | Database is unavailable                          |
| `500 Internal Server Error` | `INTERNAL_SERVER_ERROR` | Unexpected failure                               |

---

## 11.4 Update Ticket Details

### Endpoint

```text
PATCH /api/v1/tickets/{ticket_id}
```

### Purpose

Partially updates editable customer-provided ticket details.

### Editable Fields

* `customer_name`
* `customer_email`
* `subject`
* `description`

### Restricted Fields

The general update API must not directly modify:

* ticket ID
* public ticket ID
* ticket status
* category
* priority
* assigned team
* AI summary
* suggested response
* AI-analysis status
* timestamps

Status changes and AI corrections use separate operations.

### Example Request

```json
{
  "subject": "Payment deducted twice",
  "description": "The payment appears to have been deducted twice for the same order."
}
```

### Successful Response

**HTTP status:** `200 OK`

The response contains the updated ticket resource.

### AI Analysis Impact

When the subject or description changes after successful AI analysis:

* the existing AI result may be marked as outdated
* the system should require explicit reanalysis
* the ticket should not silently treat old AI results as current

The exact stale-analysis representation will be finalized during implementation.

### Possible Errors

| Status                      | Error Code              | Scenario                       |
| --------------------------- | ----------------------- | ------------------------------ |
| `404 Not Found`             | `TICKET_NOT_FOUND`      | Ticket does not exist          |
| `409 Conflict`              | `TICKET_CLOSED`         | Closed ticket cannot be edited |
| `422 Unprocessable Entity`  | `VALIDATION_ERROR`      | Update fields are invalid      |
| `503 Service Unavailable`   | `DATABASE_UNAVAILABLE`  | Database update failed         |
| `500 Internal Server Error` | `INTERNAL_SERVER_ERROR` | Unexpected failure             |

---

## 11.5 Update Ticket Status

### Endpoint

```text
PATCH /api/v1/tickets/{ticket_id}/status
```

### Purpose

Changes the lifecycle status of a ticket.

### Request Body

| Field    | Required | Type   | Description           |
| -------- | -------: | ------ | --------------------- |
| `status` |      Yes | String | Requested next status |

### Example Request

```json
{
  "status": "IN_PROGRESS"
}
```

### Allowed Transitions

| Current Status | Allowed Next Status     |
| -------------- | ----------------------- |
| `OPEN`         | `IN_PROGRESS`, `CLOSED` |
| `IN_PROGRESS`  | `RESOLVED`, `CLOSED`    |
| `RESOLVED`     | `IN_PROGRESS`, `CLOSED` |
| `CLOSED`       | None                    |

### Successful Response

**HTTP status:** `200 OK`

```json
{
  "public_id": "TKT-20260726-000001",
  "previous_status": "OPEN",
  "current_status": "IN_PROGRESS",
  "updated_at": "2026-07-26T15:45:00Z"
}
```

### Possible Errors

| Status                      | Error Code                  | Scenario                            |
| --------------------------- | --------------------------- | ----------------------------------- |
| `404 Not Found`             | `TICKET_NOT_FOUND`          | Ticket does not exist               |
| `409 Conflict`              | `INVALID_STATUS_TRANSITION` | Requested transition is not allowed |
| `422 Unprocessable Entity`  | `INVALID_TICKET_STATUS`     | Unsupported status value            |
| `503 Service Unavailable`   | `DATABASE_UNAVAILABLE`      | Database update failed              |
| `500 Internal Server Error` | `INTERNAL_SERVER_ERROR`     | Unexpected failure                  |

---

## 11.6 Close Ticket

Closing a ticket uses the status-update endpoint.

### Example

```text
PATCH /api/v1/tickets/{ticket_id}/status
```

```json
{
  "status": "CLOSED"
}
```

A separate public `DELETE` operation will not be included in the MVP.

This avoids accidental permanent deletion and preserves ticket history.

---

# 12. AI APIs

## 12.1 Analyze Ticket

### Endpoint

```text
POST /api/v1/tickets/{ticket_id}/analysis
```

### Purpose

Requests AI analysis for an existing ticket.

The operation generates:

* category
* priority
* summary
* recommended support team
* suggested response

### Path Parameter

| Parameter   | Type   | Description              |
| ----------- | ------ | ------------------------ |
| `ticket_id` | String | Public ticket identifier |

### Request Body

The first version does not require a body.

An optional future request may contain explicit regeneration settings.

### Preconditions

The ticket must:

* exist
* not be closed
* contain a valid subject
* contain a valid description
* not already have an analysis running

### Processing Rules

1. Retrieve the ticket.
2. Confirm that analysis can run.
3. Record the analysis attempt.
4. Send required ticket data to the AI provider.
5. Parse the AI response.
6. Validate all returned fields.
7. Reject invalid output.
8. Save only validated output.
9. Return the updated analysis.
10. Keep the generated response as a draft.

### Successful Response

**HTTP status:** `200 OK`

```json
{
  "public_id": "TKT-20260726-000001",
  "analysis_status": "COMPLETED",
  "analysis": {
    "category": "PAYMENT",
    "priority": "HIGH",
    "summary": "The customer reports that payment was deducted, but the related order failed.",
    "recommended_team": "PAYMENTS_SUPPORT",
    "suggested_response": "We are sorry for the inconvenience. Our payments team will review the transaction and verify the order status."
  },
  "metadata": {
    "ai_model": "configured-model-name",
    "prompt_version": "ticket-analysis-v1",
    "analyzed_at": "2026-07-26T15:50:00Z"
  }
}
```

### Possible Errors

| Status                      | Error Code                | Scenario                                    |
| --------------------------- | ------------------------- | ------------------------------------------- |
| `404 Not Found`             | `TICKET_NOT_FOUND`        | Ticket does not exist                       |
| `409 Conflict`              | `AI_ANALYSIS_IN_PROGRESS` | Analysis is already running                 |
| `409 Conflict`              | `TICKET_CLOSED`           | Closed ticket cannot be analyzed            |
| `422 Unprocessable Entity`  | `TICKET_CONTENT_INVALID`  | Ticket lacks usable content                 |
| `500 Internal Server Error` | `AI_CONFIGURATION_ERROR`  | AI configuration is missing or invalid      |
| `502 Bad Gateway`           | `AI_INVALID_OUTPUT`       | AI returned malformed or unsupported output |
| `503 Service Unavailable`   | `AI_PROVIDER_UNAVAILABLE` | AI provider cannot process the request      |
| `504 Gateway Timeout`       | `AI_REQUEST_TIMEOUT`      | AI request exceeded the timeout             |
| `503 Service Unavailable`   | `DATABASE_UNAVAILABLE`    | Analysis result cannot be stored            |

---

## 12.2 Regenerate Ticket Analysis

The MVP can use the same analysis endpoint for regeneration.

### Endpoint

```text
POST /api/v1/tickets/{ticket_id}/analysis
```

### Regeneration Conditions

Regeneration is permitted when:

* previous analysis failed
* previous output was invalid
* ticket content changed
* a support agent explicitly requests a new result

### Regeneration Rules

* previous valid analysis must remain until replacement succeeds
* failed replacement must not erase the previous valid result
* the latest successful result becomes the active analysis
* only the latest successful analysis must be retained in the MVP

A dedicated regeneration endpoint may be introduced later if clearer separation is needed.

---

## 12.3 Get Ticket Analysis

### Endpoint

```text
GET /api/v1/tickets/{ticket_id}/analysis
```

### Purpose

Returns the current AI-analysis result for a ticket.

### Successful Response

**HTTP status:** `200 OK`

```json
{
  "public_id": "TKT-20260726-000001",
  "analysis_status": "COMPLETED",
  "category": "PAYMENT",
  "priority": "HIGH",
  "summary": "The customer reports a payment deduction associated with a failed order.",
  "recommended_team": "PAYMENTS_SUPPORT",
  "suggested_response": "We are sorry for the inconvenience. Our payments team will review the transaction and verify the order status.",
  "ai_model": "configured-model-name",
  "prompt_version": "ticket-analysis-v1",
  "analyzed_at": "2026-07-26T15:50:00Z"
}
```

### Possible Errors

| Status                    | Error Code              | Scenario                          |
| ------------------------- | ----------------------- | --------------------------------- |
| `404 Not Found`           | `TICKET_NOT_FOUND`      | Ticket does not exist             |
| `404 Not Found`           | `AI_ANALYSIS_NOT_FOUND` | Ticket has no successful analysis |
| `503 Service Unavailable` | `DATABASE_UNAVAILABLE`  | Database is unavailable           |

---

## 12.4 Correct AI Analysis

### Endpoint

```text
PATCH /api/v1/tickets/{ticket_id}/analysis
```

### Purpose

Allows a support agent to correct AI-generated fields.

This operation represents human review and correction.

### Editable Fields

* `category`
* `priority`
* `assigned_team`
* `ai_summary`
* `suggested_response`

### Example Request

```json
{
  "priority": "MEDIUM",
  "assigned_team": "PAYMENTS_SUPPORT",
  "ai_summary": "Customer reports a delayed payment confirmation for an unsuccessful order."
}
```

### Validation Rules

* at least one field must be supplied
* category must be supported
* priority must be supported
* assigned team must be supported
* summary must satisfy length requirements
* suggested response must remain a draft
* correction must not change ticket status

### Successful Response

**HTTP status:** `200 OK`

The response contains the corrected ticket analysis.

### Possible Errors

| Status                     | Error Code              | Scenario                         |
| -------------------------- | ----------------------- | -------------------------------- |
| `404 Not Found`            | `TICKET_NOT_FOUND`      | Ticket does not exist            |
| `404 Not Found`            | `AI_ANALYSIS_NOT_FOUND` | No analysis exists to correct    |
| `409 Conflict`             | `TICKET_CLOSED`         | Closed ticket cannot be modified |
| `422 Unprocessable Entity` | `VALIDATION_ERROR`      | Corrected values are invalid     |
| `503 Service Unavailable`  | `DATABASE_UNAVAILABLE`  | Changes cannot be stored         |

For the MVP, corrected values may replace current stored values. Full correction history is a future enhancement.

---

# 13. Standard Error Response

All application errors should follow a consistent structure.

## 13.1 Error Response Fields

| Field        | Type                   | Description                         |
| ------------ | ---------------------- | ----------------------------------- |
| `error_code` | String                 | Stable application error identifier |
| `message`    | String                 | Human-readable error message        |
| `path`       | String                 | Request path                        |
| `timestamp`  | Timestamp              | Time the error occurred             |
| `request_id` | String or null         | Request correlation identifier      |
| `details`    | Object, array, or null | Optional additional information     |

### Example

```json
{
  "error_code": "TICKET_NOT_FOUND",
  "message": "The requested ticket was not found.",
  "path": "/api/v1/tickets/TKT-20260726-999999",
  "timestamp": "2026-07-26T16:00:00Z",
  "request_id": "req-7ca321",
  "details": null
}
```

---

## 14. Validation Error Response

Validation errors may contain field-level information.

### Example

```json
{
  "error_code": "VALIDATION_ERROR",
  "message": "The request contains invalid fields.",
  "path": "/api/v1/tickets",
  "timestamp": "2026-07-26T16:00:00Z",
  "request_id": "req-4ad251",
  "details": [
    {
      "field": "customer_email",
      "message": "A valid email address is required."
    },
    {
      "field": "description",
      "message": "Description must not be empty."
    }
  ]
}
```

The API should not expose internal framework traces or Python exception details.

---

## 15. Stable Application Error Codes

## 15.1 Ticket Errors

* `TICKET_NOT_FOUND`
* `TICKET_CLOSED`
* `TICKET_CONTENT_INVALID`
* `INVALID_TICKET_STATUS`
* `INVALID_STATUS_TRANSITION`
* `INVALID_TICKET_CATEGORY`
* `INVALID_TICKET_PRIORITY`
* `INVALID_SUPPORT_TEAM`

## 15.2 AI Errors

* `AI_ANALYSIS_NOT_FOUND`
* `AI_ANALYSIS_IN_PROGRESS`
* `AI_CONFIGURATION_ERROR`
* `AI_PROVIDER_UNAVAILABLE`
* `AI_REQUEST_TIMEOUT`
* `AI_INVALID_OUTPUT`
* `AI_RATE_LIMITED`
* `AI_AUTHENTICATION_FAILED`
* `AI_ANALYSIS_STALE`

## 15.3 Database Errors

* `DATABASE_UNAVAILABLE`
* `DATABASE_OPERATION_FAILED`
* `TRANSACTION_FAILED`

## 15.4 General Errors

* `VALIDATION_ERROR`
* `RESOURCE_CONFLICT`
* `INTERNAL_SERVER_ERROR`

---

## 16. HTTP Status Code Usage

| HTTP Status                 | Usage                                                    |
| --------------------------- | -------------------------------------------------------- |
| `200 OK`                    | Successful retrieval, update, status change, or analysis |
| `201 Created`               | Ticket successfully created                              |
| `400 Bad Request`           | Request cannot be processed due to general client error  |
| `404 Not Found`             | Requested ticket or analysis does not exist              |
| `409 Conflict`              | Business-rule or resource-state conflict                 |
| `422 Unprocessable Entity`  | Request validation failed                                |
| `500 Internal Server Error` | Unexpected application failure                           |
| `502 Bad Gateway`           | External AI provider returned unusable output            |
| `503 Service Unavailable`   | Required database or AI provider is unavailable          |
| `504 Gateway Timeout`       | AI provider did not respond within the timeout           |

---

## 17. Request Validation Rules

## 17.1 Customer Name

* required during creation
* leading and trailing whitespace removed
* cannot contain only whitespace
* recommended minimum length: `2`
* recommended maximum length: `100`

## 17.2 Customer Email

* required during creation
* must use valid email format
* recommended maximum length: `255`
* should be normalized consistently

## 17.3 Subject

* required during creation
* cannot contain only whitespace
* recommended minimum length: `5`
* recommended maximum length: `200`

## 17.4 Description

* required during creation
* cannot contain only whitespace
* recommended minimum length: `10`
* recommended maximum length: `5000`

## 17.5 AI Summary

* required after successful analysis
* cannot contain only whitespace
* recommended maximum length: `1000`

## 17.6 Suggested Response

* required after successful analysis
* cannot contain only whitespace
* recommended maximum length: `3000`
* must be treated as a draft
* should not claim an action was completed unless ticket data confirms it

## 17.7 Pagination

* page must be at least `1`
* page size must be between `1` and `100`

## 17.8 Date Range

* `created_from` must not occur after `created_to`
* unsupported date formats must be rejected

---

## 18. Search Behaviour

The `search` query parameter may search:

* public ticket ID
* subject
* description
* customer email

Search should:

* be case-insensitive where practical
* trim unnecessary whitespace
* reject unreasonably long search strings
* avoid exposing raw database query capabilities

Advanced search is outside the MVP.

---

## 19. Sorting Behaviour

The API should use a controlled list of sortable fields.

Clients must not pass arbitrary database column names.

Default ticket sorting:

```text
created_at descending
```

When two records share the same primary sort value, the backend should use a stable secondary sort, such as ticket ID.

---

## 20. Idempotency and Duplicate Requests

## 20.1 Ticket Creation

Ticket creation is not automatically idempotent in the MVP.

Submitting the same request twice may create two tickets.

Future versions may support idempotency keys.

## 20.2 AI Analysis

The system should reject or safely handle duplicate analysis requests while an analysis is already running.

## 20.3 Status Updates

Requesting the current status again may either:

* return the unchanged resource successfully
* return a controlled conflict

The selected behaviour must remain consistent.

The recommended MVP behaviour is to return the unchanged ticket successfully when the requested status already matches the current status.

---

## 21. Concurrency Behaviour

The API should protect against:

* multiple simultaneous AI-analysis requests
* stale AI results overwriting newer ticket content
* conflicting ticket updates
* status changes based on outdated ticket state

For the MVP:

* duplicate in-progress analysis requests are rejected
* AI results are rejected when the ticket changed during processing
* closed tickets cannot be modified
* update timestamps support basic stale-data detection

---

## 22. Authentication and Authorization

Authentication and authorization are outside the MVP.

Until security is added:

* the API must use only test data
* the application must not process real customer-sensitive information
* the system should not be publicly exposed without protection

Future versions may define roles such as:

* customer
* support agent
* administrator

---

## 23. Rate Limiting

Rate limiting is outside the initial MVP.

Future rate limits may apply to:

* ticket creation
* ticket search
* AI-analysis requests
* analysis regeneration

AI-analysis endpoints are the highest priority for future rate limiting because external model calls may introduce cost and provider limits.

---

## 24. API Documentation

FastAPI-generated OpenAPI documentation should be available during development.

Expected development interfaces:

```text
/docs
/redoc
/openapi.json
```

Production exposure of interactive API documentation should be controlled through configuration.

The generated API documentation should remain aligned with this specification.

---

## 25. Initial Endpoint Summary

| Method  | Endpoint                               | Purpose                            |
| ------- | -------------------------------------- | ---------------------------------- |
| `GET`   | `/health`                              | Confirm backend process health     |
| `GET`   | `/ready`                               | Confirm application readiness      |
| `POST`  | `/api/v1/tickets`                      | Create a ticket                    |
| `GET`   | `/api/v1/tickets`                      | List and filter tickets            |
| `GET`   | `/api/v1/tickets/{ticket_id}`          | Retrieve one ticket                |
| `PATCH` | `/api/v1/tickets/{ticket_id}`          | Update ticket details              |
| `PATCH` | `/api/v1/tickets/{ticket_id}/status`   | Change ticket status               |
| `POST`  | `/api/v1/tickets/{ticket_id}/analysis` | Generate or regenerate AI analysis |
| `GET`   | `/api/v1/tickets/{ticket_id}/analysis` | Retrieve AI analysis               |
| `PATCH` | `/api/v1/tickets/{ticket_id}/analysis` | Correct AI-generated values        |

No public permanent-delete endpoint is included in the MVP.

---

## 26. API Implementation Order

The recommended implementation order is:

1. Health check
2. Readiness check
3. Create ticket
4. Get ticket by ID
5. List tickets
6. Update ticket details
7. Update ticket status
8. Analyze ticket
9. Retrieve ticket analysis
10. Correct AI analysis

This order keeps basic ticket management independent from AI integration.

---

## 27. Open API Decisions

The following decisions should be confirmed before implementation:

* Should public ticket IDs be included in the first MVP?
* Should health endpoints use the `/api/v1` prefix?
* Should AI analysis use `POST /analysis` or `POST /analyze`?
* Should corrected AI values overwrite generated values?
* Should manually corrected fields be marked separately?
* Should existing AI results be returned when regeneration fails?
* Should unchanged status updates return success or conflict?
* Should description text be included in search?
* Should list responses include full descriptions?
* Should the AI reasoning summary be exposed to agents?
* Should a separate endpoint approve suggested responses?
* Should closed tickets remain visible by default?

---

## 28. API Review Checklist

* [ ] Base URL is defined
* [ ] API versioning is defined
* [ ] Content type is defined
* [ ] Timestamp format is defined
* [ ] Controlled values are documented
* [ ] Health endpoint is documented
* [ ] Readiness endpoint is documented
* [ ] Ticket creation is documented
* [ ] Ticket retrieval is documented
* [ ] Ticket listing is documented
* [ ] Filtering is documented
* [ ] Pagination is documented
* [ ] Sorting is documented
* [ ] Ticket updates are documented
* [ ] Status transitions are documented
* [ ] Ticket closure is documented
* [ ] AI analysis is documented
* [ ] AI regeneration is documented
* [ ] AI correction is documented
* [ ] Standard errors are documented
* [ ] Stable error codes are defined
* [ ] Validation rules are documented
* [ ] Concurrency behaviour is documented
* [ ] Authentication limitations are documented
* [ ] No permanent-delete endpoint is included
* [ ] Open decisions are identified

---

## 29. Related Documents

| Document               | Location                     |
| ---------------------- | ---------------------------- |
| Problem Definition     | `docs/PROBLEM_DEFINITION.md` |
| Requirements Document  | `docs/REQUIREMENTS.md`       |
| High-Level Design      | `docs/HLD.md`                |
| Low-Level Design       | `docs/LLD.md`                |
| Testing Strategy       | `docs/TESTING.md`            |
| Security Guidelines    | `docs/SECURITY.md`           |
| Architecture Decisions | `docs/adr/`                  |
| Setup Guide            | `docs/SETUP.md`              |
| Deployment Guide       | `docs/DEPLOYMENT.md`         |

---

## 30. Document History

| Version | Date       | Author               | Description               |
| ------- | ---------- | -------------------- | ------------------------- |
| 1.0     | 2026-07-26 | Raja Rangarao Moturi | Initial API Specification |
