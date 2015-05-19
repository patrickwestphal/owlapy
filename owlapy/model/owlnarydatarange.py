from .owlobject import OWLObject


class OWLNaryDataRange(OWLObject):
    """TODO: implement"""

    def __init__(self, operands):
        """
        :param operands: a set of owlapy.model.OWLDataRange objects
        """
        super().__init__()
        self.operands = operands