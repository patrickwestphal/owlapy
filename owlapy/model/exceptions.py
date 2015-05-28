class OWLRuntimeException(Exception):
    pass


class NoneValueException(Exception):
    """Should be the equivalent of the NullPointerException in Java"""


class IllegalArgumentException(Exception):
    pass


class IRIException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
