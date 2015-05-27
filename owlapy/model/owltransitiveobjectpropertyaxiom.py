from .axiomtype import AxiomType
from .owlobjectpropertycharacteristicaxiom import \
    OWLObjectPropertyCharacteristicAxiom


class OWLTransitiveObjectPropertyAxiom(OWLObjectPropertyCharacteristicAxiom):
    """TODO: implmenent"""

    def __init__(self, property, annotations):
        """
        :param property: an owlapy.model.OWLObjectPropertyExpression object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(property, annotations)

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.TRANSITIVE_OBJECT_PROPERTY
