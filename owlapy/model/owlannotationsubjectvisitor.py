class OWLAnnotationSubjectVisitor(object):
    """Marker class"""

    def visit(self, visitee):
        """
        :param visitee: an object of one of the following classes:
            - owlapy.model.IRI
            - owlapy.model.OWLAnonymousIndividual
        """
        raise NotImplementedError()


class OWLAnnotationSubjectVisitorEx(object):
    """Marker class"""

    def visit(self, visitee):
        """
        :param visitee: an object of one of the following classes:
            - owlapy.,model.IRI
            - owlapy.,model.OWLAnonymousIndividual
        :return:
        """
        raise NotImplementedError
