# FAIR² Specification

Welcome to the official documentation for **FAIR² (FAIR Squared)** — the metadata specification that advances the FAIR principles for datasets requiring context-rich, AI-ready, and responsible reuse.

FAIR² makes datasets not only **Findable, Accessible, Interoperable, and Reusable**, but also:

- **Machine-Actionable** — compatible with automated workflows
- **Provenance-Aware** — enriched with structured provenance and processing trails
- **Responsibly Governed** — aligned with ethical, legal, and licensing requirements for AI use

## What is FAIR²?

**FAIR²** is a community-driven specification designed to meet the needs of modern research, government, and industry data ecosystems. It:

- Structures metadata to be **useful in ML/AI workflows**
- Supports **automated compliance checks**, access gating, and responsible reuse
- Includes support for **computable licenses and policies** using ODRL
- Extends **Schema.org** and aligns with **DCAT**, **DataCite**, and **ODPS**

## Key Features

- **Context-Rich Metadata**: Capture details on data generation, cleaning, validation, and ethical limitations
- **AI-Ready Design**: Optimized for ML workflows, including descriptor integration and method linking
- **Responsible AI Alignment**: Support for auditability, access control, and consent via access levels and policy layers
- **Standard Compatibility**: Works with [ML Croissant](https://mlcommons.org/croissant/), [Schema.org](https://schema.org/), and other [GO FAIR](https://www.go-fair.org/) supported standards

## Core Concepts

FAIR² defines:

- **Dataset Shapes**: Metadata templates extending `schema:Dataset` with domain- and use-specific descriptors
- **Method Structures**: Stepwise, provenance-aware method documentation (e.g., for computational workflows)
- **Agreement Levels**: A 4-tier access control framework (Open → Secure) linked to machine-readable policies
- **Provenance Trails**: Link datasets, methods, tools, and people via `prov:wasGeneratedBy`, `prov:used`, etc.

## How to Use This Documentation

Browse the documentation sections:

- 📖 **[Specification](specification/)**: Detailed field definitions and reference models
- 🧩 **[Integration Guides](integration/)**: Interoperability with standards like Schema.org, ODPS, and ML Croissant
- ⚖️ **[Access & Policies](specification/access-agreements/)**: Using agreement levels and ODRL policies
- 👥 **[Community](community/)**: Contribution guide, governance, and roadmap

## Try It

To see examples of FAIR² metadata in use:
- View annotated JSON-LD examples in the [technical](technical/) section
- Try a FAIR² metadata template with live schema validation (coming soon)

## Get Involved

FAIR² is developed by the **FAIR² Alliance**, a neutral and open community.

- Join working groups
- Propose a pilot dataset
- License the specification for certification or education

For contributions, see [Contributing](community/contributing.md).

## Roadmap

Development of FAIR² is guided by both technical milestones and community feedback. For planned features and release targets, see the [Roadmap](community/roadmap.md).

---

For additional information and technical resources, please explore the full documentation via the navigation menu or the links above.


Prompt:

Update this index to accordingly