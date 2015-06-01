from .axiomtype import AxiomType
from .owlaxiomvisitor import OWLAxiomVisitor, OWLAxiomVisitorEx
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from .owlsubpropertyaxiom import OWLSubPropertyAxiom
from owlapy.util import accept_default, accept_default_ex


class OWLSubDataPropertyOfAxiom(OWLSubPropertyAxiom):
    """TODO: implement"""

    def __init__(self, sub_property, super_property, annotations):
        """
        :param sub_property: an owlapy.model.OWLDataPropertyExpression object
        :param super_property: an owlapy.model.OWLDataPropertyExpression object
        :param annotations:a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(sub_property, super_property, annotations)

        self._accept_fn_for_visitor_cls[OWLAxiomVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLAxiomVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.SUB_DATA_PROPERTY
