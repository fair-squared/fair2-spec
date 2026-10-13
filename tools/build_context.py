#!/usr/bin/env python3
"""Render the working context into an immutable, versioned, published one.

context/metadata/fair2_context.json is the working source, edited by hand. A
release freezes it as context/v<X.Y.Z>.jsonld, which is what documents point
at and what must never change once published.

Two deliberate differences between the two files:

  * The working source is a JSON-LD context *array* - schema.org, Croissant,
    then the inline term map. The published one is only the term map, so it
    resolves in a single request, works offline behind a document loader, and
    cannot be altered by an upstream change to either of those vocabularies.
    The reference example has used the flattened form throughout and both
    mlcroissant and pyshacl read it, so nothing depends on the remote pair.

  * The published file carries @version and a comment naming the release, so a
    file found on its own says what it is.

    python tools/build_context.py v1.5.0 [--check]
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "context" / "metadata" / "fair2_context.json"
OUT_DIR = ROOT / "context"
VERSION_RE = re.compile(r"^v\d+\.\d+\.\d+$")


def term_map() -> dict:
    ctx = json.loads(SOURCE.read_text())["@context"]
    return ctx[-1] if isinstance(ctx, list) else ctx


def build(version: str) -> dict:
    return {
        "@context": {
            "@version": 1.1,
            **term_map(),
        },
        "_comment": (
            f"FAIR2 {version} JSON-LD context. Immutable: published once and never "
            f"changed. Generated from context/metadata/fair2_context.json by "
            f"tools/build_context.py - do not edit by hand."
        ),
    }


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check = "--check" in sys.argv
    if len(args) != 1 or not VERSION_RE.match(args[0]):
        print("usage: build_context.py vX.Y.Z [--check]")
        return 2
    version = args[0]
    out = OUT_DIR / f"{version}.jsonld"
    text = json.dumps(build(version), indent=2, ensure_ascii=False) + "\n"

    if check:
        if not out.exists():
            print(f"{out.relative_to(ROOT)} has not been generated")
            return 1
        if out.read_text() != text:
            print(f"{out.relative_to(ROOT)} is stale - regenerate it")
            return 1
        print(f"{out.relative_to(ROOT)} is up to date ({len(term_map())} terms)")
        return 0

    if out.exists() and out.read_text() != text:
        print(f"refusing to overwrite {out.relative_to(ROOT)}: a published context is "
              f"immutable. Cut a new version instead.")
        return 1
    out.write_text(text)
    print(f"wrote {out.relative_to(ROOT)} ({len(term_map())} terms)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
