from .axiomtype import AxiomType
from .owlaxiomvisitor import OWLAxiomVisitor, OWLAxiomVisitorEx
from .owlnaryclassaxiom import OWLNaryClassAxiom
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


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

        self._accept_fn_for_visitor_cls[OWLAxiomVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLAxiomVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.EQUIVALENT_CLASSES
