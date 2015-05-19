from .owlpropertyaxiom import OWLPropertyAxiom


class OWLUnaryPropertyAxiom(OWLPropertyAxiom):
    """TODO: implement"""

    def __init__(self, property, annotations):
        """
        :param property: an owlapy.model.OWLPropertyExpression object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(annotations)
        self.property = property