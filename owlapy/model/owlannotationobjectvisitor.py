from .owlannotationaxiomvisitor import OWLAnnotationAxiomVisitor,\
    OWLAnnotationAxiomVisitorEx


class OWLAnnotationObjectVisitor(OWLAnnotationAxiomVisitor):
    """Marker class"""

    def visit(self, node):
        """
        :param node: an owlapy.model.OWLAnnotation object
        :return: None
        """
        raise NotImplementedError()


class OWLAnnotationObjectVisitorEx(OWLAnnotationAxiomVisitorEx):
    """Marker class"""

    def visit(self, node):
        """
        :param node: an owlapy.model.OWLAnnotation object
        """
        raise NotImplementedError()
