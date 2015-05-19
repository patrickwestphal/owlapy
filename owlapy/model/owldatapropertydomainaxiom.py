from .owlpropertydomainaxiom import OWLPropertyDomainAxiom


class OWLDataPropertyDomainAxiom(OWLPropertyDomainAxiom):
    """TODO: implement"""

    def __init__(self, property, domain, annotations):
        """
        :param property: an owlapy.model.OWLDataPropertyExpression object
        :param domain: an owlapy.model.OWLClassExpression object
        :param annotations: a set/list of OWLAnnotation objects
        """
        super().__init__(property, domain, annotations)