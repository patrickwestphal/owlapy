from functools import total_ordering
from .hasiri import HasIRI


@total_ordering
class OWLImportsDeclaration(HasIRI):

    def __init__(self, iri):
        self.iri = iri

    def __ge__(self, other):
        return self.compare_to(other) >= 0

    def __eq__(self, other):
        if hash(self) == hash(other):
            return True

        if not isinstance(other, OWLImportsDeclaration):
            return False

        return self.iri == other.iri

    def __hash__(self):
        return self.iri.__hash__()

    def __str__(self):
        return 'Import(%s)' % self.iri.to_quoted_string()

    def __repr__(self):
        return str(self)

    def get_uri(self):
        return self.iri.to_uri()

    def compare_to(self, other):
        """
        :param other: an owlapy.model.OWLImportsDeclaration object
        :return:
        """
        return self.iri.compare_to(other.iri)
