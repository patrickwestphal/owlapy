from .owlnarybooleanclassexpression import OWLNaryBooleanClassExpression


class OWLObjectIntersectionOf(OWLNaryBooleanClassExpression):
    """TODO: implement"""

    def __init__(self, operands):
        """
        :param operands: a set of owlapy.model.OWLClassExpression objects
        """
        super().__init__(operands)
