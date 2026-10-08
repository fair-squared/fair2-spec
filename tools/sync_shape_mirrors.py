#!/usr/bin/env python3
"""Generate shapes/json-ld/*.json from shapes/turtle/*.ttl, deterministically.

Replaces shapes/turtle_to_jsonld.py, which asked gpt-4o to perform the
translation. That approach produced every drift defect the consistency guard
now checks for: shapes attached as properties of other shapes, paths written
in the wrong namespace, missing rdf:type, and sh:or serialised as repeated
triples rather than an RDF list.

This reads the Turtle with rdflib and renders the graph, so the output is
reproducible and the guard's isomorphism check is guaranteed to pass.

    python tools/sync_shape_mirrors.py [--check]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import rdflib
from rdflib.collection import Collection
from rdflib.compare import graph_diff, to_isomorphic

SH = rdflib.Namespace("http://www.w3.org/ns/shacl#")
ROOT = Path(__file__).resolve().parent.parent
TURTLE_DIR = ROOT / "shapes" / "turtle"
JSONLD_DIR = ROOT / "shapes" / "json-ld"

# Properties whose values are IRIs, and those whose values are RDF lists.
IRI_VALUED = ["sh:path", "sh:node", "sh:targetClass", "sh:nodeKind", "sh:datatype",
              "sh:class", "sh:targetObjectsOf", "sh:targetSubjectsOf", "sh:severity",
              "sh:hasValue"]
LIST_VALUED = ["sh:or", "sh:and", "sh:xone", "sh:in", "sh:languageIn"]
# Rendered first, in this order, so a property shape reads the way it was written.
LEAD = ["sh:path", "sh:minCount", "sh:maxCount", "sh:nodeKind", "sh:datatype", "sh:node"]


def compact(graph: rdflib.Graph, term) -> str:
    for prefix, namespace in graph.namespaces():
        if prefix and str(term).startswith(str(namespace)):
            return f"{prefix}:{str(term)[len(str(namespace)):]}"
    return str(term)


def is_list(graph: rdflib.Graph, node) -> bool:
    return isinstance(node, rdflib.BNode) and (node, rdflib.RDF.first, None) in graph


def render(graph: rdflib.Graph, node, top_level: set, in_list: bool = False):
    if isinstance(node, rdflib.Literal):
        if node.datatype == rdflib.XSD.integer:
            return int(node)
        if node.datatype == rdflib.XSD.boolean:
            return bool(node)
        return str(node)
    if isinstance(node, rdflib.URIRef):
        # Inside a list the context cannot coerce: sh:in holds IRIs in one shape
        # and literal tokens in another, so IRI members say so explicitly.
        return {"@id": compact(graph, node)} if in_list else compact(graph, node)
    if is_list(graph, node):
        return [render(graph, item, top_level, in_list=True) for item in Collection(graph, node)]
    return render_node(graph, node, top_level)


def render_node(graph: rdflib.Graph, subject, top_level: set) -> dict:
    out: dict = {}
    if isinstance(subject, rdflib.URIRef):
        out["@id"] = compact(graph, subject)

    grouped: dict[str, list] = {}
    for predicate, obj in graph.predicate_objects(subject):
        if predicate == rdflib.RDF.type:
            out["@type"] = compact(graph, obj)
            continue
        grouped.setdefault(compact(graph, predicate), []).append(obj)

    def order(key: str) -> tuple:
        return (LEAD.index(key), "") if key in LEAD else (len(LEAD), key)

    for key in sorted(grouped, key=order):
        values = grouped[key]
        if key == "sh:property":
            out[key] = [render_node(graph, v, top_level) for v in values]
            out[key].sort(key=lambda d: json.dumps(d, sort_keys=True))
        elif len(values) == 1:
            out[key] = render(graph, values[0], top_level)
        else:
            out[key] = sorted((render(graph, v, top_level) for v in values),
                              key=lambda x: json.dumps(x, sort_keys=True))
    return out


def build(path: Path) -> dict:
    graph = rdflib.Graph().parse(path, format="turtle")

    named = sorted({s for s in graph.subjects(rdflib.RDF.type, SH.NodeShape)
                    if isinstance(s, rdflib.URIRef)}, key=str)
    # anything referenced only as a value stays a string, so collect the set first
    top_level = set(named)

    used = {compact(graph, p) for p in graph.predicates()}
    used |= {compact(graph, rdflib.RDF.type)}
    context = {prefix: str(ns) for prefix, ns in graph.namespaces()
               if prefix and any(compact(graph, t).startswith(f"{prefix}:")
                                 for t in set(graph.predicates()) | set(graph.objects()) | set(graph.subjects()))}
    for key in IRI_VALUED:
        if key in used:
            context[key] = {"@type": "@id"}
    for key in LIST_VALUED:
        if key in used:
            context[key] = {"@container": "@list"}

    bodies = [render_node(graph, s, top_level) for s in named]
    if len(bodies) == 1:
        return {"@context": context, **bodies[0]}
    return {"@context": context, "@graph": bodies}


def main() -> int:
    check = "--check" in sys.argv
    problems = []
    for ttl in sorted(TURTLE_DIR.glob("*.ttl")):
        out = JSONLD_DIR / f"{ttl.stem}.json"
        text = json.dumps(build(ttl), indent=4, ensure_ascii=False) + "\n"
        if check:
            if not out.exists() or out.read_text() != text:
                problems.append(out.name)
            continue
        out.write_text(text)
        a = to_isomorphic(rdflib.Graph().parse(ttl, format="turtle"))
        b = to_isomorphic(rdflib.Graph().parse(out, format="json-ld"))
        _, only_ttl, only_json = graph_diff(a, b)
        status = "ok" if not len(only_ttl) and not len(only_json) else \
                 f"MISMATCH {len(only_ttl)}/{len(only_json)}"
        print(f"  {out.name:26} {status}")
        if status != "ok":
            problems.append(out.name)

    if problems:
        print(("stale (run without --check to regenerate): " if check else "mismatched: ")
              + ", ".join(problems))
        return 1
    print("all mirrors regenerated and isomorphic to their Turtle" if not check
          else "all mirrors up to date")
    return 0


if __name__ == "__main__":
    sys.exit(main())
