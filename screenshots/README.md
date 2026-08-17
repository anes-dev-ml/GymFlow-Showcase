# GymFlow Visual Gallery

This gallery presents GymFlow across its public website, staff application, client portal, mobile layouts, localization, and engineering views. The current showcase includes **53 reviewed images** tied to the application revisions recorded in the [Build Manifest](../BUILD_MANIFEST.md).

All people, studios, messages, bookings, and financial records shown here are fictional. Payment states are manual, simulated, or Stripe test-mode only.

## Gallery overview

| Gallery | Directory | Count | What it covers |
|---|---|---:|---|
| Desktop | [`desktop/`](desktop/) | 22 | Public site and staff operations |
| Client portal | [`portal/`](portal/) | 10 | Member access and self-service |
| Mobile | [`mobile/`](mobile/) | 7 | Responsive public, staff, and portal surfaces |
| Localization | [`localization/`](localization/) | 4 | French and Arabic/RTL presentation |
| Engineering | [`engineering/`](engineering/) | 10 | Architecture, schema, API, runtime, deterministic data, and source provenance |
| **Total** |  | **53** |  |

## Selected views

| Owner operations | Client lifecycle |
|---|---|
| ![GymFlow owner dashboard](desktop/02-owner-dashboard.png) | ![GymFlow client command center](desktop/03-client-command-center.png) |

| Professional messaging | Client scheduling |
|---|---|
| ![GymFlow professional messaging](desktop/07-professional-messaging.png) | ![GymFlow client portal bookings](portal/02-bookings.png) |

| Mobile portal | Arabic RTL |
|---|---|
| ![GymFlow mobile portal](mobile/01-portal-home.png) | ![GymFlow Arabic RTL interface](localization/01-arabic-rtl.png) |

## Desktop application

| File | What it shows |
|---|---|
| [`01-public-home.png`](desktop/01-public-home.png) | Public positioning, navigation, product entry points, and multilingual presentation. |
| [`02-owner-dashboard.png`](desktop/02-owner-dashboard.png) | Workspace overview with operational totals, revenue, bookings, activity, and setup state. |
| [`03-client-command-center.png`](desktop/03-client-command-center.png) | One client context connecting membership, bookings, payments, visits, and portal access. |
| [`04-staff-presence.png`](desktop/04-staff-presence.png) | Role-aware online, away, offline, and last-seen staff visibility. |
| [`05-bookings.png`](desktop/05-bookings.png) | Operational scheduling with services, trainers, dates, and lifecycle states. |
| [`06-reports.png`](desktop/06-reports.png) | Seeded trends and filters for revenue, clients, bookings, and attendance. |
| [`07-professional-messaging.png`](desktop/07-professional-messaging.png) | Assigned communication workspace with queue, open thread, internal workflow, and composer. |
| [`08-public-features.png`](desktop/08-public-features.png) | Public explanation of connected product capabilities. |
| [`09-public-pricing.png`](desktop/09-public-pricing.png) | SaaS pricing presentation and plan boundaries. |
| [`10-public-security.png`](desktop/10-public-security.png) | Public security positioning and trust-oriented product copy. |
| [`11-auth.png`](desktop/11-auth.png) | Authentication entry point and account-access choices. |
| [`12-clients.png`](desktop/12-clients.png) | Client search, filtering, lifecycle state, and operational actions. |
| [`13-plans.png`](desktop/13-plans.png) | Membership-plan configuration, pricing, status, and lifecycle controls. |
| [`14-services.png`](desktop/14-services.png) | Bookable service definitions with duration, price, and trainer requirements. |
| [`15-trainer-availability.png`](desktop/15-trainer-availability.png) | Trainer scheduling availability used by booking validation. |
| [`16-invitations.png`](desktop/16-invitations.png) | Staff invitation lifecycle and role assignment. |
| [`17-check-ins.png`](desktop/17-check-ins.png) | Daily attendance and front-desk visit management. |
| [`18-payments.png`](desktop/18-payments.png) | Client payment ledger, methods, states, and collection actions. |
| [`19-notifications.png`](desktop/19-notifications.png) | Grouped operational notifications with read/unread state. |
| [`20-activity-logs.png`](desktop/20-activity-logs.png) | Human-readable audit history with workspace and actor context. |
| [`21-settings.png`](desktop/21-settings.png) | Workspace and application configuration surfaces. |
| [`22-billing.png`](desktop/22-billing.png) | GymFlow subscription state and provider-dependent billing controls. |

## Client portal

| File | What it shows |
|---|---|
| [`00-access.png`](portal/00-access.png) | Neutral client portal access request and one-time confirmation flow. |
| [`01-portal-home.png`](portal/01-portal-home.png) | Client-scoped overview with next actions, membership, and upcoming activity. |
| [`02-bookings.png`](portal/02-bookings.png) | Self-service scheduling and upcoming sessions. |
| [`03-membership.png`](portal/03-membership.png) | Client-visible membership status, benefits, dates, and history. |
| [`04-payments.png`](portal/04-payments.png) | Client-safe payment history and outstanding-state presentation. |
| [`05-receipt.png`](portal/05-receipt.png) | Receipt view without provider secrets or internal identifiers. |
| [`06-progress.png`](portal/06-progress.png) | Client progress and historical activity presentation. |
| [`07-check-in-pass.png`](portal/07-check-in-pass.png) | Client check-in pass using a deliberately invalid demo credential. |
| [`08-messages.png`](portal/08-messages.png) | Client-visible support conversation separated from staff-only notes. |
| [`09-profile-settings.png`](portal/09-profile-settings.png) | Portal profile, preferences, and client-scoped settings. |

## Mobile

| File | What it shows |
|---|---|
| [`01-portal-home.png`](mobile/01-portal-home.png) | Mobile-first portal dashboard and navigation. |
| [`02-portal-bookings.png`](mobile/02-portal-bookings.png) | Mobile booking experience. |
| [`03-portal-payments.png`](mobile/03-portal-payments.png) | Mobile payment history and client-safe financial state. |
| [`04-check-in-pass.png`](mobile/04-check-in-pass.png) | Full-height mobile pass with a deliberately invalid static QR. |
| [`05-public-home.png`](mobile/05-public-home.png) | Responsive public product experience. |
| [`06-dashboard.png`](mobile/06-dashboard.png) | Compact staff dashboard with key metrics and workspace readiness. |
| [`07-client-detail.png`](mobile/07-client-detail.png) | Responsive client command center on a narrow viewport. |

## Localization

| File | What it shows |
|---|---|
| [`01-arabic-rtl.png`](localization/01-arabic-rtl.png) | Arabic staff application with right-to-left layout and navigation. |
| [`02-french-dashboard.png`](localization/02-french-dashboard.png) | French dashboard with expanded localized copy. |
| [`03-arabic-portal-mobile.png`](localization/03-arabic-portal-mobile.png) | Arabic RTL portal on a mobile viewport. |
| [`04-arabic-portal-desktop.png`](localization/04-arabic-portal-desktop.png) | Arabic RTL portal on a desktop viewport. |

## Engineering views

| File | What it shows |
|---|---|
| [`07-frontend-project-structure.png`](engineering/07-frontend-project-structure.png) | Curated view of the feature-oriented Flutter repository structure. |
| [`08-backend-project-structure.png`](engineering/08-backend-project-structure.png) | Curated view of the FastAPI application and supporting backend structure. |
| [`09-postgresql-schema.png`](engineering/09-postgresql-schema.png) | Relational schema for connected business entities. |
| [`10-openapi.png`](engineering/10-openapi.png) | Versioned API surface and typed endpoint documentation. |
| [`11-docker-runtime.png`](engineering/11-docker-runtime.png) | Local backend, PostgreSQL, and Redis runtime. |
| [`12-demo-clients-data.png`](engineering/12-demo-clients-data.png) | Deterministic client and membership scenario summary. |
| [`13-demo-messages-data.png`](engineering/13-demo-messages-data.png) | Deterministic professional messaging scenario summary. |
| [`14-demo-payments-data.png`](engineering/14-demo-payments-data.png) | Deterministic payment-state and reporting summary. |
| [`15-frontend-commit-history.png`](engineering/15-frontend-commit-history.png) | Curated source-history view ending at the canonical frontend revision. |
| [`16-backend-commit-history.png`](engineering/16-backend-commit-history.png) | Curated source-history view for the canonical backend revision. |

## Capture and privacy standard

The gallery is prepared with fictional data and privacy-safe presentation. Public captures exclude credentials, valid access codes, real personal or payment information, local machine details, developer overlays, and unrelated notifications.

QR images used for portfolio presentation encode deliberately invalid static payloads rather than usable credentials.

The deterministic demo validator defines exact post-seed counts and relationships. Screenshots show representative application states, so date-relative records, presence, temporary notifications, and actions taken during review can naturally vary from the initial seed moment.

## Release integrity

The latest tagged gallery release is `v1.0.3-showcase`, representing:

- frontend `b73a623c3985e4bc458d04b4b484887ada593fa5`;
- backend `2234af20d1d9dd143bcac22edc699d3ee7fe515f`.

The release tooling keeps the gallery reproducible through a declared file inventory, dimensions and format checks, unique content hashes, exact SHA-256 records, source-revision checks, and manual privacy/localization review.

Full release mechanics are documented in [Release Integrity](../RELEASES.md) and [`release/evidence-manifest.json`](../release/evidence-manifest.json).
