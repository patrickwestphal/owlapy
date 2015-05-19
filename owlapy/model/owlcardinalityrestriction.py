from .owlrestriction import OWLRestriction


class OWLCardinalityRestriction(OWLRestriction):
    """TODO: implement"""

    def __init__(self, property, cardinality, filler):
        """
        :param property: an owlapy.model.OWLPropertyExpression object
        :param cardinality: an integer
        :param filler: an owlapy.model.OWLPropertyRange object
        """
        super().__init__(property)
        self.cardinality = cardinality
        self.filler = filler