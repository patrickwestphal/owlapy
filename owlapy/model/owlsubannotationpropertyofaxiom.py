from .axiomtype import AxiomType
from .owlaxiom import OWLAxiom
from .owlaxiomvisitor import OWLAxiomVisitor, OWLAxiomVisitorEx
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


class OWLSubAnnotationPropertyOfAxiom(OWLAxiom):
    """TODO: implement"""

    def __init__(self, sub_property, super_property, annotations):
        """
        :param sub_property: an owlapy.model.OWLAnnotationProperty object
        :param super_property: an owlapy.model.OWLAnnotationProperty object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        :return:
        """
        super().__init__(annotations)
        self.sub_property = sub_property
        self.super_property = super_property

        self._accept_fn_for_visitor_cls[OWLAxiomVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLAxiomVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.SUB_ANNOTATION_PROPERTY_OF
