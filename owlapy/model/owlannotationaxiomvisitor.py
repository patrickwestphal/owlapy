class OWLAnnotationAxiomVisitor(object):
    """Marker class"""

    def visit(self, axiom):
        """
        :param axiom: objects of one of these classes:
            - owlapy.model.OWLAnnotationAssertionAxiom
            - owlapy.model.OWLSubAnnotationPropertyOfAxiom
            - owlapy.model.OWLAnnotationPropertyDomainAxiom
            - owlapy.model.OWLAnnotationPropertyRangeAxiom
        :return: None
        """
        raise NotImplementedError()
