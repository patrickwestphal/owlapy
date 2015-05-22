from .exceptions import OWLRuntimeException
from .axiomtype import AxiomType
from .owlnarypropertyaxiom import OWLNaryPropertyAxiom
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLInverseObjectPropertiesAxiom(OWLNaryPropertyAxiom):
    """TODO: implement"""

    def __init__(self, first, second, annotations):
        """
        :param first: an owlapy.model.OWLObjectPropertyExpression object
        :param second: an owlapy.model.OWLObjectPropertyExpression object
        :param annotations: a set/list of OWLAnnotation objects
        """
        super().__init__([first, second], annotations)
        self.first = first
        self.second = second

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.INVERSE_OBJECT_PROPERTIES

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
