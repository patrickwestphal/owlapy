from .owlvaluerestriction import OWLValueRestriction


class OWLDataHasValue(OWLValueRestriction):
    """TODO: implement"""

    def __init__(self, property, value):
        """
        :param property: an owlapy.model.OWLDataPropertyExpression object
        :param value: an owlapy.model.OWLLiteral object
        """
        super().__init__(property, value)
