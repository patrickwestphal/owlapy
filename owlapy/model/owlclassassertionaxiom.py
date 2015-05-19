from .owlindividualaxiom import OWLIndividualAxiom


class OWLClassAssertionAxiom(OWLIndividualAxiom):
    """TODO: implement"""

    def __init__(self, individual, class_expression, annotations):
        """
        :param individual: an owlapy.model.OWLIndividual object
        :param class_expression: an owlapy.model.OWLClassExpression objects
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(annotations)
        self.individual = individual
        self.class_expression = class_expression