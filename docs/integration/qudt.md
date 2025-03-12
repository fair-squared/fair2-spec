# FAIR² and QUDT Integration

## 🎯 Overview

FAIR² integrates **QUDT (Quantities, Units, Dimensions, and Types)** to ensure datasets use **standardized measurement units**.  
This improves **data interpretability, interoperability, and AI-readiness** by:

✅ Providing **consistent unit definitions** across datasets.  
✅ Supporting **machine-actionable unit metadata** for AI and ML workflows.  
✅ Aligning with **scientific and engineering data standards**.  

---

## 📌 **How FAIR² Uses QUDT**
QUDT ensures that **dataset attributes and values are properly annotated with units**, preventing misinterpretation.

| **FAIR² Property** | **QUDT Mapping** | **Description** |
|-----------------|------------------|----------------|
| `cr:Field` | `qudt:QuantityKind` | Defines the **type of measurement** (e.g., `Temperature`, `Mass`). |
| `cr:unitCode` | `qudt:Unit` | Specifies the **unit of measurement** (e.g., `qudt:DegreeCelsius`). |
| `cr:format` | `xsd:string` | Defines the **data format** for numeric fields (e.g., decimal precision). |

---

## 🔍 **Example: JSON-LD with QUDT Integration**
```json
{
  "@context": [
    "https://qudt.org/vocab/unit",
    "https://fair2.ai/ns/"
  ],
  "@type": "Dataset",
  "name": "Climate Sensor Data",
  "description": "Temperature and humidity readings from a weather station.",
  "cr:recordSet": {
    "@type": "RecordSet",
    "cr:fields": [
      {
        "@type": "Field",
        "name": "Temperature",
        "cr:dataType": "xsd:float",
        "cr:unitCode": "qudt:DegreeCelsius",
        "cr:format": "##.##"
      },
      {
        "@type": "Field",
        "name": "Humidity",
        "cr:dataType": "xsd:float",
        "cr:unitCode": "qudt:Percent",
        "cr:format": "##.#"
      }
    ]
  }
}
```

✅ Ensures unit consistency – Uses QUDT for standardized units.
✅ Improves AI-readiness – Supports structured, machine-readable metadata.
✅ Enhances data interoperability – Allows seamless unit conversions.

---

## 📌 Why QUDT Matters for FAIR²
- 📏 Prevents unit ambiguity – Standardizes how units are expressed.
- 🔄 Enhances data processing – Supports automated unit conversions.
- 🤖 Machine-readable metadata – AI models can understand and process unit metadata.

---

## 🚀 Next Steps

1️⃣ [Explore the FAIR² Schema](../specification/schema.md) – Learn about dataset structure.
2️⃣ [Learn about ML Croissant Integration](./ml-croissant.md) – How FAIR² builds on Croissant.
3️⃣ [Validate Datasets](../specification/shacl-validation.md) – Ensure compliance with QUDT standards.
