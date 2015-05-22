from .exceptions import OWLRuntimeException
from .axiomtype import AxiomType
from .owlaxiom import OWLAxiom
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLDeclarationAxiom(OWLAxiom):
    """TODO: implement"""

    def __init__(self, entity, annotations):
        """
        :param entity: an owlapy.model.OWLEntity object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(annotations)
        self.entity = entity

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.DECLARATION

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
