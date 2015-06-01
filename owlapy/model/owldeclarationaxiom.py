from .axiomtype import AxiomType
from .owlaxiom import OWLAxiom
from .owlaxiomvisitor import OWLAxiomVisitor, OWLAxiomVisitorEx
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


class OWLDeclarationAxiom(OWLAxiom):
    """TODO: implement"""

    def __init__(self, entity, annotations):
        """
        :param entity: an owlapy.model.OWLEntity object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(annotations)
        self.entity = entity

        self._accept_fn_for_visitor_cls[OWLAxiomVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLAxiomVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.DECLARATION
