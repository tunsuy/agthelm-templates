# Governance

## Roles

| Role | Responsibility |
|------|----------------|
| **Maintainer** | Review PRs, merge to `main`, cut tags, operate CI |
| **Contributor** | Propose templates / schema / docs via PR with DCO |
| **Release signer（agthelm 官方）** | Build and sign production tar packages; **not** automatic on merge |

See [MAINTAINERS.md](MAINTAINERS.md).

## Decision rules

1. **Source vs production** — Merging to this repo publishes **source** under Apache-2.0. It does **not** authorize production install. Only packages signed by agthelm official keys are supported in customer environments.
2. **Curated catalog** — Maintainers may request changes, reject out-of-scope PRs (see [CONTRIBUTING.md](CONTRIBUTING.md)), or defer templates that lack a clear industry × system-stack pin.
3. **Schema changes** — Additive fields preferred; breaking schema bumps require Issue discussion and CHANGELOG entry.
4. **No marketplace** — This project will not add user ratings, self-serve publishing, or bilateral store UX.

## Releases

- Git tags on this repo mark **source** revisions (e.g. schema or example bumps).
- Product **signed template** releases are versioned and distributed by the agthelm product pipeline, referencing curated commits/tags from this repo when applicable.
