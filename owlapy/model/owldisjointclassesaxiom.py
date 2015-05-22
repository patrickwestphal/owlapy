from .axiomtype import AxiomType
from .owlnaryclassaxiom import OWLNaryClassAxiom


class OWLDisjointClassesAxiom(OWLNaryClassAxiom):
    """TODO: implement"""

    def __init__(self, class_expressions, annotations):
        """
        :param class_expressions: a set of owlapy.model.OWLClassExpression
            objects
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(class_expressions, annotations)

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.DISJOINT_CLASSES
