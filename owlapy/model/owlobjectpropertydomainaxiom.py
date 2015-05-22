from .axiomtype import AxiomType
from .owlpropertydomainaxiom import OWLPropertyDomainAxiom


class OWLObjectPropertyDomainAxiom(OWLPropertyDomainAxiom):
    """TODO: implement"""

    def __init__(self, property, domain, annotations):
        """
        :param property: an owlapy.model.OWLObjectPropertyExpression object
        :param domain: an owlapy.model.OWLClassExpression object
        :param annotations: s set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(property, domain, annotations)

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.OBJECT_PROPERTY_DOMAIN