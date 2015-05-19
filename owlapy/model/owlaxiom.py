from .owlobject import OWLObject


class OWLAxiom(OWLObject):
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
            self._annotations = list(annotations)
            self._annotations.sort()
        else:
            self._annotations = []
