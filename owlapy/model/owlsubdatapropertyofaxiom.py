from .owlsubpropertyaxiom import OWLSubPropertyAxiom


class OWLSubDataPropertyOfAxiom(OWLSubPropertyAxiom):
    """TODO: implement"""

    def __init__(self, sub_property, super_property, annotations):
        """
        :param sub_property: an owlapy.model.OWLDataPropertyExpression object
        :param super_property: an owlapy.model.OWLDataPropertyExpression object
        :param annotations:a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(sub_property, super_property, annotations)
