from .owlrestriction import OWLRestriction


class OWLObjectHasSelf(OWLRestriction):
    """TODO; implement"""

    def __init__(self, property):
        """
        :param property: an owlapy.model.OWLObjectPropertyExpression object
        """
        super().__init__(property)
