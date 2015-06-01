from .axiomtype import AxiomType
from .owlaxiomvisitor import OWLAxiomVisitor, OWLAxiomVisitorEx
from .owlindividualrelationshipaxiom import OWLIndividualRelationshipAxiom
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


class OWLNegativeDataPropertyAssertionAxiom(OWLIndividualRelationshipAxiom):
    """TODO: implement"""

    def __init__(self, subject, property, object, annotations):
        """
        :param subject: an owlapy.model.OWLIndividual object
        :param property: an owlapy.model.OWLDataPropertyExpression object
        :param object: an owlapy.model.OWLLiteral object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(subject, property, object, annotations)

        self._accept_fn_for_visitor_cls[OWLAxiomVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLAxiomVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.NEGATIVE_DATA_PROPERTY_ASSERTION
