from .exceptions import OWLRuntimeException
from .owlclassexpression import OWLClassExpression
from .owllogicalentity import OWLLogicalEntity
from .owlnamedobject import OWLNamedObject
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLClass(OWLClassExpression, OWLLogicalEntity, OWLNamedObject):
    """TODO: implement"""

    def __init__(self, iri):
        """
        :param iri: an owlapy.model.IRI object
        """
        super().__init__()
        self.iri = iri

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
