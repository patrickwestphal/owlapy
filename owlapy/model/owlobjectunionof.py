from .owlnarybooleanclassexpression import OWLNaryBooleanClassExpression


class OWLObjectUnionOf(OWLNaryBooleanClassExpression):
    """TODO: implement"""

    def __init__(self, operands):
        """
        :param operands: a set of OWLClassExpression objects
        """
        super().__init__(operands)