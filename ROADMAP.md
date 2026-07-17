# GymFlow Roadmap

GymFlow is complete as a controlled professional demonstration and is presented as a production-oriented SaaS architecture. The roadmap separates release-integrity work, product evolution, provider verification, and production operations.

## Current release baseline

The latest immutable showcase tag is `v1.0.1-showcase`.

`main` contains the tag-bound `v1.0.2-showcase` release record, a patch-level evidence and validation hardening line. It keeps the canonical application snapshots unchanged:

- frontend `b73a623c3985e4bc458d04b4b484887ada593fa5`;
- backend `2234af20d1d9dd143bcac22edc699d3ee7fe515f`.

The release line focuses on:

- accurate release-state documentation;
- centralized machine-readable provenance;
- tracked-file validation;
- traditional local release runners;
- validator regression tests;
- stronger gallery evidence indexing;
- removal of the unusable hosted workflow;
- no green hosted-CI claim.

## Implemented product scope

| Area | Current state |
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

## Release completion

Before tagging `v1.0.2-showcase`:

1. run `.\scripts\validate_release.ps1` or `bash scripts/validate_release.sh`;
2. complete the final privacy and visual review;
3. commit any resulting corrections;
4. confirm the working tree is clean;
5. create the tag on the reviewed commit;
6. run the release form of the local validator.

No application feature work or screenshot recapture is currently required by the release contract unless the final human review discovers a real defect.

## Product evolution

Possible future product work includes:

- structured workout programs and coach-assigned plans;
- client goals, measurements, and richer progress history;
- class capacity, waitlists, and automated promotion;
- recurring membership renewals and dunning workflows;
- staff shifts and schedule planning;
- deeper report drill-downs and saved report views;
- multi-location organization management;
- controlled file and media storage;
- audit retention, export, and archival policies.

These ideas are not required to demonstrate the current system. They represent possible growth after the release baseline is preserved.

## Provider verification

A live deployment requires target-environment verification for:

### Stripe

- account mode, credentials, prices, and Connect model;
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

## Production infrastructure

Commercial operation would add:

- managed frontend and backend hosting;
- managed PostgreSQL and Redis;
- domains, TLS, networking, and secret management;
- staging migrations and deployed isolation testing;
- centralized logs, uptime checks, latency and error alerts;
- backup retention, recovery objectives, and restore drills;
- dependency automation, static analysis, image scanning, SBOM, and provenance;
- accessibility, browser, device, load, and performance verification;
- privacy, terms, retention, support, and commercial operating policies.

## Visual and review experience

A future release may add an edited product or engineering walkthrough. Any media release will use a new semantic identifier and record its exact source snapshot, duration, captions status, and integrity metadata rather than silently changing an existing evidence set.

## Production claim boundary

GymFlow may be described as **production-oriented** because it implements strict configuration, tenant and credential boundaries, migrations, Docker packaging, health checks, observability foundations, and release validation.

It should be described as **production-operated** only after provider flows, deployed isolation, managed infrastructure, monitoring, backup and restore, security controls, and legal and operational responsibilities are verified in the target environment.
