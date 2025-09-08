# FAIR² and Croissant RAI Integration

## Overview

The FAIR² specification integrates the **Croissant Responsible AI Vocabulary (RAI)** to support ethical, transparent, and accountable use of datasets in machine learning workflows. This integration enables datasets to be described not only in terms of structure and provenance, but also with respect to potential risks, biases, and ethical review processes.

RAI metadata provides essential context for downstream users—particularly AI developers, data stewards, and compliance reviewers—seeking to assess the ethical implications of using a dataset in automated decision-making.

---

## Key Features

FAIR² supports the following Responsible AI metadata elements via the Croissant RAI vocabulary:

| **FAIR² Element**           | **Purpose**                                               |
|----------------------------|-----------------------------------------------------------|
| `rai:ethicsReview`         | Captures details of any formal ethical review conducted. |
| `rai:dataBiases`           | Documents known or suspected biases in the dataset.       |
| `rai:dataLimitations`      | Identifies limitations, constraints, or known weaknesses. |
| `prov:wasGeneratedBy`      | Records the provenance and generation activity.           |
| `rai:*` metadata (general) | Supports alignment with Responsible AI standards.         |

These elements extend [ML Croissant](https://mlcommons.org/croissant/) and are fully compatible with JSON-LD and SHACL validation frameworks used in FAIR².

---

## Example: JSON-LD with Croissant RAI Metadata

```json
{
  "@context": [
    "https://mlcroissant.org/",
    "https://fair2.ai/ns/"
  ],
  "@type": "Dataset",
  "name": "AI Model Training Data",
  "rai:dataBiases": [
    {
      "@type": "rai:Bias",
      "description": "Dataset underrepresents minority groups."
    }
  ],
  "rai:dataLimitations": [
    {
      "@type": "rai:Limitation",
      "description": "Annotations may contain labeling errors."
    }
  ],
  "rai:ethicsReview": {
    "@type": "rai:EthicsReview",
    "description": "Ethics review conducted by the AI Ethics Board."
  },
  "prov:wasGeneratedBy": {
    "@type": "prov:Activity",
    "description": "Data collection process."
  }
}
```

This metadata enables:

- **Ethical traceability**: Describing the ethical oversight applied to the dataset.
- **Bias documentation**: Disclosing sampling, labeling, or structural biases.
- **Transparency in limitations**: Clarifying conditions under which data may be unsuitable for reuse.
- **Provenance**: Tracking how the data was collected and processed.

---

## Alignment with Responsible AI Principles

By incorporating Croissant RAI elements, FAIR² provides compatibility with leading frameworks for Responsible AI, including:

- OECD Principles on AI
- EU AI Act compliance requirements
- MLCommons RAI and Model Card standards

Datasets using these metadata properties can be assessed programmatically for fairness, traceability, and compliance readiness.

---

## Next Steps

To incorporate Responsible AI metadata into your dataset:

1. Review the [FAIR² Schema](../specification/schema.md) for AI-relevant fields.
2. Add `rai:*` properties describing ethical oversight, limitations, and biases.
3. Use [SHACL validation rules](../specification/shacl-validation.md) to ensure conformance.
4. [Contribute to FAIR²](../community/contributing.md) by suggesting extensions or sharing Responsible AI use cases.

For questions or contributions related to Responsible AI alignment, please contact:  
📩 [feedback@fair2.ai](mailto:feedback@fair2.ai)

---

_Last updated: 2025-03-14_