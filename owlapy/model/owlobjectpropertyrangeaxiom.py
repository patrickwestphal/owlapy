from .owlpropertyrangeaxiom import OWLPropertyRangeAxiom


class OWLObjectPropertyRangeAxiom(OWLPropertyRangeAxiom):
    """TODO: implement"""

    def __init__(self, property, range, annotations):
        """
        :param property: an owlapy.model.OWLObjectPropertyExpression object
        :param range: an owlapy.model.OWLClassExpression object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(property, range, annotations)