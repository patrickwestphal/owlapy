from .exceptions import OWLRuntimeException
from .axiomtype import AxiomType
from .owlclassaxiom import OWLClassAxiom
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLDisjointUnionAxiom(OWLClassAxiom):
    """TODO: implement"""

    def __init__(self, owl_class, class_expressions, annotations):
        """
        :param owl_class: an owlapy.model.OWLClass object
        :param class_expressions: a set of OWLClassExpression objects
        :param annotations: a set/list of OWLAnnotation objects
        """
        super().__init__(annotations)
        self.owl_class = owl_class
        self.class_expressions = class_expressions

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.DISJOINT_UNION

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
