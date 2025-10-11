# FAIR² Ontology

## Overview

The FAIR² Ontology defines the core semantic entities and relations used across FAIR² metadata and datasets. It provides a structured, machine-readable vocabulary that ensures interoperability between data, methods, and publications within the FAIR² ecosystem. The ontology reuses existing standards from [Schema.org](https://schema.org/), [PROV-O](https://www.w3.org/TR/prov-o/), and the [Contributor Role Ontology (CRO)](https://credit.niso.org/contributor-roles/), while extending them with specific terms for AI-ready data curation and Responsible AI alignment.

The ontology is expressed in both JSON-LD and Turtle formats and is compatible with SHACL validation shapes defined under the `fair2s:` namespace.

---

## Namespaces

| Prefix | Namespace URI |
|:-------|:---------------|
| `schema:` | https://schema.org/ |
| `prov:` | http://www.w3.org/ns/prov# |
| `cr:` | https://credit.niso.org/contributor-roles/ |
| `fair2:` | https://fair2.ai/ns/ |
| `fair2s:` | https://fair2.ai/shapes/ |
| `rdfs:` | http://www.w3.org/2000/01/rdf-schema# |
| `rdf:` | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| `xsd:` | http://www.w3.org/2001/XMLSchema# |

---

## Classes

The following classes define the core conceptual entities in FAIR². Each class extends a compatible Schema.org or PROV-O superclass to ensure semantic interoperability.

| `@id` | `rdfs:label` | `rdfs:comment` | `rdfs:subClassOf` |
|:------|:--------------|:----------------|:------------------|
| `fair2:OpenDataArticle` | OpenDataArticle | Scholarly work describing and linking an open dataset with methods and reuse guidance. | `schema:ScholarlyArticle` |
| `fair2:MethodSection` | MethodSection | Structured section grouping procedural steps for a method. | `schema:HowToSection` |
| `fair2:Step` | Step | Atomic procedural instruction within a method. | `schema:HowToStep` |
| `fair2:Substep` | Substep | Subordinate procedural instruction nested under a Step. | `schema:HowToStep` |
| `fair2:RecordSet` | RecordSet | A coherent subset of a dataset used for analysis or curation. | `schema:Dataset` |
| `fair2:Visualization` | Visualization | A visual artifact (plot, figure, dashboard) derived from the dataset. | `schema:CreativeWork` |
| `fair2:DescriptiveStatistics` | DescriptiveStatistics | Summary statistics computed over a RecordSet or Dataset. | `schema:Dataset` |
| `fair2:Submission` | Submission | Submission package that groups dataset, article, and supporting materials for review. | `schema:CreativeWork` |

---

## Properties

The FAIR² properties define relationships between datasets, methods, contributors, and derived artifacts. They support semantic traceability and alignment with FAIR data and Responsible AI requirements.

| `@id` | `rdfs:label` | `rdfs:comment` |
|:------|:--------------|:----------------|
| `fair2:activities` | activities | Groups workflow or provenance activities related to an entity. |
| `fair2:attachment` | attachment | Points to a supporting file or supplemental material. |
| `fair2:builds` | builds | Indicates that one artifact is built from or extends another artifact. |
| `fair2:contributorRole` | contributorRole | Links a contribution to a contributor role term. |
| `fair2:dataArticle` | dataArticle | Links a dataset or submission to its associated scholarly data article. |
| `fair2:dataset` | dataset | References the dataset resource associated with the entity. |
| `fair2:digest` | digest | Provides a short textual or hash-based digest for quick identification. |
| `fair2:manuscript` | manuscript | References a manuscript file associated with the submission. |
| `fair2:roleName` | roleName | Human-readable label for a contributor role. |
| `fair2:statistics` | statistics | Links to computed descriptive statistics. |
| `fair2:step` | step | Connects a MethodSection with its constituent Step items. |
| `fair2:store` | store | Indicates the storage location or repository endpoint for an asset. |
| `fair2:variables` | variables | Lists variable or feature definitions referenced by an analysis or record set. |
| `fair2:visualization` | visualization | Links to a visualization derived from the dataset or record set. |

---

## Notes

- Each property and class is compatible with JSON-LD serialization and SHACL validation.
- The `fair2s:` namespace hosts corresponding SHACL shape definitions for data validation.
- The ontology is designed for seamless integration with ML Schema, Croissant, and PROV-O provenance structures.
