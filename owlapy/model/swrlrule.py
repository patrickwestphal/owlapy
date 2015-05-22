from .exceptions import OWLRuntimeException
from .axiomtype import AxiomType
from .owllogicalaxiom import OWLLogicalAxiom
from .owlvisitor import OWLVisitorEx, OWLVisitor


class SWRLRule(OWLLogicalAxiom):
    """TODO: implement"""

    def __init__(self, body, head, annotations):
        """
        :param body: a set of owlapy.model.SWRLAtom objects
        :param head: a set of owlapy.model.SWRLAtom objects
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(annotations)
        self.head = head
        self.body = body
        # containsAnonymousClassExpressions = hasAnon();

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.SWRL_RULE

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
