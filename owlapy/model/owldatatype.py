from functools import total_ordering

from .owldatarange import OWLDataRange
from .owllogicalentity import OWLLogicalEntity
from .owlnamedobject import OWLNamedObject


@total_ordering
class OWLDatatype(OWLDataRange, OWLLogicalEntity, OWLNamedObject):
    """TODO: implement"""

    def __init__(self, iri):
        """
        :param iri: an owlapy.model.IRI object
        """
        super().__init__()
        self.iri = iri

    def __eq__(self, other):
        if super().__eq__(other) and isinstance(other, OWLDatatype):
            return other.iri == self.iri

        return False

    def __ge__(self, other):
        return self.compare_to(other) >= 0

    def __hash__(self):
        return super().__hash__()

    def compare_object_of_same_type(self, other):
        return self.iri.compare_to(other.iri)
