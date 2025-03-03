# Getting Started with FAIR²

## 🔍 What is FAIR²?

FAIR² (**FAIR Squared**) is an enhanced version of the **FAIR principles** (Findable, Accessible, Interoperable, and Reusable), designed to make datasets **AI-ready, context-rich, and machine-actionable**. It builds on top of **ML Croissant** and integrates **SHACL validation** to ensure metadata quality and compliance with structured schemas.

---

## 🚀 Quick Start

### 1️⃣ **Install Required Tools**
To work with FAIR² metadata, you may need:
- **Python 3.8+** (for processing FAIR² metadata)
- **FAIR² Validator (coming soon)**: CLI tool for validating metadata
- **RDF Libraries** (`rdflib`, `pySHACL`) for validation
- **JSON-LD tools** (optional, for linked data processing)

You can install the necessary Python libraries with:
``bash
pip install ml-croissant torch tensorflow rdflib pyshacl
```

This installs:
- ML Croissant
- Pytorch & TensorFlow
- RDF & SHACL validation


### 2️⃣ **Define Your Dataset Using FAIR²**
A FAIR²-compliant dataset should have:
- A metadata file (fair2.json) in JSON-LD format.
- SHACL validation rules to ensure correctness.
- Persistent identifiers (PIDs) for traceability.

Here’s a minimal **fair2.json** example:

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

### 3️⃣ **Validate your FAIR² Metadata**

You can use SHACL validation to check if your metadata conforms to FAIR² standards.

If using pySHACL, run:
```bash
pyshacl -s shapes/dataset.json -d fair2.json
```

If using a web-based validator (coming soon), upload your fair2.json file for instant validation.

###  4️⃣  **Use ML Croissant features**
FAIR² is designed to work with ML Croissant for machine-learning-ready metadata. You can:
- Add ML Croissant annotations alongside FAIR² metadata.
- Use schema.org-compatible descriptions for dataset discoverability.
- Load datasets into PyTorch and TensorFlow for AI model training.

```python
from mlcroissant import Dataset
import tensorflow as tf

dataset = Dataset("fair2.json")
tensorflow_dataset = tf.data.Dataset.from_generator(
    lambda: dataset, output_types=(tf.float32, tf.int32)
)

for image, label in tensorflow_dataset:
    # Train your TensorFlow model here...
```

Thanks to ML Croissant’s structured metadata, FAIR² datasets can be directly integrated into AI training pipelines without additional preprocessing.

### 📌 Next Steps

Now that you have a basic FAIR² metadata file:
	1.	Explore the FAIR² Schema for deeper metadata structures.
	2.	Validate your dataset using SHACL or JSON-LD tools.
	3.	Integrate FAIR² with ML Croissant for AI-ready datasets.
	4.	Contribute to FAIR²! See Contributing.