from .exceptions import OWLRuntimeException
from .axiomtype import AxiomType
from .owlpropertyaxiom import OWLPropertyAxiom
from .owlvisitor import OWLVisitorEx, OWLVisitor


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

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.SUB_PROPERTY_CHAIN_OF

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
