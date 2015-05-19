from .owlobjectpropertyaxiom import OWLObjectPropertyAxiom


class OWLObjectPropertyCharacteristicAxiom(OWLObjectPropertyAxiom):
    """TODO: implement"""

    def __init__(self, property, annotations):
        """
        :param property: an owlapy.model.OWLObjectPropertyExpression object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(annotations)
        self.property = property
