from functools import total_ordering
from .exceptions import OWLRuntimeException
from .owlnarybooleanclassexpression import OWLNaryBooleanClassExpression
from .owlvisitor import OWLVisitorEx, OWLVisitor


@total_ordering
class OWLObjectUnionOf(OWLNaryBooleanClassExpression):
    """TODO: implement"""

    def __init__(self, operands):
        """
        :param operands: a set of owlapy.model.OWLClassExpression objects
        """
        super().__init__(operands)

    def __eq__(self, other):
        if super().__eq__(other):
            return isinstance(other, OWLObjectUnionOf)

        return False

    def __ge__(self, other):
        return self.compare_to(other) > 0

    def __hash__(self):
        return super().__hash__()

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
