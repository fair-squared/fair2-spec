# FAIR² Specification

Welcome to the documentation for **FAIR² (FAIR Squared)**—a metadata specification that extends the FAIR principles to support context-rich, AI-ready, and ethically aligned datasets. This specification is designed to make datasets not only **Findable, Accessible, Interoperable, and Reusable**, but also **machine-actionable**, **provenance-aware**, and aligned with **Responsible AI** practices.

## About FAIR²

**FAIR²** builds upon the original FAIR principles with a focus on:

- **Context-Rich Metadata**  
  Capturing detailed information about how datasets are created, processed, and validated, supporting reproducibility and transparency.

- **AI-Ready Compatibility**  
  Structuring data for direct usability in modern AI and machine learning pipelines, including integration with formats like [ML Croissant](https://mlcommons.org/croissant/).

- **Responsible AI Alignment**  
  Incorporating ethical oversight, documentation of potential biases, data limitations, and transparent decision-making processes.

FAIR² is designed for interoperability and ecosystem alignment. It is fully compatible with:

- [ML Croissant](https://mlcommons.org/croissant/), a standard for AI-ready dataset packaging
- [Schema.org](https://schema.org/) for structured data interoperability
- [GO FAIR](https://www.go-fair.org/), a global initiative for FAIR data practices
- SHACL shapes for schema validation and compliance

---

## Getting Started

To begin working with FAIR²:

1. Review the [Getting Started Guide](getting-started.md)
2. Understand the [FAIR² Schema](specification/schema.md)
3. Learn how to validate your data using [SHACL Shapes](specification/shacl-validation.md)
4. Explore [Example Datasets](examples/example-1/data.json)

---

## Documentation Structure

The FAIR² documentation is organized into the following sections:

### Core Specification

- **[Overview](specification/overview.md)**  
  Introduction to the core principles, design goals, and scope of FAIR².

- **[Method Representation](specification/methods.md)**  
  Structured method encoding using `schema:HowToStep` and compatible extensions for machine-actionable protocols.

- **[SHACL Validation](specification/shacl-validation.md)**  
  Shape definitions and compliance rules for automated dataset validation.

### Interoperability and Alignment

- **[ML Croissant Integration](integration/ml-croissant.md)**  
  Guidance on aligning FAIR² packages with Croissant-compliant AI workflows.

- **[Croissant RAI Vocabulary](integration/croissant-rai.md)**  
  Documentation of how FAIR² integrates ethical reviews, limitations, and responsible AI principles.

- **[PROV-O Integration](integration/prov-o.md)**  
  Provenance modeling and how FAIR² supports `prov:Activity`, `prov:Agent`, and `prov:Entity` linkages.

- **[QUDT and Units](integration/qudt.md)**  
  Use of standard unit vocabularies such as QUDT and OM for quantitative fields.

- **[CRediT Roles](integration/credit.md)**  
  Mapping contributor roles using the Contributor Role Ontology for scholarly publishing and metadata.

### Technical Reference

- **[JSON-LD and RDF Considerations](technical/json-ld.md)**  
  Detailed notes on how FAIR² implements linked data using JSON-LD, including context definitions and namespace management.

### Community and Governance

- **[Contributing Guidelines](community/contributing.md)**  
  How to contribute to FAIR², participate in specification development, and propose extensions.

- **[Governance and Roadmap](community/roadmap.md)**  
  Information on the FAIR² Alliance, release strategy, and plans for certification and adoption.

---

## Community Involvement

FAIR² is a community-driven specification. Contributions from the broader FAIR, AI, and data stewardship communities are encouraged. Please see the [Contributing Guide](community/contributing.md) to get involved.

---

## Roadmap

Development of FAIR² is guided by both technical milestones and community feedback. For planned features and release targets, see the [Roadmap](community/roadmap.md).

---

For additional information and technical resources, please explore the full documentation via the navigation menu or the links above.