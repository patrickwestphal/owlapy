from .owlobject import OWLObject


class SWRLIndividualArgument(OWLObject):
    """TOOD: implement"""

    def __init__(self, individual):
        """
        :param individual: an owlapy.model.OWLIndividual object
        """
        super().__init__()
        self.individual = individual
