from .owlobjectpropertyexpression import OWLObjectPropertyExpression
from .owlpropertyexpressionvisitor import OWLPropertyExpressionVisitor, \
    OWLPropertyExpressionVisitorEx
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


class OWLObjectInverseOf(OWLObjectPropertyExpression):
    """TODO: implement"""

    def __init__(self, inverse_property):
        """
        :param inverse_property: an owlapy.model.OWLObjectPropertyExpression
            object
        """
        super().__init__()
        self.inverse = inverse_property

        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLPropertyExpressionVisitor] = \
            accept_default
        self._accept_fn_for_visitor_cls[OWLPropertyExpressionVisitorEx] = \
            accept_default_ex
