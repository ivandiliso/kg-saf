# KG-SaF Requirements

## 1. Environment Requirements

### Programming Languages
- **Python**: 3.9 or later  
- **Java**: 11 or later (required by Robot OBO Tool)

### Tools / Frameworks
- **Robot OBO Tool**
  - Version: 1.9.x (specify your exact version)
  - Requires Java 11+

## 2. System Dependencies
- Operating System: **Linux** (project is developed and tested on Linux; requirements should be the same for macOS and Windows)
- Memory: 8 GB minimum (16 GB reccommended for reasoning services)
- Disk space: 15 GB for datasets and ontologies


## 3. Data Requirements

In order to make the scripts usable, users need to **download the class assertion data** from the ontology's main website or SPARQL endpoint.  

> ⚠️ Note: We **do not provide these files** in the repository due to their large size and GitHub/Cloud storage limitations. For the same reason, the **full object property assertion data** for each ontology is also not included. As a result, the extraction scripts may require **manual effort** to gather the necessary data.
