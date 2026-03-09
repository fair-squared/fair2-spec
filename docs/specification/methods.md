# FAIR² Method Representation

This document defines how FAIR² expresses detailed methods using structured, machine-readable JSON-LD constructs. It is fully compatible with [schema.org](https://schema.org/), [ML Croissant](https://mlcommons.org/croissant/), and the [FAIR²](https://senscience.ai/) metadata specification.

## Overview

Method descriptions in FAIR² are structured hierarchically using the following types:

- **`fair2:Section`** derived from `schema:HowToSection`
- **`fair2:Step`** derived from `schema:HowToStep`
- **`fair2:Substep`** derived from `schema:HowToStep`
- **`fair2:StepCase`** derived from `schema:HowToStep`

Each level extends or specializes the [`schema.org/HowToStep`](https://schema.org/HowToStep) pattern, enabling context-rich and modular method representation.

---

## Structure and Semantics

### Section (`fair2:Section`)

A major methodological unit (e.g., "Structure Prediction", "Binding Assays").

| Property | Vocabulary | Required | Description |
|---|---|---|---|
| `schema:name` | schema.org | Yes | Section title |
| `schema:description` | schema.org | No | Narrative description |
| `fair2:step` | FAIR² | No | Steps or StepCases within this section |
| `fair2:next` | FAIR² | No | IRI of the following section |

```jsonld
{
  "@type": "fair2:Section",
  "@id": "fair2:method:section-structure-prediction",
  "schema:name": "Structure Prediction",
  "schema:description": "Computational prediction of 3D protein structures.",
  "fair2:step": [ ... ],
  "fair2:next": { "@id": "fair2:method:section-binding-assays" }
}
```

---

### Step (`fair2:Step`)

Primary procedural element within a Section. May contain substeps and link to produced variables.

| Property | Vocabulary | Required | Description |
|---|---|---|---|
| `schema:name` | schema.org | Yes | Step title |
| `schema:description` | schema.org | No | Step instructions |
| `fair2:substep` | FAIR² | No | Nested substeps |
| `fair2:next` | FAIR² | No | IRI of the following step |
| `fair2:generated` | FAIR² | No | IRI(s) of RecordSet fields produced by this step |

```jsonld
{
  "@type": "fair2:Step",
  "@id": "fair2:method:step-alphafold",
  "schema:name": "AlphaFold Prediction",
  "schema:description": "Run AlphaFold prediction using ColabFold pipeline.",
  "fair2:substep": [ ... ],
  "fair2:next": { "@id": "fair2:method:step-rmsd" },
  "fair2:generated": [
    { "@id": "fair2:var:rmsd" },
    { "@id": "fair2:var:plddt" }
  ]
}
```

---

### Substep (`fair2:Substep`)

A finer-grained instruction nested within a `fair2:Step`.

| Property | Vocabulary | Required | Description |
|---|---|---|---|
| `schema:name` | schema.org | Yes | Substep title |
| `schema:description` | schema.org | No | Substep instructions |
| `fair2:next` | FAIR² | No | IRI of the following substep |

```jsonld
{
  "@type": "fair2:Substep",
  "@id": "fair2:method:substep-prepare-input",
  "schema:name": "Prepare FASTA input",
  "schema:description": "Prepare FASTA input and validate sequence.",
  "fair2:next": { "@id": "fair2:method:substep-launch-colabfold" }
}
```

---

### StepCase (`fair2:StepCase`)

Used to capture conditional logic (e.g., environment-dependent or tool-specific alternatives). StepCase items are placed in the same `fair2:step` array as regular Steps.

| Property | Vocabulary | Required | Description |
|---|---|---|---|
| `schema:name` | schema.org | Yes | Condition label |
| `fair2:qualifiedUsage` | FAIR² | Yes | The `if` condition string |
| `fair2:nextTrue` | FAIR² | Yes | IRI of the path taken if the condition is met |
| `fair2:next` | FAIR² | No | IRI of the default `else` / fallthrough path |

```jsonld
{
  "@type": "fair2:StepCase",
  "@id": "fair2:method:stepcase-gpu",
  "schema:name": "GPU available",
  "fair2:qualifiedUsage": "hardware.gpu == true",
  "fair2:nextTrue": { "@id": "fair2:method:step-alphafold-full-db" },
  "fair2:next": { "@id": "fair2:method:step-alphafold-reduced-db" }
}
```

---

## Ontological Alignment

Each element inherits from `schema:HowToStep`, but is semantically specialized via `fair2:` namespace identifiers. This ensures compatibility with:

- **schema.org-based search indexing**
- **Croissant `Method` constructs**
- **SHACL validation using RDF types**

---

## Integration with Variable Lineage

Steps link to the RecordSet fields/variables they produce via `fair2:generated`. This is the step-side provenance property; variables reference back to steps via the inverse `prov:wasGeneratedBy`.

```jsonld
{
  "@type": "fair2:Step",
  "@id": "fair2:method:step-rmsd",
  "schema:name": "RMSD Calculation",
  "fair2:generated": [
    { "@id": "fair2:var:rmsd" }
  ]
}
```

---

## Example JSON-LD Block

```jsonld
{
  "@type": "fair2:Section",
  "@id": "fair2:method:section-structure-prediction",
  "schema:name": "Structure Prediction",
  "schema:description": "End-to-end structure prediction pipeline.",
  "fair2:step": [
    {
      "@type": "fair2:Step",
      "@id": "fair2:method:step-alphafold",
      "schema:name": "AlphaFold Prediction",
      "schema:description": "Run AlphaFold prediction using ColabFold pipeline.",
      "fair2:substep": [
        {
          "@type": "fair2:Substep",
          "@id": "fair2:method:substep-prepare-input",
          "schema:name": "Prepare FASTA input",
          "schema:description": "Prepare FASTA input and validate sequence."
        },
        {
          "@type": "fair2:Substep",
          "@id": "fair2:method:substep-launch-colabfold",
          "schema:name": "Launch ColabFold",
          "schema:description": "Upload sequence and launch ColabFold."
        }
      ],
      "fair2:generated": [
        { "@id": "fair2:var:plddt" }
      ]
    },
    {
      "@type": "fair2:StepCase",
      "@id": "fair2:method:stepcase-gpu",
      "schema:name": "GPU available",
      "fair2:qualifiedUsage": "hardware.gpu == true",
      "fair2:nextTrue": { "@id": "fair2:method:step-alphafold-full-db" },
      "fair2:next": { "@id": "fair2:method:step-alphafold-reduced-db" }
    }
  ]
}
```

---

## SHACL Compliance

All method representations must conform to the shapes defined in `shapes/turtle/method.ttl`:

| Shape | Target class | Required properties |
|---|---|---|
| `MethodSectionShape` | `fair2:Section` | `schema:name` |
| `MethodStepShape` | `fair2:Step` | `schema:name` |
| `MethodSubstepShape` | `fair2:Substep` | `schema:name` |
| `StepCaseShape` | `fair2:StepCase` | `schema:name`, `fair2:qualifiedUsage`, `fair2:nextTrue` |

---

## Notes

- This pattern allows nesting to arbitrary depth.
- Textual content can be multilingual using `@language` tags.
- `fair2:substep` and `fair2:generated` are optional but recommended for clarity and provenance.
- `fair2:next` enables sequential ordering of sections, steps, and substeps without relying on array index.

---

This structured approach enables both human-readable and machine-actionable protocols across diverse scientific domains. For more examples, see the [`fair2.json`](https://sen.science/doi/10.71728/hw56-vj34/fair2.json) specification.
