from .owlannotationaxiomvisitor import OWLAnnotationAxiomVisitor
from .owlannotationobjectvisitor import OWLAnnotationObjectVisitor
from .owlannotationvaluevisitor import OWLAnnotationValueVisitor
from .owlaxiomvisitor import OWLAxiomVisitor
from .owlclassexpressionvisitor import OWLClassExpressionVisitor
from .owldatavisitor import OWLDataVisitor
from .owlentityvisitor import OWLEntityVisitor
from .owlindividualvisitor import OWLIndividualVisitor
from .owlnamedobjectvisitor import OWLNamedObjectVisitor
from .owlpropertyexpressionvisitor import OWLPropertyExpressionVisitor
from .owlvisitor import OWLVisitor
from .swrlobjectvisitor import SWRLObjectVisitor


class OWLObjectVisitor(OWLVisitor, OWLAxiomVisitor, OWLClassExpressionVisitor,
                       OWLDataVisitor, OWLPropertyExpressionVisitor,
                       OWLEntityVisitor, OWLNamedObjectVisitor,
                       OWLAnnotationAxiomVisitor, OWLIndividualVisitor,
                       OWLAnnotationValueVisitor, OWLAnnotationObjectVisitor,
                       SWRLObjectVisitor):
    """Marker class"""