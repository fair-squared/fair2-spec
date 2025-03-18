# FAIR² and CRO Integration

## 🎯 Overview

FAIR² integrates the **Contributor Role Ontology (CRO)** to **attribute dataset contributions** transparently.  
This ensures that **researchers, curators, and developers receive proper recognition**.

---

## 📌 **How FAIR² Uses CRO**
CRO enables **structured contributor roles** in FAIR² metadata.

| **FAIR² Property** | **CRO Mapping** | **Description** |
|-----------------|----------------|----------------|
| `schema:contribution` | `cro:ContributorRole` | Lists **contributions** using agents and assigns `prov:hadRole` properties that link to `cro:ContributorRole` instances. |

---

## 🧩 **Integrating Contributor Role Ontology (CRO)**

FAIR² supports the **Contributor Role Ontology (CRO)** for semantically structured roles. This allows for ontology-based reasoning and provenance tracking.

### Ontology Mapping

The following ontology mapping provides a structured approach to integrating CRO roles:

```json
{
  "@graph": [
    {
      "@id": "schema:Person",
      "@type": "rdfs:Class",
      "rdfs:label": "Person",
      "rdfs:comment": "An individual or entity that contributed to the dataset, supporting CRO roles."
    },
    {
      "@id": "prov:hasRole",
      "@type": "rdf:Property",
      "rdfs:label": "Has Role",
      "rdfs:comment": "Links a contributor to their role in the dataset, supporting CRO terms.",
      "rdfs:domain": "schema:Person",
      "rdfs:range": "cro:0000001"
    },
    {
      "@id": "cro:0000001",
      "@type": "rdfs:Class",
      "rdfs:label": "Contributor Role",
      "rdfs:comment": "Top-level contributor role in the Contributor Role Ontology (CRO)."
    }
  ]
}
```

---

## 🔍 **Example: JSON-LD with CRO**
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
    },
    {
      "@type": "Person",
      "name": "Dr. Emily Johnson",
      "prov:hadRole": {
        "@id": "http://purl.obolibrary.org/obo/CRO_0000003",
        "rdfs:label": "Figure Development Role"
      }
    }
  ]
}
```

## **Defining SHACL Constraints for Contributor Roles**

Using SHACL constraints, we ensure that the property `prov:hadRole` has a node of type/class `cro:ContributorRole`.

The constraints are defined as follows:
- The `sh:property` constraint specifies that the `prov:hadRole` property must have values that conform to the specified node shape.
- The `sh:or` constraint is used to allow for multiple possible types/classes for the `prov:hadRole` property.
- The `sh:class` constraint within the `sh:or` block ensures that the value of `prov:hadRole` is of type `cro:ContributorRole`.

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
        }
      ]
    }
  ]
}
```

---

## 🔗 **CRO and CRediT Taxonomy**

The **Contributor Role Ontology (CRO)** integrates the **CRediT taxonomy**, providing a structured and standardized way to **assign contributor roles** in scientific and computational research. This integration ensures that **roles defined in CRediT are fully compatible with CRO**, enabling a **FAIR** approach to contributor recognition.

### 📌 **What is the CRediT Taxonomy?**
The **CRediT (Contributor Roles Taxonomy)** defines specific roles that contributors can have in a research project, ensuring precise attribution.
Each role has a **persistent identifier (PURL) in CRO**, allowing for **machine-readable metadata and interoperability**.

---

## 🔗 **CRO and CRediT Taxonomy**

The **Contributor Role Ontology (CRO)** integrates the **CRediT taxonomy**, providing a structured and standardized way to **assign contributor roles** in scientific and computational research. This integration ensures that **roles defined in CRediT are fully compatible with CRO**, enabling a **FAIR** approach to contributor recognition.

### 📌 **What is the CRediT Taxonomy?**
The **CRediT (Contributor Roles Taxonomy)** defines specific roles that contributors can have in a research project, ensuring precise attribution.
Each role has a **persistent identifier (PURL) in CRO**, allowing for **machine-readable metadata and interoperability**.

---

## 🔍 **CRO IDs for CRediT Roles**
Below are examples of **CRO URIs** for CRediT contributor roles:

| **Role**                 | **CRO ID (PURL)**                          |
|--------------------------|-----------------------------------------|
| Conceptualization       | [http://purl.org/credit/ontology#CREDIT_00000001](http://purl.org/credit/ontology#CREDIT_00000001) |
| Data Curation           | [http://purl.org/credit/ontology#CREDIT_00000002](http://purl.org/credit/ontology#CREDIT_00000002) |
| Formal Analysis         | [http://purl.org/credit/ontology#CREDIT_00000003](http://purl.org/credit/ontology#CREDIT_00000003) |
| Funding Acquisition     | [http://purl.org/credit/ontology#CREDIT_00000004](http://purl.org/credit/ontology#CREDIT_00000004) |
| Investigation           | [http://purl.org/credit/ontology#CREDIT_00000005](http://purl.org/credit/ontology#CREDIT_00000005) |
| Methodology             | [http://purl.org/credit/ontology#CREDIT_00000006](http://purl.org/credit/ontology#CREDIT_00000006) |
| Project Administration  | [http://purl.org/credit/ontology#CREDIT_00000007](http://purl.org/credit/ontology#CREDIT_00000007) |
| Resources              | [http://purl.org/credit/ontology#CREDIT_00000008](http://purl.org/credit/ontology#CREDIT_00000008) |
| Software               | [http://purl.org/credit/ontology#CREDIT_00000009](http://purl.org/credit/ontology#CREDIT_00000009) |
| Supervision            | [http://purl.org/credit/ontology#CREDIT_00000010](http://purl.org/credit/ontology#CREDIT_00000010) |
| Validation             | [http://purl.org/credit/ontology#CREDIT_00000011](http://purl.org/credit/ontology#CREDIT_00000011) |
| Visualization          | [http://purl.org/credit/ontology#CREDIT_00000012](http://purl.org/credit/ontology#CREDIT_00000012) |
| Writing – Original Draft | [http://purl.org/credit/ontology#CREDIT_00000013](http://purl.org/credit/ontology#CREDIT_00000013) |
| Writing – Review & Editing | [http://purl.org/credit/ontology#CREDIT_00000014](http://purl.org/credit/ontology#CREDIT_00000014) |

For a **full list of CRediT roles in CRO**, visit: [http://purl.org/credit/ontology](http://purl.org/credit/ontology)

---

## 🚀 **Next Steps**
To start using FAIR² with CRO:
1. Read the [Getting Started Guide](../getting-started.md).
2. Explore the [FAIR² Schema](../specification/schema.md).
3. Check out [Example Datasets](../specification/examples.md).
4. Learn about [Responsible AI](../specification/responsible-ai.md).

Want to contribute? See [Contributing](../community/contributing.md).

---
_Last updated: [03/14/2025]_