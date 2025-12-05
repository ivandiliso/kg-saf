from rdflib import URIRef, RDF, RDFS, OWL

BUILTIN_URIS = {
    # RDF
    RDF.type,
    
    # RDFS
    RDFS.domain,
    RDFS.range,
    RDFS.subClassOf,
    RDFS.subPropertyOf,
    RDFS.label,
    RDFS.comment,
    RDFS.isDefinedBy,
    RDFS.Resource,

    # OWL classes
    OWL.Thing,
    OWL.Nothing,
    OWL.Class,
    OWL.NamedIndividual,

    # OWL properties
    OWL.ObjectProperty,
    OWL.DatatypeProperty,
    OWL.AnnotationProperty,
    OWL.topObjectProperty,
    OWL.bottomObjectProperty,
    OWL.topDataProperty,
    OWL.bottomDataProperty,

    # OWL logical axioms
    OWL.equivalentClass,
    OWL.equivalentProperty,
    OWL.disjointWith,
    
    # Custom
    URIRef("http://schema.org/Thing"),
    URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#Resource")
}