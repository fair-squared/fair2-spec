# **Using QUDT and OM in the FAIR² Specification**

## **Introduction**
This document provides guidance on how **QUDT (Quantities, Units, Dimensions, and Data Types)** and **OM (Ontology of Units of Measure)** are integrated within the **FAIR² (FAIR SQUARED) framework** to ensure semantic interoperability of measurement units in AI-ready datasets.

## **Why QUDT and OM Are Used in FAIR²**
FAIR² builds upon the FAIR principles to enhance scientific datasets with **context-rich metadata**, **AI-ready design**, and **Responsible AI alignment**. Measurement units are critical for FAIR compliance, and both **QUDT** and **OM** provide robust RDF/OWL representations for handling units in a standardized way.

### **QUDT and OM in FAIR²**

| Feature | QUDT | OM |
|---------|------|----|
| **Primary Focus** | Engineering, aerospace, industry, geospatial | Scientific precision, research |
| **RDF/OWL Compatible** | ✅ Yes | ✅ Yes |
| **Unit Conversions** | ✅ Yes (via `qudt:conversionMultiplier`) | ✅ Yes (via `om:hasConversionFactor`) |
| **Temperature Conversions (e.g., F → C)** | ❌ No | ✅ Yes (`om:hasOffset`) |
| **Complex Derived Units (e.g., m/s²)** | ❌ No | ✅ Yes (`om:derivedFromUnit`) |
| **Industry Adoption** | NASA, OGC, IoT, digital twins | Research, EOSC |

## **How FAIR² Uses QUDT and OM**
### **1. Representing Quantities and Units**
FAIR² integrates QUDT and OM to ensure standardized unit representation in RDF/OWL. Below are examples of how they are applied in FAIR².

#### **QUDT Representation**
```jsonld
{
  "@context": {
    "qudt": "http://qudt.org/schema/qudt/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ex": "http://example.org/"
  },
  "@id": "ex:measurement1",
  "@type": "qudt:QuantityValue",
  "qudt:numericValue": {
    "@value": "1000.0",
    "@type": "xsd:double"
  },
  "qudt:unit": {
    "@id": "qudt:Meter"
  }
}
```
#### **OM Representation**
```jsonld
{
  "@context": {
    "om": "http://www.ontology-of-units-of-measure.org/resource/om-2/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ex": "http://example.org/"
  },
  "@id": "ex:measurement2",
  "@type": "om:Measurement",
  "om:hasValue": {
    "@value": "1000.0",
    "@type": "xsd:double"
  },
  "om:hasUnit": {
    "@id": "om:Meter"
  }
}
```
### **2. Ensuring Unit Consistency**
When using both QUDT and OM, FAIR² ensures that units are consistently mapped:
```jsonld
{
  "@context": {
    "qudt": "http://qudt.org/schema/qudt/",
    "om": "http://www.ontology-of-units-of-measure.org/resource/om-2/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ex": "http://example.org/"
  },
  "@id": "ex:measurement3",
  "@type": ["qudt:QuantityValue", "om:Measurement"],
  "qudt:numericValue": {
    "@value": "1.0",
    "@type": "xsd:double"
  },
  "qudt:unit": {
    "@id": "qudt:Kilometer"
  },
  "om:hasValue": {
    "@value": "1000.0",
    "@type": "xsd:double"
  },
  "om:hasUnit": {
    "@id": "om:Meter"
  }
}
```

### **3. Handling Unit Conversions**
#### **QUDT-based conversion**
```jsonld
{
  "@context": {
    "qudt": "http://qudt.org/schema/qudt/",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "qudt:Kilometer",
  "@type": "qudt:Unit",
  "qudt:conversionMultiplier": {
    "@value": "1000.0",
    "@type": "xsd:double"
  }
}
```
#### **OM-based conversion (explicit conversion factors)**
```jsonld
{
  "@context": {
    "om": "http://www.ontology-of-units-of-measure.org/resource/om-2/",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "om:Kilometer",
  "@type": "om:Unit",
  "om:hasConversionFactor": {
    "@type": "om:ConversionFactor",
    "om:hasNumericalValue": {
      "@value": "1000.0",
      "@type": "xsd:double"
    },
    "om:hasUnit": {
      "@id": "om:Meter"
    }
  }
}
```

### **4. Validating Units with SHACL**
FAIR² employs **SHACL validation** to enforce unit correctness and conversions. Below is a SHACL shape for validating unit consistency between QUDT and OM.
```jsonld
{
  "@context": {
    "sh": "http://www.w3.org/ns/shacl#",
    "qudt": "http://qudt.org/schema/qudt/",
    "om": "http://www.ontology-of-units-of-measure.org/resource/om-2/",
    "ex": "http://example.org/"
  },
  "@id": "ex:UnitConsistencyShape",
  "@type": "sh:NodeShape",
  "sh:targetClass": {
    "@id": "qudt:Unit"
  },
  "sh:property": {
    "sh:path": {
      "@id": "om:hasUnit"
    },
    "sh:class": {
      "@id": "om:Unit"
    },
    "sh:maxCount": 1,
    "sh:message": "If an OM unit is used alongside a QUDT unit, they should be equivalent."
  }
}
```

## **Best Practices for FAIR² Integration**
1. **Use QUDT for broad interoperability**, especially in **industry, geospatial, and IoT applications**.
2. **Use OM for scientific and research-based measurements**, particularly **biomedical and physical sciences**.
3. **Ensure unit consistency** when using both ontologies in the same dataset.
4. **Validate unit correctness with SHACL** to ensure data quality.
5. **Adopt conversion multipliers carefully**, using `qudt:conversionMultiplier` for simple unit scaling and `om:hasConversionFactor` for complex derivations.

## **Conclusion**
FAIR² **integrates QUDT and OM** to enhance **machine-readability**, **semantic clarity**, and **interoperability** of datasets. By enforcing SHACL validation and ensuring accurate unit representation, FAIR² supports AI-ready, FAIR-compliant datasets across multiple domains.


