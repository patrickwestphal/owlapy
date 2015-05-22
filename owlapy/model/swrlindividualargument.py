from .exceptions import OWLRuntimeException
from .owlobject import OWLObject
from .owlvisitor import OWLVisitorEx, OWLVisitor


class SWRLIndividualArgument(OWLObject):
    """TOOD: implement"""

    def __init__(self, individual):
        """
        :param individual: an owlapy.model.OWLIndividual object
        """
        super().__init__()
        self.individual = individual

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
