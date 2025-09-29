# FAIR²: An Open Specification for AI-Ready, Responsible, and Reusable Research Data

## Executive Summary

FAIR² (FAIR Squared) is an open, community-governed specification that extends the FAIR principles with AI-readiness, context-rich metadata, and responsible data practices. Developed in collaboration with Frontiers and Senscience, and governed by the FAIR² Alliance, it enables the certification of datasets that are not only Findable, Accessible, Interoperable, and Reusable, but also interpretable by AI systems and aligned with responsible research norms.

This white paper outlines the rationale, architecture, and governance model of FAIR², illustrating how it supports dataset certification, interoperability with existing standards (Schema.org, ML-Schema, PROV-O), and practical implementation with SHACL validation and structured examples.

⸻

## 1. Introduction and Motivation

As AI becomes central to research workflows, datasets must be more than just FAIR. They must be semantically structured, computationally actionable, ethically documented, and responsibly shared. Current metadata standards fall short in encoding methods, provenance, and contextual boundaries essential for responsible AI reuse.

FAIR² addresses this by introducing a layered specification for AI-ready data certification, combining schema.org-based metadata, method representations, responsible AI descriptors, and access agreements.

⸻

## 2. Positioning FAIR² Within the Metadata Ecosystem

FAIR² is not a replacement, but an extension:
	•	Builds on the FAIR Principles (Wilkinson et al.)
	•	Implements ML-Schema/Croissant for structured data
	•	Uses Schema.org as a base vocabulary
	•	Incorporates PROV-O and CRediT/CRO for provenance and roles
	•	Aligns with GO FAIR, RDA, ODPS, and Responsible AI initiatives (e.g. MLCommons RAI)

FAIR² also introduces its own terms (fair2: namespace), SHACL shapes for compliance, and a certification process governed by a neutral body.

⸻

## 3. Core Principles of FAIR²

### 3.1 Context-Rich Metadata
	•	Extension of open, well-known, and widely adopted standards (Schema.org, PROV-O, ML-Schema)
	•	Structured methods with HowToStep and HowToSection
	•	Contributor roles with prov:hadRole using CRO or FAIR² URIs
	•	Temporal and spatial coverage using Google Rich Results
	•	Terms of use defined through accessRights and FAIR² Agreement Levels

### 3.2 AI-Ready Design
	•	Consistent use of controlled vocabularies
	•	SHACL-based validation
	•	Metadata templates for Croissant, Hugging Face, and Google SD

### 3.3 Responsible AI Alignment
	•	Agreement levels (1–4) with clear reuse conditions
	•	Optional inclusion of rai: metadata for intended use, bias, and restrictions
	•	Emphasis on ethical, transparent, and pseudonymized data use

⸻

## 4. Specification Components

### 4.2 Controlled Terms
	•	FAIR² builds on well-established controlled vocabularies and ontologies:
        -   Schema.org for core metadata types like Dataset, Person, and Distribution
        -   PROV-O for provenance modeling (prov:agent, prov:hadRole)
        -   CRediT/CRO for contributor roles, extended with FAIR²-specific terms where necessary
        -   QUDT for physical units and quantity kinds
        -   Dublin Core (DCT) and DCAT for access rights and catalog metadata
        -   RAI (Responsible AI) concepts for future bias and intent modeling
	•	Available in JSON-LD and Turtle formats via the FAIR² GitHub repository
	•	FAIR²-specific terms are provided through the FAIR² Ontology (fair2: namespace)

### 4.3 Validation and Shapes
	•	SHACL validation using JSON-LD
	•	Shapes cover minimum compliance and certification tiers
	•	Tools are available in the fair-square/fair2py GitHub repository to validate FAIR² datasets

⸻

## 5. Certification and Governance

FAIR² certification involves:
	•	SHACL validation of metadata
	•	Alignment with AI-readiness and responsible reuse
	•	Optional AI agent evaluation (e.g., Senscience)

⸻

## 6. Implementation Example

The borja2025.json metadata file illustrates FAIR² compliance:
	•	AI-ready structure with distribution descriptions
	•	Method and provenance encoding
	•	Contributor roles using CRO and FAIR² terms
	•	Open access agreement (Level 1)

See: Specification Example Walkthrough

⸻

## 7. References

(Placeholder for Wilkinson et al., Schema.org, PROV-O, ML Croissant, ODPS, etc.)