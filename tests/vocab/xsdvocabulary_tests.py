import unittest

from owlapy.model import NoneValueException, IllegalArgumentException
from owlapy.vocab.xsdvocabulary import XSDVocabulary


class TestXSDVocabulary(unittest.TestCase):

    def test___init__(self):
        self.assertEqual('anyType', XSDVocabulary.ANY_TYPE.short_form)
        self.assertEqual('xsd:anyType', XSDVocabulary.ANY_TYPE.prefixed_name)
        self.assertEqual('http://www.w3.org/2001/XMLSchema#anyType',
                         str(XSDVocabulary.ANY_TYPE.iri))

        self.assertEqual('anySimpleType',
                         XSDVocabulary.ANY_SIMPLE_TYPE.short_form)
        self.assertEqual('string', XSDVocabulary.STRING.short_form)
        self.assertEqual('integer', XSDVocabulary.INTEGER.short_form)
        self.assertEqual('long', XSDVocabulary.LONG.short_form)
        self.assertEqual('int', XSDVocabulary.INT.short_form)
        self.assertEqual('short', XSDVocabulary.SHORT.short_form)
        self.assertEqual('byte', XSDVocabulary.BYTE.short_form)
        self.assertEqual('decimal', XSDVocabulary.DECIMAL.short_form)
        self.assertEqual('float', XSDVocabulary.FLOAT.short_form)
        self.assertEqual('boolean', XSDVocabulary.BOOLEAN.short_form)
        self.assertEqual('double', XSDVocabulary.DOUBLE.short_form)
        self.assertEqual('nonPositiveInteger',
                         XSDVocabulary.NON_POSITIVE_INTEGER.short_form)
        self.assertEqual('negativeInteger',
                         XSDVocabulary.NEGATIVE_INTEGER.short_form)
        self.assertEqual('nonNegativeInteger',
                         XSDVocabulary.NON_NEGATIVE_INTEGER.short_form)
        self.assertEqual('unsignedLong', XSDVocabulary.UNSIGNED_LONG.short_form)
        self.assertEqual('unsignedInt', XSDVocabulary.UNSIGNED_INT.short_form)
        self.assertEqual('positiveInteger',
                         XSDVocabulary.POSITIVE_INTEGER.short_form)
        self.assertEqual('base64Binary',
                         XSDVocabulary.BASE_64_BINARY.short_form)
        self.assertEqual('normalizedString',
                         XSDVocabulary.NORMALIZED_STRING.short_form)
        self.assertEqual('hexBinary', XSDVocabulary.HEX_BINARY.short_form)
        self.assertEqual('anyURI', XSDVocabulary.ANY_URI.short_form)
        self.assertEqual('QName', XSDVocabulary.Q_NAME.short_form)
        self.assertEqual('NOTATION', XSDVocabulary.NOTATION.short_form)
        self.assertEqual('token', XSDVocabulary.TOKEN.short_form)
        self.assertEqual('language', XSDVocabulary.LANGUAGE.short_form)
        self.assertEqual('Name', XSDVocabulary.NAME.short_form)
        self.assertEqual('NCName', XSDVocabulary.NCNAME.short_form)
        self.assertEqual('NMTOKEN', XSDVocabulary.NMTOKEN.short_form)
        self.assertEqual('ID', XSDVocabulary.ID.short_form)
        self.assertEqual('IDREF', XSDVocabulary.IDREF.short_form)
        self.assertEqual('IDREFS', XSDVocabulary.IDREFS.short_form)
        self.assertEqual('ENTITY', XSDVocabulary.ENTITY.short_form)
        self.assertEqual('ENTITIES', XSDVocabulary.ENTITIES.short_form)
        self.assertEqual('duration', XSDVocabulary.DURATION.short_form)
        self.assertEqual('dateTime', XSDVocabulary.DATE_TIME.short_form)
        self.assertEqual('dateTimeStamp',
                         XSDVocabulary.DATE_TIME_STAMP.short_form)
        self.assertEqual('time', XSDVocabulary.TIME.short_form)
        self.assertEqual('date', XSDVocabulary.DATE.short_form)
        self.assertEqual('gYearMonth', XSDVocabulary.G_YEAR_MONTH.short_form)
        self.assertEqual('gYear', XSDVocabulary.G_YEAR.short_form)
        self.assertEqual('gMonthYear', XSDVocabulary.G_MONTH_DAY.short_form)
        self.assertEqual('gDay', XSDVocabulary.G_DAY.short_form)
        self.assertEqual('gMonth', XSDVocabulary.G_MONTH.short_form)
        self.assertEqual('unsignedShort',
                         XSDVocabulary.UNSIGNED_SHORT.short_form)
        self.assertEqual('unsignedByte', XSDVocabulary.UNSIGNED_BYTE.short_form)

    def test_parse_short_name_01(self):
        self.assertRaises(NoneValueException, XSDVocabulary.parse_short_name,
                          None)

    def test_parse_short_name_02(self):
        self.assertRaises(IllegalArgumentException,
                          XSDVocabulary.parse_short_name, 'date')

    def test_parse_short_name_03(self):
        self.assertEqual(XSDVocabulary.DATE,
                         XSDVocabulary.parse_short_name('xsd:date'))

    def test_parse_short_name_04(self):
        self.assertEqual(XSDVocabulary.BYTE,
                         XSDVocabulary.parse_short_name('xsd:byte'))
