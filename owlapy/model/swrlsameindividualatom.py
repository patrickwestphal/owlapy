from owlapy.vocab.owlrdfvocabulary import OWLRDFVocabulary
from .swrlbinaryatom import SWRLBinaryAtom


class SWRLSameIndividualAtom(SWRLBinaryAtom):
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
