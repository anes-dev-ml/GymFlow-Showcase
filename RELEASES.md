# GymFlow Release Integrity

GymFlow showcase releases connect public claims and visual evidence to exact
frontend, backend, schema, and demo-state revisions.

The objective is simple: a reviewer should be able to understand what the
release contains, which application snapshot it represents, which validations
were completed, and which provider or production claims remain environment
specific.

## Current release

`v1.0.0-showcase` is a screenshot-bearing engineering case study.

It includes:

- the public product and engineering documentation;
- the exact source manifest;
- 53 screenshots across desktop, client portal, mobile, localization, and
  engineering galleries;
- deterministic demo metrics and data boundaries;
- release validation evidence.

It does not include a public walkthrough video, video thumbnail, Android
package, Windows archive, or other installable binary.

## Versioning

Showcase releases use semantic identifiers such as:

```text
v1.0.0-showcase
v1.0.1-showcase
v1.1.0-showcase
```

- **major** identifies an important architecture or product generation;
- **minor** identifies a substantial product capability or refreshed visual
  release;
- **patch** identifies documentation, packaging, provenance, or other
  non-breaking corrections.

Public evidence is immutable by convention. A material source or artifact
change belongs to a new semantic release rather than a silent replacement.

## Canonical source record

Every showcase release records:

- the showcase branch and release identifier;
- the frontend branch and commit;
- the backend branch and commit;
- the Alembic head revision;
- the demo evidence date and deterministic targets;
- relevant runtime and dependency versions;
- included and omitted artifacts;
- validation evidence and known limitations.

The authoritative record for `v1.0.0-showcase` is the
[Build Manifest](BUILD_MANIFEST.md).

## Validation evidence

Green hosted CI is the preferred release evidence. For this release, GitHub
hosted jobs were blocked before checkout by an account-level spending policy.
Equivalent frontend, backend, and showcase validation was completed locally,
and the limitation is recorded without claiming that hosted checks passed.

The exception applies only to a runner that never reaches repository checkout or
code execution. A source, test, dependency, or configuration failure inside an
executing job remains a real quality failure.

## Screenshot evidence

The current gallery contains:

| Gallery | Count |
|---|---:|
| Desktop | 22 |
| Client portal | 10 |
| Mobile | 7 |
| Localization | 4 |
| Engineering | 10 |
| **Total** | **53** |

The images use fictional deterministic data and test or demo payment state. The
gallery is tied to the canonical source snapshot and is validated for approved
directories, file types, and exact counts.

The complete visual evidence is documented in the
[GymFlow Visual Gallery](screenshots/README.md).

## Video and installable artifacts

No video or installable binary is part of `v1.0.0-showcase`.

A later release containing a public video, APK, Windows package, or downloadable
archive would identify the exact source revision, platform and backend
requirements, relevant provider behavior, and integrity metadata such as
SHA-256 checksums. Video evidence would additionally record duration and captions
status.

The intended walkthrough scope is described in
[GymFlow Walkthrough Status](video/README.md).

## Data and payment boundary

The public showcase uses:

- fictional identities and business records;
- reserved `.test` addresses;
- Stripe test mode or explicitly simulated demo state;
- no stored payment-card data;
- no real charges;
- no published permanent demo password.

## Provider and production boundary

GymFlow implements production-oriented architecture and strict production
configuration. A live commercial deployment still depends on target hosting,
domains, managed PostgreSQL and Redis, provider credentials, webhook rehearsal,
verified email, OAuth redirects, monitoring, alerts, backups, restore testing,
security operations, and legal ownership.

The showcase does not collapse those deployment responsibilities into an
unsupported claim that the product is already production-operated.

## Correction policy

Broken links, leaked information, misleading claims, or incorrect artifacts are
treated as release defects. Active exposure is removed or corrected promptly,
credentials are revoked when relevant, the correction is documented, and a new
patch release is used when the public evidence set changes materially.
