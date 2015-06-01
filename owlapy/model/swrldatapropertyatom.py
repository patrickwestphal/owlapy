from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from .swrlbinaryatom import SWRLBinaryAtom
from .swrlobjectvisitor import SWRLObjectVisitor, SWRLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


class SWRLDataPropertyAtom(SWRLBinaryAtom):
    """TODO: implement"""

    def __init__(self, predicate, arg0, arg1):
        """
        :param predicate: an owlapy.model.OWLDataPropertyExpression object
        :param arg0: an owlapy.model.SWRLIArgument object
        :param arg1: an owlapy.model.SWRLIArgument object
        """
        super().__init__(predicate, arg0, arg1)

        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[SWRLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[SWRLObjectVisitorEx] = accept_default_ex
