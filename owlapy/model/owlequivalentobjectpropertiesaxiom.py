from .axiomtype import AxiomType
from .owlaxiomvisitor import OWLAxiomVisitor, OWLAxiomVisitorEx
from .owlnarypropertyaxiom import OWLNaryPropertyAxiom
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


class OWLEquivalentObjectPropertiesAxiom(OWLNaryPropertyAxiom):
    """TODO: implement"""

    def __init__(self, properties, annotations):
        """
        :param properties: a set of owlapy.model.OWLObjectPropertyExpression
            objects
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(properties, annotations)

        self._accept_fn_for_visitor_cls[OWLAxiomVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLAxiomVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.EQUIVALENT_OBJECT_PROPERTIES
