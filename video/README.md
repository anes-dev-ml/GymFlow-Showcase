# GymFlow Walkthrough

The current GymFlow showcase is built around the reviewed **53-image visual gallery**, architecture documentation, engineering case studies, and exact application provenance. That format gives visitors both a quick product view and a deeper technical path without requiring a long walkthrough video.

A future release can add a concise edited walkthrough when motion helps explain the connected workflows better than static captures.

## Suggested walkthrough narrative

Rather than moving page by page, a GymFlow walkthrough would follow one connected operating story:

| Chapter | Story |
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

A technical walkthrough could highlight:

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

## Capture standard

Any public walkthrough follows the same presentation rules as the screenshot gallery:

- fictional identities and business records;
- manual, simulated, or Stripe test-mode payment states;
- no usable credentials or access codes;
- no unrelated personal notifications or local-machine details;
- the exact frontend, backend, and showcase revisions recorded with the media release.

When a walkthrough is added, its release record can include duration, captions, format, checksum, and the application revisions it represents.

For the current product tour, see the [GymFlow Visual Gallery](../screenshots/README.md).
