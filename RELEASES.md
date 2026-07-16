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
- improved image-integrity and provenance validation;
- explicit provider, hosted-runner, historical-media, and production-operation boundaries.

The tag is intentionally not created until the exact candidate commit passes the
final media review, frontend validation, and both showcase validators.

## Historical releases and media

`v1.0.0-showcase` records the earlier screenshot-bearing baseline. The current
`main` branch contains later documentation, validator, source-provenance, and
gallery corrections. The historical tag must not be described as containing
those later changes and must not be moved.

A separate older GitHub release associated with a non-showcase `v1.0.0` tag may
contain a walkthrough asset. That asset predates the current canonical frontend
snapshot and is historical media, not evidence for `v1.0.1-showcase`. It should
be archived or removed rather than presented as the final current walkthrough.

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
before checkout by an account-level spending policy, so the repository does not
claim green hosted CI.

Equivalent backend validation completed locally on the canonical backend
revision. Earlier frontend validation also completed locally, but the final
frontend release-quality commands must be rerun on
`8242f24fb05f0918393e439b5e0f1cc2e5f3086d` before the candidate tag is created.
The base showcase validator and the provenance-bound final candidate validator
must then pass on the exact commit selected for the tag.

The hosted-runner exception applies only when a runner never reaches checkout or
code execution. A source, test, dependency, or configuration failure inside an
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
Images use fictional data and test or simulated payment state. The validators
check the exact inventory, supported formats, minimum dimensions, duplicate
content, known rejected media hashes, approved high-risk assets, and canonical
source provenance.

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

No walkthrough video or installable binary is part of the current
`v1.0.1-showcase` evidence contract. A later release containing a current video,
APK, Windows archive, or downloadable artifact would record the exact source
revision, platform requirements, integrity hashes, and provider behavior. Video
evidence would also record duration and captions status.

## Correction policy

Broken links, leaked information, misleading claims, duplicate or mislabeled
artifacts, stale application captures, and release-tag inconsistencies are
release defects. Active exposure is removed promptly, credentials are revoked
when relevant, corrections are documented, and a new patch release is used for
material evidence changes.
