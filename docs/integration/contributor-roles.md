# FAIR² and Contributor Role Ontology (CRO) Integration

## Overview

The FAIR² specification integrates the **Contributor Role Ontology (CRO)** to enable structured attribution of dataset contributions. This enhances transparency, supports scholarly credit, and aligns with established contributor role taxonomies such as **CRediT**.

By leveraging CRO, FAIR² metadata can express contributor roles in a machine-readable, semantically valid format that supports automated indexing, provenance tracking, and responsible data stewardship.

---

## Use of CRO in FAIR² Metadata

Contributor roles in FAIR² are expressed using:

- `schema:contribution` to list agents (e.g., persons or organizations)
- `prov:hadRole` to link contributors to formal role definitions from CRO
- `cro:ContributorRole` instances as the role class or term

| **FAIR² Property**        | **Ontology Term**         | **Purpose**                                                 |
|--------------------------|---------------------------|-------------------------------------------------------------|
| `schema:contribution`    | `schema:Person`, `prov:Agent` | Identifies individuals or organizations who contributed    |
| `prov:hadRole`           | `cro:ContributorRole`     | Specifies the contributor's role using CRO terms            |

---

## Example: JSON-LD Metadata with CRO Roles

```json
{
  "@context": [
    "https://fair2.ai/spec/fair2_context"
  ],
  "@type": "Dataset",
  "name": "FAIR AI Benchmark Dataset",
  "contribution": [
    {
      "@type": "Person",
      "name": "Dr. Alice Smith",
      "prov:hadRole": {
        "@id": "http://purl.obolibrary.org/obo/CRO_0000039",
        "rdfs:label": "Conceptualization"
      }
    },
    {
      "@type": "Person",
      "name": "John Doe",
      "prov:hadRole": {
        "@id": "http://purl.obolibrary.org/obo/CRO_0000027",
        "rdfs:label": "Data Curation"
      }
    }
  ]
}
```

---

## Ontology Mapping and Semantics

The following example illustrates the semantic structure of contributor roles using RDF vocabulary:

```json
{
  "@graph": [
    {
      "@id": "schema:Person",
      "@type": "rdfs:Class",
      "rdfs:label": "Person",
      "rdfs:comment": "An individual or entity that contributed to the dataset."
    },
    {
      "@id": "prov:hadRole",
      "@type": "rdf:Property",
      "rdfs:label": "Has Role",
      "rdfs:domain": "schema:Person",
      "rdfs:range": "cro:0000001"
    },
    {
      "@id": "cro:0000001",
      "@type": "rdfs:Class",
      "rdfs:label": "Contributor Role"
    }
  ]
}
```

---

## SHACL Constraints for Contributor Roles

FAIR² defines SHACL constraints to validate the use of `prov:hadRole` in contribution metadata:

```json
{
  "@context": [
    "https://fair2.ai/spec/fair2_context",
    "https://fair2.ai/spec/shacl_context"
  ],
  "@id": "fair2s:ContributionShape",
  "@type": "sh:NodeShape",
  "sh:targetClass": "schema:Contribution",
  "sh:property": [
    {
      "sh:path": "prov:hadRole",
      "sh:minCount": 1,
      "sh:description": "Each contribution must include at least one role.",
      "sh:or": [
        {
          "sh:class": "cro:CRO_0000001"
        }
      ]
    }
  ]
}
```

This ensures that each contribution includes a role and that the role is correctly typed using the CRO ontology.

---

## CRO and the CRediT Taxonomy

The **Contributor Role Ontology (CRO)** integrates the **CRediT (Contributor Roles Taxonomy)**, offering a controlled vocabulary of standardized contributor roles. Each CRediT role is mapped to a persistent URI, enabling semantic interoperability and machine-actionable credit assignment.

### Examples of CRO IDs for CRediT Roles

| **Role**                    | **CRO URI**                                                                 |
|-----------------------------|------------------------------------------------------------------------------|
| Conceptualization           | [CREDIT_00000001](http://purl.org/credit/ontology#CREDIT_00000001)          |
| Data Curation               | [CREDIT_00000002](http://purl.org/credit/ontology#CREDIT_00000002)          |
| Formal Analysis             | [CREDIT_00000003](http://purl.org/credit/ontology#CREDIT_00000003)          |
| Funding Acquisition         | [CREDIT_00000004](http://purl.org/credit/ontology#CREDIT_00000004)          |
| Methodology                 | [CREDIT_00000006](http://purl.org/credit/ontology#CREDIT_00000006)          |
| Software                    | [CREDIT_00000009](http://purl.org/credit/ontology#CREDIT_00000009)          |
| Supervision                 | [CREDIT_00000010](http://purl.org/credit/ontology#CREDIT_00000010)          |
| Writing – Original Draft    | [CREDIT_00000013](http://purl.org/credit/ontology#CREDIT_00000013)          |
| Writing – Review & Editing  | [CREDIT_00000014](http://purl.org/credit/ontology#CREDIT_00000014)          |

> For a complete list, visit: [http://purl.org/credit/ontology](http://purl.org/credit/ontology)

---

## Next Steps

To begin using contributor roles in FAIR²:

1. Review the [Getting Started Guide](../getting-started.md)
2. Examine the [FAIR² Schema](../specification/schema.md) for contribution properties
3. Validate contributor metadata using [SHACL rules](../specification/shacl-validation.md)
4. Join ongoing discussions on extending role support via [GitHub Issues](https://github.com/fair-squared/fair2-spec/issues)

For contribution-related inquiries or suggestions, please contact:  
📩 [feedback@fair2.ai](mailto:feedback@fair2.ai)

---

_Last updated: 2025-03-14_
