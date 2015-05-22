from .exceptions import OWLRuntimeException
from .axiomtype import AxiomType
from .owlindividualrelationshipaxiom import OWLIndividualRelationshipAxiom
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLObjectPropertyAssertionAxiom(OWLIndividualRelationshipAxiom):
    """TODO: implement"""

    def __init__(self, subject, property, object, annotations):
        """
        :param subject: an owlapy.model.OWLIndividual object
        :param property: an owlapy.model.OWLObjectPropertyExpression object
        :param object: an owlapy.model.OWLIndividual object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(subject, property, object, annotations)

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.OBJECT_PROPERTY_ASSERTION

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
