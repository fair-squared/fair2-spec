# FAIR²: An Open Specification for AI-Ready, Responsible, and Reusable Datasets

## Executive Summary

FAIR² (FAIR Squared) is an open, community-governed specification that extends the FAIR principles with AI-readiness, context-rich metadata, and responsible data practices. Developed in collaboration with Frontiers and Senscience, and governed by the FAIR² Alliance, it enables the certification of datasets that are not only Findable, Accessible, Interoperable, and Reusable, but also interpretable by AI systems and aligned with responsible research norms.

This white paper outlines the rationale, architecture, and governance model of FAIR², illustrating how it supports dataset certification, interoperability with existing standards (Schema.org, ML-Schema, PROV-O), and practical implementation with SHACL validation and structured examples.

⸻

## 1. Introduction and Motivation

As AI becomes central to research workflows, datasets must be more than just FAIR. They must be semantically structured, computationally actionable, ethically documented, and responsibly shared. Current metadata standards fall short in encoding methods, provenance, and contextual boundaries essential for responsible AI reuse.

FAIR² addresses this by introducing a layered specification for AI-ready data certification, combining schema.org-based metadata, method representations, responsible AI descriptors, and access agreements.

! Experience with heterogeneous data, having detailed prov, context - we know the needs, to combine/integrate datasets 
! make it validatable ?
! use of data not only within domains, but also between domains - to share and reuse across communities 
! by humans and machines - not only computable with the context, meaningful to reuse the data
(common computable representation of data, that providees the substrate for integrating data within and across domains)
! Tha it is extensible, we can support multiple domain specific vocabularies

⸻

## 2. Positioning FAIR² Within the Metadata Ecosystem

FAIR² is not a replacement, but an extension: ! intentionally chose to start with something that fits the requirements, a complete/rich model for computable/human readable of data, in all forms, all domains 
(all data in all domains, not only scientific, require this level of detail to produce meaninful analysis, reuse, etc.)

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
	•	Optional inclusion of rai: metadata for intended use, bias, and restrictions
	•	Emphasis on ethical, transparent, and pseudonymized data use


⸻

## 4. Specification Components

### 4.1 Controlled Terms
	•	FAIR² builds on well-established controlled vocabularies and ontologies:
        -   Schema.org for core metadata types like Dataset, Person, and Distribution
        -   PROV-O for provenance modeling (prov:agent, prov:hadRole)
        -   CRediT/CRO for contributor roles, extended with FAIR²-specific terms where necessary
        -   QUDT for physical units and quantity kinds
        -   Dublin Core (DCT) and DCAT for access rights and catalog metadata
        -   RAI (Responsible AI) concepts for future bias and intent modeling
	•	Available in JSON-LD and Turtle formats via the FAIR² GitHub repository
	•	FAIR²-specific terms are provided through the FAIR² Ontology (fair2: namespace)

### 4.2 Schema
	•	Shapes cover minimum compliance and certification tiers
	•	Tools are available in the fair-square/fair2py GitHub repository to validate FAIR² datasets

### 4.3 Validation and Shapes
	•	SHACL validation using JSON-LD

⸻

## 5. Certification and Governance

FAIR² certification involves:
	•	SHACL validation of metadata
	•	Alignment with AI-readiness and responsible reuse
	•	Optional AI agent evaluation (e.g., Senscience)
    Agreement levels (1–4) with clear reuse conditions

⸻

## 6. Implementation Example

The borja2025.json metadata file illustrates FAIR² compliance:
	•	AI-ready structure with distribution descriptions
	•	Method and provenance encoding
	•	Contributor roles using CRO and FAIR² terms
	•	Open access agreement (Level 1)

See: Specification Example Walkthrough
-- fair2.py mention github repo and tools, maybe code block example

⸻


## 7. Road map

what is the plan, dates, links, community ..


## 8. References

(Placeholder for Wilkinson et al., Schema.org, PROV-O, ML Croissant, ODPS, etc.)