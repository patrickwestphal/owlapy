from .swrlunaryatom import SWRLUnaryAtom


class SWRLDataRangeAtom(SWRLUnaryAtom):
    """TODO: implement"""

    def __init__(self, predicate, arg):
        """
        :param predicate: an owapy.model.OWLDataRange object
        :param arg: an owlapy.model.SWRLDArgument object
        """
        super().__init__(predicate, arg)
