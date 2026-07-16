# GymFlow Screenshot Inventory

## Current release inventory

The `v1.0.0-showcase` release includes **53 tracked screenshots** tied to the
canonical frontend and backend revisions in `../BUILD_MANIFEST.md`.

| Gallery | Directory | Count | Purpose |
|---|---|---:|---|
| Desktop | `desktop/` | 22 | Public site and staff application workflows |
| Client portal | `portal/` | 10 | Member access and self-service experience |
| Mobile | `mobile/` | 7 | Responsive staff, public, and portal surfaces |
| Localization | `localization/` | 4 | French and Arabic/RTL review |
| Engineering evidence | `engineering/` | 10 | Project structure, schema, API, Docker, demo data, and commit history |
| **Total** |  | **53** |  |

The inventory is enforced by `../scripts/check_showcase.py`. Adding, deleting,
or moving an image requires an intentional inventory and manifest update.

## Provenance

The gallery represents the application snapshot recorded in
`../BUILD_MANIFEST.md`:

- frontend `main` at `489a82e03059465755c74b1be39ae7c05f98fb9b`;
- backend `main` at `2234af20d1d9dd143bcac22edc699d3ee7fe515f`;
- fictional Northline Performance Club demo data only;
- manual/test/demo payment state only.

## Desktop gallery

The 22 desktop images cover:

- public home, features, pricing, and security;
- authentication;
- owner dashboard;
- clients and client detail;
- plans and services;
- staff presence, availability, and invitations;
- bookings and check-ins;
- payments and reports;
- professional messaging;
- notifications, activity logs, settings, and billing.

Representative entry: [`desktop/01-public-home.png`](desktop/01-public-home.png)

## Client portal gallery

The 10 portal images cover:

- access;
- portal home;
- bookings;
- membership;
- payments and receipt;
- progress;
- check-in pass;
- messages;
- profile settings.

Representative entry: [`portal/00-access.png`](portal/00-access.png)

## Mobile gallery

The 7 mobile images cover portal home, bookings, payments, check-in pass, the
public home page, the staff dashboard, and client detail.

Representative entry: [`mobile/01-portal-home.png`](mobile/01-portal-home.png)

## Localization gallery

The 4 localization images demonstrate Arabic RTL and French presentation on
public, dashboard, portal desktop, and portal mobile surfaces.

Representative entry: [`localization/01-arabic-rtl.png`](localization/01-arabic-rtl.png)

## Engineering evidence gallery

The 10 engineering images cover frontend and backend project structure,
PostgreSQL schema, OpenAPI, Docker runtime, deterministic client/message/payment
data, and frontend/backend commit history.

Representative entry:
[`engineering/07-frontend-project-structure.png`](engineering/07-frontend-project-structure.png)

## Privacy and quality rules

Every release image must:

- contain only fictional seeded identities;
- exclude credentials, access codes, environment values, local user paths, and private browser data;
- avoid error banners, loading hangs, overflow markers, debug overlays, and unfinished dialogs;
- use test/demo payment state only;
- be tied to the exact release source snapshot;
- use a clear and consistent viewport and filename.

## Replacement procedure

Before replacing or expanding the gallery:

1. use the source revisions recorded in `../BUILD_MANIFEST.md`;
2. select and rebuild `gymflow_demo`;
3. run `validate_demo_data.py`;
4. complete the full route rehearsal in `../DEMO.md`;
5. review browser and API logs for repeated serious errors;
6. capture only fictional demo state;
7. review every image for privacy, visual quality, and source accuracy;
8. update this inventory and the build manifest;
9. run `python scripts/check_showcase.py` from the repository root;
10. publish the change under a new semantic release when the public artifact set materially changes.
