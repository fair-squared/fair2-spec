# FAIR² Ontology Documentation

## Overview
The FAIR² ontology provides a structured, semantic representation of datasets adhering to **FAIR principles**, with a focus on **AI-readiness, responsible AI alignment, and context-rich metadata**. The ontology is available in **JSON-LD** and **Turtle (TTL)** formats to ensure compatibility with linked data and semantic web technologies.

## Ontology Description
The FAIR² ontology defines key classes and properties for describing datasets, including:

- **Dataset Metadata** (e.g., provenance, citation, funding, licensing)
- **AI Readiness** (e.g., data format, structure, machine learning compatibility)
- **Responsible AI** (e.g., bias assessment, ethics review, limitations)
- **Methods & Steps** (e.g., computational methods, workflow steps)

### **Ontology Formats**
The ontology is provided in the following formats:

- **JSON-LD**: [`fair2_ontology.jsonld`](./fair2_ontology.jsonld) (suitable for web interoperability)
- **Turtle (TTL)**: [`fair2_ontology.ttl`](./fair2_ontology.ttl) (compact RDF format for linked data)

## **Namespaces Used in FAIR²**
The FAIR² specification integrates multiple vocabularies to ensure broad compatibility. Below is a table of namespaces used in the ontology:

| Prefix  | Namespace URI |
|---------|--------------------------------------------------------------|
| `fair2` | `https://fair2.ai/ontology#` |
| `schema` | `https://schema.org/` |
| `cr` | `https://mlcommons.org/croissant#` |
| `sh` | `http://www.w3.org/ns/shacl#` |
| `rdfs` | `http://www.w3.org/2000/01/rdf-schema#` |
| `xsd` | `http://www.w3.org/2001/XMLSchema#` |
| `rai` | `https://fair2.ai/ontology/responsibleAI#` |
| `obo` | `http://purl.obolibrary.org/obo/` |
| `prov` | `http://www.w3.org/ns/prov#` |

## **Ontology Structure**

### **Core Classes**
- `fair2:Dataset`: A dataset that follows FAIR² principles.
- `fair2:Method`: A computational or data processing method.
- `fair2:Protocol`: A protocol used in computational or data processing methods.

### **Key Properties**
- `fair2:method`: Defines the method used to generate the dataset.
- `fair2:step`: Defines a step within a method.
- `fair2:isLiveDataset`: Indicates whether the dataset is actively updated.
- `rai:ethicsReview`: Ethics review metadata.
- `rai:dataBiases`: Known biases in the dataset.
- `rai:dataLimitations`: Dataset limitations.

## **Usage and Integration**
The FAIR² ontology can be used for:

- **Dataset Annotation:** Ensuring datasets are machine-readable and AI-ready.
- **Provenance Tracking:** Linking dataset modifications and authorship.
- **AI Model Integration:** Structuring data for ML pipelines.
- **Ethical AI Compliance:** Documenting bias assessments and ethics reviews.


## **Accessing the Ontology**
The ontology files are available in the FAIR² repository:

- **JSON-LD:** [`fair2_ontology.jsonld`](./fair2_ontology.jsonld)
- **Turtle (TTL):** [`fair2_ontology.ttl`](./fair2_ontology.ttl)

For questions visit the FAIR² project at [https://fair2.ai](https://fair2.ai), or write an email to [info@fair2.ai](mailto:info@fair2.ai).

