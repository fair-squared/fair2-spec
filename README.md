# FAIR² Specification
This repository hosts the FAIR² (FAIR SQUARED™) specification, providing data schemas, SHACL shapes, and JSON-LD context
## Description

The FAIR² specification aims to enhance the FAIR (Findable, Accessible, Interoperable, and Reusable) principles by providing a structured approach to data management. This repository includes:

- **Data Schemas**: Define the structure of the data.
- **SHACL Shapes**: Validate the data against the defined schemas.
- **JSON-LD Context**: Provide context for the data to ensure interoperability.

## Usage

### Validating Data

To validate your data against the SHACL shapes provided in this repository, you can use a SHACL validation tool such as [SHACL Playground](https://shacl.org/playground/) or a command-line tool like [rdf-toolkit](https://github.com/TopQuadrant/rdf-toolkit).

#### Example

1. **Prepare your data file** (e.g., `data.jsonld`):

    ```json
    {
      "@context": "https://example.org/context",
      "@id": "https://example.org/data/1",
      "name": "Example Data",
      "description": "This is an example data entry."
    }
    ```
    1. **Prepare your data file** (e.g., `data.jsonld`):

        ```json
        {
          "@context": "https://example.org/context",
          "@id": "https://example.org/data/1",
          "name": "Example Data",
          "description": "This is an example data entry."
        }
        ```

2. **Prepare your SHACL shapes file** (e.g., `shapes.jsonld`):

    ```json
    {
      "@context": {
        "sh": "http://www.w3.org/ns/shacl#",
        "ex": "https://example.org/",
        "xsd": "http://www.w3.org/2001/XMLSchema#"
      },
      "@id": "ex:DataShape",
      "@type": "sh:NodeShape",
      "sh:targetClass": "ex:Data",
      "sh:property": [
        {
          "sh:path": "ex:name",
          "sh:datatype": "xsd:string",
          "sh:minCount": 1
        },
        {
          "sh:path": "ex:description",
          "sh:datatype": "xsd:string",
          "sh:minCount": 1
        }
      ]
    }
    ```

3. **Run the validation** using a SHACL validation tools:

    ```sh
    python validate_shacl.py my_data.json ./shapes/fair2_dataset.json
    ```

    Where:
    - my_data.json = The RDF dataset (in JSON-LD format).
	- ./shapes/fair2_data_package.json = The SHACL shape file (in JSON-LD format).


By following these steps, you can ensure that your data adheres to the FAIR² specification, promoting better data management and interoperability.
