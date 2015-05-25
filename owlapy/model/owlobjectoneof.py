from .exceptions import OWLRuntimeException
from .owlanonymousclassexpression import OWLAnonymousClassExpression
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLObjectOneOf(OWLAnonymousClassExpression):
    """TODO: implement"""

    def __init__(self, values):
        """
        :param values: a set of owlapy.model.OWLIndividual objects
        """
        super().__init__()
        self.individuals = values


    def accept(self, visitor):
        """
        :param visitor: an object of one of the following classes:
            - owlapy.model.OWLClassExpressionVisitor
            - owlapy.model.OWLObjectVisitor
            - owlapy.model.OWLClassExpressionVisitorEx
            - owlapy.model.OWLObjectVisitorEx
        """
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
