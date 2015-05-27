class SWRLObjectVisitor(object):
    """Marker class"""

    def visit(self, node):
        """
        :param node: an object of one of the following classes:
            - owlapy.model.SWRLRule
            - owlapy.model.SWRLClassAtom
            - owlapy.model.SWRLDataRangeAtom
            - owlapy.model.SWRLObjectPropertyAtom
            - owlapy.model.SWRLDataPropertyAtom
            - owlapy.model.SWRLBuiltInAtom
            - owlapy.model.SWRLVariable
            - owlapy.model.SWRLIndividualArgument
            - owlapy.model.SWRLLiteralArgument
            - owlapy.model.SWRLSameIndividualAtom
            - owlapy.model.SWRLDifferentIndividualsAtom
        """
        raise NotImplementedError()


class SWRLObjectVisitorEx(object):
    """Marker class"""

    def visit(self, node):
        """
        :param node: an object of one of the following classes:
            - owlapy.model.SWRLRule
            - owlapy.model.SWRLClassAtom
            - owlapy.model.SWRLDataRangeAtom
            - owlapy.model.SWRLObjectPropertyAtom
            - owlapy.model.SWRLDataPropertyAtom
            - owlapy.model.SWRLBuiltInAtom
            - owlapy.model.SWRLVariable
            - owlapy.model.SWRLIndividualArgument
            - owlapy.model.SWRLLiteralArgument
            - owlapy.model.SWRLSameIndividualAtom
            - owlapy.model.SWRLDifferentIndividualsAtom
        """
        raise NotImplementedError()
