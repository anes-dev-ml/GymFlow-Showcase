# GymFlow Roadmap

This roadmap separates the completed `v1.0.0-showcase` release from later media
work and from the work required to operate GymFlow as a real commercial service.

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
| Showcase release validation | Complete locally | `python scripts/check_showcase.py` must pass before tagging |
| Screenshot gallery | Complete | 53 tracked screenshots across 5 approved galleries |
| Product video | Not included | No public URL, binary, duration, thumbnail, or checksum is claimed |
| Engineering video | Optional future release | Not included in `v1.0.0-showcase` |
| Installable artifacts | Not included | No APK, Windows archive, or checksum is claimed |
| Git tag | Pending final validation | Create `v1.0.0-showcase` after final validator success |
| GitHub release page | Manual repository task | Create or verify after tag publication |
| Social preview image | Manual repository setting | Configure from an approved current-release design |
| Repository topics | Manual repository setting | Add after public visibility is enabled |

## Screenshot inventory

| Gallery | Count |
|---|---:|
| Desktop | 22 |
| Client portal | 10 |
| Mobile | 7 |
| Localization | 4 |
| Engineering evidence | 10 |
| **Total** | **53** |

Any replacement screenshot set must come from the canonical source snapshot,
use fictional demo data, pass privacy review, and update the build manifest.

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

## Future media-bearing release

A later release may add an edited product walkthrough or technical video. Before
that release:

- [ ] Rebuild and validate `gymflow_demo`.
- [ ] Complete the route rehearsal in `DEMO.md`.
- [ ] Confirm screenshots still match the canonical source snapshot.
- [ ] Review every frame for credentials, personal paths, errors, and stale UI.
- [ ] Record the video URL, duration, source snapshot, and captions status.
- [ ] Add checksums for downloadable packs or binaries.
- [ ] Update the changelog and build manifest.
- [ ] Run the showcase validator.
- [ ] Create a new semantic release tag rather than replacing public assets silently.

## Production provider verification

These are environment-specific release tasks, not missing architecture.

### Stripe

- [ ] Configure target account and correct live/test keys.
- [ ] Verify successful and cancelled checkout.
- [ ] Verify webhook delivery, signature, and duplicate-event idempotency.
- [ ] Verify refund lifecycle and SaaS billing portal.
- [ ] Confirm the intended Connect model and KYC boundary.

### Email

- [ ] Configure a verified sender domain.
- [ ] Verify verification, recovery, invitation, and portal-access delivery.
- [ ] Define bounce, complaint, and sender-reputation handling.

### Google OAuth

- [ ] Configure production web client and redirects.
- [ ] Configure Android package and signing fingerprints.
- [ ] Verify existing-account, first-time, invalid, expired, and replay behavior.
- [ ] Confirm account-linking policy.

## Production infrastructure and operations

- [ ] Select frontend and backend hosting.
- [ ] Provision managed PostgreSQL and Redis.
- [ ] Configure domains, TLS, networking, secrets, and rotation.
- [ ] Run staging migrations, smoke tests, and deployed isolation tests.
- [ ] Centralize logs and define uptime, latency, 5xx, database, Redis, and webhook alerts.
- [ ] Configure backups, retention, RPO/RTO, and restore drills.
- [ ] Add dependency automation, SAST, image scanning, SBOM, and provenance where practical.
- [ ] Complete accessibility, browser, device, and performance review.
- [ ] Finalize privacy, terms, retention, support, and commercial operating policies.

## Production claim rule

GymFlow may be described as **production-oriented** now. It should be described
as **production-operated** only after provider flows, deployed isolation,
managed infrastructure, monitoring, backup and restore, security checks, and
legal/operational responsibilities are verified in the target environment.
