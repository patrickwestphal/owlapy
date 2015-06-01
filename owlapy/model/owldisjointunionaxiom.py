from .axiomtype import AxiomType
from .owlaxiomvisitor import OWLAxiomVisitor, OWLAxiomVisitorEx
from .owlclassaxiom import OWLClassAxiom
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


class OWLDisjointUnionAxiom(OWLClassAxiom):
    """TODO: implement"""

    def __init__(self, owl_class, class_expressions, annotations):
        """
        :param owl_class: an owlapy.model.OWLClass object
        :param class_expressions: a set of OWLClassExpression objects
        :param annotations: a set/list of OWLAnnotation objects
        """
        super().__init__(annotations)
        self.owl_class = owl_class
        self.class_expressions = class_expressions

        self._accept_fn_for_visitor_cls[OWLAxiomVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLAxiomVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.DISJOINT_UNION
