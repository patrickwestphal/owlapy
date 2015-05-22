from .exceptions import OWLRuntimeException
from .owldatamincardinality import OWLDataCardinalityRestriction
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLDataExactCardinality(OWLDataCardinalityRestriction):
    """TODO: implement"""

    def __init__(self, property, cardinality, filler):
        """
        :param property: an owlapy.model.OWLDataPropertyExpression object
        :param cardinality: an integer
        :param filler: an owlapy.model.OWLDataRange object
        """
        super().__init__(property, cardinality, filler)

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
