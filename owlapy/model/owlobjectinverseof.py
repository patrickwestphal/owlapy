from .exceptions import OWLRuntimeException
from .owlobjectpropertyexpression import OWLObjectPropertyExpression
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLObjectInverseOf(OWLObjectPropertyExpression):
    """TODO: implement"""

    def __init__(self, inverse_property):
        """
        :param inverse_property: an owlapy.model.OWLObjectPropertyExpression
            object
        """
        super().__init__()
        self.inverse = inverse_property

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
