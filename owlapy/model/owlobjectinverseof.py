from .owlobjectpropertyexpression import OWLObjectPropertyExpression


class OWLObjectInverseOf(OWLObjectPropertyExpression):
    """TODO: implement"""

    def __init__(self, inverse_property):
        """
        :param inverse_property: an owlapy.model.OWLObjectPropertyExpression
            object
        """
        super().__init__()
        self.inverse = inverse_property
