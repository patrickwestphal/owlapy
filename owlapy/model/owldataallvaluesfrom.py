from .owlquantifieddatarestriction import OWLQuantifiedDataRestriction


class OWLDataAllValuesFrom(OWLQuantifiedDataRestriction):
    """TODO: implement"""

    def __init__(self, property, filler):
        """
        :param property: an owlapy.model.OWLDataPropertyExpression object
        :param filler: an owlapy.model.OWLDataRange object
        """
        super().__init__(property, filler)