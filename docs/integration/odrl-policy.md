
# Integrating ODRL Policy Metadata in FAIR² Datasets

## Overview

The Open Digital Rights Language (ODRL) provides a formal, machine-readable way to express usage conditions, permissions, prohibitions, and obligations associated with a dataset. In the FAIR² specification, ODRL is used to enforce dataset terms of use beyond simple textual licenses, supporting responsible AI and governance-by-design.

This guide documents how to embed an ODRL policy inside a FAIR² dataset metadata record using schema.org and ODRL JSON-LD constructs.

## JSON-LD Structure

### Required Structure

ODRL policies are included under a `policy` field at the top level of the JSON-LD document (i.e., alongside `@type: Dataset`). All ODRL-specific terms use the `odrl:` prefix and are scoped to the "http://www.w3.org/ns/odrl/2/" namespace.

```json
{
  "@context": [
    "https://schema.org/",
    { "odrl": "http://www.w3.org/ns/odrl/2/" }
  ],
  "@type": "Dataset",
  "name": "...",
  "license": {
    "url": "https://licenses.fair2.org/templates/clinical-research-only.odrl.json",
    "usageInfo": "...",
    "governedBy": "ODRL"
  },
  "policy": {
    "@context": "http://www.w3.org/ns/odrl.jsonld",
    "@type": "odrl:Policy",
    "odrl:uid": "https://licenses.fair2.org/templates/clinical-research-only.odrl.json",
    "odrl:profile": "http://www.w3.org/ns/odrl/2/data",
    "odrl:permission": [...],
    "odrl:prohibition": [...]
  }
}
```

## Example Use Case: Clinical Research-Only Dataset

### High-Level Metadata

```json
"license": {
  "url": "https://licenses.fair2.org/templates/clinical-research-only.odrl.json",
  "usageInfo": "Use restricted to academic and clinical research purposes. Commercial reuse, redistribution, and reidentification attempts are strictly prohibited.",
  "isAccessibleForFree": true,
  "conditionsOfAccess": "Non-commercial research only",
  "governedBy": "ODRL"
}
```

### Embedded `policy` Block

```json
"policy": {
  "@context": "http://www.w3.org/ns/odrl.jsonld",
  "@type": "odrl:Policy",
  "odrl:uid": "https://licenses.fair2.org/templates/clinical-research-only.odrl.json",
  "odrl:profile": "http://www.w3.org/ns/odrl/2/data",
  "odrl:permission": [
    {
      "odrl:target": "urn:org:healthdata:anonymized-clinical-rct-2025",
      "odrl:action": "odrl:use",
      "odrl:constraint": {
        "odrl:leftOperand": "odrl:purpose",
        "odrl:operator": "odrl:eq",
        "odrl:rightOperand": "research"
      },
      "odrl:duty": {
        "odrl:action": "odrl:attribution",
        "odrl:target": "Ministry of Health, Tanzania"
      }
    }
  ],
  "odrl:prohibition": [
    { "odrl:action": "odrl:commercialize" },
    { "odrl:action": "odrl:redistribute" },
    { "odrl:action": "odrl:reidentify" }
  ]
}
```

## Key ODRL Concepts

| Element           | Purpose                                                                  |
|-------------------|---------------------------------------------------------------------------|
| `odrl:permission` | Defines actions users can perform (e.g., `use` for `research`)            |
| `odrl:prohibition`| Defines actions that are forbidden (e.g., `commercialize`)                |
| `odrl:constraint` | Adds conditions to permissions (e.g., limited by `purpose`)               |
| `odrl:duty`       | Specifies obligations tied to a permission (e.g., attribution required)   |

## Why Use ODRL in FAIR²?

- Machine-Enforceable: Policies can be evaluated automatically by systems.
- Responsible Use: Clearly encode non-commercial, ethical, or privacy-sensitive use terms.
- Policy Governance: Supports a layered model with business-level (ODPS) and legal-level (ODRL) enforcement.

## Validation

To ensure compliance, you can:

- Validate the policy using JSON Schema or SHACL
- Check against an ODRL reasoner or Policy Decision Point (PDP) implementation
- Link the `license.url` field to a reusable license template registry
