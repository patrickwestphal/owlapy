from functools import total_ordering
from .owlanonymousclassexpression import OWLAnonymousClassExpression


@total_ordering
class OWLNaryBooleanClassExpression(OWLAnonymousClassExpression):
    """TODO: implement"""

    def __init__(self, operands):
        """
        :param operands: a set of owlapy.model.OWLClassExpression objects
        """
        super().__init__()
        self.operands = operands

    def __eq__(self, other):
        if super().__eq__(other):
            if not isinstance(other, OWLNaryBooleanClassExpression):
                return False

            return other.operands == self.operands

        return False

    def __ge__(self, other):
        return self.compare_to(other) >= 0

    def __hash__(self):
        return super().__hash__()

    def compare_object_of_same_type(self, other):
        return self.compare_sets(self.operands, other.operands)
