from .owlannotationaxiomvisitor import OWLAnnotationAxiomVisitorEx


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
        raise NotImplementedError()


class OWLAnnotationObjectVisitorEx(OWLAnnotationAxiomVisitorEx):
    """Marker class"""

    def visit(self, visitee):
        """
        :param visitee: an owlapy.model.OWLAnnotation object
        """
        raise NotImplementedError()
