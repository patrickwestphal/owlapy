class OWLAnnotationValueVisitor(object):
    """Marker class"""

    def visit(self, visitee):
        """
        :param visitee: an object of one of the following classes:
            - owlapy.model.IRI
            - owlapy.model.OWLAnonymousIndividual
            - owlapy.model.OWLLiteral
        :return:
        """