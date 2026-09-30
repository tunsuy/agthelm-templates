# Security Policy

## Supported versions

| Component | Supported |
|-----------|-----------|
| `main` branch schemas & tools | Yes |
| Officially signed template packages (distributed by agthelm) | Yes — report packaging / supply-chain issues here or via the product channel listed by maintainers |
| Unsigned / third-party forks installed in production | Not supported |

## Reporting a vulnerability

Please **do not** open a public Issue for security problems.

1. Prefer GitHub **Private vulnerability reporting**:  
   [Security → Advisories → New draft advisory](https://github.com/tunsuy/agthelm-templates/security/advisories/new)
2. Or contact the maintainer listed in [MAINTAINERS.md](MAINTAINERS.md).

Include: affected path / schema version, impact, reproduction if possible.

We aim to acknowledge within **7 days** and follow up with a fix or mitigation plan.

## Scope notes

- This repository holds **source** templates and validators. Production trust boundary for installed packages is **cryptographic signature verification** in the agthelm product, not “YAML from git”.
- Do not attach customer data, credentials, or private keys to reports.
