from .owlanonymousclassexpression import OWLAnonymousClassExpression


class OWLRestriction(OWLAnonymousClassExpression):
    """TODO: implement"""

    def __init__(self, property):
        """
        :param property: an owlapy.model.OWLPropertyExpression object
        """
        super().__init__()
        self.property = property