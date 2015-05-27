from .owlobject import OWLObject
from owlapy.util import str_compare_to


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

    def compare_object_of_same_type(self, other):
        # diff = self.facet.compare_to(other.facet)
        diff = str_compare_to(self.facet.short_form, other.facet.short_form)
        if diff:
            return diff

        return self.facet_value.compare_to(other.facet.value)
