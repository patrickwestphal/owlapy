from .owlrestriction import OWLRestriction


class OWLQuantifiedRestriction(OWLRestriction):
    """TODO: implement"""

    def __init__(self, property, filler):
        """
        :param property: an owlapy.model.OWLPropertyExpression object
        :param filler: an owlapy.model.OWLPropertyRange object
        """
        super().__init__(property)
        self.filler = filler
