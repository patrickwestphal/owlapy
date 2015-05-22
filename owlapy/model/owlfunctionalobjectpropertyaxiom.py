from .axiomtype import AxiomType
from .owlobjectpropertycharacteristicaxiom import \
    OWLObjectPropertyCharacteristicAxiom


class OWLFunctionalObjectPropertyAxiom(OWLObjectPropertyCharacteristicAxiom):
    """TODO: implement"""

    def __init__(self, property, annotations):
        """
        :param property: an owlapy.model.OWLObjectPropertyExpression object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(property, annotations)

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.FUNCTIONAL_OBJECT_PROPERTY