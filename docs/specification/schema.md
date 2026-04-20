# FAIR² Schema

---

## schema:DatasetShape
*Targets:* `schema:Dataset`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `schema:distribution` | `schema:DataDownload`/`schema:FileObject` | `[1..∞]` | Yes |
| `cr:recordSet` | `RecordSet` | `[1..∞]` | Yes |
| `schema:description` | `xsd:string` | `[1..∞]` | Yes |
| `schema:license` | `xsd:anyURI` | `[1..∞]` | Yes |
| `schema:name` | `xsd:string` | `[1..∞]` | Yes |
| `schema:url` | `xsd:anyURI` | `[1..∞]` | Yes |
| `dct:conformsTo` | `fair2s:IdentifierShape` | `[1..∞]` | Yes |

<details><summary>Constraint notes</summary>

- **schema:distribution**: A dataset must have at least one distribution.
- **cr:recordSet**: A dataset must have at least one record set.
- **schema:description**: A dataset must have a description.
- **schema:license**: A dataset must have a license.
- **schema:name**: A dataset must have a name.
- **schema:url**: A dataset must have a URL.
- **dct:conformsTo**: A dataset must reference the URI of the FAIR² specification version it conforms to.

</details>


## fair2s:DatasetShape
*Targets:* `schema:Dataset`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `schema:accessRights` | `fair2s:AccessRightsShape` | `[0..∞]` | No |
| `cr:citeAs` | `xsd:string` | `[0..∞]` | No |
| `fair2:changeLog` | `fair2s:UpdateActionShape` | `[0..∞]` | No |
| `fair2:dataArchive` | `fair2s:DataArchiveShape` | `[0..∞]` | No |
| `fair2:dataArticle` | `fair2s:ArticleShape` | `[1..∞]` | Yes |
| `fair2:dataPortal` | `fair2s:DataPortalShape` | `[0..∞]` | No |
| `fair2:domain` | `fair2s:DomainShape` | `[0..∞]` | No |
| `fair2:methodSection` | `fair2s:MethodSectionShape` | `[0..∞]` | No |
| `fair2s:socialMedia` | `fair2s:SocialMediaShape` | `[0..∞]` | No |
| `cr:recordSet` | `fair2s:RecordSetShape` | `[0..∞]` | No |
| `schema:contributor` | `fair2s:ContributorShape` | `[0..∞]` | No |
| `schema:creator` | `fair2s:PersonOrOrganizationShape` | `[1..∞]` | Yes |
| `schema:dateCreated` | `xsd:date` | `[0..∞]` | No |
| `schema:datePublished` | `xsd:date` | `[0..∞]` | No |
| `schema:dateUpdated` | `xsd:date` | `[0..∞]` | No |
| `schema:description` | `fair2s:TextShape` | `[1..∞]` | Yes |
| `schema:distribution` | `fair2s:DistributionShape` | `[1..∞]` | Yes |
| `schema:funding` | `fair2s:GrantShape` | `[0..∞]` | No |
| `schema:identifier` | `fair2s:IdentifierShape` | `[1..∞]` | Yes |
| `schema:keywords` | `fair2s:TextShape` | `[1..∞]` | Yes |
| `schema:license` | `fair2s:IdentifierShape` | `[1..∞]` | Yes |
| `schema:name` | `fair2s:TextShape` | `[1..∞]` | Yes |
| `schema:spatialCoverage` | `fair2s:SpatialCoverageShape` | `[0..∞]` | No |
| `schema:subjectOf` | `fair2s:CreativeWorkShape` | `[0..∞]` | No |
| `schema:temporalCoverage` | `fair2s:TextShape` | `[0..∞]` | No |
| `schema:url` | `fair2s:IdentifierShape` | `[1..∞]` | Yes |
| `schema:version` | `fair2s:TextShape` | `[1..∞]` | Yes |

<details><summary>Constraint notes</summary>

- **schema:accessRights**: Dataset may specify access rights (e.g., FAIR² Agreement Level).
- **cr:citeAs**: Dataset may include a full 'cite as' text citation.
- **fair2:changeLog**: Dataset may include a structured changelog for version history.
- **fair2:dataArchive**: Dataset may be linked to one or more Data Archives for long-term preservation.
- **fair2:dataArticle**: Dataset must be linked to at least one Data Article (Scholarly Article).
- **fair2:dataPortal**: Dataset may be linked to one or more Data Portals providing access to the data.
- **fair2:domain**: Dataset may declare the domain(s) it belongs to (e.g., marine science).
- **fair2:methodSection**: Dataset may include one or more method sections describing methodology.
- **fair2s:socialMedia**: Dataset may include social media dissemination metadata.
- **cr:recordSet**: Dataset may include one or more RecordSet definitions.
- **schema:contributor**: Dataset may include contributor metadata and CRediT roles.
- **schema:creator**: Dataset must include at least one creator (Person or Organization).
- **schema:dateCreated**: Dataset may include its creation date.
- **schema:datePublished**: Dataset may include its publication date.
- **schema:dateUpdated**: Dataset may include its last updated date.
- **schema:description**: Dataset must include a description.
- **schema:distribution**: Dataset must have at least one distribution (file object).
- **schema:funding**: Dataset may include one or more funding entries.
- **schema:identifier**: Dataset must include a persistent identifier (e.g., DOI URI).
- **schema:keywords**: Dataset must include at least one keyword.
- **schema:license**: Dataset must declare an open license IRI.
- **schema:name**: Dataset must include a name.
- **schema:spatialCoverage**: Dataset may specify spatial coverage information.
- **schema:subjectOf**: Dataset may reference CreativeWorks (e.g., landing page, sameAs links).
- **schema:temporalCoverage**: Dataset may specify the temporal coverage (e.g., 1995–2023).
- **schema:url**: Dataset must include its canonical landing-page URL.
- **schema:version**: Dataset must specify its version.

</details>



## fair2s:DistributionShape
| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `cr:sha256` | `xsd:string` | `[1..∞]` | Yes |
| `schema:contentUrl` | `xsd:anyURI` | `[1..∞]` | Yes |
| `schema:encodingFormat` | `xsd:string` | `[1..∞]` | Yes |

<details><summary>Constraint notes</summary>

- **cr:sha256**: Each distribution must have a SHA-256 checksum.
- **schema:contentUrl**: Each distribution must have a content URL.
- **schema:encodingFormat**: Each distribution must specify its encoding format.

</details>


## fair2s:AccessRightsShape
*Targets:* `schema:DefinedTerm`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `@id` | `sh:IRI` | `[0..∞]` | No |
| `schema:name` | `xsd:string` | `[1..∞]` | Yes |
| `schema:url` | `sh:IRI` | `[0..∞]` | No |
| `skos:definition` | `xsd:string` | `[1..∞]` | Yes |
| `skos:note` | `xsd:string` | `[0..∞]` | No |

<details><summary>Constraint notes</summary>

- **@id**: AccessRights @id should be a FAIR² AgreementLevels URI.
- **schema:name**: AccessRights must have a name (e.g., 'Open Access').
- **schema:url**: AccessRights URL must point to a FAIR² Agreement Level definition (1–4).
- **skos:definition**: AccessRights must provide a definition describing the access conditions.
- **skos:note**: AccessRights may include a note clarifying additional access information.

</details>


## fair2s:AuthorShape
*Targets:* `schema:Person`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `schema:affiliation` | `fair2s:OrganizationShape` | `[1..∞]` | Yes |
| `schema:identifier` | `` | `[1..∞]` | Yes |
| `schema:name` | `xsd:string` | `[1..∞]` | Yes |

<details><summary>Constraint notes</summary>

- **schema:affiliation**: Each author must be affiliated with at least one organization.
- **schema:identifier**: Each author must include an identifier, preferably an ORCID.
- **schema:name**: Each author must have a name.

</details>


## fair2s:ChangeDescriptionShape
| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `fair2:bugFixes` | `xsd:string` | `[0..∞]` | No |
| `fair2:improvements` | `xsd:string` | `[0..∞]` | No |
| `fair2:newFeatures` | `xsd:string` | `[0..∞]` | No |
| `fair2:otherInformation` | `xsd:string` | `[0..∞]` | No |

<details><summary>Constraint notes</summary>

- **fair2:bugFixes**: Description may include bugFixes as a list of strings.
- **fair2:improvements**: Description may include improvements as a list of strings.
- **fair2:newFeatures**: Description may include newFeatures as a list of strings.
- **fair2:otherInformation**: Description may include otherInformation such as version notes or license changes.

</details>


## fair2s:ChangeLogShape
*Targets:* `schema:UpdateAction`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `prov:wasRevisionOf` | `fair2s:RevisionShape` | `[0..∞]` | No |
| `schema:datePublished` | `xsd:date` | `[1..∞]` | Yes |
| `schema:description` | `fair2s:ChangeDescriptionShape` | `[1..∞]` | Yes |

<details><summary>Constraint notes</summary>

- **prov:wasRevisionOf**: Each changelog entry may reference the previous dataset version using prov:wasRevisionOf.
- **schema:datePublished**: Each changelog entry must include a publication date.
- **schema:description**: Each changelog entry must include a structured description of changes.

</details>


## fair2s:ContributionShape
*Targets:* `schema:Contribution`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `prov:agent` | `fair2s:AuthorShape` | `[1..∞]` | Yes |
| `prov:hadRole` | `fair2s:ContributorRoleShape` | `[1..∞]` | Yes |

<details><summary>Constraint notes</summary>

- **prov:agent**: Each contribution must reference at least one agent (Person or Organization).
- **prov:hadRole**: Each contribution must include at least one role.

</details>


## fair2s:ContributorRoleShape
| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `@id` | `sh:IRI` | `[1..∞]` | Yes |
| `rdfs:label` | `xsd:string` | `[1..∞]` | Yes |

<details><summary>Constraint notes</summary>

- **@id**: Each role must have an IRI identifier, typically from CRO or FAIR² namespace.
- **rdfs:label**: Each role must have a human-readable label (e.g., DataCuration, Supervision).

</details>


## fair2s:DataArticleShape
*Targets:* `schema:ScholarlyArticle`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `prov:wasDerivedFrom` | `sh:IRI` | `[1..∞]` | Yes |
| `schema:datePublished` | `xsd:date` | `[1..∞]` | Yes |
| `schema:name` | `xsd:string` | `[1..∞]` | Yes |
| `schema:publication` | `fair2s:PublicationShape` | `[1..∞]` | Yes |
| `schema:publisher` | `fair2s:PublisherShape` | `[1..∞]` | Yes |
| `schema:version` | `xsd:string` | `[1..∞]` | Yes |
| `fair2:changeLog` | `fair2s:UpdateActionShape` | `[0..∞]` | No |

<details><summary>Constraint notes</summary>

- **prov:wasDerivedFrom**: Data article must reference the dataset DOI or persistent identifier.
- **schema:datePublished**: Data article must have a publication date.
- **schema:name**: Data article must include a title.
- **schema:publication**: Data article must reference a publication (journal or periodical).
- **schema:publisher**: Data article must specify a publisher organization.
- **schema:version**: Data article must specify its version (e.g., '1.0').
- **fair2:changeLog**: Data article may include a structured changelog for version history.

</details>


## fair2s:DataPortalShape
*Targets:* `fair2:DataPortal`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `schema:name` | `xsd:string` | `[1..∞]` | Yes |
| `schema:description` | `xsd:string` | `[1..∞]` | Yes |
| `schema:identifier` | `fair2s:IdentifierShape` | `[1..∞]` | Yes |
| `schema:version` | `xsd:string` | `[1..∞]` | Yes |
| `schema:url` | `sh:IRI` | `[1..∞]` | Yes |
| `schema:keywords` | `xsd:string` | `[1..∞]` | Yes |
| `schema:author` | `fair2s:PersonOrOrganizationShape` | `[1..∞]` | Yes |
| `schema:dateCreated` | `xsd:date` | `[0..∞]` | No |
| `schema:datePublished` | `xsd:date` | `[0..∞]` | No |
| `schema:dateUpdated` | `xsd:date` | `[0..∞]` | No |
| `fair2:changeLog` | `fair2s:UpdateActionShape` | `[0..∞]` | No |
| `fair2:dataset` | `fair2s:IdentifierShape` | `[0..∞]` | No |

<details><summary>Constraint notes</summary>

- **schema:name**: Data portal must include a name.
- **schema:description**: Data portal must include a description.
- **schema:identifier**: Data portal must include a persistent identifier (e.g., URL or DOI).
- **schema:version**: Data portal must specify its version.
- **schema:url**: Data portal must include a URL pointing to the portal's web address.
- **schema:keywords**: Data portal must include at least one keyword.
- **schema:author**: Data portal must include at least one author or maintaining organization.
- **schema:dateCreated**: Data portal may include its creation date.
- **schema:datePublished**: Data portal may include its publication date.
- **schema:dateUpdated**: Data portal may include its last updated date.
- **fair2:changeLog**: Data portal may include a structured changelog for version history.
- **fair2:dataset**: Data portal may reference the dataset(s) it provides access to.

</details>


## fair2s:DataArchiveShape
*Targets:* `fair2:DataArchive`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `schema:name` | `xsd:string` | `[1..∞]` | Yes |
| `schema:description` | `xsd:string` | `[1..∞]` | Yes |
| `schema:identifier` | `fair2s:IdentifierShape` | `[1..∞]` | Yes |
| `schema:version` | `xsd:string` | `[1..∞]` | Yes |
| `schema:keywords` | `xsd:string` | `[1..∞]` | Yes |
| `schema:holdingArchive` | `fair2s:IdentifierShape` | `[1..∞]` | Yes |
| `schema:author` | `fair2s:PersonOrOrganizationShape` | `[1..∞]` | Yes |
| `schema:dateCreated` | `xsd:date` | `[0..∞]` | No |
| `schema:datePublished` | `xsd:date` | `[0..∞]` | No |
| `schema:dateUpdated` | `xsd:date` | `[0..∞]` | No |
| `fair2:changeLog` | `fair2s:UpdateActionShape` | `[0..∞]` | No |
| `fair2:dataset` | `fair2s:IdentifierShape` | `[0..∞]` | No |

<details><summary>Constraint notes</summary>

- **schema:name**: Data archive must include a name.
- **schema:description**: Data archive must include a description.
- **schema:identifier**: Data archive must include a persistent identifier (e.g., DOI or URL).
- **schema:version**: Data archive must specify its version.
- **schema:keywords**: Data archive must include at least one keyword.
- **schema:holdingArchive**: Data archive must reference the institution responsible for holding the archive (e.g., Zenodo, SEANOE).
- **schema:author**: Data archive must include at least one author or responsible organization.
- **schema:dateCreated**: Data archive may include its creation date.
- **schema:datePublished**: Data archive may include its publication date.
- **schema:dateUpdated**: Data archive may include its last updated date.
- **fair2:changeLog**: Data archive may include a structured changelog for version history.
- **fair2:dataset**: Data archive may reference the dataset(s) it stores.

</details>


## fair2s:DomainShape
*Targets:* `schema:Thing`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `@id` | `sh:IRI` | `[0..∞]` | No |
| `prov:wasAttributedTo` | `fair2s:AuthorShape` | `[1..∞]` | Yes |
| `schema:name` | `xsd:string` | `[1..∞]` | Yes |

<details><summary>Constraint notes</summary>

- **@id**: Domain entries should ideally reference a controlled vocabulary (e.g., Wikidata).
- **prov:wasAttributedTo**: Each domain should be attributed to at least one Person (creator or expert).
- **schema:name**: Each domain entry must include a name (e.g., 'Marine Biology').

</details>


## fair2s:FieldShape
*Targets:* `cr:Field`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `cr:dataType` | `` | `[1..∞]` | Yes |
| `fair2:statistics` | `` | `[1..∞]` | Yes |
| `fair2:unit` | `` | `[1..∞]` | Yes |
| `schema:description` | `xsd:string` | `[1..∞]` | Yes |
| `schema:name` | `xsd:string` | `[1..∞]` | Yes |

<details><summary>Constraint notes</summary>

- **cr:dataType**: Each Field must specify a dataType (e.g., Text, Integer, Float, Date).
- **fair2:statistics**: Each Field should include descriptive statistics (count, missing values, etc.).
- **fair2:unit**: Each Field should specify a measurement unit, using QUDT or equivalent controlled vocabulary.
- **schema:description**: Each Field must include a human-readable description.
- **schema:name**: Each Field must have a name.

</details>


## fair2s:FundingOrganizationShape
*Targets:* `schema:Organization`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `schema:identifier` | `` | `[1..∞]` | Yes |
| `schema:name` | `xsd:string` | `[1..∞]` | Yes |

<details><summary>Constraint notes</summary>

- **schema:identifier**: Funding organization should include an identifier (e.g., ROR ID).
- **schema:name**: Funding organization must include a name.

</details>


## fair2s:FundingSchemeShape
*Targets:* `schema:FundingScheme`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `schema:identifier` | `` | `[1..∞]` | Yes |
| `schema:name` | `xsd:string` | `[1..∞]` | Yes |

<details><summary>Constraint notes</summary>

- **schema:identifier**: Funding scheme must include an identifier (e.g., Horizon Europe code).
- **schema:name**: Funding scheme must include a name.

</details>


## fair2s:FundingShape
*Targets:* `schema:Grant`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `schema:funder` | `fair2s:FundingOrganizationShape` | `[1..∞]` | Yes |
| `schema:fundingScheme` | `fair2s:FundingSchemeShape` | `[0..1]` | No |
| `schema:name` | `xsd:string` | `[1..∞]` | Yes |
| `schema:url` | `sh:IRI` | `[0..1]` | No |

<details><summary>Constraint notes</summary>

- **schema:funder**: Each funding entry must specify at least one funder organization.
- **schema:fundingScheme**: If provided, fundingScheme must contain valid scheme metadata.
- **schema:name**: Each funding entry must include a grant name or title.
- **schema:url**: Funding entries may optionally include a URL (e.g., project page).

</details>


## fair2s:MethodShape
*Targets:* `fair2:MethodSection`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `fair2:step` | `fair2s:StepShape` | `[1..∞]` | Yes |
| `schema:description` | `xsd:string` | `[0..∞]` | No |
| `schema:name` | `xsd:string` | `[1..∞]` | Yes |
| `fair2:next` | `sh:IRI` | `[0..1]` | No |
| `prov:used` | `sh:IRI` | `[0..∞]` | No |

<details><summary>Constraint notes</summary>

- **fair2:step**: Each MethodSection must contain at least one Step.
- **schema:description**: Each MethodSection may include a description summarizing the methodological context.
- **schema:name**: Each MethodSection must include a section name.
- **fair2:next**: MethodSection may reference the next section by IRI.
- **prov:used**: MethodSection may reference source documents or scripts (DigitalDocument or SoftwareSourceCode nodes) that were consulted during this section.

</details>


## fair2s:OrganizationShape
*Targets:* `schema:Organization`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `schema:address` | `xsd:string` | `[1..∞]` | Yes |
| `schema:identifier` | `` | `[1..∞]` | Yes |
| `schema:name` | `xsd:string` | `[1..∞]` | Yes |

<details><summary>Constraint notes</summary>

- **schema:address**: Organization should include a postal address.
- **schema:identifier**: Organization should include a persistent identifier (e.g., ROR).
- **schema:name**: Organization must have a name.

</details>


## fair2s:PublicationShape
*Targets:* `schema:Periodical`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `schema:name` | `xsd:string` | `[1..∞]` | Yes |

<details><summary>Constraint notes</summary>

- **schema:name**: Publication must include a name (journal or periodical title).

</details>


## fair2s:PublisherShape
*Targets:* `schema:Organization`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `schema:name` | `xsd:string` | `[1..∞]` | Yes |

<details><summary>Constraint notes</summary>

- **schema:name**: Publisher organization must include a name.

</details>


## fair2s:RecordSetShape
*Targets:* `cr:RecordSet`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `cr:field` | `fair2s:FieldShape` | `[1..∞]` | Yes |
| `schema:description` | `xsd:string` | `[1..∞]` | Yes |
| `schema:name` | `xsd:string` | `[1..∞]` | Yes |

<details><summary>Constraint notes</summary>

- **cr:field**: Each RecordSet must define at least one Field.
- **schema:description**: Each RecordSet must include a description.
- **schema:name**: Each RecordSet must have a name (e.g., 'WATER', 'SEDIMENTS').

</details>


## fair2s:RevisionShape
*Targets:* `schema:Dataset`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `schema:identifier` | `sh:IRI` | `[1..∞]` | Yes |
| `schema:version` | `xsd:string` | `[1..∞]` | Yes |

<details><summary>Constraint notes</summary>

- **schema:identifier**: Revision reference must include a persistent identifier (e.g., DOI).
- **schema:version**: Revision reference must include a version label.

</details>


## fair2s:SocialMediaShape
*Targets:* `schema:SocialMediaPosting`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `schema:accountServiceHomePage` | `sh:IRI` | `[1..∞]` | Yes |
| `schema:articleBody` | `xsd:string` | `[1..∞]` | Yes |
| `schema:datePublished` | `xsd:date` | `[0..∞]` | No |
| `schema:identifier` | `xsd:string` | `[1..∞]` | Yes |
| `schema:keywords` | `xsd:string` | `[1..∞]` | Yes |
| `schema:url` | `sh:IRI` | `[0..∞]` | No |

<details><summary>Constraint notes</summary>

- **schema:accountServiceHomePage**: Each entry must specify the social media service homepage as an IRI (e.g., 'https://twitter.com/').
- **schema:articleBody**: Each entry must include the message text or post body.
- **schema:datePublished**: Optionally, entries may record the publication date of the social media post.
- **schema:identifier**: Each social media entry must have a platform identifier (e.g., 'twitter', 'linkedin').
- **schema:keywords**: Each entry must list at least one keyword or tag describing its content.
- **schema:url**: Optionally, entries may include a direct URL to the social post or related resource.

</details>


## fair2s:SpatialCoverageShape
*Targets:* `schema:Place`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `schema:geo` | `sh:BlankNodeOrIRI` | `[0..∞]` | No |
| `schema:name` | `xsd:string` | `[1..∞]` | Yes |

<details><summary>Constraint notes</summary>

- **schema:geo**: Spatial coverage may include a geo reference.
- **schema:name**: Spatial coverage must include a place name.

</details>


## fair2s:StepShape
*Targets:* `fair2:Step`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `fair2:generated` | `sh:IRI` | `[0..∞]` | No |
| `fair2:next` | `sh:IRI` | `[0..∞]` | No |
| `fair2:substep` | `fair2s:SubStepShape` | `[0..∞]` | No |
| `prov:used` | `sh:IRI` | `[0..∞]` | No |
| `schema:description` | `xsd:string` | `[0..∞]` | No |
| `schema:name` | `xsd:string` | `[1..∞]` | Yes |

<details><summary>Constraint notes</summary>

- **fair2:generated**: If provided, 'generated' should reference produced data elements (e.g., fields, recordSets) by IRI.
- **fair2:next**: If provided, 'next' should reference the following step using an IRI.
- **fair2:substep**: Substeps may be defined as nested procedural components.
- **prov:used**: Step may reference source documents or scripts (DigitalDocument or SoftwareSourceCode nodes) that were used as inputs for this step.
- **schema:description**: Each Step may include a description detailing actions or parameters.
- **schema:name**: Each Step must include a name.

</details>


## fair2s:SubStepShape
*Targets:* `fair2:Substep`

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `fair2:next` | `sh:IRI` | `[0..∞]` | No |
| `prov:used` | `sh:IRI` | `[0..∞]` | No |
| `schema:description` | `xsd:string` | `[0..∞]` | No |
| `schema:name` | `xsd:string` | `[1..∞]` | Yes |

<details><summary>Constraint notes</summary>

- **fair2:next**: If provided, 'next' should reference the subsequent substep.
- **prov:used**: Substep may reference source documents or scripts used as inputs.
- **schema:description**: Each Substep may include a descriptive text.
- **schema:name**: Each Substep must include a name.

</details>


## fair2s:DigitalDocumentShape
*Targets:* `schema:DigitalDocument`

Source documents referenced via `prov:used` in method sections and steps (e.g., READMEs, data dictionaries, protocol specifications).

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `schema:name` | `xsd:string` | `[1..∞]` | Yes |
| `schema:pagination` | `xsd:string` | `[0..∞]` | No |
| `schema:encodingFormat` | `xsd:string` | `[0..∞]` | No |
| `schema:url` | `sh:IRI` | `[0..1]` | No |

<details><summary>Constraint notes</summary>

- **schema:name**: Document must have a human-readable name.
- **schema:pagination**: Relative file path to the document within the dataset package (repurposed from schema.org).
- **schema:encodingFormat**: MIME type of the document (e.g., `text/markdown`, `text/csv`).
- **schema:url**: Optionally, a persistent URL for the document.

</details>


## fair2s:SoftwareSourceCodeShape
*Targets:* `schema:SoftwareSourceCode`

Scripts and code files used or produced by method steps, referenced via `prov:used` or `fair2:generated`.

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `schema:name` | `xsd:string` | `[1..∞]` | Yes |
| `schema:identifier` | `xsd:string` | `[0..∞]` | No |
| `schema:encodingFormat` | `xsd:string` | `[0..∞]` | No |
| `schema:url` | `sh:IRI` | `[0..1]` | No |
| `schema:programmingLanguage` | `xsd:string` | `[0..∞]` | No |
| `schema:runtimePlatform` | `xsd:string` | `[0..∞]` | No |

<details><summary>Constraint notes</summary>

- **schema:name**: Script must have a human-readable name (e.g., filename).
- **schema:identifier**: Relative path or persistent identifier for the script.
- **schema:encodingFormat**: MIME type of the source file (e.g., `text/x-python`).
- **schema:url**: Optionally, a URL pointing to the script.
- **schema:programmingLanguage**: Programming language used (e.g., `Python`, `R`).
- **schema:runtimePlatform**: Runtime environment (e.g., `Python 3.11`, `R 4.3`).

</details>


## fair2s:ActivityShape
*Targets:* `prov:Activity`

A computational or manual activity that uses inputs and produces outputs. Activities link agents to the data they generate.

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `rdfs:label` | `xsd:string` | `[1..∞]` | Yes |
| `prov:wasAssociatedWith` | `sh:IRI` | `[0..∞]` | No |
| `schema:startTime` | `xsd:dateTime` | `[0..1]` | No |
| `schema:endTime` | `xsd:dateTime` | `[0..1]` | No |

<details><summary>Constraint notes</summary>

- **rdfs:label**: Activity must have a human-readable name describing the computation or process.
- **prov:wasAssociatedWith**: Activity may reference one or more responsible agents (SoftwareAgent, Person, Organization).
- **schema:startTime**: Activity may record when it began.
- **schema:endTime**: Activity may record when it completed.

</details>


## fair2s:SoftwareAgentShape
*Targets:* `prov:SoftwareAgent`

A software tool or application that performed an activity. Software agents are responsible for automated data processing, extraction, and transformation steps.

| Property | Type | Cardinality | Mandatory |
|---|---|---|---|
| `schema:name` | `xsd:string` | `[1..∞]` | Yes |
| `schema:identifier` | `fair2s:IdentifierShape` | `[0..∞]` | No |
| `schema:softwareVersion` | `xsd:string` | `[0..∞]` | No |
| `schema:programmingLanguage` | `xsd:string` | `[0..∞]` | No |

<details><summary>Constraint notes</summary>

- **schema:name**: Software agent must have a name (e.g., `Pandas`, `R`, `CESM2.2`).
- **schema:identifier**: Software agent may include a persistent identifier or homepage URL.
- **schema:softwareVersion**: Software agent may specify its version (e.g., `2.1.1`).
- **schema:programmingLanguage**: Software agent may specify its implementation language.

</details>
