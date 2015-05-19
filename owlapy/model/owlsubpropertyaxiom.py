from .owlpropertyaxiom import OWLPropertyAxiom


class OWLSubPropertyAxiom(OWLPropertyAxiom):
    """TODO: implement"""

    def __init__(self, sub_property, super_property, annotations):
        """
        :param sub_property: an owlapy.model.OWLPropertyExpression object
        :param super_property: an owlapy.model.OWLPropertyExpression object
        :param annotations: a list/set of owlapy.model.OWLAnnotations objects
        """
        super().__init__(annotations)
        self.sub_property = sub_property
        self.super_property = super_property