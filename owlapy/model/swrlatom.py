from .owlobject import OWLObject


class SWRLAtom(OWLObject):
    """TODO: implement"""

    def __init__(self, predicate):
        """
        :param predicate: an owlapy.model.SWRLPredicate object

        FIXME: should not be callable!
        """
        super().__init__()
        self.predicate = predicate

