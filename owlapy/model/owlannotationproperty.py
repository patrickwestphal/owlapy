from .exceptions import OWLRuntimeException
from .owlentity import OWLEntity
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLAnnotationProperty(OWLEntity):
    """TODO: implement"""

    def __init__(self, iri):
        """
        :param iri: an owlapy.model.IRI object
        """
        super().__init__()
        self.iri = iri

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')

    def compare_object_of_same_type(self, other):
        """
        :param other: an owlapy.model.OWLObject object
        :return: integer indicating the difference between self and other
        """
        return self.iri.compare_to(other.iri)
