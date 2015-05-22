from .exceptions import OWLRuntimeException
from .owlobject import OWLObject
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLDatatypeRestriction(OWLObject):
    """TODO: implement"""

    def __init__(self, datatype, facet_restrictions):
        """
        :param datatype: an owlapy.model.OWLDatatype object
        :param facet_restrictions: facet restrictions on this data range; a set
            of owlapy.model.OWLFacetRestriction objects
        """
        super().__init__()
        self.datatype = datatype
        self.facet_restrictions = facet_restrictions

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
