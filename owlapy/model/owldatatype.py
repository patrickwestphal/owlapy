from functools import total_ordering

from .owldatarange import OWLDataRange
from .owldatarangevisitor import OWLDataRangeVisitor, OWLDataRangeVisitorEx
from .owldatavisitor import OWLDataVisitor, OWLDataVisitorEx
from .owlentityvisitor import OWLEntityVisitor, OWLEntityVisitorEx
from .owllogicalentity import OWLLogicalEntity
from .owlnamedobject import OWLNamedObject
from .owlnamedobjectvisitor import OWLNamedObjectVisitor
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


@total_ordering
class OWLDatatype(OWLDataRange, OWLLogicalEntity, OWLNamedObject):
    """TODO: implement"""

    def __init__(self, iri):
        """
        :param iri: an owlapy.model.IRI object
        """
        super().__init__()
        self.iri = iri

        self._accept_fn_for_visitor_cls[OWLDataRangeVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLDataRangeVisitorEx] =\
            accept_default_ex
        self._accept_fn_for_visitor_cls[OWLDataVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLDataVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLEntityVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLEntityVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLNamedObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex

    def __eq__(self, other):
        if super().__eq__(other) and isinstance(other, OWLDatatype):
            return other.iri == self.iri

        return False

    def __ge__(self, other):
        return self.compare_to(other) >= 0

    def __hash__(self):
        return super().__hash__()

    def compare_object_of_same_type(self, other):
        return self.iri.compare_to(other.iri)
