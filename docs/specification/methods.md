# FAIR² Method Representation

This document defines how FAIR² expresses detailed methods using structured, machine-readable JSON-LD constructs. It is fully compatible with [schema.org](https://schema.org/), [ML Croissant](https://mlcommons.org/croissant/), and the [FAIR²](https://senscience.ai/) metadata specification.

## Overview

Method descriptions in FAIR² are structured hierarchically using the following types:

- **`schema:HowToSection`** (aliased as `dv:Section`)
- **`schema:HowToStep`** (aliased as `dv:Step`)
- **`schema:HowToStep`** (aliased as `dv:Substep`)
- **`schema:HowToStep`** (aliased as `dv:StepCase`)

Each level extends or specializes the [`schema.org/HowToStep`](https://schema.org/HowToStep) pattern, enabling context-rich and modular method representation.

---

## Structure and Semantics

### Section (`dv:Section` = `schema:HowToSection`)

A major methodological unit (e.g., "Structure Prediction", "Binding Assays").

```json
{
  "@type": "HowToSection",
  "@id": "#section-structure-prediction",
  "name": "Structure Prediction",
  "steps": [ ... ]
}
```

---

### Step (`dv:Step` = `schema:HowToStep`)

Primary procedural element. Must contain `text`, and can include substeps or conditions.

```json
{
  "@type": "HowToStep",
  "@id": "#step-alphafold",
  "text": "Run AlphaFold prediction using ColabFold pipeline.",
  "substeps": [ ... ],
  "conditions": [ ... ]
}
```

---

### Substep (`dv:Substep` = `schema:HowToStep`)

A finer-grained instruction within a `Step`.

```json
{
  "@type": "HowToStep",
  "@id": "#substep-prepare-input",
  "text": "Prepare FASTA input and validate sequence."
}
```

---

### StepCase (`dv:StepCase` = `schema:HowToStep`)

Used to capture conditional logic (e.g., environment-dependent, tool-specific alternatives).

```json
{
  "@type": "HowToStep",
  "@id": "#stepcase-gpu",
  "name": "If GPU is available",
  "text": "Run full-db AlphaFold with GPU acceleration."
}
```

---

## Ontological Alignment

Each element inherits from `schema:HowToStep`, but is semantically specialized via `dv:` namespace identifiers. This ensures compatibility with:

- **schema.org-based search indexing**
- **Croissant `Method` constructs**
- **SHACL validation using RDF types**

---

## Integration with Activities

Steps may link to provenance-aware `prov:Activity` elements for detailed tracking:

```json
"wasGeneratedBy": {
  "@type": "prov:Activity",
  "type": "Prediction",
  "wasAssociatedWith": { "@type": "prov:Agent", "name": "AlphaFold v2.3" }
}
```

---

## Example JSON-LD Block

```json
{
  "@type": "HowToSection",
  "name": "Structure Prediction",
  "steps": [
    {
      "@type": "HowToStep",
      "text": "Run AlphaFold prediction.",
      "substeps": [
        { "@type": "HowToStep", "text": "Prepare FASTA sequence input." },
        { "@type": "HowToStep", "text": "Launch ColabFold and upload sequence." }
      ],
      "conditions": [
        { "@type": "HowToStep", "name": "GPU available", "text": "Use full-db AlphaFold." },
        { "@type": "HowToStep", "name": "CPU only", "text": "Use reduced-db fallback mode." }
      ]
    }
  ]
}
```

---

## SHACL Compliance

All method representations must conform to the `MethodShape` defined in FAIR² SHACL:

- `@type` must be `schema:HowToSection` or `schema:HowToStep`
- `steps` must be an array of `schema:HowToStep`
- `text` is mandatory for all procedural steps

---

## Notes

- This pattern allows nesting to arbitrary depth.
- Textual content can be multilingual using `@language` tags.
- Conditions and substeps are optional but recommended for clarity and modularity.

---

This structured approach enables both human-readable and machine-actionable protocols across diverse scientific domains. For more examples, see the [`fair2.json`](https://sen.science/doi/10.71728/hw56-vj34/fair2.json) specification.
