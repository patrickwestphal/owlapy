from functools import total_ordering

from .owlobject import OWLObject


@total_ordering
class SWRLLiteralArgument(OWLObject):
    """TODO: implement"""

    def __init__(self, literal):
        """
        :param literal: an owlapy.model.OWLLiteral object
        """
        super().__init__()
        self.literal = literal

    def __eq__(self, other):
        if id(self) == id(other):
            return True

        if not isinstance(other, SWRLLiteralArgument):
            return False

        return other.literal == self.literal

    def __ge__(self, other):
        return self.compare_to(other) >= 0

    def __hash__(self):
        return super().__hash__()

    def compare_object_of_same_type(self, other):
        return self.literal.compare_to(other.literal)
