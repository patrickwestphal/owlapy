from .owlvaluerestriction import OWLValueRestriction


class OWLObjectHasValue(OWLValueRestriction):
    """TODO: implement"""

    def __init__(self, property, value):
        """
        :param property: an owlapy.model.OWLObjectPropertyExpression object
        :param value: an owlapy.model.OWLIndividual value
        """
        super().__init__(property, value)
