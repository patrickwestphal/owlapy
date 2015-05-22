from .exceptions import OWLRuntimeException
from .axiomtype import AxiomType
from .owlpropertyrangeaxiom import OWLPropertyRangeAxiom
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLFunctionalDataPropertyAxiom(OWLPropertyRangeAxiom):
    """TODO: implement"""

    def __init__(self, property, range, annotations):
        """
        :param property: an owlapy.model.OWLDataPropertyExpression object
        :param range: an owlapy.model.OWLDataRange object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(property, range, annotations)

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.FUNCTIONAL_DATA_PROPERTY

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
