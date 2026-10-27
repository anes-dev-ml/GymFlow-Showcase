# Engineering implementation

This document examines the implementation patterns behind GymFlow: authorization, domain state, concurrent updates, and operational failure handling. System topology and the data model are documented in [Architecture](../ARCHITECTURE.md); major design choices are in [Architecture decisions](../architecture/DECISIONS.md).

## Application layers

The Flutter application is organized by feature. Each feature separates models and API repositories, state coordination, and presentation. The router manages navigation among public, staff, and member-portal surfaces, while the backend owns authorization decisions.

FastAPI groups its routes under `/api/v1`. Pydantic schemas define request and response contracts; services coordinate business rules; repositories handle scoped persistence; SQLAlchemy models and Alembic govern relational state and schema changes.

The intent is to make each operation traceable from UI action through validation, authorization, database state, and tests.

## Authorization and ownership

Workspaces define the tenant boundary. Requests must resolve the authenticated identity, active membership, role, and resource ownership before accessing business data.

The member portal uses a distinct credential and route family rather than treating clients as staff members with fewer permissions. Portal schemas expose client-scoped information and omit internal staff metadata. Frontend route restrictions improve usability but do not substitute for backend authorization.

This design introduces two session lifecycles and additional test coverage in return for stronger separation between audiences.

## Domain consistency

### Scheduling and attendance

Bookings combine service duration, trainer requirements, published availability, overlap checks, recurrence, and lifecycle state. Occurrences in a recurring series can be managed independently. Attendance and front-desk check-ins remain separate records from scheduled sessions.

### Payments and billing

Client payments and a studio's subscription to GymFlow are different financial relationships. Stripe webhook processing verifies signatures, records provider event identifiers, and handles repeated delivery. Demonstration payments use manual, simulated, or test-mode states.

### Messaging and presence

Conversation participants, assignment, priority, and workflow status are maintained explicitly. Client-visible replies and internal notes have different audiences. Retry identifiers prevent duplicate sends, while optimistic versions detect concurrent workflow updates.

Staff presence combines connection heartbeats and recent activity across devices rather than relying on one mutable online flag. The returned information is constrained by role and visibility policy.

## Operational behavior

An `X-Request-ID` links frontend errors with structured backend diagnostics. Liveness checks distinguish an executing process from readiness checks that verify required dependencies.

Alembic migrations are executed separately from production web startup. Configuration applies stricter validation in production for secrets, provider modes, network origins, and debug exposure.

The deterministic Northline Performance Club demo is rebuilt under explicit database, environment, provider, confirmation, and schema-allowlist guards. Its records and aggregate values are checked before a transaction is committed.

## Verification and trade-offs

The private repositories contain automated tests for API contracts, tenancy, denied operations, lifecycle conflicts, provider retries, routes, localization, and demo safeguards. The public [Quality](QUALITY.md) document explains these layers and their limits.

The architecture prioritizes explicit business rules and separated trust domains. That choice increases the maintenance cost of dual credentials, platform-specific integrations, database migrations, and targeted regression tests. Production hosting, provider accounts, backups, and incident response are deployment concerns, not proven properties of the public showcase.

[Security design](SECURITY_OVERVIEW.md) · [Operations](OPERATIONS.md)
