from .exceptions import OWLRuntimeException
from .axiomtype import AxiomType
from .owlpropertyrangeaxiom import OWLPropertyRangeAxiom
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLObjectPropertyRangeAxiom(OWLPropertyRangeAxiom):
    """TODO: implement"""

    def __init__(self, property, range, annotations):
        """
        :param property: an owlapy.model.OWLObjectPropertyExpression object
        :param range: an owlapy.model.OWLClassExpression object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(property, range, annotations)

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.OBJECT_PROPERTY_RANGE

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
