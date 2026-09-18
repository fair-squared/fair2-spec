# FAIR² and Open Data Products Specification (ODPS) Integration

## Overview

FAIR² (FAIR Squared) integrates with the **Open Data Products Specification (ODPS)** to support transparency and governance in data product design, especially for datasets reused in AI and machine learning pipelines. The integration allows FAIR² metadata to include key elements from ODPS—such as licensing and governance—through a dedicated `odps` property.

This alignment ensures that FAIR² metadata can support principles of openness, accountability, and stewardship that ODPS promotes, while remaining compatible with linked data and SHACL validation frameworks.

---

## ODPS in FAIR²

A new top-level property, `odps`, is introduced in FAIR² to encapsulate metadata fields derived from the Open Data Products Specification.

### Structure

```json
{
  "odps": {
    "license": {
      "type": "Open Government Licence v3.0",
      "url": "https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
    },
    "governance": {
      "owner": "Department of Data Infrastructure",
      "contact": "opendata@example.gov",
      "oversightBody": "National Data Governance Board",
      "accountabilityMechanism": "Annual audit with public reporting"
    }
  }
}
```

---

## ODPS Metadata Fields in FAIR²

| **Property**                     | **Description**                                                                 |
|----------------------------------|---------------------------------------------------------------------------------|
| `odps.license.type`              | The name of the license under which the dataset is published                    |
| `odps.license.url`               | A URI pointing to the full license text                                        |
| `odps.governance.owner`          | The organization or department that owns the dataset                           |
| `odps.governance.contact`        | Contact information for the governance authority                               |
| `odps.governance.oversightBody` | Body or authority responsible for governance or stewardship oversight          |
| `odps.governance.accountabilityMechanism` | Description of processes ensuring transparency and accountability     |

---

## Example: Full JSON-LD Dataset with ODPS Block

```json
{
  "@context": "https://fair2.ai/ns/",
  "@type": "Dataset",
  "name": "Air Quality Index Dashboard",
  "description": "A dataset used in urban pollution modeling.",
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "odps": {
    "license": {
      "type": "Open Government Licence v3.0",
      "url": "https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
    },
    "governance": {
      "owner": "Department of Data Infrastructure",
      "contact": "opendata@example.gov",
      "oversightBody": "National Data Governance Board",
      "accountabilityMechanism": "Annual audit with public reporting"
    }
  }
}
```

---

## Purpose and Benefits

Including ODPS metadata within FAIR² enables:

- Clear definition of ownership and legal reuse rights
- Transparent data governance documentation
- Alignment with open government and open science principles
- Support for institutional data stewardship policies

---

## Validation and Interoperability

- The `odps` property can be validated using SHACL rules defined in the FAIR² validation profile.
- ODPS metadata is kept modular and namespaced to allow future expansion without impacting core FAIR² properties.
- FAIR² remains fully compatible with Schema.org, ML Croissant, and JSON-LD-based applications.

---

## Next Steps

- Refer to the [FAIR² Schema](../specification/schema.md) for usage examples
- Review the [ODPS documentation](https://opendataproducts.org)
- Submit extensions or validation rules via [GitHub](https://github.com/fair2-spec/issues)
