# Changelog

All notable changes to this repository are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project attempts to follow [Semantic Versioning](https://semver.org/) for schema/`apiVersion` where practical.

## [Unreleased]

### Added

- OSS documentation set: overview, manifest guide, governance, security, support, CoC, issue/PR templates
- Schema `templates.agthelm.io/v1beta1` (additive; v1alpha1 manifests still validate):
  `spec.glossary` (structured term/definition rows), `spec.eval_set.items`
  (question/expected rows, empty expected = expected refusal), `spec.actions`
  (self-describing action whitelist with labels and write grading), `spec.sources[].label`
  (suggested human-readable collection name)
- Example `examples/crm-customer-assistant` (v1beta1 fixture exercising all four new fields)

## [0.1.0] - 2026-09-30

### Added

- Initial public bootstrap: Apache-2.0, DCO contributing guide
- `schema/manifest.schema.json` (`templates.agthelm.io/v1alpha1`)
- Example `examples/discrete-mfg-aftersales` (schema fixture, not a customer delivery)
- `tools/validate.py` and GitHub Actions validation workflow
