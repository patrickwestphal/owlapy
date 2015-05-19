from .owlunarypropertyaxiom import OWLUnaryPropertyAxiom


class OWLPropertyDomainAxiom(OWLUnaryPropertyAxiom):
    """TODO: implement"""

    def __init__(self, property, domain, annotations):
        """
        :param property: an owlapy.model.OWLPropertyExpression object
        :param domain: an owlapy.model.OWLClassExpression object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(property, annotations)
        self.domain = domain
