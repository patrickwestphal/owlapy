from .swrlunaryatom import SWRLUnaryAtom


class SWRLClassAtom(SWRLUnaryAtom):
    """TODO: implement"""

    def __init__(self, predicate, arg):
        """
        :param predicate: an owlapy.model.OWLClassExpression object
        :param arg: an owlapy.model.SWRLIArgument object
        """
        super().__init__(predicate, arg)