from .axiomtype import AxiomType
from .owllogicalaxiom import OWLLogicalAxiom


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

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.HAS_KEY
