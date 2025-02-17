# Shapes Directory

This directory contains JSON files that define SHACL shapes for various entities. SHACL (Shapes Constraint Language) is used to validate RDF data against a set of conditions.

## Files

### `author.json`
Defines the shape for authors, including both individuals and organizations.

- **PersonShape**: Validates that a person has an optional affiliation and a name.
- **OrganizationShape**: Validates that an organization has a name.

### `fair2_data_package.json`
Defines the shape for a FAIR data package.

- **DatasetShape**: Ensures that a dataset has at least one author and is of type `Dataset`.

### `methods.json`
Defines the shape for methods sections and steps.

- **MethodsSectionShape**: Validates that a methods section has a name and at least one step.
- **MethodsStepShape**: Validates that a step has a name and description.

### `submission.json`
Defines the shape for submissions.

- **SubmissionShape**: Ensures that a submission is based on at least two creative works, scholarly articles, or datasets. If based on a dataset, it must have a distribution and record set.

### `visualizations.json`
Defines the shape for visualizations.

- **VisualizationsShape**: Ensures that a dataset has at least four visualizations.

## Usage

These shapes can be used to validate RDF data to ensure it conforms to the expected structure and constraints defined in each shape.

For more information on SHACL, visit the [SHACL specification](https://www.w3.org/TR/shacl/).