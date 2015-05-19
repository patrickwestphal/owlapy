from .owlanonymousclassexpression import OWLAnonymousClassExpression


class OWLObjectOneOf(OWLAnonymousClassExpression):
    """TODO: implement"""

    def __init__(self, values):
        """
        :param values: a set of owlapy.model.OWLIndividual objects
        """
        super().__init__()
        self.values = values