# ADR-008: Use React.js for the Frontend Application

---

## 1. Document Information

| Field           | Value                |
| --------------- | -------------------- |
| ADR Number      | ADR-008              |
| Status          | Accepted             |
| Decision Date   | 2026-07-26           |
| Author          | Raja Rangarao Moturi |
| Decision Owners | Project Developer    |

---

## 2. Context

The AI-Powered Support Ticket Assistant requires a frontend application that allows customers and support agents to interact with the FastAPI backend.

The frontend should support:

* ticket creation
* ticket listing
* ticket filtering
* ticket-detail viewing
* ticket-status updates
* AI-analysis requests
* AI-generated suggestion review
* error-message display
* responsive user interaction

The frontend should communicate with the backend through REST APIs using JSON.

The selected frontend technology should be beginner-friendly, widely used, suitable for portfolio projects, and capable of supporting future application growth.

---

## 3. Decision Drivers

The main decision drivers are:

* beginner-friendly frontend development
* familiarity with JavaScript
* component-based user-interface development
* strong ecosystem
* production relevance
* easy REST API integration
* support for reusable components
* strong community and learning resources
* suitability for portfolio projects
* compatibility with FastAPI
* future support for routing and state management

---

## 4. Options Considered

### Option 1: React.js

Advantages:

* component-based architecture
* large community
* strong ecosystem
* widely used in product companies
* good support for REST API integration
* reusable user-interface components
* suitable for single-page applications
* strong portfolio value
* works well with Vite
* flexible state-management options

Disadvantages:

* requires decisions about project structure
* state management can become complex
* React alone does not provide routing or API handling
* frequent ecosystem changes may confuse beginners
* poor component design may create unnecessary complexity

### Option 2: Angular

Advantages:

* complete frontend framework
* built-in routing
* dependency injection
* structured project architecture
* TypeScript-first development
* suitable for large enterprise applications

Disadvantages:

* steeper learning curve
* more framework concepts
* heavier than required for the MVP
* more setup and boilerplate
* unnecessary complexity for a beginner project

### Option 3: Vue.js

Advantages:

* beginner-friendly syntax
* component-based design
* good documentation
* lightweight
* suitable for small and medium applications

Disadvantages:

* less aligned with the developer's current React learning path
* smaller job-market presence in some target companies
* fewer direct learning benefits for the developer's current goals

### Option 4: Server-Rendered HTML with FastAPI Templates

Advantages:

* minimal frontend setup
* fewer technologies
* simple deployment
* suitable for basic forms

Disadvantages:

* limited exposure to modern frontend architecture
* less interactive user experience
* difficult to scale into a modern dashboard
* less suitable for practising frontend and backend separation

### Option 5: No Frontend in the MVP

Advantages:

* faster backend completion
* Swagger UI and Postman can test APIs
* reduced project scope

Disadvantages:

* no complete user-facing workflow
* weaker portfolio presentation
* no practical frontend-backend integration
* AI-review workflow is harder to demonstrate

---

## 5. Decision

The project will use **React.js** for the frontend application.

The React frontend will be created using a modern lightweight build tool such as Vite.

The frontend will communicate with the FastAPI backend through REST APIs.

The frontend will remain a separate application from the backend.

---

## 6. Rationale

React provides the best balance between:

* beginner accessibility
* industry relevance
* component reuse
* frontend-backend integration
* portfolio value
* future extensibility

The developer already has some React experience, which reduces the learning overhead and allows more attention to be given to FastAPI and AI integration.

React also supports the user interfaces required by this project, including:

* ticket forms
* ticket tables
* ticket filters
* ticket-detail panels
* AI-analysis results
* editable suggested responses
* loading and error states

---

## 7. Frontend Responsibilities

The React frontend will be responsible for:

* collecting customer ticket information
* validating basic form inputs
* sending requests to the FastAPI backend
* displaying ticket lists
* displaying ticket details
* displaying ticket status
* requesting AI analysis
* displaying AI-generated suggestions
* allowing support agents to edit suggested responses
* displaying loading states
* displaying user-friendly errors
* managing page navigation

The frontend will not:

* access PostgreSQL directly
* call the external AI provider directly
* store AI-provider API keys
* apply critical business rules
* determine valid ticket-status transitions
* trust client-side validation as the only validation layer

---

## 8. Proposed Frontend Architecture

The frontend will use a component-based architecture.

Suggested high-level structure:

```text
src/frontend/
├── src/
│   ├── api/
│   ├── components/
│   ├── pages/
│   ├── hooks/
│   ├── services/
│   ├── types/
│   ├── utils/
│   ├── constants/
│   ├── App
│   └── main
├── public/
├── package.json
├── Dockerfile
└── .env.example
```

The exact file names and implementation details will be finalized during frontend design.

---

## 9. Initial Frontend Pages

The MVP frontend may include the following pages:

### 9.1 Create Ticket Page

Responsibilities:

* collect customer name
* collect customer email
* collect ticket subject
* collect ticket description
* submit the ticket
* display validation errors
* display creation confirmation

### 9.2 Ticket List Page

Responsibilities:

* display tickets
* support pagination
* filter by status
* filter by category
* filter by priority
* display loading states
* display empty states
* navigate to ticket details

### 9.3 Ticket Details Page

Responsibilities:

* display complete ticket information
* display current ticket status
* update ticket status
* request AI analysis
* display AI-analysis state
* display generated summary
* display recommended team
* display suggested response
* allow human correction

### 9.4 Error or Not Found Page

Responsibilities:

* display user-friendly errors
* handle invalid ticket URLs
* provide navigation back to the ticket list

---

## 10. Initial Frontend Components

Potential reusable components include:

* navigation bar
* ticket form
* ticket table
* ticket row
* ticket filters
* pagination controls
* status badge
* priority badge
* category badge
* loading indicator
* error alert
* confirmation dialog
* AI-analysis panel
* suggested-response editor
* empty-state component

Components should be created only when reuse or clear separation is justified.

---

## 11. State Management Decision

The MVP will begin with:

* React component state
* React hooks
* shared state only where necessary

A global state-management library will not be introduced initially.

The project will not initially use:

* Redux
* MobX
* Zustand
* complex state machines

A state-management library may be added later if:

* shared state becomes difficult to manage
* authentication is introduced
* multiple pages depend on the same server data
* caching and synchronization become complex

---

## 12. API Communication

The frontend will communicate only with the FastAPI backend.

API communication responsibilities include:

* sending JSON requests
* reading JSON responses
* handling HTTP status codes
* displaying validation messages
* handling network failures
* handling AI-provider-related backend errors
* handling ticket-not-found responses
* supporting pagination and filters

The frontend should not depend on backend error-message text alone.

It should use stable application error codes where appropriate.

---

## 13. Routing

The frontend will use client-side routing.

Initial routes may include:

```text
/
 /tickets
 /tickets/new
 /tickets/:ticketId
```

The routing library selection may use React Router or another suitable React routing solution.

The frontend should support refreshing a ticket-detail page without losing the route.

---

## 14. Form Validation

The frontend should perform basic validation to improve user experience.

Examples include:

* required fields
* email format
* minimum field lengths
* maximum field lengths
* whitespace-only input prevention

Backend validation remains authoritative.

Client-side validation must not replace backend validation.

---

## 15. Environment Configuration

The frontend should use environment variables for:

* backend API base URL
* application environment
* optional feature flags

The frontend must not store:

* AI API keys
* database passwords
* backend secrets
* private service credentials

The repository should include `.env.example` with placeholder values only.

---

## 16. Error Handling

The frontend should provide clear error states for:

* invalid form input
* backend unavailable
* ticket not found
* database unavailable
* AI provider unavailable
* AI request timeout
* invalid AI output
* duplicate AI-analysis request
* unexpected server failure

Raw stack traces or internal backend details must not be displayed.

---

## 17. Loading and Disabled States

The frontend should show loading indicators during:

* ticket creation
* ticket retrieval
* ticket-list loading
* ticket update
* status update
* AI analysis

Buttons that trigger an active operation should be disabled when appropriate to reduce duplicate requests.

For example, the AI-analysis button should be disabled while analysis is in progress.

---

## 18. Accessibility Considerations

The frontend should support basic accessibility practices:

* semantic HTML
* labelled form fields
* keyboard navigation
* visible focus states
* readable error messages
* sufficient text contrast
* meaningful button labels
* accessible status indicators

Accessibility should be considered during component design rather than added only at the end.

---

## 19. Responsive Design

The frontend should work on:

* desktop screens
* laptop screens
* tablet-sized screens
* basic mobile layouts

The MVP does not require a dedicated mobile application.

The ticket table may use a simplified card layout on smaller screens if necessary.

---

## 20. Testing Strategy

Frontend testing should eventually include:

### Unit Tests

Used for:

* utility functions
* validation helpers
* formatting logic

### Component Tests

Used for:

* ticket form
* filters
* status indicators
* error messages
* AI-analysis panel

### Integration Tests

Used for:

* form submission
* API response handling
* ticket-list rendering
* status updates
* AI-analysis workflows

### End-to-End Tests

Future end-to-end tests may cover:

* creating a ticket
* opening ticket details
* requesting AI analysis
* updating ticket status

The exact testing tools will be selected during frontend setup.

---

## 21. Positive Consequences

* modern user interface
* reusable components
* strong portfolio presentation
* practical frontend-backend integration
* good industry relevance
* large learning ecosystem
* flexible application structure
* easy support for ticket workflows
* future support for authentication and dashboards

---

## 22. Negative Consequences

* adds frontend complexity
* requires Node.js tooling
* requires separate dependency management
* frontend and backend contracts must remain synchronized
* component state can become difficult to manage
* frontend testing requires additional tools
* Docker Compose requires an additional service

---

## 23. Risks and Mitigations

| Risk                                    | Mitigation                                                         |
| --------------------------------------- | ------------------------------------------------------------------ |
| Frontend work delays backend learning   | Complete core backend APIs before advanced UI work                 |
| State management becomes complex        | Start with local state and introduce libraries only when justified |
| API contracts become inconsistent       | Keep `API_SPEC.md` and frontend types aligned                      |
| Backend errors are poorly displayed     | Use stable application error codes                                 |
| Duplicate requests occur                | Disable active-action buttons and display loading states           |
| Secrets are added to frontend variables | Store secrets only in backend configuration                        |
| Components become too large             | Extract reusable components based on clear responsibilities        |
| Too many UI libraries are introduced    | Begin with minimal dependencies                                    |

---

## 24. Review Conditions

This decision should be reviewed if:

* React creates unnecessary complexity for the MVP
* the application becomes primarily server rendered
* the frontend requirements become extremely simple
* another framework provides a clear project or business advantage
* the frontend is replaced by a mobile or desktop application
* React maintenance or ecosystem constraints become unsuitable

---

## 25. Related Documents

* `docs/PROBLEM_DEFINITION.md`
* `docs/REQUIREMENTS.md`
* `docs/HLD.md`
* `docs/LLD.md`
* `docs/API_SPEC.md`
* `docs/SETUP.md`
* `docs/DEPLOYMENT.md`
* `docs/TESTING.md`

---

## 26. Document History

| Version | Date       | Author               | Description                      |
| ------- | ---------- | -------------------- | -------------------------------- |
| 1.0     | 2026-07-26 | Raja Rangarao Moturi | Initial decision to use React.js |
