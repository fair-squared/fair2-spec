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
| `fair2:DataArticle` | DataArticle | Scholarly article describing and linking an open dataset with methods and reuse guidance. | `schema:ScholarlyArticle` |
| `fair2:DataPortal` | DataPortal | An authored, versioned web application presenting a single FAIR² dataset — an interactive explorer or landing site, not a catalogue and not a bare API endpoint. | `schema:CreativeWork` |
| `fair2:DataArchive` | DataArchive | A long-term archive or repository that preserves the dataset. | `schema:CreativeWork` |
| `fair2:Section` | Section | Structured methodology section grouping procedural steps. | `schema:HowToSection` |
| `fair2:MethodSection` | MethodSection | Legacy alias for `fair2:Section`; retained for backward compatibility. | `schema:HowToSection` |
| `fair2:Step` | Step | Atomic procedural instruction within a method. | `schema:HowToStep` |
| `fair2:Substep` | Substep | Subordinate procedural instruction nested under a Step. | `schema:HowToStep` |
| `fair2:AuthorRole` | AuthorRole | Role played by an author in producing the dataset (e.g. Corresponding Author). | `schema:Role` |
| `fair2:ContributorRole` | ContributorRole | Contributor role drawn from CRediT/CRO vocabularies. | `schema:Role` |
| `fair2:DescriptiveStatistics` | DescriptiveStatistics | Summary statistics computed over a RecordSet or Dataset. | `schema:Dataset` |
| `fair2:Submission` | Submission | Submission package that groups dataset, article, and supporting materials for review. | `schema:CreativeWork` |
| `fair2:Certification` | Certification | Pointer node asserting the FAIR² certification or validation status of a package, and referencing the external credential. | `schema:CreativeWork` |
| `fair2:StepCase` | StepCase | Conditional branch within a method, carrying the condition and the path taken when it holds. Sits in the same fair2:step list as a Step. | `schema:HowToStep` |
| `fair2:ComplianceLevel` | ComplianceLevel | A FAIR² compliance status asserted for a package. | `skos:Concept` |
| `fair2:CertificationScope` | CertificationScope | A facet of a package that a certification covers. | `skos:Concept` |

---

## Properties

The FAIR² properties define relationships between datasets, methods, contributors, and derived artifacts. They support semantic traceability and alignment with FAIR data and Responsible AI requirements.

| `@id` | `rdfs:label` | `rdfs:comment` |
|:------|:--------------|:----------------|
| `fair2:attachment` | attachment | Points to a supporting file or supplemental material. |
| `fair2:bugFixes` | bugFixes | Bug-fix entries on a changelog `UpdateAction`. |
| `fair2:citationKey` | citationKey | Short citation key identifying the dataset. |
| `fair2:dataArchive` | dataArchive | Links a dataset to the archive that preserves it. |
| `fair2:dataArticle` | dataArticle | Links a dataset or submission to its associated scholarly data article. |
| `fair2:dataPortal` | dataPortal | Links a dataset to the portal that hosts and serves it. |
| `fair2:dataset` | dataset | References the dataset resource associated with the entity. |
| `fair2:domain` | domain | Subject-domain classification of the dataset (e.g. a Wikidata concept). |
| `fair2:generated` | generated | Links a method step to the RecordSet fields or artifacts it produced (lineage). |
| `fair2:improvements` | improvements | Improvement entries on a changelog `UpdateAction`. |
| `fair2:isExperimentRelated` | isExperimentRelated | Flags whether a field relates to experimental data. |
| `fair2:manuscript` | manuscript | References a manuscript file associated with the submission. |
| `fair2:methodSection` | methodSection | Links a dataset to its methodology section(s). |
| `fair2:newFeatures` | newFeatures | New-feature entries on a changelog `UpdateAction`. |
| `fair2:next` | next | Orders sequential method sections, steps, or substeps. |
| `fair2:nextTrue` | nextTrue | Conditional branch target taken when a StepCase condition holds. |
| `fair2:otherInformation` | otherInformation | Miscellaneous notes on a changelog `UpdateAction`. |
| `fair2:qualifiedUsage` | qualifiedUsage | Condition guarding a conditional method step (StepCase). |
| `fair2:statistics` | statistics | Links to computed descriptive statistics. |
| `fair2:step` | step | Connects a Section with its constituent Step items. |
| `fair2:store` | store | Indicates the storage location or repository endpoint for an asset. |
| `fair2:substep` | substep | Connects a Step with its constituent Substep items. |
| `fair2:unit` | unit | Unit of measurement for a field or variable. |

| `fair2:certificationDocument` | certificationDocument | Reference to the external credential document backing the certification. |
| `fair2:certificationScope` | certificationScope | What the certification covers (e.g. metadataConformance, dataIntegrity). |
| `fair2:certifiedBy` | certifiedBy | The organisation issuing the certification. |
| `fair2:changeLog` | changeLog | Record of updates made to a dataset, article, archive or portal. |
| `fair2:dateIssued` | dateIssued | Date the certification was issued. |
| `fair2:fair2ComplianceLevel` | fair2ComplianceLevel | The FAIR² compliance level asserted for the package. |
| `fair2:verificationEndpoint` | verificationEndpoint | Endpoint at which the certification can be verified. |
| `fair2:validationReport` | validationReport | The validation report backing a certification or validation claim. |
| `fair2:fundingScheme` | fundingScheme | The funding programme a grant was awarded under. |
| `fair2:metadataVersion` | metadataVersion | Version of the `fair2.json` document itself, independent of the dataset's `version`. |
| `fair2:metadataModified` | metadataModified | Date the `fair2.json` document was last edited. |
| `fair2:position` | position | Ordinal position of an agent in the author list, counting from 1. |
| `fair2:graphDigestMultibase` | graphDigestMultibase | Multihash of a `fair2.json`'s RDFC-1.0 canonical graph, companion to `sec:digestMultibase` over its bytes. |
---

---

---

## Certification vocabulary

Two small controlled vocabularies. The compliance level says **who vouches**;
the scope says **what was checked** — there is no metadata-only level.

| Individual | Type | Meaning |
|:-----------|:-----|:--------|
| `fair2:Certified` | `fair2:ComplianceLevel` | An authority assertion, backed by a credential signed by an authorised certifier. |
| `fair2:Validated` | `fair2:ComplianceLevel` | A quality status: the automated checks pass. Self-assertable, provided the claim carries its evidence. |
| `fair2:MetadataConformance` | `fair2:CertificationScope` | The metadata conforms to the declared FAIR² profile. |
| `fair2:DataIntegrity` | `fair2:CertificationScope` | The data files were retrieved and checked against their digests. |
| `fair2:LicenseVerification` | `fair2:CertificationScope` | The declared licence was checked. |
| `fair2:ProcessAttestation` | `fair2:CertificationScope` | The production process was attested by the certifier. |
| `fair2:TemporalProof` | `fair2:CertificationScope` | An RFC 3161 timestamp or blockchain anchor is attached. |

A certification whose scope omits `dataIntegrity` MUST be rendered as
**“FAIR²-Certified (metadata only)”**. That is a requirement on consumers —
SHACL can check the scope tokens, but not how they are displayed.


## Reserved terms

These four are declared so that existing documents keep resolving, but they
have no shape, no example and no stated domain or range. Other unused terms
have been removed; these are retained because the FAIR² specification has
published them as reserved. They carry
`vs:term_status "unstable"` in the ontology. **Consumers should not rely on
them, and producers should not emit them**, until they are specified.

| Term | Intended meaning |
|:-----|:-----------------|
| `fair2:Submission` | A submission package grouping dataset, article and supporting materials for review. Whether it ever appears in a *published* `fair2.json`, as opposed to a pre-publication review package, is not yet decided. |
| `fair2:manuscript` | Reference to a manuscript file in a submission package. |
| `fair2:attachment` | Reference to supplemental material in a submission package. |
| `fair2:store` | Storage location or repository endpoint for an asset. Its relationship to `schema:contentUrl` on a `FileObject` and to `fair2:dataArchive` is undefined. |


## Notes

- Each property and class is compatible with JSON-LD serialization and SHACL validation.
- The `fair2s:` namespace hosts corresponding SHACL shape definitions for data validation.
- The ontology is designed for seamless integration with ML Schema, Croissant, and PROV-O provenance structures.
