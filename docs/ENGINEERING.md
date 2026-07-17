# GymFlow Engineering

This document explains the engineering depth behind GymFlow: system boundaries, implementation choices, failure handling, reliability patterns, and trade-offs that are easy to miss in a visual product demonstration.

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
- testing and validation;
- Docker and environment design;
- deterministic demo and release engineering.

## 1. Product-to-system decomposition

The application is organized around vertical product areas rather than one technical layer with no business ownership.

Examples include clients, memberships, staff, bookings, check-ins, payments, reports, messaging, and the client portal. Each slice owns its data access, state coordination, presentation, and targeted verification.

This makes a change such as “support no-show reporting” traceable from database state through API schema, aggregation, frontend parsing, and UI display.

## 2. Frontend architecture

### Feature-oriented structure

| Layer | Responsibility |
|---|---|
| Data | Models, repositories, API payload parsing, persistence adapters |
| State | Controllers or coordinators, loading state, mutation lifecycle |
| Presentation | Pages, dialogs, responsive widgets, localized copy |

HTTP behavior is isolated from widgets, and unrelated product areas are not forced through one global controller.

### Routing as a product boundary

The router handles:

- public and protected routes;
- staff and portal session separation;
- session-expired redirects;
- safe redirect filtering;
- role-aware route access;
- billing-state gates;
- portal preview and session resolution.

These controls improve navigation and user experience. Backend authorization remains the final security authority.

### State and failure handling

Pages account for loading, refresh, empty state, partial data, API failure, mutation progress, conflict or rate-limit feedback, and session expiry.

The goal is to avoid the common portfolio pattern where only a single happy path exists.

### Localization and responsiveness

User-facing copy goes through generated localization or shared display helpers. Backend enum values are mapped into localized labels instead of being displayed raw.

The interface is reviewed across:

- large desktop;
- common laptop;
- compressed desktop and tablet;
- mobile widths;
- expanded French copy;
- Arabic RTL.

Dialogs, navigation, data cards, forms, timelines, and portal shells have explicit responsive behavior rather than relying on simple widget shrinking.

## 3. Backend architecture

FastAPI routes are grouped under `/api/v1` by business capability. Dependencies apply authentication, portal identity, workspace membership, role requirements, and rate limits near the HTTP boundary.

| Layer | Responsibility |
|---|---|
| API routes | HTTP contract, dependency injection, authorization entry point |
| Pydantic schemas | Typed validation and audience-safe response models |
| Services | Business rules, lifecycle transitions, provider coordination, transactions |
| Repositories and queries | Scoped database access |
| SQLAlchemy models | Relationships, constraints, indexes, persistence |
| Core and middleware | Settings, authentication, request IDs, headers, limits, logs |
| Alembic | Published schema migration history |

Business behavior stays outside route handlers when it involves multi-model validation, transactions, provider calls, idempotency, access rules, or reporting aggregation.

## 4. Relational data design

PostgreSQL fits the product because GymFlow contains strongly connected entities and transactional workflows.

Examples:

- bookings connect workspace, client, service, and optional trainer;
- memberships connect clients and plans;
- payments connect financial state with client and membership context;
- messages belong to authorized conversations;
- reports aggregate durable operational records.

The model uses foreign keys, unique constraints, indexes, statuses, timestamps, and migration-managed schema evolution.

## 5. Migration discipline

Alembic migrations are treated as published history.

Controls include:

- migration-graph checks;
- one-head expectations;
- model and migration metadata contracts;
- explicit production migration commands;
- separation from web startup;
- preservation of `alembic_version` during demo resets.

The deployment path favors forward fixes over destructive rollback assumptions.

## 6. Authentication and authorization

GymFlow supports staff password login, verification, recovery, Google OAuth, staff invitations, and one-time client portal access.

Authorization combines:

- user or portal identity;
- credential type;
- active workspace membership;
- role and membership status;
- requested operation;
- resource workspace;
- client ownership;
- message audience and participant rules.

Frontend permissions answer whether an action should be offered. Backend permissions answer whether the operation is allowed. Both matter, but only the backend is the security boundary.

## 7. Scheduling and attendance

Booking logic handles:

- service duration;
- optional or required trainer;
- trainer availability;
- overlapping bookings;
- staff versus portal permissions;
- recurring generation;
- future-series cancellation;
- lifecycle transitions;
- no-show reporting.

Recurring bookings are related records, allowing each occurrence to have its own lifecycle while preserving series-level operations.

Attendance is stored separately from booking state so a physical visit does not have to be represented as the same event as a scheduled session.

## 8. Payments and billing

GymFlow separates two financial domains:

1. **Client payments** between a client and studio.
2. **SaaS billing** between a studio and GymFlow.

Webhook handling verifies signatures, stores provider event identifiers, detects duplicate delivery, and applies idempotent state transitions.

Studios can represent cash, terminal, bank transfer, or Stripe test checkout while preserving a shared payment lifecycle and method context.

## 9. Messaging

Messaging is a workflow system rather than a simple chat table.

It supports:

- authorized participants;
- staff assignment and queue claiming;
- priorities and statuses;
- client-visible replies;
- staff-only internal notes;
- cursor pagination;
- retry-safe send identifiers;
- optimistic workflow versions;
- lifecycle cleanup and abuse limits.

Audience-specific response schemas prevent portal clients from receiving internal notes or operational metadata.

## 10. Presence

Presence is not a manually toggled boolean.

The system combines:

- authenticated connection heartbeat;
- recent user activity;
- multiple-device aggregation;
- online, away, and offline derivation;
- visibility policy;
- administrative reset.

One closed browser tab therefore does not incorrectly force a multi-device user offline.

## 11. Reliability and observability

| Pattern | Example |
|---|---|
| Transaction | Demo reset, seed, validation, and commit as one unit |
| Advisory lock | Prevent concurrent demo rebuilds |
| Idempotency | Stripe webhook events and message sends |
| Optimistic concurrency | Conversation workflow updates |
| Expiring one-time credential | Portal access, recovery, and verification |
| Neutral public response | Prevent identity enumeration |
| Readiness checks | Reject traffic when required dependencies are unavailable |
| Request correlation | Connect frontend failures with structured backend logs |

Every request receives an `X-Request-ID`. Liveness and readiness remain separate because “the process is running” is different from “the service can safely receive traffic.”

## 12. Environment design

| Environment | Purpose |
|---|---|
| Development | Local iteration and diagnostics |
| Test | Isolated and deterministic automated checks |
| Demo | Guarded fictional scenario and repeatable presentation |
| Production | Fail-closed configuration and provider verification |

Demo mode is not an alias for development. It has its own database, identity, payment, and destructive-operation contract.

## 13. Deterministic demo engineering

The Northline Performance Club seed is not a random fixture generator. It has fixed identities, connected relationships, relative dates, lifecycle states, financial totals, portal stories, and report targets.

The rebuild:

- refuses production;
- refuses arbitrary database names;
- refuses remote database hosts;
- refuses live Stripe configuration or stored live events;
- refuses unknown application tables;
- preserves schema and migration history;
- deletes in reviewed dependency order;
- validates before commit.

This turns demo preparation into a repeatable release process rather than manual database editing.

## 14. Validation strategy

The application and showcase use layered evidence:

| Layer | Protection |
|---|---|
| Unit and model tests | Parsing, calculations, mappings, transitions |
| API behavior tests | Contracts, business outcomes, and errors |
| Authorization tests | Workspace, role, portal, and participant isolation |
| Contract scripts | Required routes, settings, middleware, and migration structure |
| API synchronization | Frontend and backend route or payload drift |
| Static analysis | Dart and Python quality |
| Manual QA | Responsive layout, localization, provider behavior, and visuals |
| Demo validation | Deterministic counts, relationships, trends, and identities |
| Showcase validation | Documentation, privacy, provenance, and media integrity |

The showcase uses traditional local release validation:

```powershell
./scripts/validate_release.ps1
```

or:

```bash
./scripts/validate_release.sh
```

The tooling inspects tracked Git content, runs its own regression tests, validates the 53-image contract, verifies canonical source revisions, and optionally confirms the release tag on a clean working tree.

No successful hosted execution is claimed for this release line.

## 15. Release engineering

The `v1.0.2-showcase` candidate centralizes release facts in [`release/evidence-manifest.json`](../release/evidence-manifest.json).

The record includes:

- target and historical release identifiers;
- frontend and backend commits;
- Alembic head;
- evidence date;
- gallery paths and counts;
- approved and blocked media hashes;
- included and omitted artifacts;
- validation commands;
- product and production boundaries.

The canonical application snapshots remain:

- frontend `b73a623c3985e4bc458d04b4b484887ada593fa5`;
- backend `2234af20d1d9dd143bcac22edc699d3ee7fe515f`.

## 16. Key decisions and trade-offs

| Decision | Benefit | Trade-off |
|---|---|---|
| Flutter across client targets | Shared product logic and consistent design | Platform integrations still need adapters |
| FastAPI and Pydantic | Typed contracts and clear validation | Route and service boundaries require discipline |
| PostgreSQL relational model | Strong relationships and transactional rules | Schema changes require migrations |
| Workspace membership boundary | Multi-workspace users and scoped roles | Every business query must preserve scope |
| Separate portal token | Least privilege and safer client UX | Two session models must be maintained |
| Separate migration job | Predictable deployment and explicit schema changes | Deployment has an additional step |
| Redis-backed production limits | Shared abuse-control state across instances | Production requires another managed service |
| Deterministic demo rebuild | Repeatable review and release evidence | Seed contracts evolve with the product |
| Internal-note separation | Protects client-facing audiences | Messaging schemas and tests are more complex |
| Local release validation | Reproducible traditional gate without false hosted claims | Reviewers do not receive a green hosted badge |

## Production boundary

The architecture is production-oriented, but a live commercial launch still requires deployment-specific verification of hosting, managed PostgreSQL and Redis, Stripe and OAuth callbacks, verified email delivery, monitoring, alerting, backups, restore drills, vulnerability scanning, and operational ownership.
