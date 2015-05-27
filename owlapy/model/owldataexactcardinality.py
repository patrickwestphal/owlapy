from .owldatamincardinality import OWLDataCardinalityRestriction


class OWLDataExactCardinality(OWLDataCardinalityRestriction):
    """TODO: implement"""

    def __init__(self, property, cardinality, filler):
        """
        :param property: an owlapy.model.OWLDataPropertyExpression object
        :param cardinality: an integer
        :param filler: an owlapy.model.OWLDataRange object (i.e. an
            owlapy.model.OWLDataComplementOf object, an
            owlapy,model.OWLDataOneOf object, an owlapy.model.OWLDatatype
            object, an owlapy.model.OWLDatatypeRestriction, or an
            owlapy.model.OWLNaryDataRange object)
        """
        super().__init__(property, cardinality, filler)
