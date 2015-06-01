from .owldatavisitor import OWLDataVisitor, OWLDataVisitorEx
from .owlobject import OWLObject
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from owlapy.util import str_compare_to, accept_default, accept_default_ex


class OWLFacetRestriction(OWLObject):
    """TODO: implement"""

    def __init__(self, facet, facet_value):
        """
        :param facet: an owlapy.vocab.OWLFacet object
        :param facet_value: an owlapy.model.OWLLiteral object
        """
        super().__init__()
        self.facet = facet
        self.facet_value = facet_value

        self._accept_fn_for_visitor_cls[OWLDataVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLDataVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex

    def compare_object_of_same_type(self, other):
        # diff = self.facet.compare_to(other.facet)
        diff = str_compare_to(self.facet.short_form, other.facet.short_form)
        if diff:
            return diff

        return self.facet_value.compare_to(other.facet.value)
