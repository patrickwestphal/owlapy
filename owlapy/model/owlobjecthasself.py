from .exceptions import OWLRuntimeException
from .owlrestriction import OWLRestriction
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLObjectHasSelf(OWLRestriction):
    """TODO; implement"""

    def __init__(self, property):
        """
        :param property: an owlapy.model.OWLObjectPropertyExpression object
        """
        super().__init__(property)

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
