from .owldatarangevisitor import OWLDataRangeVisitor, OWLDataRangeVisitorEx
from .owldatavisitor import OWLDataVisitor, OWLDataVisitorEx
from .owlobject import OWLObject
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


class OWLDataOneOf(OWLObject):
    """TODO: implement"""

    def __init__(self, values):
        """
        :param values: a set of owlapy.model.OWLLiteral objects
        """
        super().__init__()
        self.values = values

        self._accept_fn_for_visitor_cls[OWLDataRangeVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLDataRangeVisitorEx] = \
            accept_default_ex
        self._accept_fn_for_visitor_cls[OWLDataVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLDataVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex
