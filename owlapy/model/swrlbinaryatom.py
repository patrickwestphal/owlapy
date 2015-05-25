from .swrlatom import SWRLAtom


class SWRLBinaryAtom(SWRLAtom):
    """TODO: implement"""

    def __init__(self, predicate, arg0, arg1):
        """
        :param predicate: an owlapy.model.SWRLPredicate object
        :param arg0: an owlapy.model.SWRLArgument object
        :param arg1: an owlapy.model.SWRLArgument object

        FIXME: should not be callable!
        """
        super().__init__(predicate)
        self.first_argument = arg0
        self.second_argument = arg1