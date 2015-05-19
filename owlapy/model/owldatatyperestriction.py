from .owlobject import OWLObject


class OWLDatatypeRestriction(OWLObject):
    """TODO: implement"""

    def __init__(self, datatype, facet_restrictions):
        """
        :param datatype: an owlapy.model.OWLDatatype object
        :param facet_restrictions: facet restrictions on this data range; a set
            of owlapy.model.OWLFacetRestriction objects
        """
        super().__init__()
        self.datatype = datatype
        self.facet_restrictions = facet_restrictions