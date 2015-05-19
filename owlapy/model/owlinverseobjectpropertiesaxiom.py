from .owlnarypropertyaxiom import OWLNaryPropertyAxiom


class OWLInverseObjectPropertiesAxiom(OWLNaryPropertyAxiom):
    """TODO: implement"""

    def __init__(self, first, second, annotations):
        """
        :param first: an owlapy.model.OWLObjectPropertyExpression object
        :param second: an owlapy.model.OWLObjectPropertyExpression object
        :param annotations: a set/list of OWLAnnotation objects
        """
        super().__init__([first, second], annotations)
        self.first = first
        self.second = second