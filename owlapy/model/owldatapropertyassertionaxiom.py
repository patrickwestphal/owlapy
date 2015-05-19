from .owlindividualrelationshipaxiom import OWLIndividualRelationshipAxiom


class OWLDataPropertyAssertionAxiom(OWLIndividualRelationshipAxiom):
    """TODO: implement"""

    def __init__(self, subject, property, value, annotations):
        """
        :param subject: an owlapy.model.OWLIndividual object
        :param property: an owlapy.model.OWLDataPropertyExpression object
        :param value: an owlapy.model.OWLLiteral object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(subject, property, value, annotations)