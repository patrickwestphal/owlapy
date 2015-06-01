from .owldatapropertyexpression import OWLDataPropertyExpression
from .owlentityvisitor import OWLEntityVisitor, OWLEntityVisitorEx
from .owlnamedobjectvisitor import OWLNamedObjectVisitor
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from .owlpropertyexpressionvisitor import OWLPropertyExpressionVisitor, \
    OWLPropertyExpressionVisitorEx
from owlapy.util import accept_default_ex, accept_default


class OWLDataProperty(OWLDataPropertyExpression):
    """TODO: implement"""

    def __init__(self, iri):
        """
        :param iri: an owlapy.model.IRI object
        """
        super().__init__()
        self.iri = iri

        self._accept_fn_for_visitor_cls[OWLEntityVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLEntityVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLNamedObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLPropertyExpressionVisitor] = \
            accept_default
        self._accept_fn_for_visitor_cls[OWLPropertyExpressionVisitorEx] = \
            accept_default_ex

    def compare_object_of_same_type(self, other):
        return self.iri.compare_to(other.iri)
