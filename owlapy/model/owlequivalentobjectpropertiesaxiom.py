from .exceptions import OWLRuntimeException
from .axiomtype import AxiomType
from .owlnarypropertyaxiom import OWLNaryPropertyAxiom
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLEquivalentObjectPropertiesAxiom(OWLNaryPropertyAxiom):
    """TODO: implement"""

    def __init__(self, properties, annotations):
        """
        :param properties: a set of owlapy.model.OWLObjectPropertyExpression
            objects
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(properties, annotations)

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.EQUIVALENT_OBJECT_PROPERTIES

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
