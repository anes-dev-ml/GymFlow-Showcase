# GymFlow Release Integrity

GymFlow showcase releases connect public claims and visual evidence to exact frontend, backend, schema, demo-state, and artifact records.

A reviewer should be able to determine what a release contains, which application snapshot it represents, which validations executed, and which provider or production responsibilities remain environment-specific.

## Current release record

The current release identifier is `v1.0.3-showcase`. The previous immutable release is `v1.0.2-showcase`, which points to:

`4e6f10276a5d17a51f7ddad12d9f909fd6f0fd7f`

The current record preserves the canonical application revisions:

- frontend `b73a623c3985e4bc458d04b4b484887ada593fa5`;
- backend `2234af20d1d9dd143bcac22edc699d3ee7fe515f`;
- Alembic head `9e4f6a8c2d1b`.

`v1.0.3-showcase` corrects the final release-model ambiguity by:

- replacing the dynamic “latest immutable release” field with explicit current and previous release identities;
- using neutral validator output that remains accurate before and after tagging;
- recording exact SHA-256 approval for all 53 screenshots;
- validating malformed manifest structures without tracebacks;
- expanding validator regression coverage;
- removing obsolete candidate-named release tooling.

## Versioning

Showcase releases use semantic identifiers:

```text
v1.0.0-showcase
v1.0.1-showcase
v1.0.2-showcase
v1.0.3-showcase
v1.1.0-showcase
```

- **major** identifies an important architecture or product generation;
- **minor** identifies a substantial product capability or refreshed visual release;
- **patch** identifies documentation, packaging, provenance, privacy, validation, or other non-breaking corrections.

Public evidence is immutable by convention. Material changes belong to a new semantic release rather than a silent tag replacement.

## Canonical source record

Every release records:

- current and previous showcase release identifiers;
- frontend repository, ref, and commit;
- backend repository, ref, and commit;
- Alembic head;
- evidence date and deterministic targets;
- runtime and dependency versions;
- included and omitted artifacts;
- validation mode and executed commands;
- exact screenshot inventory and SHA-256 approvals;
- known provider and production limitations.

The authoritative human-readable record is the [Build Manifest](BUILD_MANIFEST.md). The authoritative machine-readable record is [`release/evidence-manifest.json`](release/evidence-manifest.json).

## Local validation policy

This showcase release line uses traditional local validation rather than GitHub Actions.

```powershell
.\scripts\validate_release.ps1
.\scripts\validate_release.ps1 -Release
```

```bash
bash scripts/validate_release.sh
bash scripts/validate_release.sh --release
```

The local gate runs:

- validator unit tests;
- required-file and tracked-file safety checks;
- local Markdown link validation and repository-root containment;
- public wording and stale-release checks;
- screenshot inventory, format, dimension, orientation, uniqueness, and exact hash checks;
- permanently blocked rejected-media checks;
- canonical source-provenance checks;
- previous-tag immutability verification;
- optional current-tag and clean-worktree verification.

No successful hosted execution is claimed. Local evidence is recorded explicitly and **no green hosted-CI claim** is made.

## Screenshot evidence

| Gallery | Count |
|---|---:|
| Desktop | 22 |
| Client portal | 10 |
| Mobile | 7 |
| Localization | 4 |
| Engineering | 10 |
| **Total** | **53** |

A release requires all 53 declared paths, 53 unique content hashes, and 53 exact SHA-256 approvals. Known rejected-media hashes remain permanently blocked.

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

GymFlow implements production-oriented architecture and strict production configuration. A live commercial deployment still depends on target hosting, domains, managed PostgreSQL and Redis, provider credentials, webhook rehearsal, verified email, OAuth redirects, monitoring, alerts, backups, restore testing, security operations, and legal ownership.

The showcase does not collapse those responsibilities into an unsupported claim that the product is already production-operated.

## Video and installable artifacts

No current walkthrough video or installable binary is part of the `v1.0.3-showcase` evidence contract.

Historical media attached to an older non-showcase release is not evidence for the current source snapshot. A future media release would record exact source provenance, duration, captions status, integrity hashes, and platform requirements.

## Correction policy

Broken links, leaked information, misleading claims, duplicate or mislabeled artifacts, stale application captures, incorrect source revisions, validator defects, and release-tag inconsistencies are release defects.

Active exposure is removed promptly, credentials are revoked when relevant, corrections are documented, and a new patch release is used for material evidence changes. Existing release tags are never moved or silently rewritten.
