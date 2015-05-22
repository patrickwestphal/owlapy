from .exceptions import OWLRuntimeException
from .owlobject import OWLObject
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLDataOneOf(OWLObject):
    """TODO: implement"""

    def __init__(self, values):
        """
        :param values: a set of owlapy.model.OWLLiteral objects
        """
        super().__init__()
        self.values = values

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
