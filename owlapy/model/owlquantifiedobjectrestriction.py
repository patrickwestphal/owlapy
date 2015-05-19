from .owlquantifiedrestriction import OWLQuantifiedRestriction


class OWLQuantifiedObjectRestriction(OWLQuantifiedRestriction):
    """TODO: implement"""

    def __init__(self, property, filler):
        """
        :param property: an owlapy.model.OWLObjectPropertyExpression object
        :param filler: an owlapy.model.OWLClassExpression object
        """
        super().__init__(property, filler)