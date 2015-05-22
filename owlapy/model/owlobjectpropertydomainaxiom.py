from .exceptions import OWLRuntimeException
from .axiomtype import AxiomType
from .owlpropertydomainaxiom import OWLPropertyDomainAxiom
from .owlvisitor import OWLVisitorEx, OWLVisitor


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

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
