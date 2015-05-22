from .exceptions import OWLRuntimeException
from .owlobjectcardinalityrestriction import OWLObjectCardinalityRestriction
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLObjectExactCardinality(OWLObjectCardinalityRestriction):
    """TODO: implement"""

    def __init__(self, property, cardinality, filler):
        """
        :param property: an owlapy.model.OWLObjectPropertyExpression object
        :param cardinality: an integer
        :param filler: an owlapy.model.OWLClassExpression object
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
