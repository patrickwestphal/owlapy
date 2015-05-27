from .axiomtype import AxiomType
from .owlnaryindividualaxiom import OWLNaryIndividualAxiom


class OWLDifferentIndividualsAxiom(OWLNaryIndividualAxiom):
    """TODO: implement"""

    def __init__(self, individuals, annotations):
        """
        :param individuals: a set of owlapy.model.OWLIndividual objects
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(individuals, annotations)

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.DIFFERENT_INDIVIDUALS
