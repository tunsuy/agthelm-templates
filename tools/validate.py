#!/usr/bin/env python3
"""Validate an agthelm scenario template directory against schema/manifest.schema.json."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    import yaml
    from jsonschema import Draft202012Validator
except ImportError:
    print("Install deps: pip install -r tools/requirements.txt", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema" / "manifest.schema.json"


def load_manifest(template_dir: Path) -> dict:
    path = template_dir / "manifest.yaml"
    if not path.is_file():
        raise FileNotFoundError(f"missing {path}")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("manifest.yaml must be a mapping")
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "template_dir",
        type=Path,
        help="Path to template directory containing manifest.yaml",
    )
    args = parser.parse_args()
    template_dir = args.template_dir.resolve()
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    manifest = load_manifest(template_dir)
    Draft202012Validator(schema).validate(manifest)
    print(f"OK  {template_dir.name}  {manifest['metadata']['id']}@{manifest['metadata']['version']}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001 — CLI surface
        print(f"FAIL  {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
