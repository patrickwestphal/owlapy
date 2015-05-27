from .axiomtype import AxiomType
from .owlaxiom import OWLAxiom


class OWLAnnotationPropertyDomainAxiom(OWLAxiom):
    """TODO: implement"""

    def __init__(self, property, domain, annotations):
        """
        :param property: an owlapy.model.OWLAnnotationProperty object
        :param domain: an owlapy.model.IRI object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(annotations)
        self.domain = domain
        self.property = property

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.ANNOTATION_PROPERTY_DOMAIN
