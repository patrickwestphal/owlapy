from .exceptions import OWLRuntimeException
from .owlvaluerestriction import OWLValueRestriction
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLObjectHasValue(OWLValueRestriction):
    """TODO: implement"""

    def __init__(self, property, value):
        """
        :param property: an owlapy.model.OWLObjectPropertyExpression object
        :param value: an owlapy.model.OWLIndividual value
        """
        super().__init__(property, value)

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
