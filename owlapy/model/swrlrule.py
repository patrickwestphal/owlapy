from .axiomtype import AxiomType
from .owlaxiomvisitor import OWLAxiomVisitor, OWLAxiomVisitorEx
from .owllogicalaxiom import OWLLogicalAxiom
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from .swrlobjectvisitor import SWRLObjectVisitor, SWRLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


class SWRLRule(OWLLogicalAxiom):
    """TODO: implement"""

    def __init__(self, body, head, annotations):
        """
        :param body: a set of owlapy.model.SWRLAtom objects
        :param head: a set of owlapy.model.SWRLAtom objects
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(annotations)
        self.head = head
        self.body = body
        # containsAnonymousClassExpressions = hasAnon();

        self._accept_fn_for_visitor_cls[OWLAxiomVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLAxiomVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[SWRLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[SWRLObjectVisitorEx] = accept_default_ex

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.SWRL_RULE
