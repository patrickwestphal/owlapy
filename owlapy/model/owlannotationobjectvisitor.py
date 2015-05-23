from .owlannotationaxiomvisitor import OWLAnnotationAxiomVisitor


class OWLAnnotationObjectVisitor(OWLAnnotationAxiomVisitor):
    """Marker class"""

    def visit(self, node):
        """
        :param node: an owlapy.model.OWLAnnotation object
        :return: None
        """
        raise NotImplementedError()
