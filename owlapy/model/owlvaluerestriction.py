from .owlrestriction import OWLRestriction


class OWLValueRestriction(OWLRestriction):
    """TODO: implement"""

    def __init__(self, property, value):
        """
        :param property: an owlapy.model.OWLPropertyExpression object
        :param value: an owlapy.model.OWLObject
        """
        super().__init__(property)
        self.value = value