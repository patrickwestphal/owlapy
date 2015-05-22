from .exceptions import OWLRuntimeException
from .owlobject import OWLObject
from .exceptions import OWLRuntimeException
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLLiteral(OWLObject):
    """TODO: implement
    TODO: add literal wrapper
    """
    RDF_PLAIN_LITERAL = 23  # FIXME: just a dummy value

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

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
