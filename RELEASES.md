# GymFlow Releases

This document explains how GymFlow demo releases are presented.

GymFlow is a full-stack SaaS project with a Flutter frontend, FastAPI backend, PostgreSQL database, provider integrations, and multiple demo surfaces.

Because the frontend depends on the backend API, installable builds such as Android APK or Windows desktop builds are only fully functional when connected to a running backend environment.

---

## Release Strategy

The showcase release is designed to prove the product and engineering work without exposing the private source repositories.

| Release Asset | Purpose |
|---|---|
| Screenshots | Show the product visually |
| Demo video | Walk through the full product experience |
| Architecture docs | Explain the technical system |
| Security docs | Explain auth, roles, workspace isolation, and demo safety |
| APK build | Optional Android installable demo |
| Windows build | Optional desktop installable demo |
| Web demo | Optional hosted demo during review periods |
| Local demo notes | Explain how the app can run locally when backend access is available |

---

## Important Demo Boundary

GymFlow is not a static frontend-only app.

The complete product depends on:

| Component | Required For |
|---|---|
| Flutter frontend | User interface |
| FastAPI backend | Authentication, business logic, API routes |
| PostgreSQL database | Persistent app data |
| Stripe Test Mode | Payment demonstration |
| Email provider | Verification, reset, invitation, and portal email flows |
| Google OAuth | Optional provider login |
| Demo seed data | Realistic product walkthrough |

Without a running backend and database, the APK and Windows builds can open only the frontend shell or fail when calling API-backed features.

---

## Recommended Showcase Release

The recommended public showcase release includes:

| Item | Status |
|---|---|
| Product README | Included |
| Demo guide | Included |
| Architecture overview | Included |
| Security overview | Included |
| Screenshots | To be added |
| Demo video | To be recorded |
| APK build notes | To be added |
| Windows build notes | To be added |
| Optional hosted demo | Available on request |

This is the safest and cleanest release style because it demonstrates the product without requiring permanent hosting or public source code.

---

## Web Demo

A hosted web demo requires:

| Requirement | Description |
|---|---|
| Hosted frontend | Flutter web build deployed to a public URL |
| Hosted backend | FastAPI API deployed to a public URL |
| Hosted database | PostgreSQL instance available to the backend |
| Environment variables | API URLs, secrets, provider keys, CORS, trusted hosts |
| HTTPS | Required for serious public demo use |
| Demo data | Seeded users, clients, memberships, bookings, and payments |
| Stripe Test Mode | Safe payment testing |
| Optional email provider | For email verification, reset, portal access, and invitations |

Recommended position:

A hosted demo can be enabled temporarily during review periods instead of running permanently.

---

## Android APK Demo

The Android APK is useful to show that GymFlow can run as a mobile application.

| Item | Explanation |
|---|---|
| Build type | Android APK |
| Main purpose | Installable mobile demo |
| Requires backend | Yes, for full functionality |
| API configuration | Must point to a reachable backend URL |
| Google sign-in | Requires Android OAuth configuration if enabled |
| Payments | Stripe test checkout requires a reachable backend |
| Offline mode | Not intended as the main demo mode |

Recommended position:

Use the APK as a proof that the Flutter app can run on Android, while the video/screenshots remain the main showcase evidence.

---

## Windows Desktop Demo

The Windows build is useful to show that GymFlow can run as a desktop application.

| Item | Explanation |
|---|---|
| Build type | Windows desktop build |
| Main purpose | Installable desktop demo |
| Requires backend | Yes, for full functionality |
| API configuration | Must point to a reachable backend URL |
| Payments | Stripe test flows require backend and browser redirect support |
| Offline mode | Not intended as the main demo mode |

Recommended position:

Use the Windows build as an optional downloadable artifact, not as the primary way someone evaluates the project.

---

## Local Demo

A local demo requires the full stack.

| Component | Local Requirement |
|---|---|
| Backend | FastAPI running locally |
| Database | PostgreSQL running locally |
| Migrations | Alembic migrations applied |
| Frontend | Flutter web/app running with correct API base URL |
| Demo data | Seeded or manually prepared |
| Stripe | Test mode keys configured if payment flows are shown |
| Email | Test provider or disabled email behavior |
| OAuth | Local OAuth redirects configured if shown |

A local demo is useful for a technical walkthrough, but it requires more setup than screenshots or video.

---

## Demo Data

The showcase should use fictional demo data only.

Good demo data should include:

| Data Type | Examples |
|---|---|
| Studio workspace | A realistic gym/studio name |
| Owner account | Demo owner credentials |
| Staff accounts | Manager, trainer, receptionist examples |
| Clients | Several realistic fictional clients |
| Membership plans | Monthly, premium, student, or class-pass examples |
| Client memberships | Active, expiring, inactive examples |
| Services | Personal training, group class, open gym |
| Bookings | Upcoming and past bookings |
| Check-ins | Attendance records |
| Payments | Pending and paid test records |
| Reports | Enough data to make reports look useful |
| Notifications | Read and unread examples |
| Activity logs | Realistic operational history |

Good seed data makes the screenshots and video look like a real SaaS product instead of an empty admin panel.

---

## Stripe Test Mode

The showcase uses Stripe Test Mode.

| Field | Value |
|---|---|
| Test card | 4242 4242 4242 4242 |
| Expiry date | Any future date |
| CVC | Any 3 digits |
| Postal code | Any valid postal code |

No real money is processed.

Stripe Connect is demonstrated through demo mode so reviewers are not asked to upload identity documents.

---

## Email Demo Behavior

Email flows may be configured in one of three ways.

| Mode | Description |
|---|---|
| Disabled | Email actions show safe UI behavior but no real delivery |
| Test provider | Emails route through a test/sandbox provider |
| Verified domain | Emails are sent through a verified sender domain |

The showcase should be honest about which email mode is active for a given demo release.

---

## OAuth Demo Behavior

Google OAuth may be demonstrated when configured correctly.

OAuth demo requirements include:

| Requirement | Description |
|---|---|
| Web OAuth client | Required for browser Google login |
| Android OAuth client | Required for native Android sign-in |
| Correct redirect URLs | Backend and frontend callback URLs must match provider settings |
| HTTPS in production | Required for serious hosted demo use |

If OAuth is not configured for a specific demo release, the email/password demo account should be used instead.

---

## Version Naming

Recommended release names:

| Version | Meaning |
|---|---|
| v1.0-showcase | First complete public showcase package |
| v1.0-demo-video | Release focused on screenshots and video |
| v1.0-apk-preview | Android build preview |
| v1.0-windows-preview | Windows build preview |
| v1.0-hosted-review | Temporary hosted review version |

---

## What To Include In A GitHub Release

A strong GitHub release should include:

| Asset | Description |
|---|---|
| Demo video link | Main walkthrough |
| Screenshots | Visual proof of product scope |
| APK file | Optional Android build |
| Windows ZIP | Optional desktop build |
| Release notes | What works, what is demo-scoped |
| Demo limitations | Honest boundaries |
| Contact/access note | How to request live access |

---

## Release Notes Template

Use this structure for the final GitHub release:

| Section | Content |
|---|---|
| Summary | GymFlow full-stack SaaS showcase release |
| Included | Screenshots, video, docs, optional builds |
| Demo scope | Public site, dashboard, client portal, payments, localization |
| Payment note | Stripe Test Mode only |
| Source note | Source repositories are private |
| Hosting note | Live demo access available on request |
| Known limitations | Emails/OAuth/hosting depending on release mode |

---

## Known Limitations

| Limitation | Explanation |
|---|---|
| Source repositories are private | The project is a complete product-style app |
| APK needs backend | Mobile build requires reachable API for full functionality |
| Windows build needs backend | Desktop build requires reachable API for full functionality |
| Web demo needs hosting | Web demo requires frontend, backend, and database hosting |
| Stripe is test/demo only | No real money is processed |
| Stripe Connect is simulated | No identity verification in demo |
| Email may be limited | Depends on provider/domain configuration |
| OAuth may be limited | Depends on provider configuration |
| Production is not claimed by default | Full production launch needs hosting, monitoring, backups, and provider verification |

---

## Final Recommendation

The strongest release path is:

1. Keep the frontend and backend source repositories private.
2. Publish the showcase repository after final polish.
3. Add 10 to 15 high-quality screenshots.
4. Add a 3 to 5 minute demo video.
5. Add optional APK and Windows builds.
6. Offer temporary hosted demo access on request.

This approach proves the product exists, works, and demonstrates deep engineering skill without creating the extra burden of maintaining public production-grade source repositories.
