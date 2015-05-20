from .owlobject import OWLObject


class SWRLAtom(OWLObject):
    """TODO: implement"""

    def __init__(self, predicate):
        """
        :param predicate: an owlapy.model.SWRLPredicate object
        """
        super().__init__()
        self.predicate = predicate