from .exceptions import OWLRuntimeException
from .axiomtype import AxiomType
from .owlaxiom import OWLAxiom
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLAnnotationAssertionAxiom(OWLAxiom):
    """TODO: implement"""

    def __init__(self, subject, property, value, annotations):
        """
        :param subject: an owlapy.model.OWLAnnotationSubject object (i.e. an
            owlapy.model.IRI or owlapy.model.OWLAnonymousIndividual object)
        :param property: an owlapy.model.OWLAnnotationProperty object
        :param value: an owlapy.model.OWLAnnotationValue object (i.e. an
            owlapy.model.IRI, owlapy.model.OWLAnonymousIndividual or
            owlapy.model.OWLLiteral object)
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(annotations)
        self.subject = subject
        self.property = property
        self.value = value

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.ANNOTATION_ASSERTION

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
