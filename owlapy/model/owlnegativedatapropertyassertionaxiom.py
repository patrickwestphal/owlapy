from .axiomtype import AxiomType
from .owlindividualrelationshipaxiom import OWLIndividualRelationshipAxiom


class OWLNegativeDataPropertyAssertionAxiom(OWLIndividualRelationshipAxiom):
    """TODO: implement"""

    def __init__(self, subject, property, object, annotations):
        """
        :param subject: an owlapy.model.OWLIndividual object
        :param property: an owlapy.model.OWLDataPropertyExpression object
        :param object: an owlapy.model.OWLLiteral object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(subject, property, object, annotations)

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.NEGATIVE_DATA_PROPERTY_ASSERTION