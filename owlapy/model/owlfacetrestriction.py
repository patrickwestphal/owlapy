from .owlobject import OWLObject


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