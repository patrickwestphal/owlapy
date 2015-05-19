from .owlindividualaxiom import OWLIndividualAxiom


class OWLNaryIndividualAxiom(OWLIndividualAxiom):
    """TODO: implement"""

    def __init__(self, individuals, annotations):
        """
        :param individuals: a set of owlapy.model.OWLIndividual objects
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(annotations)
        self.individuals = individuals