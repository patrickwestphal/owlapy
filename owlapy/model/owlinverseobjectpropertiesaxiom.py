from .axiomtype import AxiomType
from .owlaxiomvisitor import OWLAxiomVisitor, OWLAxiomVisitorEx
from .owlnarypropertyaxiom import OWLNaryPropertyAxiom
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


class OWLInverseObjectPropertiesAxiom(OWLNaryPropertyAxiom):
    """TODO: implement"""

    def __init__(self, first, second, annotations):
        """
        :param first: an owlapy.model.OWLObjectPropertyExpression object
        :param second: an owlapy.model.OWLObjectPropertyExpression object
        :param annotations: a set/list of OWLAnnotation objects
        """
        super().__init__([first, second], annotations)
        self.first_property = first
        self.second_property = second

        self._accept_fn_for_visitor_cls[OWLAxiomVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLAxiomVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.INVERSE_OBJECT_PROPERTIES
