from .axiomtype import AxiomType
from .owlaxiomvisitor import OWLAxiomVisitor, OWLAxiomVisitorEx
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from .owlsubpropertyaxiom import OWLSubPropertyAxiom
from owlapy.util import accept_default, accept_default_ex


class OWLSubObjectPropertyOfAxiom(OWLSubPropertyAxiom):
    """TODO: implement"""

    def __init__(self, sub_property, super_property, annotations):
        """
        :param sub_property: an owlapy.model.OWLObjectPropertyExpression object
        :param super_property: an owlapy.model.OWLObjectPropertyExpression obj
        :param annotations: a set/list of OWLAnnotation objects
        """
        super().__init__(sub_property, super_property, annotations)

        self._accept_fn_for_visitor_cls[OWLAxiomVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLAxiomVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.SUB_OBJECT_PROPERTY
