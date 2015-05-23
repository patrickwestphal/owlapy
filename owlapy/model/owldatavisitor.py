from .owldatarangevisitor import OWLDataRangeVisitor


class OWLDataVisitor(OWLDataRangeVisitor):
    """Marker class"""

    def visit(self, node):
        """
        :param node: an object of one of the following classes:
            - OWLLiteral
            - OWLFacetRestriction
        :return: None
        """
        raise NotImplementedError()
