from .owlcardinalityrestriction import OWLCardinalityRestriction


class OWLObjectCardinalityRestriction(OWLCardinalityRestriction):
    """TODO: implement"""

    def __init__(self, property, cardinality, filler):
        """
        :param property: an owlapy.model.OWLObjectPropertyExpression object
        :param cardinality: an integer
        :param filler: an owlapy.model.OWLClassExpression object
        """
        super().__init__(property, cardinality, filler)