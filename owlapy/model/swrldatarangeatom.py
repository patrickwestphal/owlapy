from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from .swrlunaryatom import SWRLUnaryAtom
from .swrlobjectvisitor import SWRLObjectVisitor, SWRLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


class SWRLDataRangeAtom(SWRLUnaryAtom):
    """TODO: implement"""

    def __init__(self, predicate, arg):
        """
        :param predicate: an owapy.model.OWLDataRange object
        :param arg: an owlapy.model.SWRLDArgument object
        """
        super().__init__(predicate, arg)

        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[SWRLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[SWRLObjectVisitorEx] = accept_default_ex
