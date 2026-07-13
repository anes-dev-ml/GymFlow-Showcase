# GymFlow Roadmap

This roadmap separates work required for the public showcase from work required for a real commercial production launch.

The application is ready for a controlled professional demo. The remaining showcase work is visual capture and release packaging. Production operation remains deployment- and provider-specific.

## Status legend

| Status | Meaning |
|---|---|
| Complete | Implemented and verified in the current source/release process |
| Capture pending | Documentation is ready; final visual asset must be recorded |
| Environment-specific | Implemented in code but requires target credentials/infrastructure |
| Planned | Valuable future improvement, not claimed as complete |

## Showcase release

| Item | Status | Completion evidence |
|---|---|---|
| Product documentation | Complete | README and product case study |
| Architecture documentation | Complete | Context, containers, trust boundaries, ERD, sequences, decisions |
| Engineering case study | Complete | Design choices, reliability, messaging, presence, demo system |
| Security policy | Complete | Private disclosure process |
| Security overview and threat model | Complete | Controls, threat register, residual risks |
| Quality documentation | Complete | CI/test strategy and evidence matrix |
| Operations documentation | Complete | Deployment, migration, observability, backup plan |
| Deterministic demo guide | Complete | Guarded rebuild and validation runbook |
| Release strategy | Complete | Versioning, provenance, artifact rules |
| Showcase repository CI | Complete | Local-link, asset, stale credential, secret-pattern checks |
| Refreshed screenshots | Capture pending | Follow `screenshots/README.md` |
| Product video | Capture pending | Follow `video/README.md` |
| Engineering video | Capture pending / optional | Follow technical walkthrough plan |
| Final artifact checksums | Capture pending | Add after video/build assets are final |
| GitHub release tag | Capture pending | Create after visual assets and manifest are final |
| Social preview image | Capture pending | Use release screenshots and brand assets |
| Repository topics | Manual repository setting | Add recommended topics after public launch |

## Application release state

| Area | Status | Notes |
|---|---|---|
| Public product site | Complete | Localized product and legal surfaces |
| Staff authentication | Complete | Password, verification, recovery, OAuth foundation |
| Workspaces and roles | Complete | Owner/manager/trainer/receptionist |
| Clients and memberships | Complete | Connected lifecycle and detail views |
| Services and availability | Complete | Trainer-aware scheduling inputs |
| Bookings and recurrence | Complete | Lifecycle, no-show, recurring/future cancellation |
| Check-ins and attendance | Complete | Daily and front-desk workflows |
| Client payments | Complete for demo/test | Manual and Stripe-oriented lifecycle |
| SaaS billing | Complete for demo/test | Provider verification depends on release environment |
| Reports and export | Complete for seeded demo | Non-flat deterministic history |
| Notifications and activity | Complete | Read/archive and audit history |
| Professional messaging | Complete | Assignment, priorities, internal notes, idempotency, pagination |
| Staff presence | Complete | Multi-device connection/activity model |
| Client portal | Complete for demo | Separate access, bookings, membership, payments, messages, settings |
| English/French/Arabic | Complete for demo | Manual visual review remains part of each release |
| Web/Android/Windows targets | Implemented | Installable artifacts require reachable backend |

## Production provider verification

These are environment-specific release tasks, not missing architecture.

### Stripe

- [ ] Configure target Stripe account and correct live/test keys.
- [ ] Verify successful client checkout.
- [ ] Verify cancelled checkout return.
- [ ] Verify webhook delivery and signature.
- [ ] Verify duplicate webhook idempotency.
- [ ] Verify refund lifecycle.
- [ ] Verify SaaS billing checkout and portal.
- [ ] Verify Connect model for the intended commercial structure.

### Email

- [ ] Configure verified sender domain.
- [ ] Verify email verification delivery.
- [ ] Verify password recovery delivery.
- [ ] Verify staff invitation delivery.
- [ ] Verify client portal access delivery.
- [ ] Confirm neutral public responses remain non-enumerating.
- [ ] Define bounce, complaint, and sender-reputation handling.

### Google OAuth

- [ ] Configure production web client and redirects.
- [ ] Configure Android client/package/signing fingerprints.
- [ ] Verify existing-account login.
- [ ] Verify first-time identity behavior.
- [ ] Verify missing, invalid, expired, and replayed handoff codes.
- [ ] Verify account-linking policy.

## Production infrastructure

- [ ] Select frontend hosting.
- [ ] Select backend container platform.
- [ ] Provision managed PostgreSQL.
- [ ] Provision managed Redis.
- [ ] Configure private networking/firewall rules.
- [ ] Configure domains and TLS.
- [ ] Configure secret manager and rotation process.
- [ ] Configure production environment variables.
- [ ] Run migration job against staging.
- [ ] Run deployment smoke and isolation tests.

## Observability and incident operations

- [ ] Centralize structured logs.
- [ ] Add uptime checks for liveness and readiness.
- [ ] Define 5xx and latency alerts.
- [ ] Define database and Redis availability alerts.
- [ ] Define Stripe webhook failure alerts.
- [ ] Create operational dashboard.
- [ ] Document on-call/incident contact process.
- [ ] Test request-ID investigation workflow in hosted staging.
- [ ] Define log retention and privacy policy.

## Backups and recovery

- [ ] Configure automated database backups.
- [ ] Define retention and point-in-time recovery.
- [ ] Document RPO/RTO targets.
- [ ] Run isolated restore drill.
- [ ] Validate restored workspace/client/booking/payment/portal data.
- [ ] Record restore duration and lessons.
- [ ] Schedule periodic restore verification.

## Security and supply chain

- [ ] Enable dependency update automation.
- [ ] Enable dependency review on pull requests.
- [ ] Add CodeQL or equivalent SAST.
- [ ] Add container image vulnerability scanning.
- [ ] Review GitHub Actions token permissions.
- [ ] Pin critical actions to reviewed versions/commit SHAs.
- [ ] Generate release SBOM.
- [ ] Generate artifact checksums.
- [ ] Add signing/provenance where practical.
- [ ] Run deployed workspace/portal isolation tests.
- [ ] Schedule dependency and authorization review.

## Performance and scalability

- [ ] Define API performance budget.
- [ ] Load-test authentication and portal access limits.
- [ ] Load-test reports and booking availability.
- [ ] Review high-volume message pagination.
- [ ] Review presence WebSocket/heartbeat scale.
- [ ] Measure database query plans and indexes.
- [ ] Define audit/message retention and archival strategy.
- [ ] Verify connection-pool settings against hosting limits.

## Accessibility and compatibility

- [ ] Run automated web accessibility audit.
- [ ] Complete keyboard navigation review.
- [ ] Review focus order and dialog semantics.
- [ ] Review color contrast and reduced-motion behavior.
- [ ] Define supported browser matrix.
- [ ] Define supported Android and Windows versions.
- [ ] Add automated viewport/golden coverage where valuable.

## Commercial/product operations

- [ ] Finalize privacy policy for actual deployed data handling.
- [ ] Finalize terms and billing/refund policy.
- [ ] Define data retention/deletion workflow.
- [ ] Define customer support and incident communication.
- [ ] Define workspace export/closure process.
- [ ] Review tax, payment, and marketplace obligations for target market.
- [ ] Confirm analytics/cookie policy if analytics are added.

## Next feature work after release

Product development should remain frozen until the showcase release is captured. Afterward, potential roadmap items include:

- richer workout/program domain;
- coach/client goal tracking;
- automated membership renewals and dunning;
- waitlists and class-capacity workflows;
- staff schedule calendar and shift planning;
- richer report drill-downs;
- file/media storage with explicit privacy controls;
- organization-level multi-location management;
- audit retention and export tools;
- accessibility and performance improvements.

These are future product options, not required to prove the current system.

## Production claim rule

GymFlow may be described as **production-oriented** now.

It should be described as **production-operated** only after:

- quality gates are green on a tagged release;
- target provider flows are verified;
- deployed tenant/token isolation passes;
- managed infrastructure and TLS are configured;
- monitoring and alerts are active;
- backup and restore are tested;
- security/supply-chain checks are enabled;
- legal and operational responsibilities are assigned.
