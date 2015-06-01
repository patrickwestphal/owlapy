from .owlclassexpressionvisitor import OWLClassExpressionVisitor, \
    OWLClassExpressionVisitorEx
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from .owlquantifieddatarestriction import OWLQuantifiedDataRestriction
from owlapy.util import accept_default, accept_default_ex


class OWLDataSomeValuesFrom(OWLQuantifiedDataRestriction):
    """TODO: implement"""

    def __init__(self, property, filler):
        """
        :param property: an owlapy.model.OWLDataPropertyExpression object
        :param filler: an owlapy.model.OWLDataRange object
        """
        super().__init__(property, filler)

        self._accept_fn_for_visitor_cls[OWLClassExpressionVisitor] = \
            accept_default
        self._accept_fn_for_visitor_cls[OWLClassExpressionVisitorEx] = \
            accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex
