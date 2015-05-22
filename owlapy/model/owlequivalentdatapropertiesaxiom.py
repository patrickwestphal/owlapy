from .axiomtype import AxiomType
from .owlnarypropertyaxiom import OWLNaryPropertyAxiom


class OWLEquivalentDataPropertiesAxiom(OWLNaryPropertyAxiom):
    """TODO: implement"""

    def __init__(self, properties, annotations):
        """
        :param properties: a set of owlapy,model.OWLDataPropertyExpression
            objects
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        :return:
        """
        super().__init__(properties, annotations)

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.EQUIVALENT_DATA_PROPERTIES