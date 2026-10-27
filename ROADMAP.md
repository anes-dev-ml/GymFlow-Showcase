# Roadmap

GymFlow's current showcase records an integrated gym-operations application, not a commercially operated service. The priorities below are proposed next steps; they are not features claimed for the tagged snapshot.

## Product evolution

Potential extensions include structured training programs, deeper progress tracking, class capacity and waitlists, recurring membership renewals, staff shift scheduling, advanced reporting, and multi-location management.

These capabilities would build on the existing workspace, scheduling, membership, payments, and portal model. Each should be evaluated against demand and operational complexity before implementation.

## Commercial operations

A live service requires more than application code. Before customer operation, the deployment must have:

- verified hosting, domains, TLS, managed PostgreSQL/Redis, and secret management;
- correctly configured Stripe, email, and OAuth accounts, with end-to-end provider testing;
- backups, restore exercises, monitoring, alerting, and incident procedures;
- security and dependency reviews, load/performance checks, and cross-device acceptance;
- privacy, accessibility, retention, legal, and support processes appropriate to its market.

These are deployment gates, not assurances already established by the public Showcase. The backend's production completion checklist contains actionable technical checks.

## Product stage and release direction

The existing `v1.0.4-showcase` tag identifies the reviewed historical application and image snapshot. New public versions should tie changes in capabilities or evidence to exact source revisions without moving prior tags.

See [Release process](RELEASES.md), [Operations](docs/OPERATIONS.md), and [Build manifest](BUILD_MANIFEST.md).