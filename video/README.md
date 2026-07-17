# GymFlow Walkthrough Status

**Current media status:** Not included in `v1.0.3-showcase`.

The `v1.0.3-showcase` provenance-bound release record does **not include** a public walkthrough video, thumbnail, captions file, or downloadable video asset.

The current evidence is provided through:

- the [53-image visual gallery](../screenshots/README.md);
- the engineering case study;
- the exact source provenance in the [Build Manifest](../BUILD_MANIFEST.md);
- the machine-readable [`release/evidence-manifest.json`](../release/evidence-manifest.json).

The previous immutable release is `v1.0.2-showcase`. It also does not claim a current provenance-bound walkthrough.

An older standalone GitHub release associated with a non-showcase `v1.0.0` tag may contain a walkthrough asset. That asset is **historical media**. It predates the canonical source snapshot used by the current release and is not part of the current record.

## Intended walkthrough narrative

A future GymFlow walkthrough would present one connected product story rather than a page-by-page feature list.

| Chapter | Product or engineering evidence |
|---|---|
| Product context | Public website, target users, and the operational problem |
| Studio overview | Owner dashboard, current activity, revenue, bookings, and attendance |
| Client lifecycle | Membership, payments, visits, bookings, and portal access around one client |
| Team operations | Roles, trainer availability, invitations, and staff presence |
| Scheduling | Services, availability, recurring bookings, cancellation, and no-show states |
| Financial workflows | Client payments, receipts, reporting, and SaaS billing boundaries |
| Collaboration | Professional messaging, assignment, internal notes, notifications, and audit history |
| Client portal | Separate credential model and client-scoped self-service |
| Responsive product | Mobile experience, French presentation, and Arabic RTL support |
| Engineering close | Architecture, security, observability, Docker, validation, and demo safety |

## Engineering themes

A technical walkthrough would emphasize:

- workspace-scoped multi-tenancy;
- staff JWT and client portal token separation;
- role and resource authorization;
- relational business modeling and Alembic migrations;
- booking duration, trainer availability, and recurring scheduling;
- payment and webhook idempotency;
- audience-safe messaging and optimistic workflow versions;
- multi-device staff presence;
- request IDs, structured logs, liveness, and readiness;
- deterministic demo rebuilding with destructive-operation guards.

## Data and provider boundary

Any future public walkthrough must use fictional identities and business records. Payment demonstrations remain manual, simulated, or Stripe test-mode only and do not process real money.

Provider-dependent capabilities such as live Stripe configuration, verified email delivery, Google OAuth redirects, and production infrastructure are not presented as verified without corresponding release evidence.

## Future media releases

A later video will be published under a new provenance-bound release. Its record will include:

- exact frontend, backend, and showcase source snapshots;
- duration;
- captions status;
- file size and format;
- SHA-256 checksum;
- platform and provider boundaries;
- explicit included and omitted evidence.
