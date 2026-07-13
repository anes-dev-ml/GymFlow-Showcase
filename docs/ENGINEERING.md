# GymFlow Engineering

This document explains the engineering depth behind GymFlow: the design choices, boundaries, failure modes, and trade-offs that are easy to miss in a visual product demo.

## Engineering scope

GymFlow demonstrates work across:

- product and domain modeling;
- Flutter application architecture;
- FastAPI and typed API design;
- PostgreSQL relational modeling;
- schema migrations;
- authentication and authorization;
- provider integrations;
- real-time messaging and presence;
- reliability and idempotency;
- security and observability;
- testing and CI;
- Docker and environment design;
- deterministic demo and release engineering.

## 1. Product-to-system decomposition

The application was split into vertical product areas instead of a technical folder tree with no business ownership.

Examples:

- clients;
- memberships;
- staff;
- bookings;
- check-ins;
- payments;
- reports;
- messaging;
- portal.

Each slice owns its models, repository/API access, state/controller logic, presentation, and targeted tests. This makes a change such as “support no-show reporting” traceable from backend data through API schema, frontend parsing, dashboard aggregation, and UI display.

## 2. Frontend architecture

### Feature-oriented organization

The Flutter code uses feature modules with three main layers:

| Layer | Responsibility |
|---|---|
| Data | Models, repositories, API payload parsing, persistence adapters |
| State | Controllers/coordinators, loading and mutation lifecycle |
| Presentation | Pages, dialogs, responsive widgets, localized copy |

The architecture avoids placing all HTTP calls in widgets or making one global controller own unrelated product behavior.

### Router as a product boundary

The router handles more than navigation:

- public and protected routes;
- staff and portal session separation;
- session-expired redirects;
- safe redirect target filtering;
- role-based route access;
- billing-state gates;
- portal preview and session resolution.

This improves user experience, but backend authorization remains the final authority.

### State and failure handling

Pages account for:

- initial loading;
- refresh;
- empty state;
- partial data;
- API failure;
- mutation progress;
- conflict/rate-limit feedback;
- session expiry.

The goal is to avoid the common portfolio pattern where only the happy state exists.

### API boundary

Repositories isolate:

- route construction;
- authentication headers;
- request/response encoding;
- error envelope parsing;
- model conversion;
- retry/idempotency metadata.

Controllers then express product actions such as `load`, `create`, `cancel`, `claim`, or `markRead` without embedding raw HTTP logic in UI components.

### Localization architecture

User-facing copy goes through generated `AppLocalizations` or shared display helpers. Backend enum values are mapped into localized labels instead of being shown raw.

This matters for values such as:

- role;
- membership status;
- booking status;
- payment status/provider;
- billing state;
- presence state.

Arabic requires more than translated strings. The layout must support RTL direction, alignment, icon order, long labels, and responsive behavior.

### Responsive strategy

GymFlow uses explicit layout tiers rather than assuming desktop widgets will shrink correctly.

The app is reviewed across:

- large desktop;
- common laptop;
- compressed desktop/tablet;
- mobile widths;
- long French copy;
- Arabic RTL.

Dialogs, navigation, data cards, timelines, forms, and portal shells each need their own responsive behavior.

## 3. Backend architecture

### FastAPI route organization

Routes are grouped under `/api/v1` by business capability. Dependencies apply authentication, portal identity, workspace membership, role requirements, and rate limits near the HTTP boundary.

### Pydantic contracts

Schemas provide:

- typed request validation;
- normalized email and identifier handling;
- separate create/update/read shapes;
- audience-specific response models;
- consistent API errors.

A significant lesson was that response validation is also a runtime boundary. The deterministic `.test` identities required an explicit demo-compatible response type while registration and invitation creation retained stricter email validation.

### Service and repository responsibilities

Business behavior is kept outside route handlers when it involves:

- multi-model validation;
- transactions;
- provider calls;
- idempotency;
- access rules;
- lifecycle transitions;
- reporting aggregation.

Repository/query code must preserve workspace scoping and avoid returning a resource before authorization context is applied.

## 4. Relational data design

PostgreSQL was selected because GymFlow contains strongly related business entities and transactional workflows.

Examples:

- a booking references a workspace, client, service, and optional trainer;
- a client membership references a client and plan;
- a payment can reference client and membership context;
- a message belongs to a conversation with authorized participants;
- reports aggregate durable operational records.

The database uses:

- foreign keys;
- unique constraints;
- indexes;
- enums/status values;
- timestamps;
- migration-managed schema evolution.

### Why not store everything as unstructured JSON?

The application depends on referential integrity, filtering, lifecycle queries, aggregation, and cross-entity validation. A relational model makes those invariants visible and enforceable.

## 5. Migration discipline

Alembic migrations are treated as published history.

Controls include:

- migration graph checks;
- metadata/table contract checks;
- one-head expectations;
- explicit production migration command;
- separation from web startup;
- preservation of `alembic_version` during demo resets.

The deployment path favors forward fixes over destructive rollback assumptions.

## 6. Authentication and authorization

### Multiple access models

GymFlow supports:

- staff password login;
- email verification;
- password recovery;
- Google OAuth;
- staff invitations;
- client portal one-time access.

These flows share identity concepts but do not share one universal token.

### Workspace and role model

Role is attached to workspace membership. This supports users who can belong to different studios with different permissions.

Authorization combines:

- user identity;
- token type;
- active workspace membership;
- role;
- membership status;
- resource workspace;
- resource ownership;
- operation.

### Frontend versus backend permissions

Frontend permissions answer: “Should this action or route be offered?”

Backend permissions answer: “Is this operation allowed?”

Both are required, but only the backend is a security control.

## 7. Booking and recurrence engineering

Booking logic had to handle:

- service duration;
- optional/required trainer;
- trainer availability;
- overlapping bookings;
- staff versus portal permissions;
- recurring generation;
- future-series cancellation;
- status transitions;
- no-show reporting.

A recurring booking is represented as related records rather than one UI-only repetition rule. This allows individual occurrences to have their own lifecycle while preserving series operations.

## 8. Payment engineering

### Two financial domains

Client payments and GymFlow SaaS billing are separate domains even when both use Stripe.

This avoids mixing:

- a client's gym invoice/payment;
- the studio's subscription to GymFlow.

### Idempotency and webhook delivery

Webhooks can be delivered more than once. GymFlow stores provider event identifiers and processing outcomes so duplicate delivery does not repeat a financial state transition.

Operational logs distinguish:

- processed;
- ignored;
- duplicate.

### Manual and online collection

Studios may accept cash, terminal, bank transfer, or Stripe checkout. The application models a shared payment lifecycle while preserving provider/method context.

## 9. Messaging engineering

Messaging required stronger design than a basic chat demo.

### Audience separation

A conversation can contain:

- client-visible messages;
- staff-only internal notes;
- assignment and queue metadata.

Client-facing schemas never serialize internal notes.

### Retry-safe sends

A client may retry a request after a timeout without knowing whether the server committed it. Retry-safe identifiers prevent duplicate messages from being created.

### Optimistic workflow versions

Two staff users may update assignment, priority, or status concurrently. A workflow version allows the backend to reject stale updates rather than silently overwriting the newer state.

### Pagination

Cursor pagination avoids unstable page-number behavior as new messages arrive.

## 10. Presence engineering

Presence is not represented as a manually toggled boolean.

The system distinguishes:

- authenticated connection heartbeat;
- recent user activity;
- multi-device connection aggregation;
- online/away/offline derivation;
- visibility policy;
- administrative reset.

This prevents common errors such as one closed browser tab forcing a multi-device user offline.

## 11. Reliability patterns

GymFlow uses several reliability patterns:

| Pattern | Example |
|---|---|
| Transaction | Demo reset/seed/validation commits as one unit |
| Advisory lock | Prevent concurrent demo rebuilds |
| Idempotency | Stripe webhook events and message sends |
| Optimistic concurrency | Conversation workflow updates |
| Expiring one-time credential | Portal access, recovery, verification |
| Consistent error envelope | Frontend can interpret API failures predictably |
| Readiness dependency checks | Traffic is rejected when required dependencies are unavailable |
| Neutral public response | Prevent identity enumeration |

## 12. Security engineering

Implemented controls include:

- trusted hosts;
- controlled CORS;
- rate limiting;
- sensitive request-body limits;
- security headers;
- disabled production debug/docs;
- workspace/role/token isolation;
- generic 500 responses;
- request IDs;
- secret scanning;
- strict production provider settings;
- demo refusal when live payment configuration is detected.

Security is treated as both code and configuration. Correct source code cannot compensate for a production environment that exposes local origins, weak secrets, or misconfigured provider callbacks.

## 13. Observability engineering

The API emits structured logs with:

- request ID;
- method;
- path;
- status;
- duration;
- client context;
- event-specific metadata.

Errors return the request ID so a UI failure can be correlated with backend logs.

Liveness and readiness are separate because “the process is running” is different from “the service can safely receive traffic.”

## 14. Environment design

### Development

Optimized for local iteration and diagnostics.

### Test

Optimized for isolated and deterministic automated checks.

### Demo

Optimized for repeatable professional presentation with fictional identities and destructive safeguards.

### Production

Optimized to fail configuration validation when required security and provider settings are incomplete or unsafe.

The demo environment is intentionally not a loose development mode. It has its own database and reset contract.

## 15. Docker and deployment engineering

The backend container:

- uses a slim Python base image;
- installs dependencies at build time;
- runs as a non-root user;
- exposes a readiness health check;
- starts through an explicit script.

Production migrations run as a separate job before the web container is rolled. This makes schema changes visible and operationally intentional.

The local stack supports switching between `gymflow` and `gymflow_demo` without deleting the shared PostgreSQL volume.

## 16. Deterministic demo engineering

The professional demo seed is not a random fixture generator.

It has fixed identities, relationships, dates relative to the seed date, lifecycle states, financial totals, portal stories, and dashboard/report targets.

The rebuild:

- refuses production;
- refuses arbitrary database names;
- refuses remote database hosts;
- refuses live Stripe mode or live stored events;
- refuses unknown application tables;
- preserves schema and migrations;
- deletes in reviewed dependency order;
- validates before commit.

This turns demo preparation into a repeatable release process rather than manual database editing.

## 17. Testing strategy

GymFlow uses multiple test types because one type cannot protect all risks.

| Test type | What it protects |
|---|---|
| Unit/model tests | Parsing, mapping, calculations, state transitions |
| API behavior tests | HTTP contracts and business outcomes |
| Authorization tests | Tenant, role, portal, and participant isolation |
| Contract scripts | Required routes, middleware, migrations, settings, docs |
| Source/regression tests | Flutter architecture and UI rules difficult to exercise headlessly |
| API-sync tests | Frontend/backend route and payload alignment |
| Static analysis | Dart and Python/source quality |
| Manual QA | Responsive behavior, provider flow, localization, visual credibility |

## 18. CI design

### Backend CI

Runs with PostgreSQL and Redis services and executes the complete backend quality runner.

### Frontend CI

Runs secret scanning, dependency installation, localization generation, Flutter analysis, quality checks, and API-sync tests.

### Showcase CI

Validates documentation structure, local links, asset references, stale credentials, and common secret patterns.

## 19. Key architecture decisions

| Decision | Alternative considered | Why the chosen approach won |
|---|---|---|
| Flutter multi-platform client | Separate web/mobile implementations | Shared domain UI and consistent product experience |
| FastAPI typed API | Loosely typed endpoints | Clear validation, OpenAPI contracts, dependency-based auth |
| PostgreSQL | Document-only persistence | Strong relationships, transactions, reporting, constraints |
| Workspace membership roles | One global user role | Supports multi-workspace SaaS and scoped privilege |
| Portal token separate from staff JWT | Reuse staff auth for clients | Least privilege and client-safe experience |
| Separate migration job | Auto-migrate on every web boot | Predictable releases and visible schema change |
| Redis-backed production limits | Process-local counters only | Correct behavior across multiple API instances |
| Deterministic demo database | Manual fixture editing | Repeatable QA, screenshots, video, and failure diagnosis |
| Audience-specific messaging schemas | One universal message response | Prevent internal-note and metadata leakage |
| Presence from heartbeat + activity | Manual online switch | More truthful multi-device online/away behavior |

## 20. Engineering evidence matrix

| Skill | Concrete evidence |
|---|---|
| System design | C4-style architecture, trust boundaries, deployment model |
| API design | Versioned routes, typed schemas, consistent errors |
| Database design | Relational domain model and migration contracts |
| Security | Token separation, workspace scope, rate/body limits, headers |
| Distributed systems | Idempotency, retries, optimistic concurrency, WebSockets |
| DevOps | CI services, Docker, separate migrations, health checks |
| Observability | Request correlation, structured logs, provider diagnostics |
| Testing | Layered automated checks plus manual QA |
| Product thinking | Connected workflows and realistic edge cases |
| Internationalization | Three languages, RTL, localized domain values |
| Release engineering | Guarded deterministic seed and artifact manifest |

## 21. Known trade-offs and future work

- Flutter provides cross-platform leverage but still requires platform-specific OAuth, camera, and browser integration handling.
- Source-based UI regression tests are useful but should be complemented by more golden/integration tests over time.
- Provider integrations need real environment verification before production claims.
- Production operations need managed hosting, monitoring, backup/restore, and vulnerability scanning.
- A public API collection and generated release SBOM would strengthen external review.

These items are tracked in the [Roadmap](../ROADMAP.md) rather than hidden from the showcase.
