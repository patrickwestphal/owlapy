from .owlnaryindividualaxiom import OWLNaryIndividualAxiom


class OWLSameIndividualAxiom(OWLNaryIndividualAxiom):
    """TODO: implement"""

    def __init__(self, individuals, annotations):
        """
        :param individuals: a set of owlapy.model.OWLIndividual objects
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(individuals, annotations)