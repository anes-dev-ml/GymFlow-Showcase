# GymFlow Walkthrough Status

The current `v1.0.1-showcase` candidate does not include a public walkthrough video, thumbnail, captions file, or downloadable video asset as part of its provenance-bound evidence contract.

The current evidence is provided through the
[53-image visual gallery](../screenshots/README.md), the engineering case study,
and the exact source provenance recorded in the
[build manifest](../BUILD_MANIFEST.md).

An older standalone GitHub release associated with a non-showcase `v1.0.0` tag
may contain a walkthrough asset. That asset is historical media: it predates the
canonical frontend snapshot recorded for `v1.0.1-showcase`, is not part of the
current candidate, and must not be described as evidence for the final release
unless it is revalidated and republished under a new provenance-bound tag.

The historical `v1.0.0-showcase` tag remains the earlier documentation and
screenshot baseline. Existing historical tags are not moved or silently
retargeted.

## Intended walkthrough narrative

A future GymFlow walkthrough would present one connected product story rather
than a page-by-page feature list.

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

A technical walkthrough would emphasize the decisions that distinguish GymFlow
from a visual prototype:

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

Any public walkthrough associated with GymFlow represents fictional identities
and business records. Payment demonstrations remain in manual, simulated, or
Stripe test-mode state and do not process real money.

Provider-dependent capabilities such as live Stripe configuration, verified
email delivery, Google OAuth redirects, and production infrastructure are not
presented as verified unless the corresponding release records that evidence.

## Future media releases

A later release may add a public product or engineering walkthrough. That media
would be published under its own semantic release with an updated source
snapshot, manifest entry, duration, captions status, and integrity metadata.
