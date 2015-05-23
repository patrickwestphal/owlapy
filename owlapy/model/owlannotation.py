from functools import total_ordering

from .exceptions import OWLRuntimeException
from .owlobject import OWLObject
from .owlvisitor import OWLVisitorEx, OWLVisitor


@total_ordering
class OWLAnnotation(OWLObject):
    """TODO: implement"""

    def __init__(self, property, value, annotations):
        """
        :param property: an owlapy.model.OWLAnnotationProperty object
        :param value: an owlapy.model.OWLAnnotationValue object (i.e. either
            an owlapy.model.IRI, an owlapy.model.OWLAnonymousIndividual or
            an owlapy.model.OWLLiteral value)
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__()
        self.property = property
        self.value = value
        self.annotations = annotations

    def __eq__(self, other):
        if super().__eq__(other) and isinstance(other, OWLAnnotation):
            return other.property == self.property and \
                   other.value == self.value and \
                   other.annotations == self.annotations

        return False

    def __ge__(self, other):
        return self.compare_to(other) > 0

    def compare_object_of_same_type(self, other):
        """
        :param other: an owlapy.model.OWLObject object
        :return: an integer indicating the difference between self and other
        """
        diff = self.property.compare_to(other.property)
        if diff != 0:
            return diff
        else:
            # OWLAnonymousIndividual, OWLLiteral
            return self.value.compare_to(other.value)

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
