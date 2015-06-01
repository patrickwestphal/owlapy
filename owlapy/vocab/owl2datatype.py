import re
from enum import Enum

from owlapy.model import IllegalArgumentException
from owlapy.model import OWLRuntimeException
from owlapy.model import IRI
from owlapy.util.decorators import ClassProperty
from owlapy.vocab.owlfacet import OWLFacet
from owlapy.vocab.namespaces import Namespaces
from owlapy.vocab.xsdvocabulary import XSDVocabulary


class Category(Enum):
    CAT_NUMBER = (
        'Number', OWLFacet.MIN_INCLUSIVE, OWLFacet.MAX_INCLUSIVE,
        OWLFacet.MIN_EXCLUSIVE, OWLFacet.MAX_EXCLUSIVE)
    CAT_STRING_WITH_LANGUAGE_TAG = (
        'String with a language tag', OWLFacet.MIN_LENGTH, OWLFacet.MAX_LENGTH,
        OWLFacet.LENGTH, OWLFacet.PATTERN, OWLFacet.LANG_RANGE)
    CAT_STRING_WITHOUT_LANGUAGE_TAG = (
        'String without a language tag', OWLFacet.MIN_LENGTH,
        OWLFacet.MAX_LENGTH, OWLFacet.LENGTH, OWLFacet.PATTERN)
    CAT_BINARY = (
        'Binary data', OWLFacet.MIN_LENGTH, OWLFacet.MAX_LENGTH,
        OWLFacet.LENGTH)
    CAT_URI = (
        'URI', OWLFacet.MIN_LENGTH, OWLFacet.MAX_LENGTH, OWLFacet.PATTERN)
    CAT_TIME = ('Time instant', OWLFacet.MIN_INCLUSIVE, OWLFacet.MAX_INCLUSIVE,
                OWLFacet.MIN_EXCLUSIVE, OWLFacet.MAX_EXCLUSIVE)
    CAT_BOOLEAN = 'Boolean value'
    CAT_UNIVERSAL = 'Universal literal'

    def __init__(self, name, *facets):
        """
        :param name: a string containing the name of the category
        :param facets: owlapy.vocab.OWLFacet objects
        """
        self.name_ = name
        self.facets = set()

        for facet in facets:
            self.facets.add(facet)


class WhiteSpaceNormalisation(Enum):
    PRESERVE = 0
    REPLACE = 1
    COLLAPSE = 2

    # TODO: implement get_normalised_string method


class OWL2Datatype(Enum):
    """An optimised implementation of OWLDatatype for OWL2Datatypes."""

    RDF_XML_LITERAL = (  # 01
        Namespaces.RDF, Category.CAT_STRING_WITHOUT_LANGUAGE_TAG, False, '.*',
        'XMLLiteral')
    RDFS_LITERAL = (  # 02
        Namespaces.RDFS, Category.CAT_UNIVERSAL, False, '.*', 'Literal')
    RDF_PLAIN_LITERAL = (  # 03
        Namespaces.RDF, Category.CAT_STRING_WITHOUT_LANGUAGE_TAG, False, '.*',
        'PlainLiteral')
    OWL_REAL = (Namespaces.OWL, Category.CAT_NUMBER, False, '.*', 'real')  # 04
    OWL_RATIONAL = (  # 05
        Namespaces.OWL, Category.CAT_NUMBER, False,
        # regex altered since e.g. '2' failed (made '/...' part optional)
        '\\A(\\+|-)?([0-9]+)(\\s)*((/)(\\s)*([0-9]+))?\\Z', 'rational')
    XSD_STRING = (  # 06
        XSDVocabulary.STRING, Category.CAT_STRING_WITHOUT_LANGUAGE_TAG, False,
        '.*')
    XSD_NORMALIZED_STRING = (  # 07
        XSDVocabulary.NORMALIZED_STRING,
        Category.CAT_STRING_WITHOUT_LANGUAGE_TAG, False,
        '\\A([^\\r\\n\\t])*\\Z')
    XSD_TOKEN = (  # 08
        XSDVocabulary.TOKEN, Category.CAT_STRING_WITHOUT_LANGUAGE_TAG, False,
        '\\A([^\\s])(\\s([^\\s])|([^\\s]))*\\Z')
    XSD_LANGUAGE = (  # 09
        XSDVocabulary.LANGUAGE, Category.CAT_STRING_WITHOUT_LANGUAGE_TAG, True,
        '\\A[a-zA-Z]{1,8}(-[a-zA-Z0-9]{1,8})*\\Z')
    XSD_NAME = (  # 10
        XSDVocabulary.NAME, Category.CAT_STRING_WITHOUT_LANGUAGE_TAG, False,
        '\\A:|[A-Z]|_|[a-z]|[\\u00C0-\\u00D6]|[\\u00D8-\\u00F6]|'
        '[\\u00F8-\\u02FF]|[\\u0370-\\u037D]|[\\u037F-\\u1FFF]|'
        '[\\u200C-\\u200D]|[\\u2070-\\u218F]|[\\u2C00-\\u2FEF]|'
        '[\\u3001-\\uD7FF]|[\\uF900-\\uFDCF]|[\\uFDF0-\\uFFFD]'
        '(:|[A-Z]|_|[a-z]|[\\u00C0-\\u00D6]|[\\u00D8-\\u00F6]|'
        '[\\u00F8-\\u02FF]|[\\u0370-\\u037D]|[\\u037F-\\u1FFF]|'
        '[\\u200C-\\u200D]|[\\u2070-\\u218F]|[\\u2C00-\\u2FEF]|'
        '[\\u3001-\\uD7FF]|[\\uF900-\\uFDCF]|[\\uFDF0-\\uFFFD]|'
        '\"-\"|\".\"|[0-9]|\\u00B7|[\\u0300-\\u036F]|[\\u203F-\\u2040])*\\Z')
    XSD_NCNAME = (  # 11
        XSDVocabulary.NCNAME, Category.CAT_STRING_WITHOUT_LANGUAGE_TAG, False,
        '\\A([A-Z]|_|[a-z]|[\\u00C0-\\u00D6]|[\\u00D8-\\u00F6]|'
        '[\\u00F8-\\u02FF]|[\\u0370-\\u037D]|[\\u037F-\\u1FFF]|'
        '[\\u200C-\\u200D]|[\\u2070-\\u218F]|[\\u2C00-\\u2FEF]|'
        '[\\u3001-\\uD7FF]|[\\uF900-\\uFDCF]|[\\uFDF0-\\uFFFD])'
        # added '|\.|-'
        '([A-Z]|_|\\.|-|[a-z]|[\\u00C0-\\u00D6]|[\\u00D8-\\u00F6]|'
        '[\\u00F8-\\u02FF]|[\\u0370-\\u037D]|[\\u037F-\\u1FFF]|'
        '[\\u200C-\\u200D]|[\\u2070-\\u218F]|[\\u2C00-\\u2FEF]|'
        '[\\u3001-\\uD7FF]|[\\uF900-\\uFDCF]|[\\uFDF0-\\uFFFD]|'
        '\"-\"|\".\"|[0-9]|\\u00B7|[\\u0300-\\u036F]|[\\u203F-\\u2040])*\\Z')
    XSD_NMTOKEN = (  # 12
        XSDVocabulary.NMTOKEN, Category.CAT_STRING_WITHOUT_LANGUAGE_TAG, False,
        '.*')
    XSD_DECIMAL = (  # 13
        XSDVocabulary.DECIMAL, Category.CAT_NUMBER, False,
        '\\A(\\+|-)?([0-9]+(\\.[0-9]*)?|\\.[0-9]+)\\Z')
    XSD_INTEGER = (  # 14
        XSDVocabulary.INTEGER, Category.CAT_NUMBER,  False,
        '\\A(\\+|-)?([0-9]+)\\Z')
    XSD_NON_NEGATIVE_INTEGER = (  # 15
        XSDVocabulary.NON_NEGATIVE_INTEGER, Category.CAT_NUMBER, False,
        '\\A(((\\+)?([0-9]+))|-(0+))\\Z')
    XSD_NON_POSITIVE_INTEGER = (  # 16
        XSDVocabulary.NON_POSITIVE_INTEGER, Category.CAT_NUMBER, False,
        # wrapped \\+ in (...)?
        '\\A(-([0-9]+)|((\\+)?(0+)))\\Z')
    XSD_POSITIVE_INTEGER = (  # 17
        XSDVocabulary.POSITIVE_INTEGER, Category.CAT_NUMBER, False,
        #                     | leading zeros (with at least 1 non-zero number)
        '\\A(\\+)?([1-9][0-9]*|0+[1-9]+[0-9]*)\\Z')
    XSD_NEGATIVE_INTEGER = (  # 18
        XSDVocabulary.NEGATIVE_INTEGER, Category.CAT_NUMBER, False,
        '\\A-([0-9]+)\\Z')
    XSD_LONG = (  # 19
        XSDVocabulary.LONG, Category.CAT_NUMBER, True, '\\A(\\+|-)?([0-9]+)\\Z')
    XSD_INT = (  # 20
        XSDVocabulary.INT, Category.CAT_NUMBER, True, '\\A(\\+|-)?([0-9]+)\\Z')
    XSD_SHORT = (  # 21
        XSDVocabulary.SHORT, Category.CAT_NUMBER, True,
        '\\A(\\+|-)?([0-9]+)\\Z')
    XSD_BYTE = (  # 22
        XSDVocabulary.BYTE, Category.CAT_NUMBER, True, '\\A(\\+|-)?([0-9]+)\\Z')
    XSD_UNSIGNED_LONG = (  # 23
        XSDVocabulary.UNSIGNED_LONG, Category.CAT_NUMBER, True,
        '\\A(\\+)?([0-9]+)\\Z')
    XSD_UNSIGNED_INT = (  # 24
        XSDVocabulary.UNSIGNED_INT, Category.CAT_NUMBER, True,
        '\\A(\\+)?([0-9]+)\\Z')
    XSD_UNSIGNED_SHORT = (  # 25
        XSDVocabulary.UNSIGNED_SHORT, Category.CAT_NUMBER, True,
        '\\A(\\+)?([0-9]+)\\Z')
    XSD_UNSIGNED_BYTE = (  # 26
        XSDVocabulary.UNSIGNED_BYTE, Category.CAT_NUMBER, True,
        '\\A(\\+)?([0-9]+)\\Z')
    XSD_DOUBLE = (  # 27
        XSDVocabulary.DOUBLE, Category.CAT_NUMBER, True,
        '\\A(\\+|-)?(([0-9]+(\\.[0-9]*)?|\\.[0-9]+)(([Ee])((\\+|-)?([0-9]+)))?|'
        '((\\+|-)?INF|NaN))\\Z')
    XSD_FLOAT = (  # 28
        XSDVocabulary.FLOAT, Category.CAT_NUMBER, True,
        '\\A(\\+|-)?((([0-9]+)(\\.[0-9]*)?|(\\.[0-9]+))(([Ee])(\\+|-)?'
        '([0-9]+))?|(\\+|-)?INF|NaN)\\Z')
    XSD_BOOLEAN = (  # 29
        XSDVocabulary.BOOLEAN, Category.CAT_BOOLEAN, True,
        '\\A(true|false|1|0)\\Z')
    XSD_HEX_BINARY = (  # 30
        XSDVocabulary.HEX_BINARY, Category.CAT_BINARY, False,
        '\\A([0-9a-fA-F]{2})*\\Z')
    XSD_BASE_64_BINARY = (  # 31
        XSDVocabulary.BASE_64_BINARY, Category.CAT_BINARY, False,
        '\\A((([A-Za-z0-9+/] ?){4})*(([A-Za-z0-9+/] ?){3}([A-Za-z0-9+/])|'
        '(([A-Za-z0-9+/] ?){2}([AEIMQUYcgkosw048]) ?=)|([A-Za-z0-9+/] ?[AQgw] '
        '?= ?=)))?\\Z')
    XSD_ANY_URI = (XSDVocabulary.ANY_URI, Category.CAT_URI, False, '.*')  # 32
    XSD_DATE_TIME = (  # 33
        XSDVocabulary.DATE_TIME, Category.CAT_TIME, False,
        '-?([1-9][0-9]{3,}|0[0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T'
        '(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\\.[0-9]+)?|'
        '(24:00:00(\\.0+)?))(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))?')
    XSD_DATE_TIME_STAMP = (  # 34
        XSDVocabulary.DATE_TIME_STAMP, Category.CAT_TIME, False,
        '-?([1-9][0-9]{3,}|0[0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T'
        '(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\\\\.[0-9]+)?|'
        '(24:00:00(\\\\.0+)?))(Z|(\\\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))')

    def __init__(self, namespace_or_vocab, category, finite, regex,
                 short_form=None):
        """
        :param namespace_or_vocab: an owapy.vocab.Namespaces object
        :param short_form: a string containing the datatype's short form. Short
            forms are the local name e.g. "string" for XSD_STRING etc.
        :param category: a category from the Category enum above
        :param finite: Boolean that determines whether or not this datatype is
            finite.
        :param regex: the pattern string that specifies the regular expression
            for the allowed lexical values of a datatype.
        """
        if isinstance(namespace_or_vocab, Namespaces):
            self.iri = IRI.create(str(namespace_or_vocab), short_form)
            self.prefixed_name = namespace_or_vocab.prefix_name + ':' + \
                short_form
            self.short_form = short_form

        elif isinstance(namespace_or_vocab, XSDVocabulary):
            self.iri = namespace_or_vocab.iri
            self.prefixed_name = namespace_or_vocab.prefixed_name
            self.short_form = namespace_or_vocab.short_form

        else:
            raise IllegalArgumentException('first argument must be either a '
                                           'Namespaces or XSDVocabulary object')

        self.category = category
        self.finite = finite
        self.pattern_string = regex

        # pattern: the pattern that specifies the regular expression for the
        # allowed lexical values of a datatype.
        if regex:
            self.pattern = re.compile(regex)
        else:
            self.pattern = None

    @ClassProperty
    @classmethod
    def ALL_IRIS(cls):
        return {dtype.iri for dtype in cls}

    @classmethod
    def get_datatype_iris(cls):
        return cls.ALL_IRIS

    @classmethod
    def is_built_in(cls, datatype_iri):
        """Determines if the specified IRI identifies a built in datatype.

        :param datatype_iri: an owlapy.model.IRI object
        :return: True if the IRI identifies a built in datatype, and False if
            the IRI does not identify a built in datatype.
        """
        return datatype_iri in cls.ALL_IRIS

    @classmethod
    def get_datatype(cls, datatype):
        """Given an IRI that identifies an owlapy.model.OWLDatatype, this
        method obtains the corresponding OWL2Datatype

        :param datatype: The datatype's owlapy.model.IRI object or an
            owlapy.model.OWL2Datatype object
        :return: The OWL2Datatype that has the specified IRI
        """
        if isinstance(datatype, OWL2Datatype):
            datatype = datatype.iri

        if not cls.is_built_in(datatype):
            raise OWLRuntimeException('%s is not a built in datatype!' %
                                      str(datatype))

        for owl2dtype in cls:
            if owl2dtype.iri == datatype:
                return owl2dtype

        raise OWLRuntimeException('%s is not a built in datatype!' %
                                  str(datatype))

    def is_numeric(self):
        """Determines if this datatype is a numeric datatype.

        :return: True if this datatype is a numeric datatype
        """
        return self.category == Category.CAT_NUMBER

    def get_facets(self):
        """Gets the facets that are allowed for facet restrictions of this
        datatype.

        :return: The allowed facets
        """
        return self.category.facets

    def get_dtype(self, data_factory):
        """Gets the equivalent OWLDatatype from the given factory

        :param data_factory: an owlapy.model.OWLDataFactory
        :return: An owlapy.model.OWLDatatype that has the same IRI as this
            OWL2Datatype
        """
        from owlapy.model import OWLDatatype
        if isinstance(data_factory, OWLDatatype):
            return self.get_datatype(data_factory)

        return data_factory.get_owl_datatype(self.iri)

    def is_in_lexical_space(self, string):
        """Determines if the specified input string is in the lexical space of
        this datatype.

        :param string: The string to test
        :return: True if the string is in the lexical space, otherwise False
        """
        return self.pattern.match(string) is not None
