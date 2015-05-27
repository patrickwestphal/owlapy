from .owlvisitor import OWLVisitor, OWLVisitorEx


class OWLAnnotationAxiomVisitor(OWLVisitor):
    """Marker class"""

    def visit(self, axiom):
        """
        :param axiom: an object of one of these classes:
            - owlapy.model.OWLAnnotationAssertionAxiom
            - owlapy.model.OWLSubAnnotationPropertyOfAxiom
            - owlapy.model.OWLAnnotationPropertyDomainAxiom
            - owlapy.model.OWLAnnotationPropertyRangeAxiom
        :return: None
        """
        raise NotImplementedError()


class OWLAnnotationVisitorEx(OWLVisitorEx):
    """Marker Class"""

    def visit(self, axiom):
        """
        :param axiom: an object of one of these classes:
            - owlapy.model.OWLAnnotationAssertionAxiom
            - owlapy.model.OWLSubAnnotationPropertyOfAxiom
            - owlapy.model.OWLAnnotationPropertyDomainAxiom
            - owlapy.model.OWLAnnotationPropertyRangeAxiom
        """
        raise NotImplementedError()
