# FAIR² and Google Rich Results Integration

## Overview

FAIR² (FAIR Squared) supports integration with **Google Dataset Search** and other rich result platforms by aligning metadata with the **Schema.org `Dataset` class**. This alignment improves the discoverability of FAIR²-compliant datasets through search engines and enables automatic indexing by tools that support structured data.

By embedding Schema.org-compatible JSON-LD metadata, FAIR² datasets can be included in **Google Rich Results**, allowing users to find datasets based on spatial and temporal coverage, licensing, creators, and more.

---

## Schema.org Dataset Compatibility in FAIR²

FAIR² incorporates the following Schema.org properties to enable dataset indexing in search platforms:

| **Property**               | **Purpose**                                                 |
|----------------------------|-------------------------------------------------------------|
| `@type`: `Dataset`         | Declares the type of the resource as a Dataset              |
| `name`                     | The title of the dataset                                    |
| `description`              | Summary of dataset content                                  |
| `url`                      | Landing page or persistent identifier                       |
| `license`                  | Licensing information for reuse                             |
| `creator` / `author`       | Agent responsible for dataset creation                      |
| `keywords`                 | Tags and search keywords                                    |
| `datePublished`            | Dataset publication date                                    |
| `spatialCoverage`          | Geographic location associated with the dataset             |
| `temporalCoverage`         | Time range the data covers                                  |
| `distribution`             | Links to downloadable files                                 |

---

## Example: JSON-LD Metadata for Rich Search Integration

```json
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Global Land Use Dataset",
  "description": "A dataset describing global land use changes between 2000 and 2020.",
  "url": "https://example.org/datasets/global-land-use",
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "creator": {
    "@type": "Organization",
    "name": "Earth Data Institute"
  },
  "keywords": ["land use", "global", "environment", "remote sensing"],
  "datePublished": "2024-12-01",
  "spatialCoverage": {
    "@type": "Place",
    "geo": {
      "@type": "GeoShape",
      "box": "-90 -180 90 180"
    }
  },
  "temporalCoverage": "2000-01-01/2020-12-31",
  "distribution": {
    "@type": "DataDownload",
    "contentUrl": "https://example.org/downloads/land-use.csv",
    "encodingFormat": "text/csv"
  }
}
```

This example satisfies Google’s structured data guidelines and aligns with FAIR² validation rules.

---

## Benefits of Schema.org Integration in FAIR²

- **Improved discoverability** of datasets in Google Dataset Search
- **Semantic interoperability** with linked data platforms
- **Enhanced metadata quality** with structured spatio-temporal descriptions
- **Support for persistent identifiers** (e.g., DOIs or URIs)

---

## Recommended Practices

To ensure compatibility with search engines and FAIR² validation:

1. Use `@context: https://schema.org` and `@type: Dataset`
2. Always include `name`, `description`, `url`, and `license`
3. Provide `spatialCoverage` and `temporalCoverage` when applicable
4. Link to actual data files using the `distribution` property
5. Validate metadata using SHACL constraints and structured data testing tools

---

## Next Steps

- Refer to the [FAIR² Schema](../specification/schema.md) for additional properties
- Test rich result compatibility using [Google’s Rich Results Test](https://search.google.com/test/rich-results)
- Contribute improvements or extensions via [GitHub](https://github.com/fair2-spec/issues)
