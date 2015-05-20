from .owlobject import OWLObject


class SWRLLiteralArgument(OWLObject):
    """TODO: implement"""

    def __init__(self, literal):
        """
        :param literal: an owlapy.model.OWLLiteral object
        """
        super().__init__()
        self.literal = literal