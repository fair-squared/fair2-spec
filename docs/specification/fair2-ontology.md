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
| `fair2:OpenDataArticle` | OpenDataArticle | Legacy alias for `fair2:DataArticle`; retained for backward compatibility. | `schema:ScholarlyArticle` |
| `fair2:DataPortal` | DataPortal | An authored, versioned web application presenting a single FAIR² dataset — an interactive explorer or landing site, not a catalogue and not a bare API endpoint. | `schema:CreativeWork` |
| `fair2:DataArchive` | DataArchive | A long-term archive or repository that preserves the dataset. | `schema:CreativeWork` |
| `fair2:Section` | Section | Structured methodology section grouping procedural steps. | `schema:HowToSection` |
| `fair2:MethodSection` | MethodSection | Legacy alias for `fair2:Section`; retained for backward compatibility. | `schema:HowToSection` |
| `fair2:Step` | Step | Atomic procedural instruction within a method. | `schema:HowToStep` |
| `fair2:Substep` | Substep | Subordinate procedural instruction nested under a Step. | `schema:HowToStep` |
| `fair2:AuthorRole` | AuthorRole | Role played by an author in producing the dataset (e.g. Corresponding Author). | `schema:Role` |
| `fair2:ContributorRole` | ContributorRole | Contributor role drawn from CRediT/CRO vocabularies. | `schema:Role` |
| `fair2:RecordSet` | RecordSet | A coherent subset of a dataset used for analysis or curation. | `schema:Dataset` |
| `fair2:Visualization` | Visualization | A visual artifact (plot, figure, dashboard) derived from the dataset. | `schema:CreativeWork` |
| `fair2:DescriptiveStatistics` | DescriptiveStatistics | Summary statistics computed over a RecordSet or Dataset. | `schema:Dataset` |
| `fair2:Submission` | Submission | Submission package that groups dataset, article, and supporting materials for review. | `schema:CreativeWork` |
| `fair2:Audience` | Audience | Intended audience for a dataset or article. | `schema:Audience` |
| `fair2:Certification` | Certification | Pointer node asserting the FAIR² certification or validation status of a package, and referencing the external credential. | `schema:CreativeWork` |
| `fair2:ExperimentDataset` | ExperimentDataset | A dataset produced by an experiment, as distinct from an observational or derived one. Applied as an additional type alongside schema:Dataset. | `schema:Dataset` |
| `fair2:OpenDataArticleSection` | OpenDataArticleSection | A titled section of an open data article. | `schema:CreativeWork` |
| `fair2:Role` | Role | A role played by an agent in relation to a dataset or article. | `schema:Role` |
| `fair2:StepCase` | StepCase | Conditional branch within a method, carrying the condition and the path taken when it holds. Sits in the same fair2:step list as a Step. | `schema:HowToStep` |

---

## Properties

The FAIR² properties define relationships between datasets, methods, contributors, and derived artifacts. They support semantic traceability and alignment with FAIR data and Responsible AI requirements.

| `@id` | `rdfs:label` | `rdfs:comment` |
|:------|:--------------|:----------------|
| `fair2:activities` | activities | Groups workflow or provenance activities related to an entity. |
| `fair2:attachment` | attachment | Points to a supporting file or supplemental material. |
| `fair2:builds` | builds | Indicates that one artifact is built from or extends another artifact. |
| `fair2:bugFixes` | bugFixes | Bug-fix entries on a changelog `UpdateAction`. |
| `fair2:citationKey` | citationKey | Short citation key identifying the dataset. |
| `fair2:contributorRole` | contributorRole | Links a contribution to a contributor role term. |
| `fair2:dataArchive` | dataArchive | Links a dataset to the archive that preserves it. |
| `fair2:dataArticle` | dataArticle | Links a dataset or submission to its associated scholarly data article. |
| `fair2:dataPortal` | dataPortal | Links a dataset to the portal that hosts and serves it. |
| `fair2:dataset` | dataset | References the dataset resource associated with the entity. |
| `fair2:digest` | digest | Provides a short textual or hash-based digest for quick identification. |
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
| `fair2:roleName` | roleName | Human-readable label for a contributor role. |
| `fair2:statistics` | statistics | Links to computed descriptive statistics. |
| `fair2:step` | step | Connects a Section with its constituent Step items. |
| `fair2:store` | store | Indicates the storage location or repository endpoint for an asset. |
| `fair2:substep` | substep | Connects a Step with its constituent Substep items. |
| `fair2:unit` | unit | Unit of measurement for a field or variable. |
| `fair2:variables` | variables | Lists variable or feature definitions referenced by an analysis or record set. |
| `fair2:visualization` | visualization | Links to a visualization derived from the dataset or record set. |

| `fair2:certificationDocument` | certificationDocument | Reference to the external credential document backing the certification. |
| `fair2:certificationScope` | certificationScope | What the certification covers (e.g. metadata-conformance, data-integrity). |
| `fair2:certifiedBy` | certifiedBy | The organisation issuing the certification. |
| `fair2:changeLog` | changeLog | Record of updates made to a dataset, article, archive or portal. |
| `fair2:dateIssued` | dateIssued | Date the certification was issued. |
| `fair2:fair2ComplianceLevel` | fair2ComplianceLevel | The FAIR² compliance level asserted for the package. |
| `fair2:variable` | variable | A variable or feature definition referenced by an analysis or record set. Singular form of fair2:variables. |
| `fair2:verificationEndpoint` | verificationEndpoint | Endpoint at which the certification can be verified. |
| `fair2:validationReport` | validationReport | The validation report backing a certification or validation claim. |
| `fair2:fundingScheme` | fundingScheme | The funding programme a grant was awarded under. |
---

---

## Reserved terms

The following are declared so that existing documents keep resolving, but they
have no shape, no example and no stated domain or range. They carry
`vs:term_status "unstable"` in the ontology. **Consumers should not rely on
them, and producers should not emit them**, until they are specified.

| Term | Intended meaning |
|:-----|:-----------------|
| `fair2:Submission` | A submission package grouping dataset, article and supporting materials for review. Whether it ever appears in a *published* `fair2.json`, as opposed to a pre-publication review package, is not yet decided. |
| `fair2:manuscript` | Reference to a manuscript file in a submission package. |
| `fair2:attachment` | Reference to supplemental material in a submission package. |
| `fair2:store` | Storage location or repository endpoint for an asset. Its relationship to `schema:contentUrl` on a `FileObject` and to `fair2:dataArchive` is undefined. |
| `fair2:activities` | Grouping of provenance activities for an entity. |
| `fair2:builds` | Record that one artifact extends another. |
| `fair2:digest` | Short digest for quick identification. |


## Notes

- Each property and class is compatible with JSON-LD serialization and SHACL validation.
- The `fair2s:` namespace hosts corresponding SHACL shape definitions for data validation.
- The ontology is designed for seamless integration with ML Schema, Croissant, and PROV-O provenance structures.
