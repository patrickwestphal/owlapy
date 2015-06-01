from .axiomtype import AxiomType
from .owlaxiomvisitor import OWLAxiomVisitor, OWLAxiomVisitorEx
from .owllogicalaxiom import OWLLogicalAxiom
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


class OWLHasKeyAxiom(OWLLogicalAxiom):
    """TODO: implement"""

    def __init__(self, class_expression, property_expressions, annotations):
        """
        :param class_expression: an owlapy.model.OWLClassExpression object
        :param property_expressions: a set of owlapy.model.OWLPropertyExpression
            objects
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(annotations)
        self.class_expression = class_expression
        self.property_expressions = property_expressions

        self._accept_fn_for_visitor_cls[OWLAxiomVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLAxiomVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.HAS_KEY
