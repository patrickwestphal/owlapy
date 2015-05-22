from enum import Enum

from .namespaces import Namespaces
from owlapy.model import IRI
from owlapy.util.decorators import ClassProperty


class OWLFacet(Enum):
    LENGTH = (Namespaces.XSD, 'length', 'length')
    MIN_LENGTH = (Namespaces.XSD, 'minLength', 'minLength')
    MAX_LENGTH = (Namespaces.XSD, 'maxLength', 'maxLength')
    PATTERN = (Namespaces.XSD, 'pattern', 'pattern')
    MIN_INCLUSIVE = (Namespaces.XSD, 'minInclusive', '>=')
    MIN_EXCLUSIVE = (Namespaces.XSD, 'minExclusive', '>')
    MAX_INCLUSIVE = (Namespaces.XSD, 'maxInclusive', '<=')
    MAX_EXCLUSIVE = (Namespaces.XSD, 'maxExclusive', '<')
    TOTAL_DIGITS = (Namespaces.XSD, 'totalDigits', 'totalDigits')
    FRACTION_DIGITS = (Namespaces.XSD, 'fractionDigits', 'fractionDigits')
    LANG_RANGE = (Namespaces.RDF, 'langRange', 'langRange')

    def __init__(self, ns, short_form, symbolic_form):
        """
        :param ns: an owlapy.vocab.namespaces.Namespaces object
        :param short_form: a string containing the short form
        :param symbolic_form: a string containing the symbolic form
        :return:
        """
        self.iri = IRI(str(ns), short_form)
        self.short_form = short_form
        self.symbolic_form = symbolic_form
        self.prefixed_name = ns.prefix_name + ':' + short_form

    @ClassProperty
    @classmethod
    def FACET_IRIS(cls):
        if not hasattr(cls, '_FACET_IRIS'):
            cls._FACET_IRIS = set()
            for facet in cls:
                cls._FACET_IRIS.add(facet.iri)

        return cls._FACET_IRIS

    @classmethod
    def get_facet(cls, iri):
        """
        :param iri: an owlapy.model.IRI object
        """
        for vocabulary in cls:
            if vocabulary.iri == iri:
                return vocabulary

    @classmethod
    def get_facet_by_short_name(cls, short_form):
        """
        :param short_form: a string containing the short name
        """
        for vocabulary in cls:
            if vocabulary.short_form == short_form:
                return vocabulary

    @classmethod
    def get_facet_by_symbolic_name(cls, symbolic_form):
        for vocabulary in cls:
            if vocabulary.symbolic_form == symbolic_form:
                return vocabulary

    @classmethod
    def get_facets(cls):
        """
        :return: a set of strings containing the symbolic form if the defined
            facets
        """
        result = set()
        for facet in cls:
            result.add(facet.symbolic_form)

        return result