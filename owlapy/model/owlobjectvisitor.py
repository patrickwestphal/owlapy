from .owlannotationobjectvisitor import OWLAnnotationObjectVisitor
from .owlannotationvaluevisitor import OWLAnnotationValueVisitor
from .owlaxiomvisitor import OWLAxiomVisitor
from .owlclassexpressionvisitor import OWLClassExpressionVisitor
from .owldatavisitor import OWLDataVisitor
from .owlentityvisitor import OWLEntityVisitor
from .owlindividualvisitor import OWLIndividualVisitor
from .owlnamedobjectvisitor import OWLNamedObjectVisitor
from .owlpropertyexpressionvisitor import OWLPropertyExpressionVisitor
from .swrlobjectvisitor import SWRLObjectVisitor


class OWLObjectVisitor(OWLAxiomVisitor, OWLClassExpressionVisitor,
                       OWLDataVisitor, OWLPropertyExpressionVisitor,
                       OWLEntityVisitor, OWLNamedObjectVisitor,
                       OWLIndividualVisitor, OWLAnnotationValueVisitor,
                       OWLAnnotationObjectVisitor, SWRLObjectVisitor):
    """Marker class"""