# GymFlow Roadmap

GymFlow is complete as a professional product showcase and already covers the core operating loop of a modern gym or fitness studio. The roadmap focuses on where the product could grow next and what would be added for a live commercial deployment.

## Current product foundation

| Area | Current implementation |
|---|---|
| Public product site | Localized product, pricing, security, contact, and legal surfaces |
| Authentication | Password, verification, recovery, OAuth foundation, invitations |
| Workspaces and roles | Owner, manager, trainer, receptionist |
| Clients and memberships | Connected lifecycle, history, and detail views |
| Services and availability | Trainer-aware scheduling inputs |
| Bookings | Duration, availability, recurrence, cancellation, completion, no-show states |
| Attendance | Daily sheet plus front-desk check-in and check-out |
| Client payments | Manual and Stripe-oriented test/demo lifecycle |
| SaaS billing | Subscription and provider-boundary architecture |
| Reports | Seeded revenue, client, booking, and attendance trends |
| Notifications and audit | Read state, grouping, and operational history |
| Professional messaging | Assignment, priorities, internal notes, idempotency, pagination |
| Staff presence | Connection, activity, multi-device aggregation, visibility |
| Client portal | Separate access, bookings, membership, payments, progress, messages, settings |
| Internationalization | English, French, Arabic, RTL presentation |
| Platforms | Flutter Web, Android, Windows targets |

The tagged showcase release and exact source revisions are maintained in [Release Integrity](RELEASES.md) and the [Build Manifest](BUILD_MANIFEST.md).

## Product evolution

Natural next steps for the product include:

- structured workout programs and coach-assigned plans;
- client goals, measurements, and richer progress history;
- class capacity, waitlists, and automated promotion;
- recurring membership renewals and dunning workflows;
- staff shifts and schedule planning;
- deeper report drill-downs and saved report views;
- multi-location organization management;
- controlled file and media storage;
- audit retention, export, and archival policies.

These ideas build on the existing domain model rather than replacing it. The current system already provides the tenant, role, client, booking, payment, communication, and portal foundations they would use.

## Provider deployment

A live environment would connect the existing provider boundaries to production accounts and domains.

### Stripe

- production account mode, credentials, prices, and Connect model;
- checkout success and cancellation;
- webhook delivery, signatures, duplicate handling, and refunds;
- billing portal and KYC behavior where applicable.

### Email

- verified sender domain;
- verification, recovery, invitation, and portal-access delivery;
- bounce, complaint, and sender-reputation handling.

### Google OAuth

- production clients and redirect configuration;
- Android package and signing fingerprints;
- account linking, expiry, invalid handoffs, and replay behavior.

## Commercial operations

Moving from a professional showcase to an operated SaaS service would add:

- managed frontend and backend hosting;
- managed PostgreSQL and Redis;
- domains, TLS, networking, and secret management;
- staging migrations and deployed isolation testing;
- centralized logs, uptime checks, latency and error alerts;
- backup retention, recovery objectives, and restore drills;
- dependency automation, static analysis, image scanning, SBOM, and provenance;
- accessibility, browser, device, load, and performance verification;
- privacy, terms, retention, support, and commercial operating policies.

The application architecture already separates these environment-specific responsibilities from the core product code, which makes them deployment work rather than a redesign of the system.

## Presentation and review

The current showcase uses a large reviewed screenshot gallery to cover the product across desktop, mobile, client portal, localization, and engineering views. A future release could add a concise edited walkthrough when it adds meaningful value to the presentation.

## Product stage

GymFlow is best described as a **production-oriented SaaS implementation and professional engineering showcase**. It contains production-style configuration, tenant and credential boundaries, migrations, Docker packaging, health checks, observability foundations, provider integrations, deterministic demo tooling, and release validation.

Operating it as a commercial SaaS would be the next stage: connecting verified providers and managed infrastructure, then adding the monitoring, backup, security, legal, and support processes required by the target deployment.
