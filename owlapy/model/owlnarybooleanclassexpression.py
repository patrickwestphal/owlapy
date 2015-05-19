from .owlanonymousclassexpression import OWLAnonymousClassExpression


class OWLNaryBooleanClassExpression(OWLAnonymousClassExpression):
    """TODO: implement"""

    def __init__(self, operands):
        """
        :param operands: a set of owlapy.model.OWLClassExpression objects
        """
        super().__init__()
        self.operands = operands