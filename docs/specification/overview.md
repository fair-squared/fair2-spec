# FAIR² Specification Overview

## Overview

FAIR² (FAIR Squared) is an extension of the FAIR principles (Findable, Accessible, Interoperable, Reusable), designed to make datasets AI-ready, context-rich, and machine-actionable.

While the original FAIR principles emphasize data discoverability and reusability, FAIR² extends these by ensuring that datasets:

- Are natively structured for machine learning workflows
- Include rich metadata for contextual understanding and provenance
- Are validated using SHACL for interoperability and quality assurance
- Align with responsible AI principles to support transparency and ethical use
- Standardize units using QUDT for improved interpretability and consistency
- Support responsible AI metadata using the Croissant RAI vocabulary
- Enable detailed contributor attribution using CRediT (Contributor Roles Taxonomy)

FAIR² is built on top of ML Croissant to ensure compatibility with widely used metadata structures for machine learning datasets.

---

## Core Components of FAIR²

FAIR² enhances the FAIR framework with four primary components:

### 1. Context-Rich Metadata

- Provides domain-specific annotations with deeper semantic precision
- Utilizes metadata structures compatible with ML Croissant and Schema.org
- Includes comprehensive documentation of provenance, licensing, and ethical context

### 2. AI-Ready Design

- Uses JSON-LD and RDF formats for structured, machine-actionable metadata
- Defines schemas that support direct integration into ML workflows
- Enables validation with SHACL to support quality control
- Incorporates unit definitions through QUDT for interpretability

### 3. Responsible AI Alignment

- Facilitates transparency in data preparation and use
- Includes metadata for documenting biases, limitations, and ethical governance
- Enables compliance with principles of responsible and reproducible AI
- Uses Croissant RAI vocabulary for ethical metadata annotation

### 4. Contributor Attribution and Provenance Tracking

- Supports contributor roles through CRediT and CRO ontologies
- Captures dataset lineage using the PROV-O standard
- Recognizes multi-author contributions with specific roles and responsibilities

---

## Integration with ML Croissant

FAIR² extends the ML Croissant specification by:

- Adding SHACL validation to enforce metadata structure
- Introducing AI-specific metadata to describe training data and preprocessing steps
- Integrating ethical and governance-related metadata aligned with Responsible AI practices
- Supporting units via QUDT vocabulary for scientific datasets
- Tracking contributor roles using CRediT and CRO

FAIR² maintains full compatibility with ML Croissant and Schema.org for linked data interoperability.

---

## Contributor Roles: CRediT and CRO

FAIR² supports contributor role metadata using both the CRediT taxonomy and the CRO ontology.

- `credit:Role` identifiers are aligned with common publishing practices
- `cro:CRO_*` identifiers are intended for ontology-based reasoning and semantic validation

Example role usage:

- A dataset author may be annotated with:
  - `credit:WritingOriginalDraft`
  - `cro:CRO_0000039` (Writing Original Draft)

- A dataset curator may be annotated with:
  - `credit:DataCuration`
  - `cro:CRO_0000027` (Data Curation)

---

## Ontology

FAIR² defines a machine-readable ontology describing relationships between dataset components, contributors, activities, and provenance. The ontology is available in both JSON-LD and Turtle formats.

For more information, see the [Ontology Documentation](ontology.md).

---

## Technical Features

FAIR² relies on the following technologies:

- JSON-LD and RDF for structured metadata encoding
- SHACL for metadata validation
- Schema.org for semantic discoverability
- Persistent identifiers and signposting for findability

Further reading:

- [FAIR² Schema](schema.md)
- [SHACL Validation](shacl-validation.md)
- [JSON-LD & RDF](../technical/json-ld.md)

---

## Getting Started

To adopt the FAIR² specification:

1. Review the [Getting Started Guide](../getting-started.md)
2. Explore the [FAIR² Schema](schema.md)
3. Examine [A full Example Dataset](../examples/example-walkthrough.md)
4. Learn about [Responsible AI Integration](./responsible-ai.md)

To contribute to the specification or share feedback, see [Contributing](../community/contributing.md).

---

_Last updated: 2025-10-10_