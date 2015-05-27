class OWLIndividualVisitor(object):
    """Marker class"""

    def visit(self, individual):
        """
        :param individual: an object of one of the following classes:
            - owlapy.model.OWLNamedIndividual
            - owlapy.model.OWLAnonymousIndividual
        :return:
        """
        raise NotImplementedError()


class OWLIndividualVisitorEx(object):
    """Marker class"""

    def visit(self, individual):
        """
        :param individual: an object of one of the following classes:
            - owlapy.model.OWLNamedIndividual
        """
        raise NotImplementedError()