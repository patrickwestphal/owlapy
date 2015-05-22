from .exceptions import OWLRuntimeException
from .swrlunaryatom import SWRLUnaryAtom
from .owlvisitor import OWLVisitorEx, OWLVisitor


class SWRLDataRangeAtom(SWRLUnaryAtom):
    """TODO: implement"""

    def __init__(self, predicate, arg):
        """
        :param predicate: an owapy.model.OWLDataRange object
        :param arg: an owlapy.model.SWRLDArgument object
        """
        super().__init__(predicate, arg)

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')