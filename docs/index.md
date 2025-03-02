# FAIR2 Specification Documentation

## Overview

The FAIR2 Specification provides a structured and standardized way to describe datasets, their authors, and related metadata. This documentation outlines the key components and shapes used in the FAIR2 Specification.

## Contexts

### FAIR2 Context

The FAIR2 context defines the vocabulary and terms used in the specification. It includes terms from schema.org, croissant, and custom FAIR2 terms.

### SHACL Context

The SHACL context defines the shapes and constraints for validating the data against the FAIR2 Specification.

## Shapes

### DatasetShape

The `DatasetShape` defines the structure and constraints for describing a dataset. It includes properties such as author, citation, content URL, and more.

#### Properties

- **author**: The author of the dataset. Must be a `PersonShape`.
- **citation**: A citation or reference to another creative work. Must be a string.
- **citeAs**: The preferred way to cite this dataset. Must be a string.
- **conformsTo**: An established standard to which the dataset conforms. Must be a URI.
- **contentUrl**: A URL to the actual dataset file. Must be a URI.
- **datePublished**: The date on which the dataset was published. Must be a date.
- **description**: A description of the dataset. Must be a string.
- **distribution**: Details about the distribution of the dataset. Must be a `NodeShape`.
- **funding**: Details about the funding of the dataset. Must be a `NodeShape`.
- **identifier**: A unique identifier for the dataset. Must be a URI.
- **keywords**: Keywords or tags used to describe the dataset. Must be a string.
- **license**: The license under which the dataset is published. Must be a URI.
- **name**: The name of the dataset. Must be a string.
- **isPartOf**: Indicates that the dataset is part of a scholarly article. Must be a `ScholarlyArticleShape`.
- **recordSet**: Details about the record set. Must be a `NodeShape`.

### PersonShape

The `PersonShape` defines the structure and constraints for describing a person. It includes properties such as name and affiliation.

#### Properties

- **name**: The name of the person. Must be a string.
- **affiliation**: The affiliation of the person. Must be an `OrganizationShape`.

### OrganizationShape

The `OrganizationShape` defines the structure and constraints for describing an organization. It includes properties such as name and address.

#### Properties

- **name**: The name of the organization. Must be a string.
- **address**: The address of the organization. Must be a string.

### RecordSetShape

The `RecordSetShape` defines the structure and constraints for describing a record set. It includes properties such as description and fields.

#### Properties

- **description**: A description of the record set. Must be a string.
- **field**: Details about the fields in the record set. Must be a `NodeShape`.

## Example

Here is an example of a dataset described using the FAIR2 Specification:

```json
{
  "@context": [
    "https://fair2.ai/spec/fair2_context",
    "https://fair2.ai/spec/shacl_context.json"
  ],
  "@id": "https://sen.science/doi/10.71728/r1rj-f947",
  "@type": "Dataset",
  "author": [
    {
      "@id": "/authors/c1b96691-fbbf-4157-a2c5-e8fb78c799f1",
      "@type": "Person",
      "affiliation": [
        {
          "@id": "/organizations/0d6a7bd5-95ee-4b5a-9ea9-35747624b353",
          "@type": "Organization",
          "address": "Herrera Kaia Portualdea s/n, 20110 Pasaia, Spain",
          "name": "AZTI, Marine Research, Basque Research and Technology Alliance (BRTA)"
        }
      ],
      "name": "Ángel Borja"
    }
  ],
  "citation": "https://doi.org/10.3389/focsu.2024.1528837",
  "citeAs": "Borja Á, Adarraga I, Bald J, et al. (2024). Marine Biodiversity and Environmental Data: An AI-Ready, Open Dataset from the long term (1995–2023) Basque Country Monitoring Network. Front. Ocean Sustain. 2:1528837. doi: 10.3389/focsu.2024.1528837",
  "conformsTo": "http://mlcommons.org/croissant/1.0",
  "contentUrl": "fair2.json",
  "datePublished": "2025-02-05",
  "description": "This dataset encompasses extensive long-term monitoring data from the Basque Country, focusing on assessing the responsiveness of 83 environmental variables across water, sediment, biota, phytoplankton, macroinvertebrates, and fish. It includes metadata and biodiversity data from various aquatic environments, detailing site-specific identifiers, sampling methods, and instruments used. The dataset is crucial for understanding trends in environmental quality and the effects of human pressures and management actions over time.",
  "distribution": [
    {
      "@id": "resources/AUTHORS",
      "@type": "FileObject",
      "contentSize": "1742",
      "contentUrl": "https://sen.science/doi/10.71728/r1rj-f947/AUTHORS.csv",
      "description": "Contains information about authors, including their affiliations, contact details, and institutional information, primarily from AZTI in Spain.",
      "encodingFormat": "text/csv",
      "name": "AUTHORS.csv",
      "sha256": "2ebf316803d056aa3f8471c19458db744d41189c095eb9dc3b656b63a45b810c"
    }
  ]
}