from .owlpropertyaxiom import OWLPropertyAxiom


class OWLNaryPropertyAxiom(OWLPropertyAxiom):
    """TODO: implement"""

    def __init__(self, properties, annotations):
        """
        :param properties: a set of owlapy.model.OWLPropertyExpression objects
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(annotations)
        self.properties = properties