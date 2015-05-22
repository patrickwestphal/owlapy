from .exceptions import OWLRuntimeException
from .owlobject import OWLObject
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLFacetRestriction(OWLObject):
    """TODO: implement"""

    def __init__(self, facet, facet_value):
        """
        :param facet: an owlapy.vocab.OWLFacet object
        :param facet_value: an owlapy.model.OWLLiteral object
        """
        super().__init__()
        self.facet = facet
        self.facet_value = facet_value

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
