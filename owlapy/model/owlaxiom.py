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

        from owlapy import CollectionContainerVisitor
        self._accept_fn_for_visitor_cls[CollectionContainerVisitor] = \
            self._accept_coll_cont_visitor

    @staticmethod
    def _accept_coll_cont_visitor(self, t):
        """
        :param t: :param visitor: an owlapy.CollectionContainerVisitor object
        """
        size = len(self.annotations)

        for item in self.annotations:
            t.visit_item(item)
