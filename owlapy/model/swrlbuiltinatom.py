from .exceptions import OWLRuntimeException
from .swrlatom import SWRLAtom
from .owlvisitor import OWLVisitorEx, OWLVisitor


class SWRLBuiltInAtom(SWRLAtom):
    """TODO: implement"""

    def __init__(self, predicate, args):
        """
        :param predicate: an owlapy.model.IRI object
        :param args: a list of owlapy.model.SWRLDArgument objects
        """
        super().__init__(predicate)
        self.arguments = args

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
