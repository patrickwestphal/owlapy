from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from .swrlbinaryatom import SWRLBinaryAtom
from .swrlobjectvisitor import SWRLObjectVisitor, SWRLObjectVisitorEx
from owlapy.util import accept_default_ex, accept_default
from owlapy.vocab.owlrdfvocabulary import OWLRDFVocabulary


class SWRLDifferentIndividualsAtom(SWRLBinaryAtom):
    """TODO: implement"""

    def __init__(self, data_factory, arg0, arg1):
        """
        :param data_factory: an owlapy.model.OWLDataFactory object
        :param arg0: an owlapy.model.SWRLIArgument object
        :param arg1: an owlapy.model.SWRLIArgument object
        """
        super().__init__(
            data_factory.get_owl_object_property(
                OWLRDFVocabulary.OWL_DIFFERENT_FROM.iri),
            arg0, arg1)

        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[SWRLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[SWRLObjectVisitorEx] = accept_default_ex
