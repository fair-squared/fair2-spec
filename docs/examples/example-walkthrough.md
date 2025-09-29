# Example Walkthrough of a FAIR²-Compliant Metadata File

This page walks through a real metadata file (`borja2025.json`) to illustrate how each component of the FAIR² specification is used in practice.

> 🔗 You can [download the example here](https://raw.githubusercontent.com/fair-squared/fair2-spec/refs/heads/main/examples/example-1/borja2025.json)

---

## Dataset Overview

- `@type`: `schema:Dataset`
- `schema:name`, `schema:description`, `schema:keywords`: Present and rich in content.
- `schema:license`: Open data license (Creative Commons)
- `schema:version`: Matches software and dataset versioning guidelines.

➡️ Related Spec Section: [Schema](../specification/schema.md)

---

## Distributions

Multiple files are described using `schema:distribution`, each with:

- `encodingFormat`
- `schema:name`
- `contentUrl` (resolvable)
- `variableMeasured` (linked to columns)

➡️ Related Spec Section: [Schema](../specification/schema.md)

---

## 🧪 Methods

The file uses:

- `schema:hasPart` with `schema:HowToSection`
- Nested `schema:HowToStep`, `schema:HowToDirection`

➡️ Related Spec Section: [Methods](../specification/methods.md)

---

## Access Rights

Access agreement is defined using:

```json
"dct:accessRights": {
  "@id": "fair2:AgreementLevel1",
  "schema:name": "Open Access",
  "schema:url": "https://fair2.ai/ns/AgreementLevels/1"
}
```

➡️ Related Spec Section: [Access Agreements](../specification/access-agreements.md)

---

## Contributor Roles & Provenance

Each `schema:Contribution` block follows the FAIR² pattern:

- `prov:agent` → `schema:Person`
- `prov:hadRole` → list of CRO or FAIR² URIs with `rdfs:label`

➡️ Related Spec Section: [Provenance](../specification/provenance.md)  
➡️ Integration: [Contributor Roles](../integration/contributor-roles.md)

---

## Temporal & Spatial Coverage

This example includes:

- `schema:temporalCoverage`: `"1995/2023"`
- `schema:spatialCoverage`: a `schema:Place` with bounding box

➡️ Related Spec Section: [Schema](../specification/schema.md)

---

## Responsible AI

While this file handles biases and licensing responsibly, it does not yet use:

- `rai:BiasStatement`
- `rai:UseRestriction`
- `rai:FairnessCriterion`

➡️ See: [Responsible AI](../specification/responsible-ai.md)

---

## Alignment with External Standards

- **Schema.org**: Used throughout (`schema:Dataset`, `schema:Person`, etc.)
- **PROV-O**: Used for contributors
- **CRediT/CRO**: Contributor roles properly linked
- **ML Croissant**: Fully aligned structure
- **ODPS**: Not yet implemented
- **Google Rich Search**: Some fields match, but not fully optimized

Integration Sections:
- [Schema.org](../integration/schema-org.md)
- [PROV-O](../integration/prov-o.md)
- [Croissant RAI](../integration/croissant-rai.md)
- [Google Rich Search](../integration/google-rich-search.md)
- [ODPS](../integration/odps.md)

---

## ✅ Summary Compliance

| Feature                        | Status |
|-------------------------------|--------|
| Schema.org compliance         | ✅ Yes |
| ML Croissant compatibility    | ✅ Yes |
| Access agreements             | ✅ Level 1 used |
| Contributor roles             | ✅ CRO + FAIR² |
| Responsible AI annotations    | ✅ Yes |
| Google structured data        | ⚠️ Partially covered |
| ODPS properties               | ❌ Not used |
