from .owlobject import OWLObject


class OWLDataComplementOf(OWLObject):
    """TODO: implement"""

    def __init__(self, data_range):
        """
        :param data_range: an owlapy.model.OWLDataRange object
        """
        super().__init__()
        self.data_range = data_range
