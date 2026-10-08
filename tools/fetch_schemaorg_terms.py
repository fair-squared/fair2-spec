#!/usr/bin/env python3
"""Vendor the list of schema.org term names for the consistency guard.

Prefix expansion is purely syntactic: a bound prefix will happily produce a
URI that does not exist, and no processor objects. The guard therefore needs
to know which schema.org terms are real. Run this with network access; CI
refreshes it automatically.

    python tools/fetch_schemaorg_terms.py
"""

import json
import sys
import urllib.request
from pathlib import Path

SOURCE = "https://schema.org/version/latest/schemaorg-current-https.jsonld"
OUT = Path(__file__).resolve().parent / "schemaorg-terms.json"


def main() -> int:
    print(f"fetching {SOURCE}")
    with urllib.request.urlopen(SOURCE, timeout=60) as fh:
        vocab = json.load(fh)

    terms = sorted(
        node["@id"].split(":", 1)[1]
        for node in vocab.get("@graph", [])
        if isinstance(node.get("@id"), str) and node["@id"].startswith("schema:")
    )
    if len(terms) < 1000:
        print(f"only {len(terms)} terms parsed — refusing to write a partial snapshot")
        return 1

    OUT.write_text(json.dumps({"source": SOURCE, "terms": terms}, indent=0) + "\n")
    print(f"wrote {len(terms)} terms to {OUT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
