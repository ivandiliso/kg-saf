# KG-SaF: Building Complete and Curated Datasets for Machine Learning and Reasoning on Knowledge Graphs

[![DOI](https://zenodo.org/badge/1110012490.svg)](https://doi.org/10.5281/zenodo.17817931)
![GitHub License](https://img.shields.io/github/license/ivandiliso/sphm4kg)
![Python Version](https://img.shields.io/badge/python-3.12.8%2B-blue)


**KG-SaF** provides a workflow (*KG-SaF-JDeX*) and curated datasets  (*KG-SaF-Data*) for knowledge graph refinement (KGR) research. The resource includes datasets with both **schema (ontologies)** and **ground facts**, making it ready for **machine learning** and **reasoning services**.

### Key Features
- 🗂️ Extracts datasets from RDF-based KGs with expressive schemas (RDFS/OWL2)  
- 📦 Provides datasets in **OWL** and **TSV** formats, easily loadable in both **PyTorch** and **Protege**  
- ⚡ Handles inconsistencies and leverages reasoning to infer implicit knowledge (entailment, realization, materialization)  
- 🤖 Provides ML-ready **tensor representations** compatible with PyTorch and PyKEEN  
- 🧩 Offers **schema decomposition** into themed partitions (modularization of ontology components)


## Dataset Documentation (*KG-SaF-Data*)

### Available Ontologies (Schema) and Datasets

The table below lists the currently available **ontologies** and their corresponding **datasets** included in this resource.  
> Note: This table will be **updated** as new datasets and ontologies become available.

| Ontology | Datasets | DL Fragment |
|----------|---------|-------------|
| 📚 [DBpedia](https://www.dbpedia.org/resources/ontology/) | `DBPEDIA25-50K-C`, `DBPEDIA25-100K-C` | $\mathcal{ALCHF}$ |
| 📚 [YAGO3](https://yago-knowledge.org/downloads/yago-3) | `YAGO3-39K-C`, `YAGO3-10-C` | $\mathcal{ALHIF+}$ |
| 📚 [YAGO4](https://yago-knowledge.org/downloads/yago-4ap) | `YAGO4-20-C` | $\mathcal{ALCHIF}$ |
| 📚 [ArCo](http://wit.istc.cnr.it/arco) | `ARCO25-20`, `ARCO25-10`, `ARCO25-5` | $\mathcal{SROIQ}$ |
| 📚 [WHOW](https://whowproject.eu/) | `WHOW25-5` | $\mathcal{SROIQ}$ |
| 📚 [ApuliaTravel](https://github.com/rbarile17/ApuliaTravelKG) | `ATRAVEL` | $\mathcal{SRIQ}$ |



### Dataset File Structure

All datasets are provided in a **standardized format** following the **Description Logic (DL) formalization**, separating the dataset into **ABox** (instance-level data), **TBox** (schema-level information), and **RBox** (roles and properties)

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

## Code and Workflow Documentation (*KG-SaF-JDeX*)
