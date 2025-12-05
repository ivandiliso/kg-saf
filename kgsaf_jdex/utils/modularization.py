#!/usr/bin/env python3
import sys
from pathlib import Path

import utils.conventions.paths as pc
from rdflib import OWL, RDF, RDFS, BNode, Graph, URIRef
from utils.conventions.builtins import BUILTIN_URIS


class SignatureModularizer:
    def __init__(self, schema, seed):
        self.schema = schema
        self.seed = seed

    def modularize(self):
        return self._extract_recursive_description()

    def _extract_recursive_description(self) -> Graph:

        extracted_graph = Graph()
        elem_to_process = set(self.seed)
        processed = set()

        while elem_to_process:

            e = elem_to_process.pop()
            processed.add(e)

            print(f"Processing {e}")

            for s, p, o in self.schema.triples((e, None, None)):
                extracted_graph.add((s, p, o))

                if (o not in BUILTIN_URIS) and (o not in processed):

                    if isinstance(o, BNode):
                        elem_to_process.add(o)

                    if (o, RDF.type, OWL.Class) in self.schema:
                        elem_to_process.add(o)

                    if (o, RDF.type, OWL.ObjectProperty) in self.schema:
                        elem_to_process.add(o)

                    if (o, RDF.type, OWL.DatatypeProperty) in self.schema:
                        elem_to_process.add(o)

        return extracted_graph


class SchemaDecomposition:
    def __init__(self, input_graph):
        self.onto_graph = input_graph

    def decompose(self):
        return (
            self._rbox_decompose(),
            self._taxonomy_decompose(),
            self._schema_decompose(),
        )

    def _rbox_decompose(self):
        rbox_graph = Graph()
        for prop in (
            set(self.onto_graph.subjects(RDF.type, OWL.ObjectProperty)) - BUILTIN_URIS
        ):
            rbox_graph += self._extract_description(prop)

        for prop in (
            set(self.onto_graph.subjects(RDF.type, OWL.DatatypeProperty)) - BUILTIN_URIS
        ):
            rbox_graph += self._extract_description(prop)
        return rbox_graph

    def _taxonomy_decompose(self):
        taxonomy_graph = Graph()

        for c in set(self.onto_graph.subjects(RDF.type, OWL.Class)) - BUILTIN_URIS:
            for s, p, o in self.onto_graph.triples((c, None, None)):
                if p == RDFS.subClassOf:
                    taxonomy_graph.add((s, p, o))
                    if isinstance(o, BNode):
                        taxonomy_graph += self._extract_description(o)

        return taxonomy_graph

    def _schema_decompose(self):
        schema_graph = Graph()

        for c in set(self.onto_graph.subjects(RDF.type, OWL.Class)) - BUILTIN_URIS:
            if not isinstance(c, BNode):
                for s, p, o in self.onto_graph.triples((c, None, None)):
                    if p != RDFS.subClassOf:

                        schema_graph.add((s, p, o))

                        for elem in self.onto_graph.objects(o, RDF.type):
                            schema_graph.add((o, RDF.type, elem))

                        if isinstance(o, BNode):
                            print(f"Found BNODE in Triple {s, p, o}")
                            schema_graph += self._extract_description(o)

        return schema_graph

    def _extract_description(self, elem: URIRef) -> Graph:

        extracted_graph = Graph()
        elem_to_process = {elem}
        processed = set()

        while elem_to_process:

            e = elem_to_process.pop()
            processed.add(e)

            print(f"Processing {e}")

            for s, p, o in self.onto_graph.triples((e, None, None)):
                extracted_graph.add((s, p, o))

                if (o not in BUILTIN_URIS) and (o not in processed):
                    if isinstance(o, BNode):
                        elem_to_process.add(o)

                    if (o, RDF.type, OWL.Class) in self.onto_graph:
                        extracted_graph.add((o, RDF.type, OWL.Class))

                    if (o, RDF.type, OWL.ObjectProperty) in self.onto_graph:
                        extracted_graph.add((o, RDF.type, OWL.ObjectProperty))

                    if (o, RDF.type, OWL.DatatypeProperty) in self.onto_graph:
                        extracted_graph.add((o, RDF.type, OWL.DatatypeProperty))

        return extracted_graph
