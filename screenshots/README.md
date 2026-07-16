# GymFlow Screenshot Release Procedure

## Current inventory

The `v1.0.0-showcase` engineering case-study release includes no current
application screenshots. The former 19-image root gallery was removed because it
represented an older product generation and could not be tied to the audited
source snapshot.

The tables below define approved filenames and capture requirements for a later
media-bearing release. A partial set is acceptable only when the build manifest
lists exactly what is included. No image may be described as current without
source provenance and privacy review.

## Canonical capture state

Before capture:

1. use the frontend and backend revisions in `../BUILD_MANIFEST.md`;
2. select the `gymflow_demo` database;
3. rebuild and validate Northline Performance Club;
4. complete one uninterrupted route rehearsal;
5. confirm there are no repeated serious API or browser errors;
6. create a new release version rather than silently changing the existing tag.

## Privacy and quality rules

Every image must:

- contain only fictional seeded identities;
- exclude credentials, access codes, environment values, local file paths, and private browser data;
- avoid error banners, loading hangs, overflow markers, debug overlays, and unfinished dialogs;
- use test or demo payment state only;
- use a clear, consistent browser frame and viewport;
- be reviewed at full resolution before publication.

Prefer PNG, lowercase kebab-case names, and 1440×900 or 1600×900 desktop
captures. Use 100% browser zoom unless demonstrating responsive behavior.

## Root README set

Capture these first for a later media release:

| File | Route | Story |
|---|---|---|
| `desktop/01-public-home.png` | `/` | Product positioning |
| `desktop/02-owner-dashboard.png` | `/dashboard` | Populated KPIs and activity |
| `desktop/03-client-command-center.png` | `/clients/:id` | Connected client lifecycle |
| `desktop/04-staff-presence.png` | `/staff` | Roles and presence states |
| `desktop/05-bookings.png` | `/bookings` | Scheduling and lifecycle states |
| `desktop/06-reports.png` | `/reports` | Non-flat business charts |
| `desktop/07-professional-messaging.png` | `/messages` | Assignment and conversation workflow |
| `portal/01-portal-home.png` | `/portal` | Client-safe dashboard |
| `mobile/01-portal-home.png` | Mobile `/portal` | Mobile member experience |
| `localization/01-arabic-rtl.png` | Arabic public or portal page | RTL quality |

## Complete desktop gallery

| File | Route |
|---|---|
| `desktop/01-public-home.png` | `/` |
| `desktop/08-public-features.png` | `/features` |
| `desktop/09-public-pricing.png` | `/pricing` |
| `desktop/10-public-security.png` | `/security` |
| `desktop/11-auth.png` | `/auth` |
| `desktop/02-owner-dashboard.png` | `/dashboard` |
| `desktop/12-clients.png` | `/clients` |
| `desktop/03-client-command-center.png` | `/clients/:id` |
| `desktop/13-plans.png` | `/membership-plans` |
| `desktop/14-services.png` | `/service-types` |
| `desktop/04-staff-presence.png` | `/staff` |
| `desktop/15-trainer-availability.png` | `/staff/availability` |
| `desktop/16-invitations.png` | `/invitations` |
| `desktop/05-bookings.png` | `/bookings` |
| `desktop/17-check-ins.png` | `/check-ins` |
| `desktop/18-payments.png` | `/payments` |
| `desktop/06-reports.png` | `/reports` |
| `desktop/07-professional-messaging.png` | `/messages` |
| `desktop/19-notifications.png` | `/notifications` |
| `desktop/20-activity-logs.png` | `/activity-logs` |
| `desktop/21-settings.png` | `/settings` |
| `desktop/22-billing.png` | `/settings/billing` |

## Client portal gallery

| File | Route |
|---|---|
| `portal/00-access.png` | `/portal/access` |
| `portal/01-portal-home.png` | `/portal` |
| `portal/02-bookings.png` | `/portal/bookings` |
| `portal/03-membership.png` | `/portal/membership` |
| `portal/04-payments.png` | `/portal/payments` |
| `portal/05-receipt.png` | `/portal/payments/:receiptId` |
| `portal/06-progress.png` | `/portal/progress` |
| `portal/07-check-in-pass.png` | `/portal/check-in-pass` |
| `portal/08-messages.png` | `/portal/messages` |
| `portal/09-profile-settings.png` | `/portal/profile` |
| `portal/10-amina-risk-story.png` | Relevant Amina page |

Use Lena Martin for the healthy-member story and Amina Haddad for the
expiring-membership and payment-risk story.

## Mobile gallery

Capture at one consistent mobile resolution such as 390×844.

| File | Route |
|---|---|
| `mobile/01-portal-home.png` | `/portal` |
| `mobile/02-portal-bookings.png` | `/portal/bookings` |
| `mobile/03-portal-payments.png` | `/portal/payments` |
| `mobile/04-check-in-pass.png` | `/portal/check-in-pass` |
| `mobile/05-public-home.png` | `/` |
| `mobile/06-dashboard.png` | `/dashboard` |
| `mobile/07-client-detail.png` | `/clients/:id` |

## Localization gallery

| File | Surface |
|---|---|
| `localization/01-arabic-rtl.png` | Arabic public or portal page |
| `localization/02-french-dashboard.png` | French dashboard with long labels |
| `localization/03-arabic-portal-mobile.png` | Arabic mobile portal |

## Engineering evidence

| File | Evidence |
|---|---|
| `engineering/01-backend-validation.png` | Backend release-validation summary |
| `engineering/02-frontend-validation.png` | Frontend release-validation summary |
| `engineering/03-demo-validation.png` | Deterministic validation output |
| `engineering/04-docker-selector.png` | Demo environment selector |
| `engineering/05-readiness.png` | Safe readiness response |
| `engineering/06-architecture.png` | Rendered architecture overview |

Do not label a validation screenshot as hosted CI unless it came from an
executed hosted run. Local evidence must be described as local validation.

## Capture order

1. Rebuild and validate the demo data.
2. Capture public pages while signed out.
3. Capture authentication.
4. Capture the staff application with the owner session.
5. Capture Lena portal pages with a fresh session.
6. Capture the Amina risk story if used.
7. Capture mobile and localized states.
8. Capture engineering evidence.
9. Review every image for privacy, consistency, and release accuracy.

After capture, update the README gallery, record the exact inventory and source
revisions in `../BUILD_MANIFEST.md`, add checksums for any downloadable pack,
run the showcase validator, and create a new semantic release tag.