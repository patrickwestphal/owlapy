from .owlobjectcardinalityrestriction import OWLObjectCardinalityRestriction


class OWLObjectMaxCardinality(OWLObjectCardinalityRestriction):
    """TODO: implement"""

    def __init__(self, property, cardinality, filler):
        """
        :param property: an owlapy.model.OWLObjectPropertyExpression object
        :param cardinality: an integer
        :param filler: an owlapy.model.OWLClassExpression
        """
        super().__init__(property, cardinality, filler)
