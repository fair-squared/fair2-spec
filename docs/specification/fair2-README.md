
# FAIR² README Generation Specification
**Data Dictionary–First Profile**

This document specifies how to generate a dataset package `README.md` deterministically from `fair2.json`,
following **web-aligned best practices** that prioritize **variable-level documentation (Data Dictionary)**
over internal structural abstractions (e.g. RecordSets).

This profile supersedes v0.1 for all FAIR² dataset packages intended for public reuse,
AI/ML workflows, and repository distribution.

---

## 1. Rationale (Normative)

Across major research data repositories (Zenodo, Dataverse, Dryad, Figshare, Hugging Face),
the README is expected to document:

- What variables exist
- What they mean
- How to interpret their values
- How to reuse them responsibly

---

## 2. Design principles

1. **Variables are first-class**
   - README MUST document variables, not internal storage abstractions.
2. **No new facts**
   - README content MUST be derived strictly from `fair2.json` or referenced artifacts.
3. **Deterministic generation**
   - The same `fair2.json` MUST always produce the same `README.md`.
4. **Separation of concerns**
   - Human-readable summaries live in README.
   - Full machine-actionable metadata lives in `fair2.json`.

---

## 3. Inputs and outputs

### Input
- `fair2.json` (JSON-LD, FAIR²-compliant)
- Optional: CSV/Excel Data Dictionary files referenced from metadata

### Output
- `README.md` (UTF-8 Markdown)

---

## 4. Required README sections (Normative)

The generator MUST render the following sections, in order:

1. `# <Dataset Name>`
2. `## Overview`
3. `## How to cite`
4. `## License`
5. `## Contents of this package`
6. `## Data dictionary`
7. `## Methods and provenance`
8. `## Access and reuse conditions`
9. `## Responsible use and limitations`
10. `## Versioning and changelog`
11. `## Contributors`
12. `## Standards and conformance`
13. `## Machine-readable metadata`

---

## 5. Data Dictionary section (Normative)

### 5.1 Authoritative source

The README MUST state explicitly that the authoritative variable documentation is provided via:

- `schema:variableMeasured` entries in `fair2.json`
- FAIR² Core Data Dictionary–compliant representations

### 5.2 Variable overview table (Required)

The generator MUST render a summary table derived from `schema:variableMeasured` with at least:

| Column | Source |
|------|-------|
| Variable ID | `@id` |
| Technical name | `schema:identifier` |
| Human label | `schema:name` |
| Value type | `fair2:valueType` |
| Unit | `fair2:unit` / `schema:unitCode` |
| Definition | `skos:definition` |


For detailed variable documentation including value domains, missing value codes, examples, and statistics, see [Data Dictionary](./data-dictionary.md).


### 5.3 Extended documentation

The README SHOULD include a note pointing users to:

- Full value domains
- Missing value codes
- Examples
- Statistics with provenance

These MUST NOT be duplicated verbatim in the README.

---

## 6. RecordSets (De-emphasized, Optional)

If `recordSet` objects are present in `fair2.json`, the README MAY include a short,
non-tabular explanatory note such as:

> “Internally, the dataset is organized into one or more RecordSets for processing
> and validation purposes. These structures are documented in `fair2.json` and are
> not required for typical reuse.”

RecordSets MUST NOT be presented as the primary data documentation mechanism.

---

## 7. Mapping rules (Summary)

| README section | FAIR² source |
|---------------|-------------|
| Overview | `name`, `description`, `keywords`, `domain` |
| Citation | `citeAs`, `citation`, `identifier` |
| License | `license` |
| Contents | `distribution` |
| Data dictionary | `schema:variableMeasured` |
| Methods | `method`, `prov:*`, `subjectOf` |
| Access | `accessRights` |
| Responsible use | Explicit structured fields only |
| Contributors | `author`, `contributor` |
| Conformance | `conformsTo` |

---

## 8. Compliance rule (Normative)

A FAIR² dataset package claiming README compliance:

- MUST include a Data Dictionary section
- MUST document variables, not just files
- MUST NOT require readers to inspect `fair2.json` to understand variable meaning

---

## 9. Relationship to FAIR² Core Data Dictionary

This specification is fully aligned with the FAIR² Core Data Dictionary, which defines:

- Variables as first-class entities
- `schema:variableMeasured` as the canonical attachment point
- `skos:definition` as the semantic definition of a variable

The README is a **projection** of this dictionary for human reuse, not a replacement.

---

**End of FAIR² README Generation Specification**
