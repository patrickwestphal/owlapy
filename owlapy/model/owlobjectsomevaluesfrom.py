from .exceptions import OWLRuntimeException
from .owlquantifiedobjectrestriction import OWLQuantifiedObjectRestriction
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLObjectSomeValuesFrom(OWLQuantifiedObjectRestriction):
    """TODO: implement"""

    def __init__(self, property, filler):
        """
        :param property: an owlapy.model.OWLObjectPropertyExpression object
        :param filler: an owlapy.model.OWLClassExpression object
        """
        super().__init__(property, filler)

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
