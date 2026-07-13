# GymFlow Architecture Decisions

This document records the most important architectural choices in a compact ADR-style format.

Each decision includes context, the selected approach, consequences, and alternatives. The source repositories contain implementation details; this public record explains the reasoning.

## ADR-001 — Use Flutter across web, Android, and Windows

**Status:** Accepted

### Context

GymFlow needs a strong web showcase plus mobile and desktop build targets. Reimplementing product logic and visual systems separately would multiply maintenance and make cross-surface consistency harder.

### Decision

Use Flutter and Dart as the shared client platform, with platform adapters for OAuth, camera/QR, browser redirects, and desktop behavior.

### Consequences

- Shared feature models, localization, routing, and design language.
- Faster cross-platform product iteration.
- Platform-specific behavior still requires explicit testing.
- Web rendering, native plugins, and desktop packaging create different failure modes.

### Alternatives considered

- React web plus native mobile.
- Separate web and desktop clients.
- Web-only portfolio application.

## ADR-002 — Use FastAPI with typed Pydantic contracts

**Status:** Accepted

### Context

The backend exposes many business routes and multiple authentication surfaces. Request and response contracts need to remain explicit and testable.

### Decision

Use FastAPI for route/dependency composition and Pydantic for typed validation and audience-specific response schemas.

### Consequences

- Clear OpenAPI-compatible contracts.
- Dependency-based authentication and authorization.
- Response validation catches data-contract mistakes, not only request mistakes.
- Schema changes must remain synchronized with frontend parsing.

### Alternatives considered

- Loosely typed Python endpoints.
- A backend-as-a-service model.
- A monolithic frontend-only mock API.

## ADR-003 — Use PostgreSQL as the system of record

**Status:** Accepted

### Context

GymFlow has strongly related entities, business constraints, transactions, history, and reports.

### Decision

Use PostgreSQL with SQLAlchemy and Alembic.

### Consequences

- Referential integrity and transactional updates.
- Relational reporting and filtering.
- Explicit migration responsibility.
- Query/index performance must be monitored as data grows.

### Alternatives considered

- Document database.
- Local-only persistence.
- Provider-owned database abstraction.

## ADR-004 — Make workspace membership the tenant and role boundary

**Status:** Accepted

### Context

A user may work with multiple studios and may hold a different role in each one.

### Decision

Represent workspace access through membership records containing role and status. Scope business resources to workspace ownership.

### Consequences

- Multi-workspace users are supported.
- Roles remain tenant-specific.
- Every protected query must preserve workspace scope.
- Authorization testing becomes a core requirement.

### Alternatives considered

- One global user role.
- One database per workspace.
- Duplicate user accounts for each studio.

## ADR-005 — Separate client portal identity from staff identity

**Status:** Accepted

### Context

Clients need private self-service but should not become staff users or inherit the staff dashboard security surface.

### Decision

Use a separate portal token model and protected portal route family. Derive workspace/client identity from the token for authenticated portal requests.

### Consequences

- Stronger least privilege.
- Client-safe response models.
- Separate session storage and router logic.
- More authentication and testing complexity.

### Alternatives considered

- Give clients a restricted staff role.
- Use public query parameters for client access.
- Reuse staff JWTs with client claims.

## ADR-006 — Run migrations separately from production web startup

**Status:** Accepted

### Context

Automatically running migrations whenever a web instance starts can create race conditions and hidden release behavior.

### Decision

Build one image but use a separate explicit migration command/job before rolling the web process.

### Consequences

- Schema change is visible and intentional.
- Migration failure blocks release before traffic shifts.
- Deployment orchestration has one additional step.
- Operators need backup and forward-fix procedures.

### Alternatives considered

- Migrate on every container start.
- Manually edit production schema.
- Disable migrations and recreate databases.

## ADR-007 — Use Redis-backed rate limits in production

**Status:** Accepted

### Context

Process-local counters do not provide correct abuse protection across multiple API instances.

### Decision

Require Redis in production for shared public auth and portal rate-limit state.

### Consequences

- Consistent limits across horizontal instances.
- Redis becomes a required production dependency.
- Readiness must reflect Redis availability when required.

### Alternatives considered

- In-memory counters only.
- Database-backed counters for every request.
- Depend entirely on an external gateway.

## ADR-008 — Model client payments separately from SaaS billing

**Status:** Accepted

### Context

Money a client pays a gym is not the same business relationship as the gym paying GymFlow.

### Decision

Keep client payment records and workspace SaaS billing as distinct domains while sharing provider infrastructure where appropriate.

### Consequences

- Clearer lifecycle and reporting.
- Safer authorization boundaries.
- Provider events require explicit entity context.
- More models and integration paths than one universal payment table.

### Alternatives considered

- One generic payment model for every financial event.
- Stripe-only records without an internal ledger.
- No SaaS billing model.

## ADR-009 — Separate internal notes from client-visible messages

**Status:** Accepted

### Context

A support workflow needs staff collaboration without exposing operational notes to clients.

### Decision

Represent message audience/type explicitly and return audience-specific response schemas.

### Consequences

- Internal notes remain staff-only.
- Portal and staff APIs can share conversation state safely.
- Every new field and endpoint needs audience review.
- Tests must cover serialization as well as access control.

### Alternatives considered

- One message type with a UI-only hidden flag.
- Separate unrelated staff and client conversation systems.
- No internal collaboration notes.

## ADR-010 — Use idempotency and optimistic versions in messaging

**Status:** Accepted

### Context

Network retries can duplicate messages, and multiple staff can update conversation workflow at the same time.

### Decision

Support retry-safe send identifiers and optimistic workflow versions for assignment/status/priority updates.

### Consequences

- Client retries do not create duplicate messages when identifiers are reused correctly.
- Stale staff updates fail instead of silently overwriting newer state.
- Clients must handle conflict responses and refresh.

### Alternatives considered

- Assume each request is delivered exactly once.
- Last-write-wins for every workflow update.
- Pessimistic database locks across user interactions.

## ADR-011 — Derive presence from connection and activity signals

**Status:** Accepted

### Context

A manual online flag or one heartbeat per user is inaccurate for multiple tabs/devices and idle users.

### Decision

Track connection heartbeats separately from user activity, aggregate devices, and derive online/away/offline state according to policy.

### Consequences

- More truthful presence.
- One closed tab does not force the user offline.
- Visibility and last-seen privacy need explicit policy.
- Background browser/network behavior requires testing.

### Alternatives considered

- Manual online/offline switch.
- One device/session per user.
- Last-login timestamp presented as presence.

## ADR-012 — Use a guarded deterministic demo database

**Status:** Accepted

### Context

Portfolio review needs realistic, repeatable data. Manual setup creates stale, duplicated, or empty states and introduces data-destruction risk.

### Decision

Maintain a separate `gymflow_demo` database and rebuild it through a transactional allowlisted workflow with environment, host, database-name, Stripe, migration, confirmation, and validation guards.

### Consequences

- Screenshots and videos are reproducible.
- Development data remains separate.
- New tables and metrics require deliberate seed-contract updates.
- The reset code receives production-level review despite being demo tooling.

### Alternatives considered

- Random fixture generation.
- Database dump committed to source.
- Manual DBeaver edits.
- Recreate/drop the whole schema.

## ADR-013 — Preserve a single familiar local Compose command

**Status:** Accepted

### Context

Adding the dedicated demo database risked creating separate, confusing Docker workflows.

### Decision

Use `GYMFLOW_DATABASE` as a safe selector for only `gymflow` or `gymflow_demo`, then keep `docker compose up --build` as the standard command.

### Consequences

- Low-friction switching.
- Both databases remain in one PostgreSQL volume.
- Selector validation must reject arbitrary names.
- Operators must avoid deleting the shared volume unintentionally.

### Alternatives considered

- Separate Compose files for each local database.
- Edit `DATABASE_URL` manually for every switch.
- Recreate PostgreSQL volume for the demo.

## ADR-014 — Correlate every API failure with a request ID

**Status:** Accepted

### Context

A frontend “network error” can originate from validation, authorization, dependencies, or an unhandled exception. Generic messages without correlation slow diagnosis.

### Decision

Assign/accept an `X-Request-ID`, return it in headers and error envelopes, and include it in structured access/error logs.

### Consequences

- Frontend reports can be traced to backend events.
- Clients may provide a bounded request ID.
- Logs must avoid sensitive payloads.
- Monitoring/search tooling should index the field.

### Alternatives considered

- Unstructured console logs.
- Stack traces returned to clients.
- Provider-specific identifiers only.

## ADR-015 — Keep private source and publish an evidence-focused showcase

**Status:** Accepted

### Context

GymFlow is a complete product-style application and includes implementation patterns, provider configuration, and commercial potential. Public evaluation still needs credible evidence.

### Decision

Keep source repositories private while publishing architecture, security, quality, operations, screenshots, video, release manifests, and optional controlled technical access.

### Consequences

- Public portfolio remains understandable without exposing full source.
- Claims require stronger evidence and provenance.
- Reviewers cannot independently inspect every implementation detail by default.
- Temporary read-only walkthrough access may be offered when appropriate.

### Alternatives considered

- Publish all source repositories.
- Publish only screenshots with no technical documentation.
- Distribute source archives privately without a public case study.
