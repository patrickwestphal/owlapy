from .owldatarangevisitor import OWLDataRangeVisitor


class OWLDataVisitor(OWLDataRangeVisitor):
    """Marker class"""

    def visit(self, node):
        """
        :param node: an object of one of the following classes:
            - owlapy.model.OWLLiteral
            - owlapy.model.OWLFacetRestriction
        :return: None
        """
        raise NotImplementedError()

class OWLDataVisitorEx(object):
    """Marker class"""

    def visit(self, node):
        """
        :param node: an object of one of the following classes:
            - owlapy.model.OWLDatatype
            - owlapy.model.OWLDataComplementOf
            - owlapy.model.OWLDataOneOf
            - owlapy.model.OWLDataIntersectionOf
            - owlapy.model.OWLDataUnionOf
            - owlapy.model.OWLDatatypeRestriction
            - owlapy.model.OWLLiteral
            - owlapy.model.OWLFacetRestriction
        """
        raise NotImplementedError()
