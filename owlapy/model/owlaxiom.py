from .exceptions import OWLRuntimeException
from .owlobject import OWLObject
from owlapy.collectioncontainer import CollectionContainer
from .owlvisitor import OWLVisitorEx, OWLVisitor


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

    def accept(self, visitor):
        """
        :param visitor: an owlapy.CollectionContainerVisitor object
        """
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')

