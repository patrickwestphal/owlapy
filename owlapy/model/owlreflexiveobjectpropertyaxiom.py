from .axiomtype import AxiomType
from .owlaxiomvisitor import OWLAxiomVisitor, OWLAxiomVisitorEx
from .owlobjectpropertycharacteristicaxiom import \
    OWLObjectPropertyCharacteristicAxiom
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


class OWLReflexiveObjectPropertyAxiom(OWLObjectPropertyCharacteristicAxiom):
    """TODO: implement"""

    def __init__(self, property, annotations):
        """
        :param property: an owlapy.model.OWLObjectPropertyExpression object
        :param annotations: a list/set of owlapy.model.OWLAnnotation objects
        """
        super().__init__(property, annotations)

        self._accept_fn_for_visitor_cls[OWLAxiomVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLAxiomVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.REFLEXIVE_OBJECT_PROPERTY
