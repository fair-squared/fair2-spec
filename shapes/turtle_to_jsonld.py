import json
import re
from pathlib import Path
import rdflib
from rdflib.namespace import NamespaceManager

# Configuration
INPUT_DIR = Path("./turtle")
OUTPUT_DIR = Path("./json-ld")
FAIR2S_NS = rdflib.Namespace("https://fair2.ai/shapes/")

def suggest_prefix(uri_base, count):
    """
    Tries to guess a short prefix from the URI path. 
    If it's too complex, falls back to ns{count}.
    """
    # Try to take the last word from the URI (e.g., 'ontology' or 'terms')
    match = re.search(r'([a-zA-Z0-9]+)[/#]$', uri_base)
    if match:
        suggestion = match.group(1).lower()
        if len(suggestion) > 2:
            return f"{suggestion}_{count}"
    return f"ns{count}"

def discover_and_bind_namespaces(graph):
    """
    Scans the graph for URIs and binds a prefix to any namespace
    that is not currently covered.
    """
    existing_namespaces = {str(ns) for _, ns in graph.namespaces()}
    
    # Ensure fair2s is always covered as requested
    if str(FAIR2S_NS) not in existing_namespaces:
        graph.bind("fair2s", FAIR2S_NS)
        existing_namespaces.add(str(FAIR2S_NS))

    uncovered_count = 0
    
    # Iterate through all triples (subject, predicate, object)
    for s, p, o in graph:
        for node in (s, p, o):
            if isinstance(node, rdflib.URIRef):
                uri_str = str(node)
                # Find the base of the URI (everything before the last # or /)
                if "#" in uri_str:
                    base = uri_str.rsplit("#", 1)[0] + "#"
                elif "/" in uri_str:
                    base = uri_str.rsplit("/", 1)[0] + "/"
                else:
                    continue

                if base not in existing_namespaces:
                    uncovered_count += 1
                    prefix = suggest_prefix(base, uncovered_count)
                    graph.bind(prefix, rdflib.Namespace(base))
                    existing_namespaces.add(base)
                    print(f"    [*] Discovered & defined: {prefix} -> {base}")

def batch_transform():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"🚀 Batch Processing with Dynamic Discovery: {INPUT_DIR} ➔ {OUTPUT_DIR}")

    ttl_files = list(INPUT_DIR.glob("*.ttl"))
    for ttl_path in ttl_files:
        try:
            g = rdflib.Graph()
            g.parse(str(ttl_path), format="turtle")

            # 🔥 DYNAMIC STEP: Discover unknown namespaces
            discover_and_bind_namespaces(g)

            # Build context from ALL bound prefixes (old and discovered)
            dynamic_context = {prefix: str(ns) for prefix, ns in g.namespaces() if prefix}
            dynamic_context["@language"] = "en"

            jsonld_data = g.serialize(
                format="json-ld", 
                context=dynamic_context, 
                indent=4
            )
            
            output_path = OUTPUT_DIR / ttl_path.with_suffix(".json").name
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(jsonld_data)

            print(f"  [+] Converted: {ttl_path.name}")

        except Exception as e:
            print(f"  [!] Error: {ttl_path.name} -> {e}")

if __name__ == "__main__":
    batch_transform()