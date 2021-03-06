class OWLNamedObjectVisitor(object):
    """Marker class"""

    def visit(self, visitee):
        """
        :param visitee: an object of one of the following classes:
            - owlapy.model.OWLClass
            - owlapy.model.OWLObjectProperty
            - owlapy.model.OWLDataProperty
            - owlapy.model.OWLNamedIndividual
            - owlapy.model.OWLOntology
            - owlapy.model.OWLDatatype
            - owlapy.model.OWLAnnotationProperty
        :return: None
        """
        raise NotImplementedError()


class OWLNamedObjectVisitorEx(object):
    """Marker class"""

    def visit(self, visitee):
        """
        :param visitee: an object of one of the following classes:
            - owlapy.model.OWLClass
            - owlapy.model.OWLObjectProperty
            - owlapy.model.OWLDataProperty
            - owlapy.model.OWLNamedIndividual
            - owlapy.model.OWLOntology
            - owlapy.model.OWLDatatype
            - owlapy.model.OWLAnnotationProperty
        """
        raise NotImplementedError()
