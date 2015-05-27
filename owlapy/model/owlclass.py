from .owlclassexpression import OWLClassExpression
from .owlclassexpressionvisitor import OWLClassExpressionVisitor, \
    OWLClassExpressionVisitorEx
from .owlentityvisitor import OWLEntityVisitor, OWLEntityVisitorEx
from .owllogicalentity import OWLLogicalEntity
from .owlnamedobject import OWLNamedObject
from .owlnamedobjectvisitor import OWLNamedObjectVisitor
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx

from owlapy.util import accept_default, accept_default_ex


class OWLClass(OWLClassExpression, OWLLogicalEntity, OWLNamedObject):
    """TODO: implement"""

    def __init__(self, iri):
        """
        :param iri: an owlapy.model.IRI object
        """
        super().__init__()
        self.iri = iri

        self._accept_fn_for_visitor_cls[OWLClassExpressionVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLClassExpressionVisitorEx] = \
            accept_default_ex
        self._accept_fn_for_visitor_cls[OWLEntityVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLEntityVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLNamedObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex

    def compare_object_of_same_type(self, other):
        """
        :param other: an owlapy.model.OWLObject object
        :return: an integer indicating the difference  between self and other
        """
        return self.iri.compare_to(other.iri)
