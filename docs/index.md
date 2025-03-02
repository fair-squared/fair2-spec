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
    "@id": "https://example.org/dataset/12345",
    "@type": "Dataset",
    "author": [
        {
            "@id": "/authors/abc123",
            "@type": "Person",
            "affiliation": [
                {
                    "@id": "/organizations/xyz789",
                    "@type": "Organization",
                    "address": "123 Research Lane, Science City, Country",
                    "name": "Institute of Data Science"
                }
            ],
            "name": "Jane Doe"
        }
    ],
    "citation": "https://doi.org/10.1234/example.2024.56789",
    "citeAs": "Doe J, Smith A, Johnson R, et al. (2024). Example Dataset for Research Purposes. Journal of Data Science. 1:56789. doi: 10.1234/example.2024.56789",
    "conformsTo": "http://example.org/spec/1.0",
    "contentUrl": "example_dataset.json",
    "datePublished": "2024-01-01",
    "description": "This dataset includes sample data for research purposes, covering various aspects of data science and analytics. It provides metadata and detailed descriptions of the data collection methods and instruments used.",
    "distribution": [
        {
            "@id": "resources/DATA",
            "@type": "FileObject",
            "contentSize": "2048",
            "contentUrl": "https://example.org/dataset/12345/DATA.csv",
            "description": "Contains the main dataset, including all relevant data points and metadata.",
            "encodingFormat": "text/csv",
            "name": "DATA.csv",
            "sha256": "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890"
        }
    ]
}