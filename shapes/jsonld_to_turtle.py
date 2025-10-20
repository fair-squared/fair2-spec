"""
FAIR² Shape Conversion Utility
------------------------------
Converts all JSON-LD FAIR² SHACL shape files in a directory to Turtle (.ttl),
adds all required prefixes, and fixes literal-prefixed terms (like "schema:name").
"""

import rdflib
from rdflib import URIRef, Literal, Namespace
from pathlib import Path


# ============================================================
# FAIR² and standard namespaces
# ============================================================
NAMESPACES = {
    "schema": Namespace("https://schema.org/"),
    "fair2": Namespace("https://fair2.ai/ns/"),
    "fair2s": Namespace("https://fair2.ai/shapes/"),
    "cr": Namespace("http://mlcommons.org/croissant/"),
    "sh": Namespace("http://www.w3.org/ns/shacl#"),
    "prov": Namespace("http://www.w3.org/ns/prov#"),
    "skos": Namespace("http://www.w3.org/2004/02/skos/core#"),
    "dct": Namespace("http://purl.org/dc/terms/"),
    "xsd": Namespace("http://www.w3.org/2001/XMLSchema#"),
    "rdf": Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#"),
    "rdfs": Namespace("http://www.w3.org/2000/01/rdf-schema#"),
}

PREFIX_BLOCK = """@prefix fair2s: <https://fair2.ai/shapes/> .
@prefix fair2:  <https://fair2.ai/ns/> .
@prefix sh:     <http://www.w3.org/ns/shacl#> .
@prefix schema: <https://schema.org/> .
@prefix cr:     <http://mlcommons.org/croissant/> .
@prefix prov:   <http://www.w3.org/ns/prov#> .
@prefix skos:   <http://www.w3.org/2004/02/skos/core#> .
@prefix dct:    <http://purl.org/dc/terms/> .
@prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .
@prefix rdf:    <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:   <http://www.w3.org/2000/01/rdf-schema#> .\n\n"""


# ============================================================
# Utility Functions
# ============================================================

def convert_jsonld_to_ttl(jsonld_path: Path, output_path: Path):
    """Convert a single JSON-LD file to Turtle format."""
    g = rdflib.Graph()
    g.parse(jsonld_path, format="json-ld")
    for pref, ns in NAMESPACES.items():
        g.bind(pref, ns)
    ttl_data = g.serialize(format="turtle")
    output_path.write_text(PREFIX_BLOCK + ttl_data)
    print(f"💾 Converted {jsonld_path.name} -> {output_path.name}")


def fix_literals_in_ttl(ttl_path: Path):
    """Fix predicates and objects that are string literals representing prefixed terms."""
    g = rdflib.Graph()
    g.parse(ttl_path, format="turtle")

    to_add, to_remove = [], []
    for s, p, o in g:
        # Fix predicate literals (e.g. "schema:name")
        if isinstance(p, Literal):
            text = str(p)
            if ":" in text:
                pref, local = text.split(":", 1)
                if pref in NAMESPACES:
                    to_add.append((s, URIRef(NAMESPACES[pref] + local), o))
                    to_remove.append((s, p, o))

        # Fix object literals (e.g. "xsd:string")
        if isinstance(o, Literal):
            text = str(o)
            if ":" in text:
                pref, local = text.split(":", 1)
                if pref in NAMESPACES:
                    to_add.append((s, p, URIRef(NAMESPACES[pref] + local)))
                    to_remove.append((s, p, o))

    for t in to_remove:
        g.remove(t)
    for t in to_add:
        g.add(t)

    for pref, ns in NAMESPACES.items():
        g.bind(pref, ns)

    ttl_output = g.serialize(format="turtle")
    ttl_path.write_text(PREFIX_BLOCK + ttl_output)
    print(f"✅ Fixed {ttl_path.name}: {len(to_add)} replacements")


# ============================================================
# Main Conversion Pipeline
# ============================================================

def convert_and_fix_all_shapes(input_dir: str, output_dir: str):
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    jsonld_files = list(input_dir.glob("*.jsonld"))
    if not jsonld_files:
        print(f"⚠️ No JSON-LD files found in {input_dir}")
        return

    for jsonld_file in jsonld_files:
        ttl_path = output_dir / jsonld_file.with_suffix(".ttl").name
        convert_jsonld_to_ttl(jsonld_file, ttl_path)
        fix_literals_in_ttl(ttl_path)

    print(f"\n🎉 Conversion complete! Fixed TTL files saved to: {output_dir.resolve()}")


# ============================================================
# Example Usage
# ============================================================
if __name__ == "__main__":
    # Adjust paths as needed
    INPUT_DIR = "./json-ld"   # folder with your .jsonld shape files
    OUTPUT_DIR = "./turtle"     # folder for the generated .ttl files
    convert_and_fix_all_shapes(INPUT_DIR, OUTPUT_DIR)