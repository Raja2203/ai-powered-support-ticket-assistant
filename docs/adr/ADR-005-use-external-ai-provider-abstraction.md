# ADR-005: Integrate an External AI Provider Through an Abstraction

---

## 1. Document Information

| Field         | Value                |
| ------------- | -------------------- |
| ADR Number    | ADR-005              |
| Status        | Accepted             |
| Decision Date | 2026-07-26           |
| Author        | Raja Rangarao Moturi |

---

## 2. Context

The system needs AI capabilities for:

* ticket classification
* ticket-priority recommendation
* ticket summarization
* support-team recommendation
* suggested-response generation

The backend must communicate with an AI model while remaining resilient to:

* timeouts
* invalid responses
* authentication failures
* provider outages
* rate limits
* model changes

The project has not yet selected the final external AI provider.

---

## 3. Decision Drivers

* beginner-friendly integration
* provider isolation
* structured-output support
* failure handling
* testability
* provider replacement
* prompt versioning
* cost awareness
* no model-training requirement

---

## 4. Options Considered

### Option 1: External AI Provider Through an AI Service

Advantages:

* quick integration
* no local model infrastructure
* access to capable hosted models
* provider-specific code remains isolated
* easy to mock during testing

Disadvantages:

* external cost
* network dependency
* data-privacy considerations
* rate limits and outages
* provider-specific behavior

### Option 2: Direct AI Calls from Routes

Advantages:

* fastest initial implementation
* fewer modules

Disadvantages:

* provider logic becomes coupled to HTTP routes
* difficult to test
* inconsistent timeout and error handling
* difficult to replace the provider

### Option 3: Local AI Model

Advantages:

* greater local data control
* no per-request provider API cost
* offline execution may be possible

Disadvantages:

* hardware requirements
* model setup complexity
* weaker beginner experience
* operational burden
* potentially lower output quality

### Option 4: Multiple Providers in the MVP

Advantages:

* fallback capability
* provider comparison
* reduced vendor dependency

Disadvantages:

* unnecessary complexity
* multiple SDKs
* inconsistent output
* more tests and configuration
* increased scope

---

## 5. Decision

The MVP will use **one external AI provider**.

Provider-specific communication will be isolated behind:

* an AI service
* an AI client
* provider-independent output schemas

The ticket service will not directly depend on provider SDK details.

The specific provider and model will be selected in a separate ADR when finalized.

---

## 6. Rationale

One external provider provides the simplest way to practise practical AI integration.

An abstraction is still necessary because it centralizes:

* prompt construction
* provider requests
* timeout handling
* response parsing
* error translation
* model configuration
* testing

The abstraction does not need to become a complex multi-provider framework.

---

## 7. Positive Consequences

* faster AI integration
* provider code remains isolated
* easier mocking
* easier model replacement
* consistent error handling
* centralized prompt management
* centralized timeout and retry configuration
* ticket logic remains provider independent

---

## 8. Negative Consequences

* external service dependency
* provider cost
* internet connectivity required
* privacy review required
* output may change when models change
* abstraction adds additional modules

---

## 9. Risks and Mitigations

| Risk                          | Mitigation                                              |
| ----------------------------- | ------------------------------------------------------- |
| AI provider is unavailable    | Return controlled errors and preserve ticket operations |
| AI returns invalid data       | Validate all output before saving                       |
| API costs increase            | Track usage and restrict unnecessary regeneration       |
| Provider changes its API      | Keep provider logic inside the AI client                |
| Sensitive data is transmitted | Minimize prompt data and use test data                  |
| Automated tests call live AI  | Use mocked provider responses                           |
| Model behavior changes        | Store model and prompt versions                         |

---

## 10. Review Conditions

Review this decision if:

* provider cost becomes unacceptable
* privacy requirements prevent hosted AI usage
* a local model becomes operationally justified
* multiple providers become a real availability requirement
* provider output quality becomes insufficient

---

## 11. Related Documents

* `docs/HLD.md`
* `docs/LLD.md`
* `docs/SECURITY.md`
