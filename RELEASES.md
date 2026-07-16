# GymFlow Releases

This document defines how GymFlow showcase and review releases are versioned,
verified, and distributed.

## Release goals

A GymFlow release should prove that:

- the documented product corresponds to exact frontend and backend source revisions;
- included screenshots, video, or binaries represent that same snapshot;
- demo data is fictional and repeatable;
- provider and production boundaries are stated honestly;
- no source code, credentials, or real client or payment data are exposed;
- validation evidence is recorded without claiming checks that did not run.

## Current release

The `v1.0.0-showcase` tag includes a provenance-backed screenshot gallery.
It contains 53 tracked screenshots across desktop, portal, mobile,
localization, and engineering galleries. It does not include a public video,
thumbnail, Android package, Windows archive, or other installable binary.

## Release types

| Release | Purpose | Typical assets |
|---|---|---|
| Screenshot-bearing engineering showcase | Main portfolio case study | Documentation, manifest, changelog, current screenshot gallery |
| Media-bearing showcase | Extended visual portfolio package | Documentation, screenshots, edited product video |
| Technical walkthrough | Deeper engineering review | Architecture video, diagrams, manifest |
| Android preview | Installable mobile evaluation | APK, checksum, backend requirement note |
| Windows preview | Desktop evaluation | ZIP or MSIX, checksum, backend note |
| Hosted review | Temporary interactive review | Time-limited URL and privately shared credentials |

## Versioning

Recommended naming:

```text
v1.0.0-showcase
v1.0.1-showcase
v1.1.0-showcase
```

Use semantic meaning:

- **major**: important architecture or product generation;
- **minor**: significant new product capability or refreshed media release;
- **patch**: documentation, release packaging, or non-breaking corrections.

Do not silently replace public release assets. Create a new semantic tag when
source revisions or the public artifact set materially changes.

## Canonical source snapshot

Every public release must identify:

- showcase branch and tag or commit;
- frontend branch and commit;
- backend branch and commit;
- Alembic head revision;
- demo seed contract date or version;
- relevant runtime and dependency versions;
- validation date and evidence;
- exact included and omitted artifacts;
- known limitations and provider boundaries.

The source snapshot is recorded in [BUILD_MANIFEST.md](BUILD_MANIFEST.md).

## Validation evidence rule

The preferred evidence is green GitHub Actions on the canonical commits. When a
hosted runner cannot start because of a documented account-level or platform
restriction, a release may use equivalent local validation only when all of the
following are true:

1. the failure occurs before repository checkout or code execution;
2. the reason is recorded in the build manifest;
3. the equivalent release commands are completed locally;
4. the release does not claim green hosted CI;
5. the source commits and local validation scope are recorded exactly.

A code failure, test failure, configuration failure inside a running job, or
missing local dependency is not an acceptable reason to bypass a quality gate.

## Required release artifacts

### Always include

- product README;
- architecture, engineering, security, quality, operations, and demo documentation;
- release manifest;
- changelog or release notes;
- known limitations and provider boundary;
- explicit artifact inventory;
- validation evidence or an honest validation limitation.

### Screenshot-bearing release

A release containing screenshots must:

- use only fictional deterministic demo data;
- tie every image to the canonical source snapshot;
- organize images under approved gallery directories;
- contain no credential, access code, local path, unrelated browser data, or real identity;
- avoid error banners, debug overlays, layout overflow, loading hangs, and unfinished dialogs;
- record the exact gallery counts in the manifest and screenshot inventory;
- pass the showcase inventory validator before tagging.

For `v1.0.0-showcase`, the approved counts are:

| Gallery | Count |
|---|---:|
| Desktop | 22 |
| Client portal | 10 |
| Mobile | 7 |
| Localization | 4 |
| Engineering evidence | 10 |
| **Total** | **53** |

### Video and binaries

A future release containing video or installable artifacts must additionally
record:

- public URL or attached release asset;
- duration and captions status for video;
- exact source revision;
- SHA-256 checksum;
- platform and backend requirements;
- OAuth and payment redirect status;
- explicit demo-only or production status.

## Provider and production boundary

GymFlow implements production-oriented architecture and strict production
configuration. A live commercial deployment additionally requires target
hosting, domains, managed PostgreSQL and Redis, provider credentials, webhook
rehearsal, verified email, OAuth redirects, monitoring, alerts, backups, restore
testing, and legal/operational ownership.

Release notes must not collapse those states into one unsupported
“production-operated” claim.

## Public data and payment boundary

The showcase uses:

- fictional identities and business records;
- Stripe test mode or explicitly simulated demo state;
- no stored payment-card data;
- no real charges;
- no published permanent demo password.

## Publication sequence

1. Freeze canonical frontend and backend commits.
2. Rebuild and validate `gymflow_demo` when product media changes.
3. Complete the route rehearsal.
4. Capture and privacy-review screenshots.
5. Update `BUILD_MANIFEST.md` and `screenshots/README.md`.
6. Run frontend, backend, and showcase release validation.
7. Review every public claim and asset.
8. Create the Git tag and GitHub release.
9. Verify the repository from a logged-out or public-review perspective.

## Correction rule

If a release contains a broken link, leaked information, misleading claim, or
incorrect asset:

1. remove or replace the affected material immediately;
2. revoke any exposed credential;
3. record the correction in `CHANGELOG.md`;
4. create a patch release when the public artifact set changes;
5. do not leave a compromised or misleading artifact available.
