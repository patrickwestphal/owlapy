from .owlnarydatarange import OWLNaryDataRange


class OWLDataIntersectionOf(OWLNaryDataRange):
    """TODO: implement"""

    def __init__(self, operands):
        """
        :param operands: a set of owlapy.model.OWLDataRange objects
        """
        super().__init__(operands)