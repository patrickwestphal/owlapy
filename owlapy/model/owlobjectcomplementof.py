from .exceptions import OWLRuntimeException
from .owlanonymousclassexpression import OWLAnonymousClassExpression
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLObjectComplementOf(OWLAnonymousClassExpression):
    """TODO: implement"""

    def __init__(self, operand):
        """
        :param operands: an owlapy.model.OWLClassExpression object
        """
        super().__init__()
        self.operand = operand

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
