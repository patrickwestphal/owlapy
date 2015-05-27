from .owlobject import OWLObject
from owlapy.collectioncontainer import CollectionContainer


class OWLAxiom(OWLObject, CollectionContainer):
    """Represents an Axiom in the OWL 2 Specification. An OWL ontology
    contains a set of axioms. These axioms can be annotation axioms,
    declaration axioms, imports axioms or logical axioms
    """

    def __init__(self, annotations):
        """
        :param annotations: a set/list of OWLAnnotation objects
        """
        super().__init__()
        if annotations:
            self.annotations = list(annotations)
            self.annotations.sort()
        else:
            self.annotations = []


