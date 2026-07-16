# GymFlow Roadmap

GymFlow is complete as a controlled professional demonstration and is presented
as a production-oriented SaaS architecture. The roadmap below separates future
product evolution from the deployment, provider, and operational work required
for a live commercial service.

## Current showcase release

The `v1.0.0-showcase` release includes:

- the public product, architecture, engineering, security, quality, operations,
  and demo case studies;
- exact frontend and backend source provenance;
- a deterministic Northline Performance Club demo contract;
- 53 screenshots across desktop, client portal, mobile, localization, and
  engineering galleries;
- documented local release validation and the hosted-runner limitation;
- no public walkthrough video or installable binary.

## Implemented product scope

| Area | Current state |
|---|---|
| Public product site | Localized product, pricing, security, contact, and legal surfaces |
| Authentication | Password, verification, recovery, OAuth foundation, invitations |
| Workspaces and roles | Owner, manager, trainer, receptionist |
| Clients and memberships | Connected lifecycle, history, and detail views |
| Services and availability | Trainer-aware scheduling inputs |
| Bookings | Duration, availability, recurrence, cancellation, completion, and no-show states |
| Attendance | Daily sheet plus front-desk check-in and check-out |
| Client payments | Manual and Stripe-oriented demo/test lifecycle |
| SaaS billing | Subscription and provider-boundary architecture |
| Reports | Seeded revenue, client, booking, and attendance trends |
| Notifications and audit | Read state, grouping, and operational history |
| Professional messaging | Assignment, priorities, internal notes, idempotency, pagination |
| Staff presence | Connection, activity, multi-device aggregation, visibility |
| Client portal | Separate access, bookings, membership, payments, progress, messages, settings |
| Internationalization | English, French, Arabic, and RTL presentation |
| Platforms | Flutter Web, Android, and Windows targets |

## Product evolution

Future product development may extend GymFlow in several directions:

- structured workout programs and coach-assigned plans;
- client goals, measurements, and richer progress history;
- class capacity, waitlists, and automated promotion;
- recurring membership renewals and dunning workflows;
- staff shifts and schedule planning;
- deeper report drill-downs and saved report views;
- multi-location organization management;
- controlled file and media storage;
- audit retention, export, and archival policies.

These ideas are not required to demonstrate the current system. They represent
possible product growth after the release baseline is preserved.

## Provider verification

A live deployment would require target-environment verification for:

### Stripe

- account mode and credentials;
- checkout success and cancellation;
- webhook delivery, signatures, and duplicate-event handling;
- refund lifecycle and SaaS billing portal;
- the intended Stripe Connect and KYC model.

### Email

- verified sender domain;
- verification, recovery, invitation, and portal-access delivery;
- bounce, complaint, and sender-reputation handling.

### Google OAuth

- production web client and redirect configuration;
- Android package and signing fingerprints;
- account linking, first-time access, expiry, invalid handoffs, and replay
  behavior.

## Production infrastructure

Commercial operation would add:

- managed frontend and backend hosting;
- managed PostgreSQL and Redis;
- domains, TLS, networking, and secret management;
- staging migrations and deployed isolation testing;
- centralized logs, uptime checks, latency and error alerts;
- database backup retention, recovery objectives, and restore drills;
- dependency automation, static analysis, image scanning, SBOM, and provenance;
- accessibility, browser, device, and performance verification;
- privacy, terms, retention, support, and commercial operating policies.

## Visual and review experience

The current release is screenshot-bearing and self-contained. A future release
may add an edited product walkthrough or a deeper engineering walkthrough. Any
such media would be tied to its own source snapshot and semantic release rather
than silently changing the evidence attached to `v1.0.0-showcase`.

## Production claim boundary

GymFlow may be described as **production-oriented** because it implements strict
configuration, tenant and credential boundaries, migrations, Docker packaging,
health checks, observability foundations, and release validation.

It should be described as **production-operated** only after provider flows,
deployed isolation, managed infrastructure, monitoring, backup and restore,
security controls, and legal and operational responsibilities are verified in
the target environment.
