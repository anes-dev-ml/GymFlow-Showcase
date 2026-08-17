# GymFlow Showcase Releases

GymFlow showcase releases connect each public case-study snapshot to exact frontend, backend, schema, demo-state, and gallery records. The goal is simple: make every tagged showcase easy to identify and reproduce without turning release mechanics into the product story itself.

## Current release

The current release record is **`v1.0.4-showcase`**. It represents:

- frontend `b73a623c3985e4bc458d04b4b484887ada593fa5`;
- backend `2234af20d1d9dd143bcac22edc699d3ee7fe515f`;
- Alembic head `9e4f6a8c2d1b`;
- the reviewed 53-image gallery;
- the deterministic Northline Performance Club demo state.

The previous immutable release is `v1.0.3-showcase` at `7262227bdc925f236f2c1c4257c8630513931b64`.

`v1.0.4-showcase` is a documentation and presentation patch. It keeps the application and gallery snapshot unchanged while refining the public narrative, source-access wording, roadmap, gallery presentation, and supporting technical documentation.

## Versioning

Showcase releases use semantic identifiers:

```text
v1.0.0-showcase
v1.0.1-showcase
v1.0.2-showcase
v1.0.3-showcase
v1.0.4-showcase
v1.1.0-showcase
```

- **major** identifies an important architecture or product generation;
- **minor** identifies a substantial product capability or refreshed visual release;
- **patch** identifies documentation, packaging, provenance, privacy, validation, or other non-breaking corrections.

Tagged releases are immutable by convention. Material changes receive a new semantic release instead of moving an existing tag.

## Canonical release record

Each release can record:

- showcase release identifiers;
- frontend repository, ref, and commit;
- backend repository, ref, and commit;
- Alembic head;
- release/demo date and deterministic targets;
- runtime and dependency versions;
- included artifacts;
- validation mode and commands;
- screenshot inventory and SHA-256 records;
- provider and deployment context.

The human-readable source record is the [Build Manifest](BUILD_MANIFEST.md). The machine-readable record is [`release/evidence-manifest.json`](release/evidence-manifest.json).

## Local release gate

This showcase release line uses a local validation gate:

```powershell
.\scripts\validate_release.ps1
.\scripts\validate_release.ps1 -Release
```

```bash
bash scripts/validate_release.sh
bash scripts/validate_release.sh --release
```

The gate covers validator regression tests, tracked-file safety, Markdown links, gallery inventory and hashes, source provenance, release identifiers, and optional tag/clean-worktree verification.

GitHub Actions are not part of this release line; the local gate is the release mechanism recorded by the showcase.

## Gallery integrity

| Gallery | Count |
|---|---:|
| Desktop | 22 |
| Client portal | 10 |
| Mobile | 7 |
| Localization | 4 |
| Engineering | 10 |
| **Total** | **53** |

The release record preserves the declared gallery paths and exact content hashes so a tagged visual snapshot remains tied to the application revisions it represents.

Browse the gallery in [GymFlow Visual Gallery](screenshots/README.md).

## Demo data and payments

The public showcase uses fictional identities and business records, reserved `.test` or IANA example-domain addresses, and manual/simulated/Stripe test-mode payment states. Reusable credentials and live payment information are kept outside the public presentation.

This keeps product review realistic while preserving a clear separation between demonstration data and any real deployment environment.

## Deployment context

GymFlow's application architecture includes production-oriented configuration and provider boundaries. Operating it commercially would connect those boundaries to selected hosting, domains, managed PostgreSQL/Redis, Stripe, verified email, OAuth, monitoring, backups, restore procedures, and the legal/support processes of the deployment.

The [Roadmap](ROADMAP.md) describes that path separately from the tagged product showcase.

## Release media

`v1.0.4-showcase` is centered on documentation, diagrams, and the reviewed screenshot gallery. A future release can add an edited walkthrough or installable review artifact when it adds value, with its own versioned record.

## Correction policy

If a public release contains a broken link, exposed information, incorrect source revision, misleading artifact, stale capture, validator defect, or tag inconsistency, the active presentation is corrected and a new patch release is used when the change affects the tagged record.

Existing release tags remain immutable.
