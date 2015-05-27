from .axiomtype import AxiomType
from .owlindividualrelationshipaxiom import OWLIndividualRelationshipAxiom


class OWLObjectPropertyAssertionAxiom(OWLIndividualRelationshipAxiom):
    """TODO: implement"""

    def __init__(self, subject, property, object, annotations):
        """
        :param subject: an owlapy.model.OWLIndividual object
        :param property: an owlapy.model.OWLObjectPropertyExpression object
        :param object: an owlapy.model.OWLIndividual object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(subject, property, object, annotations)

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.OBJECT_PROPERTY_ASSERTION
