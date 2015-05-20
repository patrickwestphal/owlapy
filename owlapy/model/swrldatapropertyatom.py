from .swrlbinaryatom import SWRLBinaryAtom


class SWRLDataPropertyAtom(SWRLBinaryAtom):
    """TODO: implement"""

    def __init__(self, predicate, arg0, arg1):
        """
        :param predicate: an owlapy.model.OWLDataPropertyExpression object
        :param arg0: an owlapy.model.SWRLIArgument object
        :param arg1: an owlapy.model.SWRLIArgument object
        """
        super().__init__(predicate, arg0, arg1)