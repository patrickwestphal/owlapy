from .exceptions import OWLRuntimeException
from .owlobject import OWLObject
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLDataComplementOf(OWLObject):
    """TODO: implement"""

    def __init__(self, data_range):
        """
        :param data_range: an owlapy.model.OWLDataRange object
        """
        super().__init__()
        self.data_range = data_range

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
