from .owlunarypropertyaxiom import OWLUnaryPropertyAxiom


class OWLPropertyRangeAxiom(OWLUnaryPropertyAxiom):
    """TODO: implement"""

    def __init__(self, property, range, annotations):
        """
        :param property: an owlapy.model.OWLPropertyExpression object
        :param range: an owlapy.model.OWLPropertyRange object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(property, annotations)
        self.range = range