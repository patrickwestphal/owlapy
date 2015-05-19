from .owldatamincardinality import OWLDataCardinalityRestriction


class OWLDataExactCardinality(OWLDataCardinalityRestriction):
    """TODO: implement"""

    def __init__(self, property, cardinality, filler):
        """
        :param property: an owlapy.model.OWLDataPropertyExpression object
        :param cardinality: an integer
        :param filler: an owlapy.model.OWLDataRange object
        """
        super().__init__(property, cardinality, filler)