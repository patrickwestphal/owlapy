from .owlclassexpressionvisitor import OWLClassExpressionVisitor, \
    OWLClassExpressionVisitorEx
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from .owlrestriction import OWLRestriction
from owlapy.util import accept_default, accept_default_ex


class OWLObjectHasSelf(OWLRestriction):
    """TODO; implement"""

    def __init__(self, property):
        """
        :param property: an owlapy.model.OWLObjectPropertyExpression object
        """
        super().__init__(property)

        self._accept_fn_for_visitor_cls[OWLClassExpressionVisitor] = \
            accept_default
        self._accept_fn_for_visitor_cls[OWLClassExpressionVisitorEx] = \
            accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex
