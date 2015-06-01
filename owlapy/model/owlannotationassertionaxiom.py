from .axiomtype import AxiomType
from .owlaxiom import OWLAxiom
from .owlaxiomvisitor import OWLAxiomVisitor, OWLAxiomVisitorEx
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


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

        self._accept_fn_for_visitor_cls[OWLAxiomVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLAxiomVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.ANNOTATION_ASSERTION
