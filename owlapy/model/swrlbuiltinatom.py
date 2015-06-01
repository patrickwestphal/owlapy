from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from .swrlatom import SWRLAtom
from .swrlobjectvisitor import SWRLObjectVisitor, SWRLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


class SWRLBuiltInAtom(SWRLAtom):
    """TODO: implement"""

    def __init__(self, predicate, args):
        """
        :param predicate: an owlapy.model.IRI object
        :param args: a list of owlapy.model.SWRLDArgument objects
        """
        super().__init__(predicate)
        self.arguments = args

        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[SWRLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[SWRLObjectVisitorEx] = accept_default_ex
