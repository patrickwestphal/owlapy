from .axiomtype import AxiomType
from .owlnaryclassaxiom import OWLNaryClassAxiom


class OWLEquivalentClassesAxiom(OWLNaryClassAxiom):
    """TODO: implement"""

    def __init__(self, class_expressions, annotations):
        """
        :param class_expressions: a set of owlapy.model.OWLClassExpression
            objects
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(class_expressions, annotations)
        self.named_classes = None

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.EQUIVALENT_CLASSES