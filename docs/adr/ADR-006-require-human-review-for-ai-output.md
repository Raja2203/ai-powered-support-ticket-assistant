# ADR-006: Require Human Review for AI-Generated Output

---

## 1. Document Information

| Field         | Value                |
| ------------- | -------------------- |
| ADR Number    | ADR-006              |
| Status        | Accepted             |
| Decision Date | 2026-07-26           |
| Author        | Raja Rangarao Moturi |

---

## 2. Context

The AI provider will generate:

* ticket category
* ticket priority
* ticket summary
* recommended support team
* suggested customer response

AI-generated output may be incomplete, incorrect, misleading, or unsupported by the ticket.

Automatically sending AI-generated responses or applying irreversible actions could negatively affect customers and the business.

---

## 3. Decision Drivers

* AI output is probabilistic
* customer communication requires accuracy
* ticket priority may affect handling
* AI may hallucinate actions or facts
* safe AI engineering practices
* beginner-friendly risk control
* support-agent accountability
* ability to correct AI results

---

## 4. Options Considered

### Option 1: Human Review Before Use

Advantages:

* reduces incorrect customer communication
* allows correction
* creates clear accountability
* supports safe AI adoption
* suitable for early-stage AI quality

Disadvantages:

* does not fully automate the workflow
* requires agent time
* slower than autonomous response delivery

### Option 2: Automatic Response Sending

Advantages:

* maximum automation
* potentially faster first responses
* reduced agent effort

Disadvantages:

* risk of incorrect or harmful responses
* AI may claim unsupported actions
* difficult to control customer impact
* inappropriate for MVP

### Option 3: Confidence-Based Automation

Advantages:

* high-confidence results may be automated
* balances automation and review

Disadvantages:

* LLM confidence may not be reliable
* requires evaluation data
* requires thresholds and monitoring
* too complex for the MVP

---

## 5. Decision

All AI-generated information will be presented as a **suggestion**.

A human support agent must be able to:

* review the category
* review the priority
* review the recommended team
* review the summary
* edit the suggested response
* correct generated values
* reject unsuitable output

The MVP will not automatically send customer responses.

---

## 6. Rationale

AI can reduce repetitive effort without being treated as an authoritative decision-maker.

Human review provides a practical safety boundary while the project lacks:

* production evaluation data
* confidence calibration
* automated quality monitoring
* complete business rules
* customer communication controls

---

## 7. Positive Consequences

* safer customer communication
* incorrect output can be corrected
* agents retain responsibility
* easier to introduce AI gradually
* reduced hallucination impact
* suitable for portfolio demonstration of responsible AI
* enables future AI-quality evaluation

---

## 8. Negative Consequences

* less automation
* agent review remains necessary
* response time depends partly on the agent
* additional review interface is required
* the system cannot independently complete tickets

---

## 9. Rules Created by This Decision

* AI responses must be labelled as drafts or suggestions.
* AI output must be validated before display or storage.
* No AI-generated customer response is sent automatically.
* AI priority does not trigger irreversible actions.
* Support agents may correct generated values.
* The system should not claim that an action occurred unless confirmed by system data.
* Detailed hidden model reasoning should not be requested or stored.

---

## 10. Risks and Mitigations

| Risk                                      | Mitigation                                                |
| ----------------------------------------- | --------------------------------------------------------- |
| Agent assumes AI output is always correct | Clearly label output as AI-generated                      |
| Agent sends suggestion without reading    | Provide a review and edit step                            |
| AI claims refund or payment completion    | Add prompt and content restrictions                       |
| Corrections are lost                      | Store corrected values and add audit history later        |
| Human review becomes a bottleneck         | Evaluate assisted workflows before introducing automation |

---

## 11. Review Conditions

Review this decision only after the project has:

* reliable evaluation data
* measured AI accuracy
* confidence thresholds
* monitoring
* audit history
* clearly defined business rules
* approved automated-response use cases

---

## 12. Related Documents

* `docs/PROBLEM_DEFINITION.md`
* `docs/REQUIREMENTS.md`
* `docs/HLD.md`
* `docs/LLD.md`
