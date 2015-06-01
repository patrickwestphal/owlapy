from .owlanonymousclassexpression import OWLAnonymousClassExpression
from .owlclassexpressionvisitor import OWLClassExpressionVisitor, \
    OWLClassExpressionVisitorEx
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


class OWLObjectComplementOf(OWLAnonymousClassExpression):
    """TODO: implement"""

    def __init__(self, operand):
        """
        :param operands: an owlapy.model.OWLClassExpression object
        """
        super().__init__()
        self.operand = operand

        self._accept_fn_for_visitor_cls[OWLClassExpressionVisitor] = \
            accept_default
        self._accept_fn_for_visitor_cls[OWLClassExpressionVisitorEx] = \
            accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex
