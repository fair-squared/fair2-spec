from rdflib import Graph
import argparse

def convert_turtle_to_jsonld(input_file, output_file):
    # Create a new RDF graph
    g = Graph()

    # Parse the Turtle file
    g.parse(input_file, format='turtle')

    # Serialize the graph to JSON-LD format
    jsonld_data = g.serialize(format='json-ld', indent=4)

    # Write the JSON-LD data to the output file
    with open(output_file, 'w') as f:
        f.write(jsonld_data)

def convert_jsonld_to_turtle(input_file, output_file):
    # Create a new RDF graph
    g = Graph()

    # Parse the JSON-LD file
    g.parse(input_file, format='json-ld')

    # Serialize the graph to Turtle format
    turtle_data = g.serialize(format='turtle')

    # Write the Turtle data to the output file
    with open(output_file, 'w') as f:
        f.write(turtle_data)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Convert Turtle files to JSON-LD format.")
    parser.add_argument("input_file", help="Path to the input Turtle file.")
    parser.add_argument("output_file", help="Path to the output JSON-LD file.")

    args = parser.parse_args()

    convert_turtle_to_jsonld(args.input_file, args.output_file)
