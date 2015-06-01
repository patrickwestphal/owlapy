from functools import total_ordering

from .owlclassexpressionvisitor import OWLClassExpressionVisitor, \
    OWLClassExpressionVisitorEx
from .owlnarybooleanclassexpression import OWLNaryBooleanClassExpression
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


@total_ordering
class OWLObjectUnionOf(OWLNaryBooleanClassExpression):
    """TODO: implement"""

    def __init__(self, operands):
        """
        :param operands: a set of owlapy.model.OWLClassExpression objects
        """
        super().__init__(operands)

        self._accept_fn_for_visitor_cls[OWLClassExpressionVisitor] = \
            accept_default
        self._accept_fn_for_visitor_cls[OWLClassExpressionVisitorEx] = \
            accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex

    def __eq__(self, other):
        if super().__eq__(other):
            return isinstance(other, OWLObjectUnionOf)

        return False

    def __ge__(self, other):
        return self.compare_to(other) > 0

    def __hash__(self):
        return super().__hash__()
