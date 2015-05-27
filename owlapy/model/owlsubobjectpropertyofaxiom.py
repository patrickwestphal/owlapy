from .axiomtype import AxiomType
from .owlsubpropertyaxiom import OWLSubPropertyAxiom


class OWLSubObjectPropertyOfAxiom(OWLSubPropertyAxiom):
    """TODO: implement"""

    def __init__(self, sub_property, super_property, annotations):
        """
        :param sub_property: an owlapy.model.OWLObjectPropertyExpression object
        :param super_property: an owlapy.model.OWLObjectPropertyExpression obj
        :param annotations: a set/list of OWLAnnotation objects
        """
        super().__init__(sub_property, super_property, annotations)

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.SUB_OBJECT_PROPERTY
