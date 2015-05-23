class OWLPropertyExpressionVisitor(object):
    """Marker class"""

    def visit(self, property):
        """
        :param property: an object of one of the following classes:
            - owlapy.model.OWLObjectProperty
            - owlapy.model.OWLObjectInverseOf
            - owlapy.model.OWLDataProperty
        :return: None
        """
        raise NotImplementedError()
