from .owlanonymousclassexpression import OWLAnonymousClassExpression


class OWLRestriction(OWLAnonymousClassExpression):
    """TODO: implement"""

    def __init__(self, propery):
        """
        :param propery: an owlapy.model.OWLPropertyExpression object
        """
        super().__init__()
        self.property = property