# FAIR² and CRediT Integration

## 🎯 Overview

FAIR² integrates **CRediT (Contributor Roles Taxonomy)** to **attribute dataset contributions** transparently.  
This ensures that **researchers, curators, and developers receive proper recognition**.

---

## 📌 **How FAIR² Uses CRediT**
CRediT enables **structured contributor roles** in FAIR² metadata.
| **FAIR² Property** | **CRediT Mapping** | **Description** |
|-----------------|----------------|----------------|
| `schema:contribution` | `credit:Role` | Lists **contributions** using agents and assigns `schema:hadRole` properties that link to `credit:Role` instances. |

---

## 🧩 **Integrating Contributor Role Ontology (CRO)**

FAIR² also supports the **Contributor Role Ontology (CRO)** for more semantically structured roles. This allows for ontology-based reasoning and provenance tracking.

### Ontology Mapping

The following ontology mapping provides a structured approach to integrating CRediT and CRO roles:

```json
{
  "@graph": [
    {
      "@id": "fair2:Contributor",
      "@type": "rdfs:Class",
      "rdfs:label": "Contributor",
      "rdfs:comment": "An individual or entity that contributed to the dataset, supporting both CRediT and CRO roles."
    },
    {
      "@id": "schema:hasRole",
      "@type": "rdf:Property",
      "rdfs:label": "Has Role",
      "rdfs:comment": "Links a contributor to their role in the dataset, supporting both CRediT and CRO terms.",
      "rdfs:domain": "fair2:Contributor",
      "rdfs:range": ["credit:Role", "cro:CRO_0000001"]
    },
    {
      "@id": "credit:Role",
      "@type": "rdfs:Class",
      "rdfs:label": "CRediT Role",
      "rdfs:comment": "Contributor role based on the CRediT taxonomy."
    },
    {
      "@id": "cro:CRO_0000001",
      "@type": "rdfs:Class",
      "rdfs:label": "Contributor Role",
      "rdfs:comment": "Top-level contributor role in the Contributor Role Ontology (CRO)."
    },
    {
      "@id": "fair2:roleMapping",
      "@type": "rdf:Property",
      "rdfs:label": "Role Mapping",
      "rdfs:comment": "Provides a mapping between CRediT roles and equivalent CRO roles.",
      "rdfs:domain": "credit:Role",
      "rdfs:range": "cro:CRO_0000001"
    }
  ]
}
```

---

## 🔍 **Example: JSON-LD with CRediT and CRO**
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
      "schema:hasRole": {
        "@id": "https://credit.niso.org/contributor-roles/conceptualization/",
        "rdfs:label": "Conceptualization"
      }
    },
    {
      "@type": "Person",
      "name": "John Doe",
      "schema:hasRole": {
        "@id": "https://credit.niso.org/contributor-roles/data-curation/",
        "rdfs:label": "Data Curation"
      }
    },
    {
      "@type": "Person",
      "name": "Dr. Emily Johnson",
      "schema:hasRole": {
        "@id": "http://purl.obolibrary.org/obo/CRO_0000003",
        "rdfs:label": "figure development role"
      }
    }
  ]
} 
```

## **Defining SHACL Constraints for Contributor Roles**

Using SHACL constraints, we to ensure that the property `schema:hasRole` has a node of type/class `cro:0000000` (contributor role) or `credit:Role`.
 *
 * The constraints are defined as follows:
  - The `sh:property` constraint specifies that the `schema:hasRole` property must have values that conform to the specified node shape.
  - The `sh:or` constraint is used to allow for multiple possible types/classes for the `schema:hasRole` property.
  - The `sh:class` constraint within the `sh:or` block ensures that the value of `schema:hasRole` is either of type `cro:0000000` or `credit:Role`.


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
            "sh:description": "Each contribution must have at least one role.",
            "sh:or": [
                {
                    "sh:class": "cro:CRO_0000001"
                },
                {
                    "sh:class": "credit:Role"
                }
            ]
        },
        ...
    ]
}
```