from .owlpropertyaxiom import OWLPropertyAxiom


class OWLSubPropertyChainOfAxiom(OWLPropertyAxiom):
    """TODO: implement"""

    def __init__(self, property_chain, super_property, annotations):
        """
        :param property_chain: a list of
            owlapy.model.OWLObjectPropertyExpression objects
        :param super_property: an owlapy.model.OWLObjectPropertyExpression
            object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(annotations)
        self.property_chain = property_chain
        self.super_property = super_property