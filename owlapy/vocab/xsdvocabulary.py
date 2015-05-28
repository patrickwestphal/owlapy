from enum import Enum

from owlapy.model import IRI
from owlapy.model import NoneValueException, IllegalArgumentException
from owlapy.vocab.namespaces import Namespaces


class XSDVocabulary(Enum):
    ANY_TYPE = 'anyType'
    ANY_SIMPLE_TYPE = 'anySimpleType'
    STRING = 'string'
    INTEGER = 'integer'
    LONG = 'long'
    INT = 'int'
    SHORT = 'short'
    BYTE = 'byte'
    DECIMAL = 'decimal'
    FLOAT = 'float'
    BOOLEAN = 'boolean'
    DOUBLE = 'double'
    NON_POSITIVE_INTEGER = 'nonPositiveInteger'
    NEGATIVE_INTEGER = 'negativeInteger'
    NON_NEGATIVE_INTEGER = 'nonNegativeInteger'
    UNSIGNED_LONG = 'unsignedLong'
    UNSIGNED_INT = 'unsignedInt'
    POSITIVE_INTEGER = 'positiveInteger'
    BASE_64_BINARY = 'base64Binary'
    NORMALIZED_STRING = 'normalizedString'
    HEX_BINARY = 'hexBinary'
    ANY_URI = 'anyURI'
    Q_NAME = 'QName'
    NOTATION = 'NOTATION'
    TOKEN = 'token'
    LANGUAGE = 'language'
    NAME = 'Name'
    NCNAME = 'NCName'
    NMTOKEN = 'NMTOKEN'
    ID = 'ID'
    IDREF = 'IDREF'
    IDREFS = 'IDREFS'
    ENTITY = 'ENTITY'
    ENTITIES = 'ENTITIES'
    DURATION = 'duration'
    DATE_TIME = 'dateTime'
    DATE_TIME_STAMP = 'dateTimeStamp'
    TIME = 'time'
    DATE = 'date'
    G_YEAR_MONTH = 'gYearMonth'
    G_YEAR = 'gYear'
    G_MONTH_DAY = 'gMonthYear'
    G_DAY = 'gDay'
    G_MONTH = 'gMonth'
    UNSIGNED_SHORT = 'unsignedShort'
    UNSIGNED_BYTE = 'unsignedByte'

    def __init__(self, name):
        self.short_form = name
        self.prefixed_name = Namespaces.XSD.prefix_name + ':' + name
        self.iri = IRI(str(Namespaces.XSD), name)

    def __str__(self):
        return str(self.iri)

    @classmethod
    def parse_short_name(cls, s):
        """
        :param s: a string containing the short form xsd:typename
        :return: the XSDVocabulary item matching xsd:typename, e.g., STRING for
            "xsd:string"
        """
        if s is None:
            raise NoneValueException('the input string cannot be None')

        if s.startswith('xsd:'):
            name = s[4:]

            for vocab in cls:
                if vocab.short_form == name:
                    return vocab

        raise IllegalArgumentException('the input value does not match any of '
                                       'the known xsd types: ' + s)
