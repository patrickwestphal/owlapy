from .owlannotationobjectvisitor import OWLAnnotationObjectVisitor,\
    OWLAnnotationObjectVisitorEx
from .owlannotationvaluevisitor import OWLAnnotationValueVisitor
from .owlaxiomvisitor import OWLAxiomVisitor, OWLAxiomVisitorEx
from .owlclassexpressionvisitor import OWLClassExpressionVisitor,\
    OWLClassExpressionVisitorEx
from .owldatavisitor import OWLDataVisitor, OWLDataVisitorEx
from .owlentityvisitor import OWLEntityVisitor, OWLEntityVisitorEx
from .owlindividualvisitor import OWLIndividualVisitor, OWLIndividualVisitorEx
from .owlnamedobjectvisitor import OWLNamedObjectVisitor,\
    OWLNamedObjectVisitorEx
from .owlpropertyexpressionvisitor import OWLPropertyExpressionVisitor,\
    OWLPropertyExpressionVisitorEx
from .swrlobjectvisitor import SWRLObjectVisitor, SWRLObjectVisitorEx


class OWLObjectVisitor(OWLAxiomVisitor, OWLClassExpressionVisitor,
                       OWLDataVisitor, OWLPropertyExpressionVisitor,
                       OWLEntityVisitor, OWLNamedObjectVisitor,
                       OWLIndividualVisitor, OWLAnnotationValueVisitor,
                       OWLAnnotationObjectVisitor, SWRLObjectVisitor):
    """Marker class"""


class OWLObjectVisitorEx(OWLAxiomVisitorEx, OWLClassExpressionVisitorEx,
                         OWLDataVisitorEx, OWLPropertyExpressionVisitorEx,
                         OWLEntityVisitorEx, OWLAnnotationObjectVisitorEx,
                         SWRLObjectVisitorEx, OWLNamedObjectVisitorEx,
                         OWLIndividualVisitorEx):
    """Marker class"""
