di# Getting Started with FAIR²

This guide provides the foundational steps to begin using the **FAIR² (FAIR Squared)** specification for preparing, validating, and integrating AI-ready datasets.

---

## What is FAIR²?

**FAIR²** extends the original FAIR principles—**Findable, Accessible, Interoperable, and Reusable**—by introducing capabilities that make datasets:

- **AI-Ready**: Structured for compatibility with machine learning workflows.
- **Context-Rich**: Enhanced with metadata that captures provenance, methodology, and ethical considerations.
- **Machine-Actionable**: Validated using SHACL rules and described using [JSON-LD](https://json-ld.org/) and [schema.org](https://schema.org/) standards.

FAIR² builds upon [ML Croissant](https://mlcommons.org/croissant/) and uses **SHACL** to enforce schema compliance, enabling robust dataset validation and seamless downstream use in AI pipelines.

---

## Step 1: Install Required Tools

To work with FAIR² metadata, you may require the following:

### Core Requirements

- **Python 3.8+**
- **RDF Libraries** for validation:
  - `rdflib`
  - `pyshacl`
- **ML Croissant**
- **TensorFlow** and/or **PyTorch** (optional, for AI training pipelines)

### Installation

Use the following command to install recommended packages:

```bash
pip install ml-croissant torch tensorflow rdflib pyshacl
```

This installs the following components:

- `ml-croissant`: Metadata handling and dataset loading
- `torch` and `tensorflow`: AI frameworks
- `rdflib`, `pyshacl`: RDF graph processing and SHACL validation

> Note: The **FAIR² Validator CLI** is under development and will be released in a future version.

---

## Step 2: Define a FAIR² Metadata File

A FAIR²-compliant dataset includes a metadata file named `fair2.json` written in [JSON-LD](https://json-ld.org/) format. This file should include:

- A globally unique identifier (e.g., DOI or URI)
- Dataset description and license
- Distribution entries describing downloadable data assets
- References to validation shapes and method sections (optional)

### Minimal Example

```json
{
  "@context": "https://fair2.ai/spec/fair2_context",
  "@type": "Dataset",
  "name": "Example AI-ready Dataset",
  "description": "A dataset demonstrating FAIR² compliance",
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "distribution": [
    {
      "@type": "DataDownload",
      "contentUrl": "https://example.com/dataset.csv",
      "encodingFormat": "text/csv"
    }
  ]
}
```

---

## Step 3: Validate FAIR² Metadata Using SHACL

FAIR² metadata is designed to be machine-validated. SHACL validation ensures that datasets conform to the required structure.

### Using `pySHACL`

To run validation locally:

```bash
pyshacl -s shapes/dataset.json -d fair2.json
```

Where:
- `shapes/dataset.json` is your SHACL shape graph (provided by FAIR²)
- `fair2.json` is your dataset metadata file

### Web-Based Validation (Coming Soon)

A browser-based validator is under development and will allow validation of FAIR² metadata via file upload or URL.

---

## Step 4: Integrate with ML Croissant

FAIR² metadata is compatible with [ML Croissant](https://mlcommons.org/croissant/), allowing seamless integration with machine learning pipelines.

### Example: Loading FAIR² Dataset into TensorFlow

```python
from mlcroissant import Dataset
import tensorflow as tf

dataset = Dataset("fair2.json")
tensorflow_dataset = tf.data.Dataset.from_generator(
    lambda: dataset, output_types=(tf.float32, tf.int32)
)

for image, label in tensorflow_dataset:
    # Train your TensorFlow model here
```

This workflow allows you to describe your dataset once and reuse it across multiple AI environments without additional preprocessing.

---

## Next Steps

Once you have created and validated your FAIR² metadata file, you can:

1. Explore the full [FAIR² Schema](specification/schema.md) to describe your data in greater detail.
2. Use [SHACL validation](specification/shacl-validation.md) to check compliance.
3. Combine FAIR² with [ML Croissant features](integration/ml-croissant.md) for scalable dataset reuse.
4. [Contribute to the specification](community/contributing.md) by providing feedback or submitting extensions.

---

FAIR² is actively evolving. For updates, please refer to the [project roadmap](community/roadmap.md) and join the community discussions on specification development.


Prompt:

Update this getting-started documentation based on new content and the fair2.py examples. 