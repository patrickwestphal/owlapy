from .owlclassexpressionvisitor import OWLClassExpressionVisitor, \
    OWLClassExpressionVisitorEx
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from .owlvaluerestriction import OWLValueRestriction
from owlapy.util import accept_default, accept_default_ex


class OWLObjectHasValue(OWLValueRestriction):
    """TODO: implement"""

    def __init__(self, property, value):
        """
        :param property: an owlapy.model.OWLObjectPropertyExpression object
        :param value: an owlapy.model.OWLIndividual value
        """
        super().__init__(property, value)

        self._accept_fn_for_visitor_cls[OWLClassExpressionVisitor] = \
            accept_default
        self._accept_fn_for_visitor_cls[OWLClassExpressionVisitorEx] = \
            accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex
