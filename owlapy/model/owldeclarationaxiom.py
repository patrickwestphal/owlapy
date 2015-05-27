from .axiomtype import AxiomType
from .owlaxiom import OWLAxiom


class OWLDeclarationAxiom(OWLAxiom):
    """TODO: implement"""

    def __init__(self, entity, annotations):
        """
        :param entity: an owlapy.model.OWLEntity object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(annotations)
        self.entity = entity

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.DECLARATION
