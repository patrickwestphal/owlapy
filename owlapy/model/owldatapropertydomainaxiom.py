from .axiomtype import AxiomType
from .owlaxiomvisitor import OWLAxiomVisitor, OWLAxiomVisitorEx
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from .owlpropertydomainaxiom import OWLPropertyDomainAxiom
from owlapy.util import accept_default, accept_default_ex


class OWLDataPropertyDomainAxiom(OWLPropertyDomainAxiom):
    """TODO: implement"""

    def __init__(self, property, domain, annotations):
        """
        :param property: an owlapy.model.OWLDataPropertyExpression object
        :param domain: an owlapy.model.OWLClassExpression object
        :param annotations: a set/list of OWLAnnotation objects
        """
        super().__init__(property, domain, annotations)

        self._accept_fn_for_visitor_cls[OWLAxiomVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLAxiomVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.DATA_PROPERTY_DOMAIN
