from .exceptions import OWLRuntimeException
from .axiomtype import AxiomType
from .owlindividualaxiom import OWLIndividualAxiom
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLClassAssertionAxiom(OWLIndividualAxiom):
    """TODO: implement"""

    def __init__(self, individual, class_expression, annotations):
        """
        :param individual: an owlapy.model.OWLIndividual object
        :param class_expression: an owlapy.model.OWLClassExpression objects
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(annotations)
        self.individual = individual
        self.class_expression = class_expression

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.CLASS_ASSERTION

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
