from functools import total_ordering

from .exceptions import OWLRuntimeException
from .owl2datatype import OWL2Datatype
from .owldatavisitor import OWLDataVisitor, OWLDataVisitorEx
from .owlannotationvaluevisitor import OWLAnnotationValueVisitor, \
    OWLAnnotationValueVisitorEx
from .owlobject import OWLObject
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from owlapy.util import str_compare_to, accept_default, accept_default_ex
from owlapy.vocab.owl2datatype import OWL2Datatype as OWL2DatatypeVoc


@total_ordering
class OWLLiteral(OWLObject):
    """TODO: implement
    TODO: add literal wrapper
    """
    RDF_PLAIN_LITERAL = \
        OWL2Datatype.get_datatype(OWL2DatatypeVoc.RDF_PLAIN_LITERAL)

    def __init__(self, literal, lang=None, datatype=None):
        """
        :param literal: a string containing the actual literal value
        :param lang: a string containing the literal's language tag; can be
            None or an empty string, in which case datatype can be any datatype
            but not None
        :param datatype: an owlapy.model.OWLDatatype indicating the literal's
            datatype; if lang is None or the empty string, it can be None or it
            MUST be RDFPlainLiteral
        """
        super().__init__()
        self.literal = literal
        if not lang:
            self.lang = ''

            if datatype is None:
                self.datatype = self.RDF_PLAIN_LITERAL
            else:
                self.datatype = datatype

        else:
            if datatype is not None and not datatype.is_rdf_plain_literal():
                # ERROR: attempting to build a literal with a language tag and
                # type different from plain literal
                raise OWLRuntimeException('Error: cannot build a literal with '
                                          'type: ' + datatype.iri + ' and '
                                          'language: ' + lang)

            self.lang = lang
            self.datatype = self.RDF_PLAIN_LITERAL

        self._accept_fn_for_visitor_cls[OWLAnnotationValueVisitor] = \
            accept_default
        self._accept_fn_for_visitor_cls[OWLAnnotationValueVisitorEx] = \
            accept_default_ex
        self._accept_fn_for_visitor_cls[OWLDataVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLDataVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex

    def __eq__(self, other):
        if super().__eq__(other):
            if not isinstance(other, OWLLiteral):
                return False

            return self.literal == other.literal and \
                self.datatype == other.datatype and self.lang == other.lang
        return False

    def __hash__(self):
        hash_code = 277
        hash_code = hash_code * 37 + hash(self.datatype)
        hash_code = hash_code * 37
        hash_code += hash(self.literal)
        if self.lang:
            hash_code = hash_code * 37 + hash(self.lang)

        return hash_code

    def __ge__(self, other):
        return self.compare_to(other) >= 0

    def compare_object_of_same_type(self, other):
        diff = str_compare_to(self.literal, other.literal)
        if diff:
            return diff

        diff = self.datatype.compare_to(other.datatype)
        if diff:
            return diff

        return str_compare_to(self.lang, other.lang)
