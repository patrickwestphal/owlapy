from .swrlatom import SWRLAtom


class SWRLUnaryAtom(SWRLAtom):
    """TODO: implement"""

    def __init__(self, predicate, arg):
        """
        :param predicate: an owlapy.model.SWRLPredicate object
        :param arg: an owlapy.model.SWRLArgument object
        """
        super().__init__(predicate)
        self.argument = arg