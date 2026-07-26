# Pull Request

## Summary

Describe what this pull request changes and why the change is required.

---

## Type of Change

Select the applicable change type.

* [ ] Feature
* [ ] Bug fix
* [ ] Refactoring
* [ ] Documentation
* [ ] Testing
* [ ] CI/CD
* [ ] Security
* [ ] Dependency update
* [ ] Database migration
* [ ] Other

---

## Related Issue

Add the related issue number or link.

```text
Closes #
```

Use `N/A` when no issue exists.

---

## Changes Made

Describe the main changes included in this pull request.

*
*
*

---

## Architecture Impact

Does this change affect the architecture?

* [ ] No architecture impact
* [ ] HLD updated
* [ ] LLD updated
* [ ] ADR added or updated
* [ ] API specification updated
* [ ] Database design updated
* [ ] Deployment design updated

Explain any architectural impact:

```text
N/A
```

---

## API Changes

Does this pull request change an API contract?

* [ ] No API changes
* [ ] New endpoint added
* [ ] Existing endpoint modified
* [ ] Endpoint removed
* [ ] Request model changed
* [ ] Response model changed
* [ ] Error response changed
* [ ] Validation rule changed

Affected endpoint or contract:

```text
N/A
```

Confirm:

* [ ] `docs/API_SPEC.md` was updated when required
* [ ] Generated OpenAPI documentation matches the intended contract
* [ ] Backward compatibility was reviewed

---

## Database Changes

Does this pull request change the database?

* [ ] No database changes
* [ ] Table added
* [ ] Column added
* [ ] Column modified
* [ ] Constraint added or modified
* [ ] Index added or modified
* [ ] Migration added
* [ ] Data migration required

Migration name:

```text
N/A
```

Confirm:

* [ ] Migration was tested on a clean database
* [ ] Migration was tested on an existing database
* [ ] Rollback or recovery impact was reviewed
* [ ] No unintended data loss is expected

---

## AI Changes

Does this pull request affect AI functionality?

* [ ] No AI changes
* [ ] Prompt changed
* [ ] Prompt version changed
* [ ] AI model changed
* [ ] AI provider changed
* [ ] Output schema changed
* [ ] AI validation changed
* [ ] Timeout or retry behavior changed
* [ ] Suggested-response behavior changed

AI-related details:

```text
N/A
```

Confirm:

* [ ] AI output remains validated
* [ ] AI output remains human-reviewed
* [ ] No automatic customer response was introduced
* [ ] Mocked AI tests were added or updated
* [ ] Prompt-injection scenarios were considered
* [ ] Model and prompt versions remain traceable

---

## Frontend Changes

Does this pull request affect the React frontend?

* [ ] No frontend changes
* [ ] New page
* [ ] New component
* [ ] Existing component updated
* [ ] Routing changed
* [ ] API integration changed
* [ ] Form validation changed
* [ ] Error handling changed
* [ ] Styling changed

Frontend details:

```text
N/A
```

Confirm:

* [ ] Loading states were handled
* [ ] Error states were handled
* [ ] User-generated content is rendered safely
* [ ] No secrets were added to frontend configuration
* [ ] Responsive behavior was reviewed where relevant

---

## Testing

Describe the testing completed for this change.

### Automated Tests

* [ ] Unit tests
* [ ] Service-layer tests
* [ ] Repository integration tests
* [ ] API integration tests
* [ ] AI mock tests
* [ ] Frontend component tests
* [ ] Frontend integration tests
* [ ] End-to-end tests
* [ ] No automated tests required

### Manual Verification

Describe the manual verification performed:

```text
N/A
```

---

## Test Results

Confirm the following:

* [ ] Backend tests pass
* [ ] Frontend tests pass
* [ ] Backend lint checks pass
* [ ] Frontend lint checks pass
* [ ] Frontend production build succeeds
* [ ] Database migrations succeed
* [ ] Docker Compose verification completed when required
* [ ] Existing functionality remains unaffected

---

## Security Review

Confirm:

* [ ] No secrets were committed
* [ ] No real customer data was added
* [ ] User input is validated
* [ ] AI output is validated
* [ ] Logs do not expose sensitive information
* [ ] Raw exceptions are not exposed
* [ ] CORS changes were reviewed
* [ ] New dependencies were reviewed
* [ ] Security documentation was updated when required

Security impact:

```text
N/A
```

---

## Documentation

Select all documentation updated by this pull request.

* [ ] No documentation changes required
* [ ] Root `README.md`
* [ ] `docs/README.md`
* [ ] `docs/PROBLEM_DEFINITION.md`
* [ ] `docs/REQUIREMENTS.md`
* [ ] `docs/HLD.md`
* [ ] `docs/LLD.md`
* [ ] `docs/API_SPEC.md`
* [ ] `docs/TESTING.md`
* [ ] `docs/SECURITY.md`
* [ ] `docs/SETUP.md`
* [ ] `docs/DEPLOYMENT.md`
* [ ] Architecture Decision Record
* [ ] Other documentation

---

## Screenshots

Add screenshots for user-interface changes.

Use `N/A` when there are no visual changes.

```text
N/A
```

---

## Deployment Impact

Does this pull request affect deployment?

* [ ] No deployment impact
* [ ] Environment variable added
* [ ] Environment variable changed
* [ ] Dockerfile changed
* [ ] Docker Compose changed
* [ ] CI workflow changed
* [ ] Database migration required
* [ ] Deployment steps changed
* [ ] Rollback procedure changed

Deployment notes:

```text
N/A
```

---

## Risks

Describe any known risks introduced by this change.

```text
N/A
```

---

## Rollback Plan

Explain how this change can be safely rolled back.

```text
Revert this pull request and redeploy the previous stable version.
```

Add database-specific recovery steps when migrations are involved.

---

## Reviewer Checklist

* [ ] The change matches the stated requirements
* [ ] The implementation follows the documented architecture
* [ ] Business logic is not placed directly in route handlers
* [ ] Database operations remain inside the repository layer
* [ ] AI-provider logic remains isolated
* [ ] API contracts are consistent
* [ ] Error handling is consistent
* [ ] Tests cover important success and failure paths
* [ ] Security risks were considered
* [ ] Documentation is current
* [ ] No unnecessary complexity was introduced
* [ ] The pull request is small enough to review effectively

---

## Final Author Checklist

* [ ] I reviewed my own changes
* [ ] I removed debugging statements
* [ ] I removed commented-out code
* [ ] I used meaningful names
* [ ] I added or updated tests
* [ ] I updated relevant documentation
* [ ] I verified that no secrets are included
* [ ] I confirmed that CI checks pass
* [ ] I confirmed that this pull request is ready for review
