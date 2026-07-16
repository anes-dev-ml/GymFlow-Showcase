# GymFlow Release Integrity

GymFlow showcase releases connect public claims and visual evidence to exact
frontend, backend, schema, and demo-state revisions.

A reviewer should be able to determine what a release contains, which application
snapshot it represents, which validations executed, and which provider or
production responsibilities remain environment-specific.

## Current candidate

`main` is preparing `v1.0.1-showcase`, an evidence-hardening release for the
screenshot-bearing engineering case study.

The candidate includes:

- public product and engineering documentation;
- exact frontend and backend source revisions;
- 53 stable screenshot paths across five galleries;
- deterministic demo targets and data boundaries;
- improved image-integrity validation;
- explicit provider, hosted-runner, and production-operation boundaries.

The tag is intentionally not created until the exact candidate commit passes the
final media review and showcase validator.

## Historical release

`v1.0.0-showcase` records the earlier screenshot-bearing baseline. The current
`main` branch contains later documentation, validator, and gallery corrections.
The historical tag must not be described as containing those later changes.

## Versioning

Showcase releases use semantic identifiers:

```text
v1.0.0-showcase
v1.0.1-showcase
v1.1.0-showcase
```

- **major** identifies an important architecture or product generation;
- **minor** identifies a substantial product capability or refreshed visual release;
- **patch** identifies documentation, packaging, provenance, privacy, or other non-breaking corrections.

Public evidence is immutable by convention. Material source or artifact changes
belong to a new semantic release rather than a silent tag replacement.

## Canonical source record

Every release records:

- showcase release identifier and exact commit;
- frontend branch and commit;
- backend branch and commit;
- Alembic head revision;
- evidence date and deterministic targets;
- relevant runtime and dependency versions;
- included and omitted artifacts;
- validation evidence and known limitations.

The authoritative candidate record is the [Build Manifest](BUILD_MANIFEST.md).

## Validation evidence

Green hosted CI is preferred. Hosted jobs for this release line were blocked
before checkout by an account-level spending policy. Equivalent frontend,
backend, and showcase validation was completed locally, and the release does not claim green hosted CI.

The exception applies only when a runner never reaches checkout or code
execution. A source, test, dependency, or configuration failure inside an
executing job remains a real quality failure.

## Screenshot evidence

| Gallery | Count |
|---|---:|
| Desktop | 22 |
| Client portal | 10 |
| Mobile | 7 |
| Localization | 4 |
| Engineering | 10 |
| **Total** | **53** |

A final release requires all 53 paths and all 53 content hashes to be unique.
Images use fictional data and test or simulated payment state. The validator
checks the exact inventory, supported formats, minimum dimensions, duplicate
content, and known rejected media hashes.

The gallery is documented in the [GymFlow Visual Gallery](screenshots/README.md).

## Data and payment boundary

The showcase uses:

- fictional identities and business records;
- reserved `.test` or IANA example-domain addresses;
- Stripe test mode or explicitly simulated demo state;
- no stored payment-card data;
- no real charges;
- no published permanent demo password;
- no valid credential encoded in a public QR image.

## Provider and production boundary

GymFlow implements production-oriented architecture and strict production
configuration. A live commercial deployment still depends on target hosting,
domains, managed PostgreSQL and Redis, provider credentials, webhook rehearsal,
verified email, OAuth redirects, monitoring, alerts, backups, restore testing,
security operations, and legal ownership.

The showcase does not collapse those responsibilities into an unsupported claim
that the product is already production-operated.

## Video and installable artifacts

No public video or installable binary is part of the current candidate. A later
release containing a video, APK, Windows archive, or downloadable artifact would
record the exact source revision, platform requirements, integrity hashes, and
provider behavior. Video evidence would also record duration and captions status.

## Correction policy

Broken links, leaked information, misleading claims, duplicate or mislabeled
artifacts, and release-tag inconsistencies are release defects. Active exposure
is removed promptly, credentials are revoked when relevant, corrections are
documented, and a new patch release is used for material evidence changes.