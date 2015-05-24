from .exceptions import OWLRuntimeException
from .owldatapropertyexpression import OWLDataPropertyExpression
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLDataProperty(OWLDataPropertyExpression):
    """TODO: implement"""

    def __init__(self, iri):
        """
        :param iri: an owlapy.model.IRI object
        """
        super().__init__()
        self.iri = iri

    def compare_object_of_same_type(self, other):
        return self.iri.compare_to(other.iri)

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
