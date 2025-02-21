import sys
import rdflib
from pyshacl import validate

def validate_jsonld_against_shacl(data_file, shacl_file, shape_format="json-ld"):
    """
    Validates an RDF dataset (JSON-LD format) against SHACL shapes.

    Args:
        data_file (str): Path to the JSON-LD file containing the RDF data.
        shacl_file (str): Path to the SHACL shapes file (Turtle, JSON-LD, or RDF/XML).
    """
    try:
        # Load JSON-LD data into an RDF Graph
        data_graph = rdflib.Graph()
        data_graph.parse(data_file, format="json-ld")

        # Load SHACL shapes into an RDF Graph
        shacl_graph = rdflib.Graph()
        shacl_graph.parse(shacl_file, format=shape_format)

        # Run SHACL validation
        conforms, report_graph, report_text = validate(
            data_graph,
            shacl_graph=shacl_graph,
            inference="rdfs",  # Enables RDFS inference for better validation
            abort_on_first=False,  # Continue checking all constraints
            meta_shacl=False,  # Do not validate SHACL syntax itself
            debug=False
        )

        # Print validation result
        print("🔍 SHACL Validation Results:")
        print(report_text)
        print("\n✅ Data conforms to SHACL shapes:", conforms)

        # Return validation result
        return conforms

    except Exception as e:
        print(f"❌ Error during validation: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python validate_shacl.py <data.jsonld> <shapes.ttl>")
        sys.exit(1)

    data_file = sys.argv[1]
    shacl_file = sys.argv[2]

    validate_jsonld_against_shacl(data_file, shacl_file)