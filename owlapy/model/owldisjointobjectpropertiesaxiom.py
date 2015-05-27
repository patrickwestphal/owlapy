from .axiomtype import AxiomType
from .owlnarypropertyaxiom import OWLNaryPropertyAxiom


class OWLDisjointObjectPropertiesAxiom(OWLNaryPropertyAxiom):
    """TODO: implement"""

    def __init__(self, properties, annotations):
        """
        :param properties: a set of owlapy.model.OWLObjectPropertyExpression
            objects
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(properties, annotations)

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.DISJOINT_OBJECT_PROPERTIES
