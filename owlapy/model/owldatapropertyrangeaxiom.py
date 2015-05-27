from .axiomtype import AxiomType
from .owlpropertyrangeaxiom import OWLPropertyRangeAxiom


class OWLDataPropertyRangeAxiom(OWLPropertyRangeAxiom):
    """TODO: implement"""

    def __init__(self, property, range, annotations):
        """
        :param property: an owlapy.model.OWLDataPropertyExpression object
        :param range: an owlapy.model.OWLDataRange object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        :return:
        """
        super().__init__(property, range, annotations)

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.DATA_PROPERTY_RANGE
