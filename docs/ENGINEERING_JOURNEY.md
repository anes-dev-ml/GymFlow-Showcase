# Engineering development

GymFlow developed from a CRUD-oriented gym application into a multi-tenant system connecting member management, scheduling, payments, communication, and a private client portal. This document records the design problems that emerged during that evolution.

## Domain consistency

A booking references a workspace, client, service, and potentially a trainer. Membership and payment states affect the actions available to staff and clients. Reports depend on the same persisted records rather than a separate UI-only dataset.

The central change was to treat product features as workflows with shared data and invariants, not independent screens.

## Multi-tenancy and portal isolation

Users belong to workspaces through memberships carrying their role and status. Workspace ownership is checked by the backend when accessing business resources. This supports staff who work across studios but increases the importance of scoped repository queries and denied-access tests.

The member portal was deliberately separated from staff identities. Its credentials, routes, and response contracts expose client-scoped information instead of reusing dashboard permissions. This introduces a second session lifecycle in exchange for clearer trust boundaries.

## Scheduling and concurrency

Bookings evolved to account for service duration, trainer availability, overlapping reservations, recurrence, cancellation, completion, and no-show states. Some operations require coordinated validation and transaction handling across several records.

Messaging raised a different concurrency problem: retries and simultaneous staff updates. Retry identifiers and optimistic workflow versions address duplicate sends and conflicting queue actions, while response schemas distinguish internal notes from client replies.

## Platform behavior

Flutter provides shared application code, but Web, Android, and Windows have different runtime and integration constraints. Authentication handoff, QR/camera support, window sizes, and release packaging require platform-specific validation.

Localization similarly affects architecture rather than only copy. French expansion and Arabic right-to-left layout exposed constraints in navigation, forms, tables, and dialogs. The application uses localization catalogs and responsive composition, with regression checks for the affected surfaces.

## Operational reliability

The backend adopted Alembic migrations, separate production migration execution, liveness and readiness endpoints, structured request IDs, and environment-aware validation.

A concrete integration issue involved fictional `.test` email identities: a user could authenticate, but strict response validation rejected the demo address and produced a server error in dependent staff views. The response validation was adjusted for the controlled demo context without weakening normal account-registration rules.

The deterministic Northline demo also evolved beyond random fixtures. It uses known identities and connected records, applies database and provider guardrails, and verifies relationships and expected aggregates before committing a rebuild.

## Trade-offs

The result favors explicit business rules, verifiable environment boundaries, and testable authorization over a minimal code footprint. It also brings maintenance costs: two auth domains, provider-specific flows, extensive regression checks, responsive UI variations, and database migrations.

The private repositories contain the implementation and test suite. This public documentation describes the historical snapshot identified by the [Build manifest](../BUILD_MANIFEST.md), not an independently audited production service.

For system topology and decisions, see [Architecture](../ARCHITECTURE.md) and [Architecture decisions](../architecture/DECISIONS.md).