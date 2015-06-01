from .owlanonymousclassexpression import OWLAnonymousClassExpression
from .owlclassexpressionvisitor import OWLClassExpressionVisitor, \
    OWLClassExpressionVisitorEx
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


class OWLObjectOneOf(OWLAnonymousClassExpression):
    """TODO: implement"""

    def __init__(self, values):
        """
        :param values: a set of owlapy.model.OWLIndividual objects
        """
        super().__init__()
        self.individuals = values

        self._accept_fn_for_visitor_cls[OWLClassExpressionVisitor] = \
            accept_default
        self._accept_fn_for_visitor_cls[OWLClassExpressionVisitorEx] = \
            accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex
