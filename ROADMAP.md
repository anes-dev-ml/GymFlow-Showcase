# GymFlow Roadmap

This roadmap separates the completed `v1.0.0-showcase` engineering case study
from later media work and from the work required to operate GymFlow as a real
commercial service.

The current tag is a documentation-only portfolio release. It intentionally
omits screenshots, video, and installable binaries rather than presenting stale
or weakly sourced media. Those assets may be added in a later media-bearing
release after a fresh demo rebuild, route rehearsal, capture, privacy review,
and provenance update.

## Status legend

| Status | Meaning |
|---|---|
| Complete | Implemented and verified for the current source or release process |
| Deferred to media release | Deliberately omitted from `v1.0.0-showcase`; requires a later provenance-backed capture |
| Environment-specific | Implemented in code but requires target credentials or infrastructure |
| Manual repository setting | Must be configured in GitHub rather than committed as source |
| Planned | Valuable future improvement, not claimed as complete |

## `v1.0.0-showcase` release state

| Item | Status | Completion evidence |
|---|---|---|
| Product documentation | Complete | README and product case study |
| Architecture documentation | Complete | Context, containers, trust boundaries, ERD, sequences, decisions |
| Engineering case study | Complete | Design choices, reliability, messaging, presence, demo system |
| Security policy | Complete | Private disclosure process |
| Security overview and threat model | Complete | Controls, threat register, residual risks |
| Quality documentation | Complete | Test strategy and evidence matrix |
| Operations documentation | Complete | Deployment, migration, observability, backup plan |
| Deterministic demo guide | Complete | Guarded rebuild and validation runbook |
| Release strategy | Complete | Versioning, provenance, artifact rules |
| Showcase validator | Complete | Required-file, local-link, unsafe-file, stale-value, secret-pattern, and release-contract checks |
| Frontend release validation | Complete locally | Equivalent local validation completed before merge because hosted jobs could not start |
| Backend release validation | Complete locally | Equivalent local validation completed before merge because hosted jobs could not start |
| Showcase release validation | Complete locally | `python scripts/check_showcase.py` passed before tagging |
| Refreshed screenshots | Deferred to media release | Not included in `v1.0.0-showcase` |
| Product video | Deferred to media release | Not included in `v1.0.0-showcase` |
| Engineering video | Deferred and optional | Not included in `v1.0.0-showcase` |
| Artifact checksums | Not applicable | No downloadable media or binaries are included |
| Git tag | Complete | `v1.0.0-showcase` |
| GitHub release page | Manual repository task | Create or verify from `v1.0.0-showcase` before public promotion |
| Social preview image | Manual repository setting | Configure from an approved current-release design |
| Repository topics | Manual repository setting | Add after public visibility is enabled |

## Application release state

| Area | Status | Notes |
|---|---|---|
| Public product site | Complete | Localized product and legal surfaces |
| Staff authentication | Complete | Password, verification, recovery, OAuth foundation |
| Workspaces and roles | Complete | Owner, manager, trainer, receptionist |
| Clients and memberships | Complete | Connected lifecycle and detail views |
| Services and availability | Complete | Trainer-aware scheduling inputs |
| Bookings and recurrence | Complete | Lifecycle, no-show, recurring and future cancellation |
| Check-ins and attendance | Complete | Daily and front-desk workflows |
| Client payments | Complete for demo/test | Manual and Stripe-oriented lifecycle |
| SaaS billing | Complete for demo/test | Provider verification depends on the release environment |
| Reports and export | Complete for seeded demo | Non-flat deterministic history |
| Notifications and activity | Complete | Read, archive, and audit history |
| Professional messaging | Complete | Assignment, priorities, internal notes, idempotency, pagination |
| Staff presence | Complete | Multi-device connection and activity model |
| Client portal | Complete for demo | Separate access, bookings, membership, payments, messages, settings |
| English, French, and Arabic | Complete for demo | Manual visual review remains part of each media release |
| Web, Android, and Windows targets | Implemented | Installable artifacts require a reachable backend |

## Later media-bearing showcase release

A later visual release is optional. If created, it must use the exact source
snapshot recorded in the updated build manifest and complete all of the
following:

- [ ] Rebuild and validate `gymflow_demo`.
- [ ] Complete the route rehearsal in `DEMO.md`.
- [ ] Capture only fictional identities and test/demo payments.
- [ ] Review every frame for credentials, personal paths, errors, and stale UI.
- [ ] Record the exact screenshot inventory.
- [ ] Record the video URL, duration, source snapshot, and captions status.
- [ ] Add checksums for downloadable packs or binaries.
- [ ] Update the changelog and build manifest.
- [ ] Run the expanded showcase validator.
- [ ] Create a new semantic release tag rather than silently replacing public assets.

## Production provider verification

These are environment-specific release tasks, not missing architecture.

### Stripe

- [ ] Configure the target Stripe account and correct live/test keys.
- [ ] Verify successful client checkout.
- [ ] Verify cancelled checkout return.
- [ ] Verify webhook delivery and signature.
- [ ] Verify duplicate-webhook idempotency.
- [ ] Verify the refund lifecycle.
- [ ] Verify SaaS billing checkout and portal.
- [ ] Verify the Connect model for the intended commercial structure.

### Email

- [ ] Configure a verified sender domain.
- [ ] Verify email-verification delivery.
- [ ] Verify password-recovery delivery.
- [ ] Verify staff-invitation delivery.
- [ ] Verify client-portal-access delivery.
- [ ] Confirm neutral public responses remain non-enumerating.
- [ ] Define bounce, complaint, and sender-reputation handling.

### Google OAuth

- [ ] Configure the production web client and redirects.
- [ ] Configure Android client, package, and signing fingerprints.
- [ ] Verify existing-account login.
- [ ] Verify first-time identity behavior.
- [ ] Verify missing, invalid, expired, and replayed handoff codes.
- [ ] Verify the account-linking policy.

## Production infrastructure

- [ ] Select frontend hosting.
- [ ] Select a backend container platform.
- [ ] Provision managed PostgreSQL.
- [ ] Provision managed Redis.
- [ ] Configure private networking and firewall rules.
- [ ] Configure domains and TLS.
- [ ] Configure a secret manager and rotation process.
- [ ] Configure production environment variables.
- [ ] Run the migration job against staging.
- [ ] Run deployment smoke and isolation tests.

## Observability and incident operations

- [ ] Centralize structured logs.
- [ ] Add uptime checks for liveness and readiness.
- [ ] Define 5xx and latency alerts.
- [ ] Define database and Redis availability alerts.
- [ ] Define Stripe webhook failure alerts.
- [ ] Create an operational dashboard.
- [ ] Document the on-call and incident contact process.
- [ ] Test request-ID investigation in hosted staging.
- [ ] Define log retention and privacy policy.

## Backups and recovery

- [ ] Configure automated database backups.
- [ ] Define retention and point-in-time recovery.
- [ ] Document RPO and RTO targets.
- [ ] Run an isolated restore drill.
- [ ] Validate restored workspace, client, booking, payment, and portal data.
- [ ] Record restore duration and lessons.
- [ ] Schedule periodic restore verification.

## Security and supply chain

- [ ] Enable dependency-update automation.
- [ ] Enable dependency review on pull requests.
- [ ] Add CodeQL or equivalent SAST.
- [ ] Add container-image vulnerability scanning.
- [ ] Review GitHub Actions token permissions.
- [ ] Pin critical actions to reviewed full commit SHAs.
- [ ] Generate a release SBOM for binary releases.
- [ ] Generate artifact checksums for downloadable releases.
- [ ] Add signing or provenance where practical.
- [ ] Run deployed workspace and portal isolation tests.
- [ ] Schedule dependency and authorization review.

## Performance and scalability

- [ ] Define an API performance budget.
- [ ] Load-test authentication and portal-access limits.
- [ ] Load-test reports and booking availability.
- [ ] Review high-volume message pagination.
- [ ] Review presence WebSocket and heartbeat scale.
- [ ] Measure database query plans and indexes.
- [ ] Define audit and message retention and archival strategy.
- [ ] Verify connection-pool settings against hosting limits.

## Accessibility and compatibility

- [ ] Run an automated web accessibility audit.
- [ ] Complete keyboard-navigation review.
- [ ] Review focus order and dialog semantics.
- [ ] Review color contrast and reduced-motion behavior.
- [ ] Define the supported browser matrix.
- [ ] Define supported Android and Windows versions.
- [ ] Add automated viewport or golden coverage where valuable.

## Commercial and product operations

- [ ] Finalize the privacy policy for actual deployed data handling.
- [ ] Finalize terms and billing/refund policy.
- [ ] Define the data-retention and deletion workflow.
- [ ] Define customer support and incident communication.
- [ ] Define the workspace export and closure process.
- [ ] Review tax, payment, and marketplace obligations for the target market.
- [ ] Confirm the analytics and cookie policy if analytics are added.

## Potential product work after the release freeze

Possible future areas include:

- richer workout and program domains;
- coach and client goal tracking;
- automated membership renewals and dunning;
- waitlists and class-capacity workflows;
- staff schedule calendar and shift planning;
- richer report drill-downs;
- file and media storage with explicit privacy controls;
- organization-level multi-location management;
- audit retention and export tools;
- accessibility and performance improvements.

These are future product options, not requirements for the current engineering
case study.

## Production claim rule

GymFlow may be described as **production-oriented** now.

It should be described as **production-operated** only after:

- quality gates pass on a deployment release;
- target provider flows are verified;
- deployed tenant and token isolation passes;
- managed infrastructure and TLS are configured;
- monitoring and alerts are active;
- backup and restore are tested;
- security and supply-chain checks are enabled;
- legal and operational responsibilities are assigned.