#!/usr/bin/env python3
"""Keep the four artefacts of the FAIR² spec in agreement.

The SHACL shapes in shapes/turtle/ are the source of truth. The ontology, the
JSON-LD context and the JSON-LD shape mirrors must follow them. Nothing used to
check that, which is how the spec came to declare 27 terms in the ontology while
the context defined 54 and the shapes targeted classes neither of them knew
about.

Run with no arguments from the repository root:

    python tools/check_spec_consistency.py
"""

from __future__ import annotations

import glob
import json
import sys
from pathlib import Path

import rdflib
from rdflib.compare import graph_diff, to_isomorphic

FAIR2 = "https://fair2.ai/ns/"
SH = rdflib.Namespace("http://www.w3.org/ns/shacl#")

ROOT = Path(__file__).resolve().parent.parent
TURTLE_DIR = ROOT / "shapes" / "turtle"
JSONLD_DIR = ROOT / "shapes" / "json-ld"
ONTOLOGY = ROOT / "ontologies" / "fair2_ontology.ttl"
ONTOLOGY_DOC = ROOT / "docs" / "specification" / "fair2-ontology.md"
SCHEMAORG_TERMS = Path(__file__).resolve().parent / "schemaorg-terms.json"
CONTEXT = ROOT / "context" / "metadata" / "fair2_context.json"
EXAMPLES = ROOT / "examples"

# Keys an individual document may add to its own copy of the shared context.
DOCUMENT_LOCAL_CONTEXT_KEYS = {"@base", "@language"}

failures: list[str] = []


def fail(check: str, message: str, items: list[str] | None = None) -> None:
    detail = "".join(f"\n      - {i}" for i in sorted(items)) if items else ""
    failures.append(f"  [{check}] {message}{detail}")


def local(term: rdflib.term.Node) -> str | None:
    return str(term)[len(FAIR2):] if str(term).startswith(FAIR2) else None


def shapes_graph() -> rdflib.Graph:
    g = rdflib.Graph()
    for path in sorted(TURTLE_DIR.glob("*.ttl")):
        g.parse(path, format="turtle")
    return g


def context_terms() -> tuple[dict, set[str]]:
    """The inline term map of the shared context, and the fair2: terms in it."""
    doc = json.loads(CONTEXT.read_text())
    ctx = doc["@context"]
    inline = ctx[-1] if isinstance(ctx, list) else ctx
    terms = set()
    for value in inline.values():
        iri = value.get("@id") if isinstance(value, dict) else value
        if isinstance(iri, str) and iri.startswith("fair2:"):
            terms.add(iri.split(":", 1)[1])
    return inline, terms


def check_term_coverage(shapes: rdflib.Graph, ctx_inline: dict, ctx_fair2: set[str]) -> None:
    """Every fair2: term the shapes use must be declared and defined."""
    used = {
        t
        for t in (
            local(x)
            for x in list(shapes.objects(None, SH.targetClass)) + list(shapes.objects(None, SH.path))
        )
        if t
    }
    ontology = rdflib.Graph().parse(ONTOLOGY, format="turtle")
    declared = {t for t in (local(s) for s in ontology.subjects(rdflib.RDF.type, None)) if t}

    if missing := used - declared:
        fail("ontology", "fair2: terms used by the shapes but not declared in the ontology:",
             [f"fair2:{t}" for t in missing])
    if missing := used - ctx_fair2:
        fail("context", "fair2: terms used by the shapes but not defined in the context:",
             [f"fair2:{t}" for t in missing])
    if missing := ctx_fair2 - declared:
        fail("ontology", "fair2: terms defined in the context but not declared in the ontology:",
             [f"fair2:{t}" for t in missing])


def check_ontology_documented() -> None:
    """Every declared term must appear on the ontology documentation page."""
    import re

    ontology = rdflib.Graph().parse(ONTOLOGY, format="turtle")
    declared = {t for t in (local(s) for s in ontology.subjects(rdflib.RDF.type, None)) if t}
    documented = set(re.findall(r"`fair2:(\w+)`", ONTOLOGY_DOC.read_text()))
    if missing := declared - documented:
        fail("docs", f"terms declared in the ontology but absent from "
                     f"{ONTOLOGY_DOC.relative_to(ROOT)}:", [f"fair2:{t}" for t in missing])


def check_context_coercions(ctx_inline: dict) -> None:
    """@type in a term definition is value coercion, not a subclass axiom.

    Coercing to a class IRI turns string values into literals with that class as
    their datatype, which is never what is meant.
    """
    offenders = [
        f"{term}: {json.dumps(defn)}"
        for term, defn in ctx_inline.items()
        if isinstance(defn, dict)
        and isinstance(defn.get("@type"), str)
        and not defn["@type"].startswith(("@", "xsd:", "http://www.w3.org/2001/XMLSchema#"))
    ]
    if offenders:
        fail("context",
             "term definitions coerce @type to a class IRI (use @id, or declare "
             "rdfs:subClassOf in the ontology instead):", offenders)


def check_schemaorg_terms_exist(ctx_inline: dict) -> None:
    """A term bound to schema:X must be a term schema.org actually has.

    Prefix expansion is syntactic, so `schema:dateUpdated` expands to a
    plausible IRI that resolves to nothing and joins to nothing, and every
    processor stays silent. Needs tools/schemaorg-terms.json; regenerate it
    with tools/fetch_schemaorg_terms.py.
    """
    if not SCHEMAORG_TERMS.exists():
        print(f"  [skip] {SCHEMAORG_TERMS.name} absent — run tools/fetch_schemaorg_terms.py "
              f"to enable the schema.org term check")
        return
    known = set(json.loads(SCHEMAORG_TERMS.read_text())["terms"])
    offenders = []
    for term, defn in ctx_inline.items():
        iri = defn.get("@id") if isinstance(defn, dict) else defn
        if isinstance(iri, str) and iri.startswith("schema:"):
            name = iri.split(":", 1)[1]
            if name not in known:
                offenders.append(f"{term} -> {iri} (no such schema.org term)")
    if offenders:
        fail("context", "terms bound to schema.org URIs that do not exist:", offenders)


def check_types_are_mapped() -> None:
    """Every @type value in an example must resolve through the context.

    An unmapped @type is not caught by undefined-term policies, which govern
    properties. With @vocab set it becomes https://schema.org/<Type>; without
    one it resolves against @base into the document's own namespace. Either
    way the node carries a type that means nothing.
    """
    for path in example_files():
        doc = json.loads(path.read_text())
        ctx = doc.get("@context")
        if not isinstance(ctx, dict):
            continue
        defined = {k for k in ctx if not k.startswith("@")}
        prefixes = {k for k, v in ctx.items() if isinstance(v, str) and v.startswith("http")}
        unmapped: set[str] = set()

        def walk(node) -> None:
            if isinstance(node, dict):
                types = node.get("@type")
                for t in ([types] if isinstance(types, str) else types or []):
                    if not isinstance(t, str) or t.startswith("@"):
                        continue
                    if ":" in t:
                        if t.split(":", 1)[0] not in prefixes:
                            unmapped.add(t)
                    elif t not in defined:
                        unmapped.add(t)
                for value in node.values():
                    walk(value)
            elif isinstance(node, list):
                for item in node:
                    walk(item)

        walk({k: v for k, v in doc.items() if k != "@context"})
        if unmapped:
            fail("context", f"{path.relative_to(ROOT)} uses @type values the context does not map:",
                 sorted(unmapped))


def check_shape_mirrors() -> None:
    """Each shapes/json-ld/*.json must express the same graph as its .ttl."""
    drifted = []
    for ttl in sorted(TURTLE_DIR.glob("*.ttl")):
        mirror = JSONLD_DIR / f"{ttl.stem}.json"
        if not mirror.exists():
            drifted.append(f"{mirror.name}: missing")
            continue
        t = to_isomorphic(rdflib.Graph().parse(ttl, format="turtle"))
        j = to_isomorphic(rdflib.Graph().parse(mirror, format="json-ld"))
        _, only_ttl, only_json = graph_diff(t, j)
        if len(only_ttl) or len(only_json):
            drifted.append(f"{mirror.name}: {len(only_ttl)} triples only in .ttl, {len(only_json)} only in .json")
    if drifted:
        fail("mirrors", "JSON-LD shape mirrors no longer match their Turtle source:", drifted)


def example_files() -> list[Path]:
    """Examples tracked by git.

    CI checks committed content, so an untracked scratch copy in examples/ is
    not the spec's problem. Falls back to the filesystem outside a checkout.
    """
    import subprocess

    try:
        out = subprocess.run(
            ["git", "-C", str(ROOT), "ls-files", "examples/*.json", "examples/**/*.json"],
            capture_output=True, text=True, check=True,
        ).stdout.split()
        candidates = [ROOT / line for line in out]
    except (subprocess.CalledProcessError, FileNotFoundError):
        candidates = sorted(EXAMPLES.rglob("*.json"))
    return [p for p in candidates if p.exists() and "@context" in p.read_text()]


def check_example_contexts(ctx_inline: dict) -> None:
    """An example's inline context must be the shared context, not a stale copy."""
    for path in example_files():
        doc = json.loads(path.read_text())
        inline = doc.get("@context")
        if not isinstance(inline, dict):
            continue
        shared = {k: v for k, v in inline.items() if k not in DOCUMENT_LOCAL_CONTEXT_KEYS}
        if shared != ctx_inline:
            diffs = [
                f"{k}: example={json.dumps(shared.get(k))} spec={json.dumps(ctx_inline.get(k))}"
                for k in sorted(set(shared) | set(ctx_inline))
                if shared.get(k) != ctx_inline.get(k)
            ]
            fail("context", f"{path.relative_to(ROOT)} carries a context that differs from the shared one:", diffs)


def check_no_vocab_fallthrough() -> None:
    """Every key in an example must be defined; @vocab must not be the safety net.

    A key the context does not define silently becomes https://schema.org/<key>,
    so a typo such as `departament` produces a predicate that does not exist
    rather than an error.
    """
    for path in example_files():
        doc = json.loads(path.read_text())
        ctx = doc.get("@context")
        if not isinstance(ctx, dict):
            continue
        defined = {k for k in ctx if not k.startswith("@")}
        prefixes = {k for k, v in ctx.items() if isinstance(v, str) and v.startswith("http")}
        undefined: set[str] = set()

        def walk(node) -> None:
            if isinstance(node, dict):
                for key, value in node.items():
                    if not key.startswith("@") and key not in defined:
                        if ":" not in key or key.split(":", 1)[0] not in prefixes:
                            undefined.add(key)
                    walk(value)
            elif isinstance(node, list):
                for item in node:
                    walk(item)

        walk({k: v for k, v in doc.items() if k != "@context"})
        if undefined:
            fail("context", f"{path.relative_to(ROOT)} uses keys the context does not define "
                            f"(they fall through @vocab):", sorted(undefined))


def check_id_constraints() -> None:
    """Identifier rules that nothing else enforces (Issue 18).

    1. An entity's @id must not equal the @id of its own identifier.
       mlcroissant indexes nodes by @id and its expander mutates shared
       nodes destructively, so the second visit raises KeyError and the
       document does not load at all.
    2. @id must be unique among node definitions within a document.
    """
    for path in example_files():
        doc = json.loads(path.read_text())
        self_ref, seen, dupes = [], {}, []

        def walk(node) -> None:
            if isinstance(node, dict):
                nid = node.get("@id")
                if isinstance(nid, str):
                    # Only a node-valued identifier collides: it makes two nodes
                    # share one @id. A plain string equal to the @id is merely
                    # redundant, and the Dataset shape requires one for harvesters.
                    ident = node.get("identifier")
                    for i in (ident if isinstance(ident, list) else [ident]):
                        if isinstance(i, dict) and i.get("@id") == nid:
                            self_ref.append(nid)
                    # a definition carries more than just @id
                    if len(node) > 1:
                        if nid in seen and seen[nid] != _fingerprint(node):
                            dupes.append(nid)
                        seen[nid] = _fingerprint(node)
                for value in node.values():
                    walk(value)
            elif isinstance(node, list):
                for item in node:
                    walk(item)

        def _fingerprint(node) -> str:
            return json.dumps(node, sort_keys=True)

        walk({k: v for k, v in doc.items() if k != "@context"})
        if self_ref:
            fail("identifiers", f"{path.relative_to(ROOT)}: nodes whose @id equals their own "
                                f"identifier (breaks the mlcroissant expander):", sorted(set(self_ref)))
        if dupes:
            fail("identifiers", f"{path.relative_to(ROOT)}: one @id used for two different "
                                f"node definitions:", sorted(set(dupes)))


def check_examples_validate(shapes: rdflib.Graph) -> None:
    import pyshacl

    for path in example_files():
        data = rdflib.Graph().parse(path, format="json-ld")
        conforms, _, text = pyshacl.validate(data, shacl_graph=shapes, advanced=True)
        if not conforms:
            fail("shacl", f"{path.relative_to(ROOT)} does not conform to the shapes "
                          f"({text.count('Constraint Violation')} violations)")


def check_examples_load_in_mlcroissant() -> None:
    """Croissant compatibility is the gate: mlcroissant must still load each example.

    This is not covered by SHACL. A context change can leave every shape
    satisfied and still break the reference loader — coercing dct:conformsTo
    to @id did exactly that, because mlcroissant reads it to decide which
    Croissant version's rules apply.
    """
    try:
        import mlcroissant as mlc
    except ImportError:
        print("  [skip] mlcroissant not installed — Croissant compatibility unchecked")
        return

    import warnings

    for path in example_files():
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                mlc.Dataset(jsonld=str(path))
        except Exception as exc:  # noqa: BLE001 - any loader failure is a failure
            first = next((l.strip() for l in str(exc).splitlines() if l.strip().startswith("-")), "")
            fail("croissant", f"mlcroissant cannot load {path.relative_to(ROOT)}: "
                              f"{type(exc).__name__}" + (f" — {first[:120]}" if first else ""))


def main() -> int:
    shapes = shapes_graph()
    ctx_inline, ctx_fair2 = context_terms()

    check_term_coverage(shapes, ctx_inline, ctx_fair2)
    check_ontology_documented()
    check_context_coercions(ctx_inline)
    check_schemaorg_terms_exist(ctx_inline)
    check_types_are_mapped()
    check_shape_mirrors()
    check_example_contexts(ctx_inline)
    check_no_vocab_fallthrough()
    check_id_constraints()
    check_examples_validate(shapes)
    check_examples_load_in_mlcroissant()

    if failures:
        print("Spec consistency check FAILED\n")
        print("\n".join(failures))
        print("\nThe shapes are the source of truth: update the ontology, the context "
              "and the JSON-LD mirrors to match them.")
        return 1
    print("Spec consistency check passed: ontology, context, shape mirrors and examples all agree.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
