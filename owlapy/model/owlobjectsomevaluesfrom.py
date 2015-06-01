from .owlclassexpressionvisitor import OWLClassExpressionVisitor, \
    OWLClassExpressionVisitorEx
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from .owlquantifiedobjectrestriction import OWLQuantifiedObjectRestriction
from owlapy.util import accept_default, accept_default_ex


class OWLObjectSomeValuesFrom(OWLQuantifiedObjectRestriction):
    """TODO: implement"""

    def __init__(self, property, filler):
        """
        :param property: an owlapy.model.OWLObjectPropertyExpression object
        :param filler: an owlapy.model.OWLClassExpression object
        """
        super().__init__(property, filler)

        self._accept_fn_for_visitor_cls[OWLClassExpressionVisitor] = \
            accept_default
        self._accept_fn_for_visitor_cls[OWLClassExpressionVisitorEx] = \
            accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex
