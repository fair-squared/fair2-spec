# FAIR² Example Walkthrough (Updated)

This walkthrough illustrates how the FAIR² ontology and metadata model are applied in a real dataset. The examples below are drawn directly from the **Borja et al. (2025)** FAIR² dataset (`borja2025.json`) and demonstrate how constrained shapes and entities interlink across submissions, data articles, methods, contributors, and results.

All examples are truncated to 1–2 representative instances for clarity.

---

## Submission

The submission represents the root entity linking the dataset, its methods, and the published data article.

```json
{
  "@id": "https://doi.org/10.5281/zenodo.10850318",
  "@type": "fair2:Submission",
  "schema:name": "Structure-Based Prediction of SARS-CoV-2 Variant Properties Using Machine Learning on Mutational Neighborhoods",
  "fair2:dataArticle": {
    "@id": "https://doi.org/10.3389/focsu.2024.1528837",
    "@type": "fair2:OpenDataArticle"
  },
  "fair2:dataset": {
    "@id": "https://zenodo.org/record/10850318/files/fair2.json",
    "@type": "schema:Dataset"
  },
  "fair2:method": {
    "@id": "https://fair2.ai/examples/borja2025#method",
    "@type": "fair2:MethodSection"
  }
}
```

This example shows how a FAIR² Submission aggregates its associated `Dataset`, `OpenDataArticle`, and `MethodSection` through clearly defined FAIR² linking properties.

---

## Data Article

The FAIR² Data Article describes the dataset and its scientific context.

```json
{
  "@id": "https://doi.org/10.3389/focsu.2024.1528837",
  "@type": "fair2:OpenDataArticle",
  "schema:name": "Structure-Based Prediction of SARS-CoV-2 Variant Properties Using Machine Learning on Mutational Neighborhoods",
  "schema:publisher": {
    "@type": "schema:Organization",
    "schema:name": "Frontiers in Ocean Sustainability"
  },
  "schema:author": [
    {
      "@type": "schema:Person",
      "schema:name": "Borja, Efren"
    },
    {
      "@type": "schema:Person",
      "schema:name": "Schultes, Erik"
    }
  ]
}
```

This JSON-LD fragment illustrates how a `fair2:OpenDataArticle` aligns with `schema:ScholarlyArticle` while referencing real contributors.

---

## Method

Methods in FAIR² are structured hierarchically as `fair2:MethodSection` objects containing ordered `fair2:Step` and `fair2:Substep` items.

```json
{
  "@id": "https://fair2.ai/examples/borja2025#method",
  "@type": "fair2:MethodSection",
  "schema:name": "Machine Learning Workflow",
  "fair2:step": [
    {
      "@type": "fair2:Step",
      "schema:name": "Feature Extraction",
      "schema:description": "Bio2Byte descriptors were extracted for each protein variant.",
      "fair2:step": [
        {
          "@type": "fair2:Substep",
          "schema:name": "Normalization",
          "schema:description": "Features were normalized using z-scores."
        }
      ]
    }
  ]
}
```

This structure demonstrates how the FAIR² Method representation supports multi-level procedural hierarchy and captures computational steps with clarity.

---

## Contributors and Roles

Contributor information in FAIR² uses `schema:Contribution` entities enriched with role identifiers from the Contributor Role Ontology and FAIR² extensions.

```json
{
  "@type": "schema:Contribution",
  "schema:agent": {
    "@type": "schema:Person",
    "schema:name": "Efren Borja"
  },
  "prov:hadRole": [
    {
      "@id": "cr:data-curation",
      "rdfs:label": "Data Curation"
    },
    {
      "@id": "cr:formal-analysis",
      "rdfs:label": "Formal Analysis"
    }
  ]
}
```

This example shows how FAIR² contributions maintain explicit attribution through PROV-compatible `prov:hadRole` relationships.

---

## RecordSet and Statistics

FAIR² datasets include RecordSets linked to computed statistics and variable definitions.

```json
{
  "@id": "https://fair2.ai/examples/borja2025#recordset",
  "@type": "fair2:RecordSet",
  "schema:name": "RBD Variant Features",
  "fair2:statistics": {
    "@type": "fair2:DescriptiveStatistics",
    "schema:name": "Feature Distribution Statistics",
    "schema:description": "Summary of Bio2Byte feature distributions across variants."
  },
  "fair2:variables": [
    {
      "schema:name": "RMSD",
      "schema:description": "Root-mean-square deviation between predicted and experimental structures."
    },
    {
      "schema:name": "TM-score",
      "schema:description": "Template modeling score for structural alignment."
    }
  ]
}
```

This section exemplifies how FAIR² captures analytical data products, linking them to their computed statistics and variable-level metadata.

---

## Visualization

Visual outputs are represented as `fair2:Visualization` entities linked to the RecordSet or dataset.

```json
{
  "@id": "https://fair2.ai/examples/borja2025#visualization",
  "@type": "fair2:Visualization",
  "schema:name": "RMSD Distribution Plot",
  "schema:encodingFormat": "image/png",
  "schema:contentUrl": "https://fair2.ai/examples/borja2025/rmsd_distribution.png"
}
```

This final example shows how visualization artifacts are incorporated as linked digital objects following Schema.org’s `MediaObject` pattern while preserving FAIR² semantic traceability.

---

## Summary

These examples illustrate the implementation of the FAIR² ontology in a real dataset. The JSON-LD structures demonstrate how methods, data, contributors, and derived outputs are interconnected through consistent FAIR² linking properties, enabling full traceability and AI-ready reuse.
