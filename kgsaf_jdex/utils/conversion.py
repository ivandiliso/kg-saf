import utils.conventions.ids as idc
import utils.conventions.paths as pc
import json
from rdflib import Graph, RDF, RDFS, OWL, Namespace, Literal, BNode
from rdflib.namespace import split_uri
from rdflib.term import URIRef
from pathlib import Path
from utils.conventions.builtins import BUILTIN_URIS


def rdf_list_to_python_list(graph, head, depth):
    """Convert an RDF list (rdf:first/rest/nil chain) into a Python list."""
    items = []
    while head and head != RDF.nil:
        first = next(graph.objects(head, RDF.first), None)
        print(f"{"\t"*depth}List Element {first}")
        if first is not None:
            items.append(bnode_to_dict(graph, first, depth + 1))
        head = next(graph.objects(head, RDF.rest), None)
    return items


def bnode_to_dict(graph, node, depth=1):
    """Recursively convert an RDF node (especially blank nodes) into JSON."""

    if isinstance(node, URIRef):
        return str(node)
    if isinstance(node, Literal):
        return str(node)
    if not isinstance(node, BNode):
        return str(node)

    node_dict = {}

    print(f"{"\t"*depth}Found BNode {node} Starting Recursive Evaluation")

    for _, p, o in graph.triples((node, None, None)):
        pred = str(p)

        print(f"{"\t"*depth}Evaluating  - {p} {o}")

        # Detect RDF lists (owl:unionOf, owl:intersectionOf, etc.)
        if pred in {
            str(OWL.unionOf),
            str(OWL.intersectionOf),
            str(OWL.oneOf),
        }:
            print(
                f"{"\t"*(depth+1)}Found Collection {pred} Starting Recursive Evaluation"
            )
            node_dict[pred] = rdf_list_to_python_list(graph, o, depth + 1)
        else:
            node_dict.setdefault(pred, []).append(bnode_to_dict(graph, o, depth + 1))
    return node_dict


class OWLConverter:
    def __init__(
        self,
        path: str,
    ):

        self.p_data = dict()
        self.base_path = Path(path).resolve().absolute()

    def preprocess(
        self,
        taxonomy: bool = True,
        class_assertions: bool = True,
        obj_prop_domain_range: bool = True,
        obj_prop_hierarchy: bool = True,
    ):

        if taxonomy:
            self.p_data["taxonomy"] = (
                self.preprocess_taxonomy(),
                self.base_path / pc.TAXONOMY,
            )

        if class_assertions:
            self.p_data["class_assertions"] = (
                self.preprocess_class_assertions(),
                self.base_path / pc.CLASS_ASSERTIONS,
            )

        if obj_prop_hierarchy:
            self.p_data["obj_prop_hierarchy"] = (
                self.preprocess_obj_prop_hierarchy(),
                self.base_path / pc.OBJ_PROP_HIERARCHY,
            )

        if obj_prop_domain_range:
            self.p_data["obj_prop_domain_range"] = (
                self.preprocess_obj_prop_domain_range(),
                self.base_path / pc.OBJ_PROP_DOMAIN_RANGE,
            )

    def serialize(self):
        for key, values in self.p_data.items():
            obj = values[0]
            path = values[1]

            with open(path, "w") as f:
                json.dump(obj, f, indent=4)


    def preprocess_taxonomy(self):

        onto = Graph()
        onto.parse(self.base_path / pc.RDF_TAXONOMY)
        classes = set(onto.subjects(RDF.type, OWL.Class))

        out_json = {}

        for c in classes:
            print(f"Processing main class {c}")
            sup_c = []
            for o in set(onto.objects(c, RDFS.subClassOf)) - BUILTIN_URIS:
                sup_c.append(bnode_to_dict(onto, o))
            if sup_c:
                out_json[c] = sup_c

        return out_json

    def preprocess_class_assertions(self):

        onto = Graph()
        onto.parse(self.base_path / pc.RDF_CLASS_ASSERTIONS)
        individuals = set(onto.subjects(RDF.type, OWL.NamedIndividual))

        out_json = {}

        for ind in individuals:
            ind_cls = []
            for cls in set(onto.objects(ind, RDF.type)) - BUILTIN_URIS:
                if cls != OWL.NamedIndividual:
                    ind_cls.append(cls)
            if ind_cls:
                out_json[ind] = ind_cls

        return out_json

    def preprocess_obj_prop_domain_range(self):

        onto = Graph()
        onto.parse(self.base_path / pc.RDF_OBJ_PROP)

        obj_props = set(onto.subjects(RDF.type, OWL.ObjectProperty))

        out_json = {}

        for prop in obj_props:
            prop_data = {}

            # Get domains
            domains = list(onto.objects(prop, RDFS.domain))
            prop_data["domain"] = (
                [bnode_to_dict(onto, d) for d in domains] if domains else [OWL.Thing]
            )

            # Get ranges
            ranges = list(onto.objects(prop, RDFS.range))
            prop_data["range"] = (
                [bnode_to_dict(onto, r) for r in ranges] if ranges else [OWL.Thing]
            )

            out_json[str(prop)] = prop_data

        return out_json

    def preprocess_obj_prop_hierarchy(self):
        onto = Graph()
        onto.parse(self.base_path / pc.RDF_OBJ_PROP)

        out_json = {}

        for r in onto.subjects(RDF.type, OWL.ObjectProperty):
            val = []
            for sup_r in set(onto.objects(r, RDFS.subPropertyOf)) - BUILTIN_URIS:
                val.append(bnode_to_dict(onto, sup_r))
            if val:
                out_json[r] = val

        return out_json


if __name__ == "__main__":
    processor = OWLConverter(
        "/home/navis/dev/semantic-web-datasets/datasets/✅ARCO25-5-REASONED"
    )
    processor.preprocess()
    processor.serialize()
