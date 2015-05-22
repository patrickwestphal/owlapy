from .exceptions import OWLRuntimeException
from .swrlbinaryatom import SWRLBinaryAtom
from .owlvisitor import OWLVisitorEx, OWLVisitor


class SWRLDataPropertyAtom(SWRLBinaryAtom):
    """TODO: implement"""

    def __init__(self, predicate, arg0, arg1):
        """
        :param predicate: an owlapy.model.OWLDataPropertyExpression object
        :param arg0: an owlapy.model.SWRLIArgument object
        :param arg1: an owlapy.model.SWRLIArgument object
        """
        super().__init__(predicate, arg0, arg1)

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
