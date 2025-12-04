# KG-SaF: Building Complete and Curated Datasets for Machine Learning and Reasoning on Knowledge Graphs

[![DOI](https://zenodo.org/badge/1110012490.svg)](https://doi.org/10.5281/zenodo.17817931)


## Available Datases

```
📚 YAGO ............................................. # 
│   ├── 🗂️ YAGO4-20-C................................ # 
│   ├── 🗂️ YAGO3-39K-C .............................. # 
│   ├── 🗂️ YAGO3-10-C................................ # 


📚 DBPEDIA .......................................... # 
│   ├── 🗂️ DBPEDIA25-50K ............................ # 
│   ├── 🗂️ DBPEDIA25-100K ........................... # 

📚 ARCO ............................................. # 
│   ├── 🗂️ ARCO25-20 ................................ # 
│   ├── 🗂️ ARCO25-10 ................................ #
│   ├── 🗂️ ARCO25-5 ................................. #

📚 OTHER ............................................ # 
│   ├── 🗂️ APULIATRAVEL ............................. #
│   ├── 🗂️ WHOW25-5 ................................. #

```

## Dataset Standard Structure

```
📁 abox ............................................. # Assertional Box (instance-level data)
│   ├── 📁 splits ................................... # Train/test/validation splits
│   │   ├── 📜 test.nt .............................. # Test triples (N-Triples)
│   │   ├── 📜 test.txt ............................. # Test triples (Text)
│   │   ├── 📜 train.nt ............................. # Training triples (N-Triples)
│   │   ├── 📜 train.txt ............................ # Training triples (Text)
│   │   ├── 📜 valid.nt ............................. # Validation triples (N-Triples)
│   │   └── 📜 valid.txt ............................ # Validation triples (Text)
│   │ 
│   ├── 📜 triples.nt ............................... # Combined triples (N-Triples)
│   ├── 📜 triples.txt .............................. # Combined triples (Text)
│   │ 
│   ├── 🧾 class_assertions.json .................... # Class membership data (JSON)
│   └── 🦉 class_assertions.owl ..................... # Class membership data (OWL)

📁 rbox ............................................. # Role Box (relations and properties)
│   ├── 🦉 roles.owl ................................ # Role definitions (OWL)
|   ├── 🧾 roles_hierarchy.json ......................# Role Hierarchy (Subproperty, JSON)
│   └── 🧾 roles_domain_range.json .................. # Domain and range constraints (JSON)

📁 tbox ............................................. # Terminological Box (schema-level info)
│   ├── 🦉 schema.owl ............................... # Ontology schema (OWL)
│   ├── 🧾 taxonomy.json ............................ # Hierarchical taxonomy (JSON)
│   ├── 🦉 taxonomy.owl ............................. # Hierarchical taxonomy (OWL)

🦉 knowledge_graph.owl .............................. # Full merged ontology + instances
🦉 ontology.owl ..................................... # Core ontology definition
📘 README.md ........................................ # Documentation and usage notes

📁 mappings ......................................... # Mappings to IDs
│   ├── 🧾 class_to_id.json ......................... # Map ontology classes to IDs
│   ├── 🧾 individual_to_id.json .................... # Map entities/instances to IDs
│   └── 🧾 object_property_to_id.json ............... # Map object properties to IDs
```