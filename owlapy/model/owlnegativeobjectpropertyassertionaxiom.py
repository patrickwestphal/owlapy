from .owlpropertyassertionaxiom import OWLPropertyAssertionAxiom


class OWLNegativeObjectPropertyAssertionAxiom(OWLPropertyAssertionAxiom):
    """TODO: implement"""

    def __init__(self, subject, property, object, annotations):
        """
        :param subject: an owlapy.model.OWLIndividual object
        :param property: an owlapy.model.OWLObjectPropertyExpression object
        :param object: an owlapy.model.OWLIndividual object
        :param annotations: a list/set of owlapy.model.OWLAnnotation objects
        """
        super().__init__(subject, property, object, annotations)