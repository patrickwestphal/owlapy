from .owlanonymousclassexpression import OWLAnonymousClassExpression


class OWLObjectComplementOf(OWLAnonymousClassExpression):
    """TODO: implement"""

    def __init__(self, operand):
        """
        :param operands: an owlapy.model.OWLClassExpression object
        """
        super().__init__()
        self.operand = operand
