from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from .swrlobjectvisitor import SWRLObjectVisitor, SWRLObjectVisitorEx
from .swrlunaryatom import SWRLUnaryAtom
from owlapy.util import accept_default, accept_default_ex


class SWRLClassAtom(SWRLUnaryAtom):
    """TODO: implement"""

    def __init__(self, predicate, arg):
        """
        :param predicate: an owlapy.model.OWLClassExpression object
        :param arg: an owlapy.model.SWRLIArgument object
        """
        super().__init__(predicate, arg)

        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[SWRLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[SWRLObjectVisitorEx] = accept_default_ex
