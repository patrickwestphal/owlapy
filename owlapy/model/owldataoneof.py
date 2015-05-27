from .owlobject import OWLObject


class OWLDataOneOf(OWLObject):
    """TODO: implement"""

    def __init__(self, values):
        """
        :param values: a set of owlapy.model.OWLLiteral objects
        """
        super().__init__()
        self.values = values
