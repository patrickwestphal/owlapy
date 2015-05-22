from .exceptions import OWLRuntimeException
from .axiomtype import AxiomType
from .owlnaryclassaxiom import OWLNaryClassAxiom
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLDisjointClassesAxiom(OWLNaryClassAxiom):
    """TODO: implement"""

    def __init__(self, class_expressions, annotations):
        """
        :param class_expressions: a set of owlapy.model.OWLClassExpression
            objects
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(class_expressions, annotations)

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.DISJOINT_CLASSES

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
