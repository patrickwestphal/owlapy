from .swrlatom import SWRLAtom


class SWRLBuiltInAtom(SWRLAtom):
    """TODO: implement"""

    def __init__(self, predicate, args):
        """
        :param predicate: an owlapy.model.IRI object
        :param args: a list of owlapy.model.SWRLDArgument objects
        """
        super().__init__(predicate)
        self.arguments = args