class OWLDataRangeVisitor(object):
    """Marker class"""

    def visit(self, node):
        """
        :param node: an object of one of the following classes:
            - owlapy.model.OWLDatatype
            - owlapy.model.OWLDataOneOf
            - owlapy.model.OWLDataComplementOf
            - owlapy.model.OWLDataIntersectionOf
            - owlapy.model.OWLDataUnionOf
            - owlapy.model.OWLDatatypeRestriction
        :return: None
        """
        raise NotImplementedError()


class OWLDataRangeVisitorEx(object):
    """Marker class"""

    def visit(self, node):
        """
        :param node: an object of one of the following classes:
            - owlapy.model.OWLDatatype
            - owlapy.model.OWLDataOneOf
            - owlapy.model.OWLDataComplementOf
            - owlapy.model.OWLDataIntersectionOf
            - owlapy.model.OWLDataUnionOf
            - owlapy.model.OWLDatatypeRestriction
        """
        raise NotImplementedError()
