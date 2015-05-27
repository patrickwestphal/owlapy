from functools import total_ordering
from .exceptions import OWLRuntimeException
from .owlobjectpropertyexpression import OWLObjectPropertyExpression


@total_ordering
class OWLObjectProperty(OWLObjectPropertyExpression):
    """TODO: implement"""

    def __init__(self, iri):
        """
        :param iri: an owlapy.model.IRI object
        """
        super().__init__()
        self.iri = iri

    def __eq__(self, other):
        if super().__eq__(other):
            if not isinstance(other, OWLObjectProperty):
                return False

            return other.iri == self.iri

        return False

    def __ge__(self, other):
        return self.compare_to(other)

    def __hash__(self):
        return super().__hash__()

    def compare_object_of_same_type(self, other):
        return self.iri.compare_to(other.iri)
