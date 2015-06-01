from .axiomtype import AxiomType
from .owlaxiomvisitor import OWLAxiomVisitor, OWLAxiomVisitorEx
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from .owlpropertyrangeaxiom import OWLPropertyRangeAxiom
from owlapy.util import accept_default, accept_default_ex


class OWLObjectPropertyRangeAxiom(OWLPropertyRangeAxiom):
    """TODO: implement"""

    def __init__(self, property, range, annotations):
        """
        :param property: an owlapy.model.OWLObjectPropertyExpression object
        :param range: an owlapy.model.OWLClassExpression object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(property, range, annotations)

        self._accept_fn_for_visitor_cls[OWLAxiomVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLAxiomVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.OBJECT_PROPERTY_RANGE
