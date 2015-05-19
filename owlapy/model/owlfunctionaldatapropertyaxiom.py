from .owlpropertyrangeaxiom import OWLPropertyRangeAxiom


class OWLFunctionalDataPropertyAxiom(OWLPropertyRangeAxiom):
    """TODO: implement"""

    def __init__(self, property, range, annotations):
        """
        :param property: an owlapy.model.OWLDataPropertyExpression object
        :param range: an owlapy.model.OWLDataRange object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(property, range, annotations)