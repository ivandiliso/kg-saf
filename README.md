# KG-SaF: Building Complete and Curated Datasets for Machine Learning and Reasoning on Knowledge Graphs

[![DOI](https://zenodo.org/badge/1110012490.svg)](https://doi.org/10.5281/zenodo.17817931)
![GitHub License](https://img.shields.io/github/license/ivandiliso/sphm4kg)
![Python Version](https://img.shields.io/badge/python-3.12.8%2B-blue)

### Available Ontologies (Schema)
```
📚 DBpedia
📚 YAGO3
📚 YAGO4
📚 ArCo
📚 WHOW
📚 ApuliaTravel
```
### Available Datases
```
📚 YAGO 
    ├── 🗂️ YAGO4-20-C................................ # 
    ├── 🗂️ YAGO3-39K-C .............................. # 
    └── 🗂️ YAGO3-10-C................................ #
📚 DBPEDIA 
    ├── 🗂️ DBPEDIA25-50K ............................ # 
    └── 🗂️ DBPEDIA25-100K ........................... # 
📚 ARCO 
    ├── 🗂️ ARCO25-20 ................................ # 
    ├── 🗂️ ARCO25-10 ................................ #
    └── 🗂️ ARCO25-5 ................................. #
📚 OTHER 
    ├── 🗂️ APULIATRAVEL ............................. #
    └── 🗂️ WHOW25-5 ................................. #

```
### Dataset File Structure
```
📁 abox ............................................. # Assertional Box (instance-level data)
│   ├── 📁 splits ................................... # Train/test/validation splits
│   │   ├── 🦉 test.nt .............................. # Test triples (N-Triples)
│   │   ├── 📜 test.tsv ............................. # Test triples (TSV)
│   │   ├── 🦉 train.nt ............................. # Training triples (N-Triples)
│   │   ├── 📜 train.tsv ............................ # Training triples (TSV)
│   │   ├── 🦉 valid.nt ............................. # Validation triples (N-Triples)
│   │   └── 📜 valid.tsv ............................ # Validation triples (TSV)
│   │ 
│   ├── 🦉 obj_prop_assertions.nt ................... # Combined triples (N-Triples)
│   ├── 📜 obj_prop_assertions.tsv .................. # Combined triples (TSV)
│   │ 
│   ├── 🦉 individuals.owl .......................... # Individuals definitions
│   └── 🦉 class_assertions.owl ..................... # Individuals class assertions 

📁 rbox ............................................. # Role Box (relations and properties)
│   ├── 🦉 roles.owl ................................ # Role definitions

📁 tbox ............................................. # Terminological Box (schema-level info)
│   ├── 🦉 classes.owl .............................. # Classs non taxonomical Axioms
│   ├── 🦉 taxonomy.owl ............................. # Hierarchical taxonomy

🦉 knowledge_graph.owl .............................. # Full merged TBox + RBox + ABox
🦉 ontology.owl ..................................... # Core Modularized Schema

📁 mappings ......................................... # Mappings to IDs
│   ├── 🧾 class_to_id.json ......................... # Map ontology classes to IDs
│   ├── 🧾 individual_to_id.json .................... # Map entities/instances to IDs
│   └── 🧾 object_property_to_id.json ............... # Map object properties to IDs
```