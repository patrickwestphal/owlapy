from .exceptions import OWLRuntimeException
from .owlnarydatarange import OWLNaryDataRange
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLDataIntersectionOf(OWLNaryDataRange):
    """TODO: implement"""

    def __init__(self, operands):
        """
        :param operands: a set of owlapy.model.OWLDataRange objects
        """
        super().__init__(operands)

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
