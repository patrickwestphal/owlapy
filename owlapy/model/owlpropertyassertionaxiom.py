from .owlindividualrelationshipaxiom import OWLIndividualRelationshipAxiom


class OWLPropertyAssertionAxiom(OWLIndividualRelationshipAxiom):
    """TODO: implement"""

    def __init__(self, subject, property, object, annotations):
        super().__init__(subject, property, object, annotations)