from .axiomtype import AxiomType
from .owlaxiomvisitor import OWLAxiomVisitor, OWLAxiomVisitorEx
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from .owlpropertyaxiom import OWLPropertyAxiom
from owlapy.util import accept_default, accept_default_ex


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

        self._accept_fn_for_visitor_cls[OWLAxiomVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLAxiomVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.SUB_PROPERTY_CHAIN_OF
