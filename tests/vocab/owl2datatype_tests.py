import unittest

from owlapy.vocab.owl2datatype import OWL2Datatype
from owlapy.vocab.owl2datatype import Category
from owlapy.model import IRI
from owlapy.model import EntityType
from owlapy.model import OWLDatatype
from owlapy.model import OWLDataVisitor, OWLDataVisitorEx
from owlapy.model import OWLRuntimeException
from owlapy.model import DataRangeType


class TestOWL2Datatype(unittest.TestCase):
    def test___init__(self):
        self.assertEqual(34, len(OWL2Datatype))

        # all attributes tested in two examples
        self.assertEqual(IRI('http://www.w3.org/2002/07/owl#real'),
                         OWL2Datatype.OWL_REAL.iri)
        self.assertEqual('owl:real', OWL2Datatype.OWL_REAL.prefixed_name)
        self.assertEqual('real', OWL2Datatype.OWL_REAL.short_form)
        self.assertEqual(Category.CAT_NUMBER, OWL2Datatype.OWL_REAL.category)
        self.assertFalse(OWL2Datatype.OWL_REAL.finite)
        self.assertEqual('.*', OWL2Datatype.OWL_REAL.pattern_string)
        self.assertIsNotNone(OWL2Datatype.OWL_REAL.pattern)

        self.assertEqual(IRI('http://www.w3.org/2001/XMLSchema#double'),
                         OWL2Datatype.XSD_DOUBLE.iri)
        self.assertEqual('xsd:double', OWL2Datatype.XSD_DOUBLE.prefixed_name)
        self.assertEqual('double', OWL2Datatype.XSD_DOUBLE.short_form)
        self.assertEqual(Category.CAT_NUMBER, OWL2Datatype.XSD_DOUBLE.category)
        self.assertTrue(OWL2Datatype.XSD_DOUBLE.finite)
        self.assertEqual(
            '\\A(\\+|-)?(([0-9]+(\\.[0-9]*)?|\\.[0-9]+)(([Ee])((\\+|-)?'
            '([0-9]+)))?|((\\+|-)?INF|NaN))\\Z',
            OWL2Datatype.XSD_DOUBLE.pattern_string)
        self.assertIsNotNone(OWL2Datatype.XSD_DOUBLE.pattern)

        # all examples tested on one attribute
        self.assertEqual('XMLLiteral', OWL2Datatype.RDF_XML_LITERAL.short_form)
        self.assertEqual('Literal', OWL2Datatype.RDFS_LITERAL.short_form)  # 2
        self.assertEqual('PlainLiteral',
                         OWL2Datatype.RDF_PLAIN_LITERAL.short_form)  # 3

        self.assertEqual('real', OWL2Datatype.OWL_REAL.short_form)  # 4
        self.assertEqual('rational', OWL2Datatype.OWL_RATIONAL.short_form)  # 5
        self.assertEqual('string', OWL2Datatype.XSD_STRING.short_form)  # 6
        self.assertEqual('normalizedString',
                         OWL2Datatype.XSD_NORMALIZED_STRING.short_form)  # 7
        self.assertEqual('token', OWL2Datatype.XSD_TOKEN.short_form)  # 8
        self.assertEqual('language', OWL2Datatype.XSD_LANGUAGE.short_form)  # 9
        self.assertEqual('Name', OWL2Datatype.XSD_NAME.short_form)  # 10
        self.assertEqual('NCName', OWL2Datatype.XSD_NCNAME.short_form)  # 11
        self.assertEqual('NMTOKEN', OWL2Datatype.XSD_NMTOKEN.short_form)  # 12
        self.assertEqual('decimal', OWL2Datatype.XSD_DECIMAL.short_form)  # 13
        self.assertEqual('integer', OWL2Datatype.XSD_INTEGER.short_form)  # 14
        self.assertEqual('nonNegativeInteger',
                         OWL2Datatype.XSD_NON_NEGATIVE_INTEGER.short_form)  # 15
        self.assertEqual('nonPositiveInteger',
                         OWL2Datatype.XSD_NON_POSITIVE_INTEGER.short_form)  # 16
        self.assertEqual('positiveInteger',
                         OWL2Datatype.XSD_POSITIVE_INTEGER.short_form)  # 17
        self.assertEqual('negativeInteger',
                         OWL2Datatype.XSD_NEGATIVE_INTEGER.short_form)  # 18
        self.assertEqual('long', OWL2Datatype.XSD_LONG.short_form)  # 19
        self.assertEqual('int', OWL2Datatype.XSD_INT.short_form)  # 20
        self.assertEqual('short', OWL2Datatype.XSD_SHORT.short_form)  # 21
        self.assertEqual('byte', OWL2Datatype.XSD_BYTE.short_form)  # 22
        self.assertEqual('unsignedLong',
                         OWL2Datatype.XSD_UNSIGNED_LONG.short_form)  # 23
        self.assertEqual('unsignedInt',
                         OWL2Datatype.XSD_UNSIGNED_INT.short_form)  # 24
        self.assertEqual('unsignedShort',
                         OWL2Datatype.XSD_UNSIGNED_SHORT.short_form)  # 25
        self.assertEqual('unsignedByte',
                         OWL2Datatype.XSD_UNSIGNED_BYTE.short_form)  # 26
        self.assertEqual('double', OWL2Datatype.XSD_DOUBLE.short_form)  # 27
        self.assertEqual('float', OWL2Datatype.XSD_FLOAT.short_form)  # 28
        self.assertEqual('boolean', OWL2Datatype.XSD_BOOLEAN.short_form)  # 29
        self.assertEqual('hexBinary', OWL2Datatype.XSD_HEX_BINARY.short_form)
        self.assertEqual('base64Binary',
                         OWL2Datatype.XSD_BASE_64_BINARY.short_form)  # 31
        self.assertEqual('anyURI', OWL2Datatype.XSD_ANY_URI.short_form)  # 32
        self.assertEqual('dateTime', OWL2Datatype.XSD_DATE_TIME.short_form)
        self.assertEqual('dateTimeStamp',
                         OWL2Datatype.XSD_DATE_TIME_STAMP.short_form)  # 34

    def test_all_iris(self):
        self.assertIn(
            IRI('http://www.w3.org/1999/02/22-rdf-syntax-ns#XMLLiteral'),
            OWL2Datatype.ALL_IRIS)  # 1
        self.assertIn(
            IRI('http://www.w3.org/2000/01/rdf-schema#Literal'),
            OWL2Datatype.ALL_IRIS)  # 2
        self.assertIn(
            IRI('http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral'),
            OWL2Datatype.ALL_IRIS)  # 3
        self.assertIn(
            IRI('http://www.w3.org/2002/07/owl#real'), OWL2Datatype.ALL_IRIS)
        self.assertIn(
            IRI('http://www.w3.org/2002/07/owl#rational'),
            OWL2Datatype.ALL_IRIS)  # 5
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#string'),
            OWL2Datatype.ALL_IRIS)  # 6
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#normalizedString'),
            OWL2Datatype.ALL_IRIS)  # 7
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#token'),
            OWL2Datatype.ALL_IRIS)  # 8
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#language'),
            OWL2Datatype.ALL_IRIS)  # 9
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#Name'),
            OWL2Datatype.ALL_IRIS)  # 10
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#NCName'),
            OWL2Datatype.ALL_IRIS)  # 11
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#NMTOKEN'),
            OWL2Datatype.ALL_IRIS)  # 12
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#decimal'),
            OWL2Datatype.ALL_IRIS)  # 13
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#integer'),
            OWL2Datatype.ALL_IRIS)  # 14
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#nonNegativeInteger'),
            OWL2Datatype.ALL_IRIS)  # 15
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#nonPositiveInteger'),
            OWL2Datatype.ALL_IRIS)  # 16
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#positiveInteger'),
            OWL2Datatype.ALL_IRIS)  # 17
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#negativeInteger'),
            OWL2Datatype.ALL_IRIS)  # 18
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#long'), OWL2Datatype.ALL_IRIS)
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#int'), OWL2Datatype.ALL_IRIS)
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#short'),
            OWL2Datatype.ALL_IRIS)  # 21
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#byte'), OWL2Datatype.ALL_IRIS)
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#unsignedLong'),
            OWL2Datatype.ALL_IRIS)  # 23
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#unsignedInt'),
            OWL2Datatype.ALL_IRIS)  # 24
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#unsignedShort'),
            OWL2Datatype.ALL_IRIS)  # 25
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#unsignedByte'),
            OWL2Datatype.ALL_IRIS)  # 26
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#double'),
            OWL2Datatype.ALL_IRIS)  # 27
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#float'),
            OWL2Datatype.ALL_IRIS)  # 28
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#boolean'),
            OWL2Datatype.ALL_IRIS)  # 29
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#hexBinary'),
            OWL2Datatype.ALL_IRIS)  # 30
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#base64Binary'),
            OWL2Datatype.ALL_IRIS)  # 31
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#anyURI'),
            OWL2Datatype.ALL_IRIS)  # 32
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#dateTime'),
            OWL2Datatype.ALL_IRIS)  # 33
        self.assertIn(
            IRI('http://www.w3.org/2001/XMLSchema#dateTimeStamp'),
            OWL2Datatype.ALL_IRIS)  # 34

    def test_is_built_in(self):
        built_in_dtype_01 = IRI('http://www.w3.org/2001/XMLSchema#unsignedByte')
        built_in_dtype_02 = IRI('http://www.w3.org/2001/XMLSchema#integer')
        not_built_in_dtype = IRI('http://ex.org/dtype/integer')
        not_a_dtype_iri = 23
        self.assertTrue(OWL2Datatype.is_built_in(built_in_dtype_01))
        self.assertTrue(OWL2Datatype.is_built_in(built_in_dtype_02))
        self.assertFalse(OWL2Datatype.is_built_in(not_built_in_dtype))
        self.assertFalse(OWL2Datatype.is_built_in(not_a_dtype_iri))

    def test__get_datatype(self):
        built_in_dtype_01 = IRI('http://www.w3.org/2001/XMLSchema#unsignedByte')
        built_in_dtype_02 = IRI('http://www.w3.org/2001/XMLSchema#integer')
        not_built_in_dtype = IRI('http://ex.org/dtype/integer')
        not_a_dtype_iri = 23

        self.assertEqual(
            OWL2Datatype.XSD_UNSIGNED_BYTE,
            OWL2Datatype.get_datatype(built_in_dtype_01))
        self.assertEqual(
            OWL2Datatype.XSD_INTEGER,
            OWL2Datatype.get_datatype(built_in_dtype_02))
        self.assertRaises(OWLRuntimeException, OWL2Datatype.get_datatype,
                          not_built_in_dtype)
        self.assertRaises(OWLRuntimeException, OWL2Datatype.get_datatype,
                          not_a_dtype_iri)

    def test_is_numeric(self):
        self.assertTrue(OWL2Datatype.OWL_REAL.is_numeric())
        self.assertTrue(OWL2Datatype.XSD_INTEGER.is_numeric())
        self.assertTrue(OWL2Datatype.XSD_NEGATIVE_INTEGER.is_numeric())
        self.assertFalse(OWL2Datatype.XSD_STRING.is_numeric())
        self.assertFalse(OWL2Datatype.RDF_PLAIN_LITERAL.is_numeric())
        self.assertFalse(OWL2Datatype.XSD_DATE_TIME.is_numeric())

    def test_get_facets(self):
        self.assertEqual(
            Category.CAT_NUMBER.facets, OWL2Datatype.XSD_INTEGER.get_facets())

    def test_get_datatype(self):
        self.fail('OWLDataFactory needs to be implemented first')

    def test_is_in_lexical_space_rdf_xmlliteral(self):  # 01
        lex01 = 'test01'
        lex02 = '<test<lala>blah/>'
        lex03 = '23'
        lex04 = ''

        self.assertTrue(OWL2Datatype.RDF_XML_LITERAL.is_in_lexical_space(lex01))
        self.assertTrue(OWL2Datatype.RDF_XML_LITERAL.is_in_lexical_space(lex02))
        self.assertTrue(OWL2Datatype.RDF_XML_LITERAL.is_in_lexical_space(lex03))
        self.assertTrue(OWL2Datatype.RDF_XML_LITERAL.is_in_lexical_space(lex04))

    def test_is_in_lexical_space_rdf_rdfs_literal(self):  # 02
        lex01 = 'test01'
        lex02 = '<test<lala>blah/>'
        lex03 = '23'
        lex04 = ''

        self.assertTrue(OWL2Datatype.RDFS_LITERAL.is_in_lexical_space(lex01))
        self.assertTrue(OWL2Datatype.RDFS_LITERAL.is_in_lexical_space(lex02))
        self.assertTrue(OWL2Datatype.RDFS_LITERAL.is_in_lexical_space(lex03))
        self.assertTrue(OWL2Datatype.RDFS_LITERAL.is_in_lexical_space(lex04))

    def test_is_in_lexical_space_rdf_plain_literal(self):  # 03
        lx1 = 'test01'
        lx2 = '<test<lala>blah/>'
        lx3 = '23'
        lx4 = ''

        self.assertTrue(OWL2Datatype.RDF_PLAIN_LITERAL.is_in_lexical_space(lx1))
        self.assertTrue(OWL2Datatype.RDF_PLAIN_LITERAL.is_in_lexical_space(lx2))
        self.assertTrue(OWL2Datatype.RDF_PLAIN_LITERAL.is_in_lexical_space(lx3))
        self.assertTrue(OWL2Datatype.RDF_PLAIN_LITERAL.is_in_lexical_space(lx4))

    def test_is_in_lexical_space_owl_real(self):  # 04
        """
        http://www.w3.org/TR/owl2-syntax/#Real_Numbers.2C_Decimal_Numbers.2C_and_Integers
        --> 'The owl:real datatype does not directly provide any lexical forms.'
        """
        lex01 = 'test01'
        lex02 = '<test<lala>blah/>'
        lex03 = '23'
        lex04 = ''

        self.assertTrue(OWL2Datatype.OWL_REAL.is_in_lexical_space(lex01))
        self.assertTrue(OWL2Datatype.OWL_REAL.is_in_lexical_space(lex02))
        self.assertTrue(OWL2Datatype.OWL_REAL.is_in_lexical_space(lex03))
        self.assertTrue(OWL2Datatype.OWL_REAL.is_in_lexical_space(lex04))

    def test_is_in_lexical_space_owl_rational(self):  # 05
        """
        http://www.w3.org/TR/owl2-syntax/#Real_Numbers.2C_Decimal_Numbers.2C_and_Integers
        -->`The owl:rational datatype supports lexical forms defined by the
            following grammar (whitespace within the grammar MUST be ignored
            and MUST NOT be included in the lexical forms of owl:rational, and
            single quotes are used to introduce terminal symbols):
            numerator '/' denominator`
        """
        # pos examples taken from https://www.w3.org/2007/OWL/wiki/OWL_Rational
        lex01 = '-1/3'
        lex02 = '41/7'
        lex03 = '0/19'
        lex04 = '4/2'
        lex05 = '-6/1'
        lex06 = '0'  # fails with OWLAPI regex
        lex07 = '2'  # fails with OWLAPI regex
        lex08 = '-6'  # fails with OWLAPI regex
        # own deviations
        lex09 = '41 /7'
        lex10 = '41/ 7'
        lex11 = '41 / 7'
        lex12 = '41   /   7'
        lex13 = '2 '  # fails with OWLAPI regex
        # neg examples
        lex14 = 'test01'
        lex15 = '41//7'
        lex16 = '41/7/3'
        lex17 = ''
        lex18 = '/'
        self.assertTrue(OWL2Datatype.OWL_RATIONAL.is_in_lexical_space(lex01))
        self.assertTrue(OWL2Datatype.OWL_RATIONAL.is_in_lexical_space(lex02))
        self.assertTrue(OWL2Datatype.OWL_RATIONAL.is_in_lexical_space(lex03))
        self.assertTrue(OWL2Datatype.OWL_RATIONAL.is_in_lexical_space(lex04))
        self.assertTrue(OWL2Datatype.OWL_RATIONAL.is_in_lexical_space(lex05))
        self.assertTrue(OWL2Datatype.OWL_RATIONAL.is_in_lexical_space(lex06))
        self.assertTrue(OWL2Datatype.OWL_RATIONAL.is_in_lexical_space(lex07))
        self.assertTrue(OWL2Datatype.OWL_RATIONAL.is_in_lexical_space(lex08))
        self.assertTrue(OWL2Datatype.OWL_RATIONAL.is_in_lexical_space(lex09))
        self.assertTrue(OWL2Datatype.OWL_RATIONAL.is_in_lexical_space(lex10))
        self.assertTrue(OWL2Datatype.OWL_RATIONAL.is_in_lexical_space(lex11))
        self.assertTrue(OWL2Datatype.OWL_RATIONAL.is_in_lexical_space(lex12))
        self.assertTrue(OWL2Datatype.OWL_RATIONAL.is_in_lexical_space(lex13))
        self.assertFalse(OWL2Datatype.OWL_RATIONAL.is_in_lexical_space(lex14))
        self.assertFalse(OWL2Datatype.OWL_RATIONAL.is_in_lexical_space(lex15))
        self.assertFalse(OWL2Datatype.OWL_RATIONAL.is_in_lexical_space(lex16))
        self.assertFalse(OWL2Datatype.OWL_RATIONAL.is_in_lexical_space(lex17))
        self.assertFalse(OWL2Datatype.OWL_RATIONAL.is_in_lexical_space(lex18))

    def test_is_in_lexical_space_xsd_string(self):  # 06
        lex01 = 'test01'
        lex02 = '<test<lala> blah/>'
        lex03 = '23'
        lex04 = ''

        self.assertTrue(OWL2Datatype.OWL_REAL.is_in_lexical_space(lex01))
        self.assertTrue(OWL2Datatype.OWL_REAL.is_in_lexical_space(lex02))
        self.assertTrue(OWL2Datatype.OWL_REAL.is_in_lexical_space(lex03))
        self.assertTrue(OWL2Datatype.OWL_REAL.is_in_lexical_space(lex04))

    def test_is_in_lexical_space_xsd_norm_string(self):  # 07
        lex01 = 'test01'
        lex02 = '<test<lala>blah/>'
        lex03 = '23'
        lex04 = ''
        lex05 = 'test 01'
        lex06 = '<test\r<lala>blah/>'
        lex07 = '2\t3'
        lex08 = '\n'

        self.assertTrue(
            OWL2Datatype.XSD_NORMALIZED_STRING.is_in_lexical_space(lex01))
        self.assertTrue(
            OWL2Datatype.XSD_NORMALIZED_STRING.is_in_lexical_space(lex02))
        self.assertTrue(
            OWL2Datatype.XSD_NORMALIZED_STRING.is_in_lexical_space(lex03))
        self.assertTrue(
            OWL2Datatype.XSD_NORMALIZED_STRING.is_in_lexical_space(lex04))
        self.assertTrue(
            OWL2Datatype.XSD_NORMALIZED_STRING.is_in_lexical_space(lex05))
        self.assertFalse(
            OWL2Datatype.XSD_NORMALIZED_STRING.is_in_lexical_space(lex06))
        self.assertFalse(
            OWL2Datatype.XSD_NORMALIZED_STRING.is_in_lexical_space(lex07))
        self.assertFalse(
            OWL2Datatype.XSD_NORMALIZED_STRING.is_in_lexical_space(lex08))

    def test_is_in_lexical_space_xsd_token(self):  # 08
        lex01 = 'test01'
        lex02 = 'test 0 1'
        lex03 = '23'
        lex04 = '<test<lala>blah/>'
        lex05 = '<test <lala>blah/>'
        lex06 = ' test 0 1'
        lex07 = 'test 0 1 '
        lex08 = ' test 0 1 '
        lex09 = ' test\t0 1 '
        lex10 = ' test  0 1 '
        lex11 = ' test\n0 1 '

        self.assertTrue(OWL2Datatype.XSD_TOKEN.is_in_lexical_space(lex01))
        self.assertTrue(OWL2Datatype.XSD_TOKEN.is_in_lexical_space(lex02))
        self.assertTrue(OWL2Datatype.XSD_TOKEN.is_in_lexical_space(lex03))
        self.assertTrue(OWL2Datatype.XSD_TOKEN.is_in_lexical_space(lex04))
        self.assertTrue(OWL2Datatype.XSD_TOKEN.is_in_lexical_space(lex05))
        self.assertFalse(OWL2Datatype.XSD_TOKEN.is_in_lexical_space(lex06))
        self.assertFalse(OWL2Datatype.XSD_TOKEN.is_in_lexical_space(lex07))
        self.assertFalse(OWL2Datatype.XSD_TOKEN.is_in_lexical_space(lex08))
        self.assertFalse(OWL2Datatype.XSD_TOKEN.is_in_lexical_space(lex09))
        self.assertFalse(OWL2Datatype.XSD_TOKEN.is_in_lexical_space(lex10))
        self.assertFalse(OWL2Datatype.XSD_TOKEN.is_in_lexical_space(lex11))

    def test_is_in_lexical_space_xsd_language(self):  # 09
        lex01 = 'eng'
        lex02 = 'engengeng'  # longer than 8 chars --> fail
        lex03 = ''  # less than 1 char --> fail
        lex04 = 'sächs'  # umlaut --> fail
        lex05 = 'eng-foo-bar-baz'
        lex06 = 'eng-foo1-bar2-baz3'
        lex07 = 'eng-lalalalala'  # 2nd part longer than 8 chars --> fail
        lex08 = 'eng1-foo2-bar3-baz4'  # number in first part --> fail
        lex09 = 'eng1-foo'  # number in first part --> fail
        lex10 = '23'  # fail

        self.assertTrue(OWL2Datatype.XSD_LANGUAGE.is_in_lexical_space(lex01))
        self.assertFalse(OWL2Datatype.XSD_LANGUAGE.is_in_lexical_space(lex02))
        self.assertFalse(OWL2Datatype.XSD_LANGUAGE.is_in_lexical_space(lex03))
        self.assertFalse(OWL2Datatype.XSD_LANGUAGE.is_in_lexical_space(lex04))
        self.assertTrue(OWL2Datatype.XSD_LANGUAGE.is_in_lexical_space(lex05))
        self.assertTrue(OWL2Datatype.XSD_LANGUAGE.is_in_lexical_space(lex06))
        self.assertFalse(OWL2Datatype.XSD_LANGUAGE.is_in_lexical_space(lex07))
        self.assertFalse(OWL2Datatype.XSD_LANGUAGE.is_in_lexical_space(lex08))
        self.assertFalse(OWL2Datatype.XSD_LANGUAGE.is_in_lexical_space(lex09))
        self.assertFalse(OWL2Datatype.XSD_LANGUAGE.is_in_lexical_space(lex10))

    def test_is_in_lexical_space_xsd_name(self):  # 10
        # pos/neg examples taken from
        # http://www.datypic.com/sc/xsd/t-xsd_Name.html
        lex01 = 'myElement'
        lex02 = '_my.Element'
        lex03 = 'my-element'
        lex04 = 'pre:myelement3'
        lex05 = '-myelement'
        lex06 = '3rdElement'
        lex07 = ''

        self.assertTrue(OWL2Datatype.XSD_NAME.is_in_lexical_space(lex01))
        self.assertTrue(OWL2Datatype.XSD_NAME.is_in_lexical_space(lex02))
        self.assertTrue(OWL2Datatype.XSD_NAME.is_in_lexical_space(lex03))
        self.assertTrue(OWL2Datatype.XSD_NAME.is_in_lexical_space(lex04))
        self.assertFalse(OWL2Datatype.XSD_NAME.is_in_lexical_space(lex05))
        self.assertFalse(OWL2Datatype.XSD_NAME.is_in_lexical_space(lex06))
        self.assertFalse(OWL2Datatype.XSD_NAME.is_in_lexical_space(lex07))

    def test_is_in_lexical_space_xsd_ncname(self):  # 11
        # pos/neg examples taken from
        # http://www.datypic.com/sc/xsd/t-xsd_NCName.html
        lex01 = 'myElement'
        lex02 = '_my.Element'  # only worked after altering orig. OWLAPI regex
        lex03 = 'my-element'  # only worked after altering orig. OWLAPI regex
        lex04 = 'pre:myElement'
        lex05 = '-myelement'
        lex06 = ''

        self.assertTrue(OWL2Datatype.XSD_NCNAME.is_in_lexical_space(lex01))
        self.assertTrue(OWL2Datatype.XSD_NCNAME.is_in_lexical_space(lex02))
        self.assertTrue(OWL2Datatype.XSD_NCNAME.is_in_lexical_space(lex03))
        self.assertFalse(OWL2Datatype.XSD_NCNAME.is_in_lexical_space(lex04))
        self.assertFalse(OWL2Datatype.XSD_NCNAME.is_in_lexical_space(lex05))
        self.assertFalse(OWL2Datatype.XSD_NCNAME.is_in_lexical_space(lex06))

    def test_is_in_lexical_space_nmtoken(self):  # 12
        lex01 = 'test01'
        lex02 = '<test<lala> blah/>'
        lex03 = '23'
        lex04 = ''

        self.assertTrue(OWL2Datatype.XSD_NMTOKEN.is_in_lexical_space(lex01))
        self.assertTrue(OWL2Datatype.XSD_NMTOKEN.is_in_lexical_space(lex02))
        self.assertTrue(OWL2Datatype.XSD_NMTOKEN.is_in_lexical_space(lex03))
        self.assertTrue(OWL2Datatype.XSD_NMTOKEN.is_in_lexical_space(lex04))

    def test_is_in_lexical_space_xsd_decimal(self):  # 13
        # pos/neg examples taken from
        # http://www.datypic.com/sc/xsd/t-xsd_decimal.html
        lex01 = '3.0'
        lex02 = '-3.0'
        lex03 = '+3.5'
        lex04 = '3'
        lex05 = '.3'
        lex06 = '3.'
        lex07 = '0'
        lex08 = '-.3'
        lex09 = '0003.0'
        lex10 = '3.0000'
        lex11 = '3,5'  # fail
        lex12 = ''  # fail

        self.assertTrue(OWL2Datatype.XSD_DECIMAL.is_in_lexical_space(lex01))
        self.assertTrue(OWL2Datatype.XSD_DECIMAL.is_in_lexical_space(lex02))
        self.assertTrue(OWL2Datatype.XSD_DECIMAL.is_in_lexical_space(lex03))
        self.assertTrue(OWL2Datatype.XSD_DECIMAL.is_in_lexical_space(lex04))
        self.assertTrue(OWL2Datatype.XSD_DECIMAL.is_in_lexical_space(lex05))
        self.assertTrue(OWL2Datatype.XSD_DECIMAL.is_in_lexical_space(lex06))
        self.assertTrue(OWL2Datatype.XSD_DECIMAL.is_in_lexical_space(lex07))
        self.assertTrue(OWL2Datatype.XSD_DECIMAL.is_in_lexical_space(lex08))
        self.assertTrue(OWL2Datatype.XSD_DECIMAL.is_in_lexical_space(lex09))
        self.assertTrue(OWL2Datatype.XSD_DECIMAL.is_in_lexical_space(lex10))
        self.assertFalse(OWL2Datatype.XSD_DECIMAL.is_in_lexical_space(lex11))
        self.assertFalse(OWL2Datatype.XSD_DECIMAL.is_in_lexical_space(lex12))

    def test_is_in_lexical_space_xsd_integer(self):  # 14
        # pos/neg examples taken from
        # http://www.datypic.com/sc/xsd/t-xsd_integer.html
        lex01 = '122'
        lex02 = '00122'
        lex03 = '0'
        lex04 = '-3'
        lex05 = '+3'
        lex06 = '3.'  # fail
        lex07 = '3.0'  # fail
        lex08 = ''  # fail

        self.assertTrue(OWL2Datatype.XSD_INTEGER.is_in_lexical_space(lex01))
        self.assertTrue(OWL2Datatype.XSD_INTEGER.is_in_lexical_space(lex02))
        self.assertTrue(OWL2Datatype.XSD_INTEGER.is_in_lexical_space(lex03))
        self.assertTrue(OWL2Datatype.XSD_INTEGER.is_in_lexical_space(lex04))
        self.assertTrue(OWL2Datatype.XSD_INTEGER.is_in_lexical_space(lex05))
        self.assertFalse(OWL2Datatype.XSD_INTEGER.is_in_lexical_space(lex06))
        self.assertFalse(OWL2Datatype.XSD_INTEGER.is_in_lexical_space(lex07))
        self.assertFalse(OWL2Datatype.XSD_INTEGER.is_in_lexical_space(lex08))

    def test_is_in_lexical_space_xsd_non_negative_integer(self):  # 15
        # pos/neg examples taken from
        # http://www.datypic.com/sc/xsd/t-xsd_nonNegativeInteger.html
        lex01 = '+3'
        lex02 = '122'
        lex03 = '0'
        lex04 = '00122'
        lex05 = '-3'  # negative --> fail
        lex06 = '3.0'  # decimal point --> fail
        lex07 = ''

        self.assertTrue(
            OWL2Datatype.XSD_NON_NEGATIVE_INTEGER.is_in_lexical_space(lex01))
        self.assertTrue(
            OWL2Datatype.XSD_NON_NEGATIVE_INTEGER.is_in_lexical_space(lex02))
        self.assertTrue(
            OWL2Datatype.XSD_NON_NEGATIVE_INTEGER.is_in_lexical_space(lex03))
        self.assertTrue(
            OWL2Datatype.XSD_NON_NEGATIVE_INTEGER.is_in_lexical_space(lex04))
        self.assertFalse(
            OWL2Datatype.XSD_NON_NEGATIVE_INTEGER.is_in_lexical_space(lex05))
        self.assertFalse(
            OWL2Datatype.XSD_NON_NEGATIVE_INTEGER.is_in_lexical_space(lex06))
        self.assertFalse(
            OWL2Datatype.XSD_NON_NEGATIVE_INTEGER.is_in_lexical_space(lex07))

    def test_is_in_lexical_space_xsd_non_positive_integer(self):  # 16
        # pos/neg examples taken from
        # http://www.datypic.com/sc/xsd/t-xsd_nonPositiveInteger.html
        lex01 = '-3'
        lex02 = '0'
        lex03 = '-00122'
        lex04 = '122'  # fail
        lex05 = '+3'  # fail
        lex06 = '3.0'  # fail
        lex07 = ''  # fail

        self.assertTrue(
            OWL2Datatype.XSD_NON_POSITIVE_INTEGER.is_in_lexical_space(lex01))
        self.assertTrue(
            OWL2Datatype.XSD_NON_POSITIVE_INTEGER.is_in_lexical_space(lex02))
        self.assertTrue(
            OWL2Datatype.XSD_NON_POSITIVE_INTEGER.is_in_lexical_space(lex03))
        self.assertFalse(
            OWL2Datatype.XSD_NON_POSITIVE_INTEGER.is_in_lexical_space(lex04))
        self.assertFalse(
            OWL2Datatype.XSD_NON_POSITIVE_INTEGER.is_in_lexical_space(lex05))
        self.assertFalse(
            OWL2Datatype.XSD_NON_POSITIVE_INTEGER.is_in_lexical_space(lex06))
        self.assertFalse(
            OWL2Datatype.XSD_NON_POSITIVE_INTEGER.is_in_lexical_space(lex07))

    def test_is_in_lexical_space_xsd_positive_integer(self):  # 17
        # pos/neg examples taken from
        # http://www.datypic.com/sc/xsd/t-xsd_positiveInteger.html
        lex01 = '122'
        lex02 = '+3'
        lex03 = '00122'
        lex04 = '0'  # fail
        lex05 = '-3'  # fail
        lex06 = '3.0'  # fail
        lex07 = ''  # fail

        self.assertTrue(
            OWL2Datatype.XSD_POSITIVE_INTEGER.is_in_lexical_space(lex01))
        self.assertTrue(
            OWL2Datatype.XSD_POSITIVE_INTEGER.is_in_lexical_space(lex02))
        self.assertTrue(
            OWL2Datatype.XSD_POSITIVE_INTEGER.is_in_lexical_space(lex03))
        self.assertFalse(
            OWL2Datatype.XSD_POSITIVE_INTEGER.is_in_lexical_space(lex04))
        self.assertFalse(
            OWL2Datatype.XSD_POSITIVE_INTEGER.is_in_lexical_space(lex05))
        self.assertFalse(
            OWL2Datatype.XSD_POSITIVE_INTEGER.is_in_lexical_space(lex06))
        self.assertFalse(
            OWL2Datatype.XSD_POSITIVE_INTEGER.is_in_lexical_space(lex07))

    def test_is_in_lexical_space_xsd_negative_integer(self):  # 18
        # pos/neg examples taken from
        # http://www.datypic.com/sc/xsd/t-xsd_negativeInteger.html
        lex01 = '-3'
        lex02 = '-00122'
        lex03 = '0'  # fail
        lex04 = '122'  # fail
        lex05 = '+3'  # fail
        lex06 = '3.0'  # fail
        lex07 = ''

        self.assertTrue(
            OWL2Datatype.XSD_NEGATIVE_INTEGER.is_in_lexical_space(lex01))
        self.assertTrue(
            OWL2Datatype.XSD_NEGATIVE_INTEGER.is_in_lexical_space(lex02))
        self.assertFalse(
            OWL2Datatype.XSD_NEGATIVE_INTEGER.is_in_lexical_space(lex03))
        self.assertFalse(
            OWL2Datatype.XSD_NEGATIVE_INTEGER.is_in_lexical_space(lex04))
        self.assertFalse(
            OWL2Datatype.XSD_NEGATIVE_INTEGER.is_in_lexical_space(lex05))
        self.assertFalse(
            OWL2Datatype.XSD_NEGATIVE_INTEGER.is_in_lexical_space(lex06))
        self.assertFalse(
            OWL2Datatype.XSD_NEGATIVE_INTEGER.is_in_lexical_space(lex07))

    def test_is_in_lexical_space_xsd_long(self):  # 19
        # pos/neg examples taken from
        # http://www.datypic.com/sc/xsd/t-xsd_long.html
        lex01 = '+3'
        lex02 = '122'
        lex03 = '0'
        lex04 = '-1231235555'
        # not checked in OWLAPI (maybe not possible with regex at all)
        lex05 = '9223372036854775810'  # too large --> fail
        lex06 = '3.0'  # decimal point --> fail
        lex07 = ''

        self.assertTrue(OWL2Datatype.XSD_LONG.is_in_lexical_space(lex01))
        self.assertTrue(OWL2Datatype.XSD_LONG.is_in_lexical_space(lex02))
        self.assertTrue(OWL2Datatype.XSD_LONG.is_in_lexical_space(lex03))
        self.assertTrue(OWL2Datatype.XSD_LONG.is_in_lexical_space(lex04))
        # self.assertFalse(OWL2Datatype.XSD_LONG.is_in_lexical_space(lex05))
        self.assertFalse(OWL2Datatype.XSD_LONG.is_in_lexical_space(lex06))
        self.assertFalse(OWL2Datatype.XSD_LONG.is_in_lexical_space(lex07))

    def test_is_in_lexical_space_xsd_int(self):  # 20
        # pos/neg examples taken from
        # http://www.datypic.com/sc/xsd/t-xsd_int.html
        lex01 = '+3'
        lex02 = '122'
        lex03 = '0'
        lex04 = '-12312'
        lex05 = '3.0'  # decimal point --> fail
        lex06 = ''  # fail

        self.assertTrue(OWL2Datatype.XSD_INT.is_in_lexical_space(lex01))
        self.assertTrue(OWL2Datatype.XSD_INT.is_in_lexical_space(lex02))
        self.assertTrue(OWL2Datatype.XSD_INT.is_in_lexical_space(lex03))
        self.assertTrue(OWL2Datatype.XSD_INT.is_in_lexical_space(lex04))
        self.assertFalse(OWL2Datatype.XSD_INT.is_in_lexical_space(lex05))
        self.assertFalse(OWL2Datatype.XSD_INT.is_in_lexical_space(lex06))

    def test_is_in_lexical_space_xsd_short(self):  # 21
        # pos/neg examples taken from
        # http://www.datypic.com/sc/xsd/t-xsd_short.html
        lex01 = '+3'
        lex02 = '122'
        lex03 = '0'
        lex04 = '-1231'
        lex05 = '3.0'  # fail
        lex06 = ''  # fail

        self.assertTrue(OWL2Datatype.XSD_SHORT.is_in_lexical_space(lex01))
        self.assertTrue(OWL2Datatype.XSD_SHORT.is_in_lexical_space(lex02))
        self.assertTrue(OWL2Datatype.XSD_SHORT.is_in_lexical_space(lex03))
        self.assertTrue(OWL2Datatype.XSD_SHORT.is_in_lexical_space(lex04))
        self.assertFalse(OWL2Datatype.XSD_SHORT.is_in_lexical_space(lex05))
        self.assertFalse(OWL2Datatype.XSD_SHORT.is_in_lexical_space(lex06))

    def test_is_in_lexical_space_xsd_byte(self):  # 22
        # pos/neg examples taken from
        # http://www.datypic.com/sc/xsd/t-xsd_byte.html
        lex01 = '+3'
        lex02 = '122'
        lex03 = '0'
        lex04 = '-123'
        lex05 = '3.0'  # fail
        lex06 = ''  # fail

        self.assertTrue(OWL2Datatype.XSD_BYTE.is_in_lexical_space(lex01))
        self.assertTrue(OWL2Datatype.XSD_BYTE.is_in_lexical_space(lex02))
        self.assertTrue(OWL2Datatype.XSD_BYTE.is_in_lexical_space(lex03))
        self.assertTrue(OWL2Datatype.XSD_BYTE.is_in_lexical_space(lex04))
        self.assertFalse(OWL2Datatype.XSD_BYTE.is_in_lexical_space(lex05))
        self.assertFalse(OWL2Datatype.XSD_BYTE.is_in_lexical_space(lex06))

    def test_is_in_lexical_space_xsd_unsigned_long(self):  # 23
        # pos/neg examples taken from
        # http://www.datypic.com/sc/xsd/t-xsd_unsignedLong.html
        lex01 = '+3'
        lex02 = '122'
        lex03 = '0'
        lex04 = '-123'  # fail
        lex05 = '3.0'  # fail
        lex06 = ''

        self.assertTrue(
            OWL2Datatype.XSD_UNSIGNED_LONG.is_in_lexical_space(lex01))
        self.assertTrue(
            OWL2Datatype.XSD_UNSIGNED_LONG.is_in_lexical_space(lex02))
        self.assertTrue(
            OWL2Datatype.XSD_UNSIGNED_LONG.is_in_lexical_space(lex03))
        self.assertFalse(
            OWL2Datatype.XSD_UNSIGNED_LONG.is_in_lexical_space(lex04))
        self.assertFalse(
            OWL2Datatype.XSD_UNSIGNED_LONG.is_in_lexical_space(lex05))
        self.assertFalse(
            OWL2Datatype.XSD_UNSIGNED_LONG.is_in_lexical_space(lex06))

    def test_is_in_lexical_space_xsd_unsigned_int(self):  # 24
        # pos/neg examples taken from
        # http://www.datypic.com/sc/xsd/t-xsd_unsignedInt.html
        lex01 = '+3'
        lex02 = '122'
        lex03 = '0'
        lex04 = '-123'  # fail
        lex05 = '3.0'  # fail
        lex06 = ''  # fail

        self.assertTrue(
            OWL2Datatype.XSD_UNSIGNED_INT.is_in_lexical_space(lex01))
        self.assertTrue(
            OWL2Datatype.XSD_UNSIGNED_INT.is_in_lexical_space(lex02))
        self.assertTrue(
            OWL2Datatype.XSD_UNSIGNED_INT.is_in_lexical_space(lex03))
        self.assertFalse(
            OWL2Datatype.XSD_UNSIGNED_INT.is_in_lexical_space(lex04))
        self.assertFalse(
            OWL2Datatype.XSD_UNSIGNED_INT.is_in_lexical_space(lex05))
        self.assertFalse(
            OWL2Datatype.XSD_UNSIGNED_INT.is_in_lexical_space(lex06))

    def test_is_in_lexical_space_xsd_unsigned_short(self):  # 25
        # pos/neg examples taken from
        # http://www.datypic.com/sc/xsd/t-xsd_unsignedShort.html
        lex01 = '+3'
        lex02 = '122'
        lex03 = '0'
        lex04 = '-123'  # fail
        lex05 = '3.0'  # fail
        lex06 = ''  # fail

        self.assertTrue(
            OWL2Datatype.XSD_UNSIGNED_SHORT.is_in_lexical_space(lex01))
        self.assertTrue(
            OWL2Datatype.XSD_UNSIGNED_SHORT.is_in_lexical_space(lex02))
        self.assertTrue(
            OWL2Datatype.XSD_UNSIGNED_SHORT.is_in_lexical_space(lex03))
        self.assertFalse(
            OWL2Datatype.XSD_UNSIGNED_SHORT.is_in_lexical_space(lex04))
        self.assertFalse(
            OWL2Datatype.XSD_UNSIGNED_SHORT.is_in_lexical_space(lex05))
        self.assertFalse(
            OWL2Datatype.XSD_UNSIGNED_SHORT.is_in_lexical_space(lex06))

    def test_is_in_lexical_space_xsd_unsigned_byte(self):  # 26
        # pos/neg examples taken from
        # http://www.datypic.com/sc/xsd/t-xsd_unsignedByte.html
        lex01 = '+3'
        lex02 = '122'
        lex03 = '0'
        lex04 = '-123'  # fail
        lex05 = '3.0'  # fail
        lex06 = ''  # fail

        self.assertTrue(
            OWL2Datatype.XSD_UNSIGNED_BYTE.is_in_lexical_space(lex01))
        self.assertTrue(
            OWL2Datatype.XSD_UNSIGNED_BYTE.is_in_lexical_space(lex02))
        self.assertTrue(
            OWL2Datatype.XSD_UNSIGNED_BYTE.is_in_lexical_space(lex03))
        self.assertFalse(
            OWL2Datatype.XSD_UNSIGNED_BYTE.is_in_lexical_space(lex04))
        self.assertFalse(
            OWL2Datatype.XSD_UNSIGNED_BYTE.is_in_lexical_space(lex05))
        self.assertFalse(
            OWL2Datatype.XSD_UNSIGNED_BYTE.is_in_lexical_space(lex06))

    def test_is_in_lexical_space_xsd_double(self):  # 27
        # pos/neg exampes taken from
        # http://www.datypic.com/sc/xsd/t-xsd_double.html
        lex01 = '-3E2'
        lex02 = '4268.22752E11'
        lex03 = '+24.3e-3'
        lex04 = '12'
        lex05 = '+3.5'
        lex06 = '-INF'
        lex07 = '-0'
        lex08 = 'NaN'
        lex09 = '-3E2.4'  # the exponent must be an integer --> fail
        lex10 = '12E'  # fail
        lex11 = 'NAN'  # wrong capitalization --> fail
        lex12 = ''

        self.assertTrue(OWL2Datatype.XSD_DOUBLE.is_in_lexical_space(lex01))
        self.assertTrue(OWL2Datatype.XSD_DOUBLE.is_in_lexical_space(lex02))
        self.assertTrue(OWL2Datatype.XSD_DOUBLE.is_in_lexical_space(lex03))
        self.assertTrue(OWL2Datatype.XSD_DOUBLE.is_in_lexical_space(lex04))
        self.assertTrue(OWL2Datatype.XSD_DOUBLE.is_in_lexical_space(lex05))
        self.assertTrue(OWL2Datatype.XSD_DOUBLE.is_in_lexical_space(lex06))
        self.assertTrue(OWL2Datatype.XSD_DOUBLE.is_in_lexical_space(lex07))
        self.assertTrue(OWL2Datatype.XSD_DOUBLE.is_in_lexical_space(lex08))
        self.assertFalse(OWL2Datatype.XSD_DOUBLE.is_in_lexical_space(lex09))
        self.assertFalse(OWL2Datatype.XSD_DOUBLE.is_in_lexical_space(lex10))
        self.assertFalse(OWL2Datatype.XSD_DOUBLE.is_in_lexical_space(lex11))
        self.assertFalse(OWL2Datatype.XSD_DOUBLE.is_in_lexical_space(lex12))

    def test_is_in_lexical_space_xsd_float(self):  # 28
        # pos/neg examples taken from
        # http://www.datypic.com/sc/xsd/t-xsd_float.html
        lex01 = '-3E2'
        lex02 = '4268.22752E11'
        lex03 = '+24.3e-3'
        lex04 = '12'
        lex05 = '+3.5'
        lex06 = '-INF'
        lex07 = '-0'
        lex08 = 'NaN'
        lex09 = '-3E2.4'  # the exponent must be an integer --> fail
        lex10 = '12E'  # fail
        lex11 = 'NAN'  # wrong capitalization --> fail
        lex12 = ''

        self.assertTrue(OWL2Datatype.XSD_FLOAT.is_in_lexical_space(lex01))
        self.assertTrue(OWL2Datatype.XSD_FLOAT.is_in_lexical_space(lex02))
        self.assertTrue(OWL2Datatype.XSD_FLOAT.is_in_lexical_space(lex03))
        self.assertTrue(OWL2Datatype.XSD_FLOAT.is_in_lexical_space(lex04))
        self.assertTrue(OWL2Datatype.XSD_FLOAT.is_in_lexical_space(lex05))
        self.assertTrue(OWL2Datatype.XSD_FLOAT.is_in_lexical_space(lex06))
        self.assertTrue(OWL2Datatype.XSD_FLOAT.is_in_lexical_space(lex07))
        self.assertTrue(OWL2Datatype.XSD_FLOAT.is_in_lexical_space(lex08))
        self.assertFalse(OWL2Datatype.XSD_FLOAT.is_in_lexical_space(lex09))
        self.assertFalse(OWL2Datatype.XSD_FLOAT.is_in_lexical_space(lex10))
        self.assertFalse(OWL2Datatype.XSD_FLOAT.is_in_lexical_space(lex11))
        self.assertFalse(OWL2Datatype.XSD_FLOAT.is_in_lexical_space(lex12))

    def test_is_in_lexical_space_xsd_boolean(self):  # 29
        # pos/neg examples taken from
        # http://www.datypic.com/sc/xsd/t-xsd_boolean.html
        lex01 = 'true'
        lex02 = 'false'
        lex03 = '0'
        lex04 = '1'
        lex05 = 'TRUE'  # wrong capitalization --> fail
        lex06 = 'T'  # fail
        lex07 = ''

        self.assertTrue(OWL2Datatype.XSD_BOOLEAN.is_in_lexical_space(lex01))
        self.assertTrue(OWL2Datatype.XSD_BOOLEAN.is_in_lexical_space(lex02))
        self.assertTrue(OWL2Datatype.XSD_BOOLEAN.is_in_lexical_space(lex03))
        self.assertTrue(OWL2Datatype.XSD_BOOLEAN.is_in_lexical_space(lex04))
        self.assertFalse(OWL2Datatype.XSD_BOOLEAN.is_in_lexical_space(lex05))
        self.assertFalse(OWL2Datatype.XSD_BOOLEAN.is_in_lexical_space(lex06))
        self.assertFalse(OWL2Datatype.XSD_BOOLEAN.is_in_lexical_space(lex07))

    def test_is_in_lexical_space_xsd_hex_binary(self):  # 30
        # pos/neg examples taken from
        # http://www.datypic.com/sc/xsd/t-xsd_hexBinary.html
        lex01 = '0FB8'
        lex02 = '0fb8'
        lex03 = ''
        lex04 = 'FB8'  # odd number of characters --> fail

        self.assertTrue(OWL2Datatype.XSD_HEX_BINARY.is_in_lexical_space(lex01))
        self.assertTrue(OWL2Datatype.XSD_HEX_BINARY.is_in_lexical_space(lex02))
        self.assertTrue(OWL2Datatype.XSD_HEX_BINARY.is_in_lexical_space(lex03))
        self.assertFalse(OWL2Datatype.XSD_HEX_BINARY.is_in_lexical_space(lex04))

    def test_is_in_lexical_space_xsd_base64_binary(self):  # 31
        # pos/neg examples taken from
        # http://www.datypic.com/sc/xsd/t-xsd_base64Binary.html
        lex01 = '0FB8'
        lex02 = '0fb8'
        lex03 = '0 FB8 0F+9'
        lex04 = '0F+40A=='
        lex05 = ''
        lex06 = 'FB8'  # odd number of characters --> fail
        lex07 = '==0F'  # equals signs may only appear at the end --> fail

        self.assertTrue(
            OWL2Datatype.XSD_BASE_64_BINARY.is_in_lexical_space(lex01))
        self.assertTrue(
            OWL2Datatype.XSD_BASE_64_BINARY.is_in_lexical_space(lex02))
        self.assertTrue(
            OWL2Datatype.XSD_BASE_64_BINARY.is_in_lexical_space(lex03))
        self.assertTrue(
            OWL2Datatype.XSD_BASE_64_BINARY.is_in_lexical_space(lex04))
        self.assertTrue(
            OWL2Datatype.XSD_BASE_64_BINARY.is_in_lexical_space(lex05))
        self.assertFalse(
            OWL2Datatype.XSD_BASE_64_BINARY.is_in_lexical_space(lex06))
        self.assertFalse(
            OWL2Datatype.XSD_BASE_64_BINARY.is_in_lexical_space(lex07))

    def test_is_in_lexical_space_xsd_any_uri(self):  # 32
        # pos/neg examples taken from
        # http://www.datypic.com/sc/xsd/t-xsd_anyURI.html
        lex01 = 'http://datypic.com'
        lex02 = 'mailto:info@datypic.com'
        lex03 = '../%C3%A9dition.html'
        lex04 = '../édition.html'
        lex05 = 'http://datypic.com/prod.html#shirt'
        lex06 = '../prod.html#shirt'
        lex07 = 'urn:example:org'
        lex08 = ''
        # OWLAPI uses wildcard regex and hence the negative examples do not work
        lex09 = 'http://datypic.com#frag1#frag2'  # two #'s --> fail
        # % character followed by something other than two hexadecimal digits
        lex10 = 'http://datypic.com#f% rag'  # --> fail

        self.assertTrue(OWL2Datatype.XSD_ANY_URI.is_in_lexical_space(lex01))
        self.assertTrue(OWL2Datatype.XSD_ANY_URI.is_in_lexical_space(lex02))
        self.assertTrue(OWL2Datatype.XSD_ANY_URI.is_in_lexical_space(lex03))
        self.assertTrue(OWL2Datatype.XSD_ANY_URI.is_in_lexical_space(lex04))
        self.assertTrue(OWL2Datatype.XSD_ANY_URI.is_in_lexical_space(lex05))
        self.assertTrue(OWL2Datatype.XSD_ANY_URI.is_in_lexical_space(lex06))
        self.assertTrue(OWL2Datatype.XSD_ANY_URI.is_in_lexical_space(lex07))
        self.assertTrue(OWL2Datatype.XSD_ANY_URI.is_in_lexical_space(lex08))
        # self.assertFalse(OWL2Datatype.XSD_ANY_URI.is_in_lexical_space(lex09))
        # self.assertFalse(OWL2Datatype.XSD_ANY_URI.is_in_lexical_space(lex10))

    def test_is_in_lexical_space_xsd_date_time(self):  # 33
        # pos/neg examples taken from
        # http://www.datypic.com/sc/xsd/t-xsd_dateTime.html
        lex01 = '2004-04-12T13:20:00'
        lex02 = '2004-04-12T13:20:15.5'
        lex03 = '2004-04-12T13:20:00-05:00'
        lex04 = '2004-04-12T13:20:00Z'
        lex05 = '2004-04-12T13:00'  # no seconds specified --> fail
        lex06 = '2004-04-1213:20:00'  # letter T missing --> fail
        lex07 = '99-04-12T13:00'  # truncated century --> fail
        lex08 = '2004-04-12'  # time missing --> fail
        lex09 = ''

        self.assertTrue(OWL2Datatype.XSD_DATE_TIME.is_in_lexical_space(lex01))
        self.assertTrue(OWL2Datatype.XSD_DATE_TIME.is_in_lexical_space(lex02))
        self.assertTrue(OWL2Datatype.XSD_DATE_TIME.is_in_lexical_space(lex03))
        self.assertTrue(OWL2Datatype.XSD_DATE_TIME.is_in_lexical_space(lex04))
        self.assertFalse(OWL2Datatype.XSD_DATE_TIME.is_in_lexical_space(lex05))
        self.assertFalse(OWL2Datatype.XSD_DATE_TIME.is_in_lexical_space(lex06))
        self.assertFalse(OWL2Datatype.XSD_DATE_TIME.is_in_lexical_space(lex07))
        self.assertFalse(OWL2Datatype.XSD_DATE_TIME.is_in_lexical_space(lex08))
        self.assertFalse(OWL2Datatype.XSD_DATE_TIME.is_in_lexical_space(lex09))

    def test_is_in_lexical_space_xsd_date_time_stamp(self):  # 34
        # pos/neg examples taken from
        # http://www.datypic.com/sc/xsd11/t-xsd_dateTimeStamp.html
        lex01 = '2004-04-12T13:20:00-05:00'
        lex02 = '2004-04-12T13:20:00Z'
        lex03 = '2004-04-12T13:20:00'  # time zone missing --> fail
        lex04 = '2004-04-12T13:00Z'  # seconds missing --> fail
        lex05 = '2004-04-12Z'  # time missing
        lex06 = ''

        self.assertTrue(
            OWL2Datatype.XSD_DATE_TIME_STAMP.is_in_lexical_space(lex01))
        self.assertTrue(
            OWL2Datatype.XSD_DATE_TIME_STAMP.is_in_lexical_space(lex02))
        self.assertFalse(
            OWL2Datatype.XSD_DATE_TIME_STAMP.is_in_lexical_space(lex03))
        self.assertFalse(
            OWL2Datatype.XSD_DATE_TIME_STAMP.is_in_lexical_space(lex04))
        self.assertFalse(
            OWL2Datatype.XSD_DATE_TIME_STAMP.is_in_lexical_space(lex05))
        self.assertFalse(
            OWL2Datatype.XSD_DATE_TIME_STAMP.is_in_lexical_space(lex06))

    # ------------------- original tests from OWLAPI -------------------
    def test_should_return_correct_prefix_name_for_xmlliteral(self):
        prefixed_name = OWL2Datatype.RDF_XML_LITERAL.prefixed_name

        self.assertEqual('rdf:XMLLiteral', prefixed_name)

    def test_should_return_correct_prefix_name_for_literal(self):
        prefixed_name = OWL2Datatype.RDFS_LITERAL.prefixed_name

        self.assertEqual('rdfs:Literal', prefixed_name)

    def test_should_return_correct_prefix_name_for_plain_literal(self):
        prefixed_name = OWL2Datatype.RDF_PLAIN_LITERAL.prefixed_name

        self.assertEqual('rdf:PlainLiteral', prefixed_name)

    def test_should_return_correct_prefix_name_for_real(self):
        prefixed_name = OWL2Datatype.OWL_REAL.prefixed_name

        self.assertEqual('owl:real', prefixed_name)

    def test_should_return_correct_prefix_name_for_rational(self):
        prefixed_name = OWL2Datatype.OWL_RATIONAL.prefixed_name

        self.assertEqual('owl:rational', prefixed_name)

    def test_should_return_correct_prefix_name_for_string(self):
        prefixed_name = OWL2Datatype.XSD_STRING.prefixed_name

        self.assertEqual('xsd:string', prefixed_name)

    def test_should_return_correct_prefix_name_for_normalizedString(self):
        prefixed_name = OWL2Datatype.XSD_NORMALIZED_STRING.prefixed_name

        self.assertEqual('xsd:normalizedString', prefixed_name)

    def test_should_return_correct_prefix_name_for_token(self):
        prefixed_name = OWL2Datatype.XSD_TOKEN.prefixed_name

        self.assertEqual('xsd:token', prefixed_name)

    def test_should_return_correct_prefix_name_for_language(self):
        prefixed_name = OWL2Datatype.XSD_LANGUAGE.prefixed_name

        self.assertEqual('xsd:language', prefixed_name)

    def test_should_return_correct_prefix_name_for_name(self):
        prefixed_name = OWL2Datatype.XSD_NAME.prefixed_name

        self.assertEqual('xsd:Name', prefixed_name)

    def test_should_return_correct_prefix_name_for_ncname(self):
        prefixed_name = OWL2Datatype.XSD_NCNAME.prefixed_name

        self.assertEqual('xsd:NCName', prefixed_name)

    def test_should_return_correct_prefix_name_for_nmtoken(self):
        prefixed_name = OWL2Datatype.XSD_NMTOKEN.prefixed_name

        self.assertEqual('xsd:NMTOKEN', prefixed_name)

    def test_should_return_correct_prefix_name_for_decimal(self):
        prefixed_name = OWL2Datatype.XSD_DECIMAL.prefixed_name

        self.assertEqual('xsd:decimal', prefixed_name)

    def test_should_return_correct_prefix_name_for_integer(self):
        prefixed_name = OWL2Datatype.XSD_INTEGER.prefixed_name

        self.assertEqual('xsd:integer', prefixed_name)

    def test_should_return_correct_prefix_name_for_non_negative_integer(self):
        prefixed_name = OWL2Datatype.XSD_NON_NEGATIVE_INTEGER.prefixed_name

        self.assertEqual('xsd:nonNegativeInteger', prefixed_name)

    def test_should_return_correct_prefix_name_for_non_positive_integer(self):
        prefixed_name = OWL2Datatype.XSD_NON_POSITIVE_INTEGER.prefixed_name

        self.assertEqual('xsd:nonPositiveInteger', prefixed_name)

    def test_should_return_correct_prefix_name_for_positive_integer(self):
        prefixed_name = OWL2Datatype.XSD_POSITIVE_INTEGER.prefixed_name

        self.assertEqual('xsd:positiveInteger', prefixed_name)

    def test_should_return_correct_prefix_name_for_negative_integer(self):
        prefixed_name = OWL2Datatype.XSD_NEGATIVE_INTEGER.prefixed_name

        self.assertEqual('xsd:negativeInteger', prefixed_name)

    def test_should_return_correct_prefix_name_for_long(self):
        prefixed_name = OWL2Datatype.XSD_LONG.prefixed_name

        self.assertEqual('xsd:long', prefixed_name)

    def test_should_return_correct_prefix_name_for_int(self):
        prefixed_name = OWL2Datatype.XSD_INT.prefixed_name

        self.assertEqual('xsd:int', prefixed_name)

    def test_should_return_correct_prefix_name_for_short(self):
        prefixed_name = OWL2Datatype.XSD_SHORT.prefixed_name

        self.assertEqual('xsd:short', prefixed_name)

    def test_should_return_correct_prefix_name_for_byte(self):
        prefixed_name = OWL2Datatype.XSD_BYTE.prefixed_name

        self.assertEqual('xsd:byte', prefixed_name)

    def test_should_return_correct_prefix_name_for_unsigned_long(self):
        prefixed_name = OWL2Datatype.XSD_UNSIGNED_LONG.prefixed_name

        self.assertEqual('xsd:unsignedLong', prefixed_name)

    def test_should_return_correct_prefix_name_for_unsigned_int(self):
        prefixed_name = OWL2Datatype.XSD_UNSIGNED_INT.prefixed_name

        self.assertEqual('xsd:unsignedInt', prefixed_name)

    def test_should_return_correct_prefix_name_for_unsigned_short(self):
        prefixed_name = OWL2Datatype.XSD_UNSIGNED_SHORT.prefixed_name

        self.assertEqual('xsd:unsignedShort', prefixed_name)

    def test_should_return_correct_prefix_name_for_unsigned_byte(self):
        prefixed_name = OWL2Datatype.XSD_UNSIGNED_BYTE.prefixed_name

        self.assertEqual('xsd:unsignedByte', prefixed_name)

    def test_should_return_correct_prefix_name_for_double(self):
        prefixed_name = OWL2Datatype.XSD_DOUBLE.prefixed_name

        self.assertEqual('xsd:double', prefixed_name)

    def test_should_return_correct_prefix_name_for_float(self):
        prefixed_name = OWL2Datatype.XSD_FLOAT.prefixed_name

        self.assertEqual('xsd:float', prefixed_name)

    def test_should_return_correct_prefix_name_for_boolean(self):
        prefixed_name = OWL2Datatype.XSD_BOOLEAN.prefixed_name

        self.assertEqual('xsd:boolean', prefixed_name)

    def test_should_return_correct_prefix_name_for_hex_binary(self):
        prefixed_name = OWL2Datatype.XSD_HEX_BINARY.prefixed_name

        self.assertEqual('xsd:hexBinary', prefixed_name)

    def test_should_return_correct_prefix_name_for_base64_binary(self):
        prefixed_name = OWL2Datatype.XSD_BASE_64_BINARY.prefixed_name

        self.assertEqual('xsd:base64Binary', prefixed_name)

    def test_should_return_correct_prefix_name_for_any_uri(self):
        prefixed_name = OWL2Datatype.XSD_ANY_URI.prefixed_name

        self.assertEqual('xsd:anyURI', prefixed_name)

    def test_should_return_correct_prefix_name_for_date_time(self):
        prefixed_name = OWL2Datatype.XSD_DATE_TIME.prefixed_name

        self.assertEqual('xsd:dateTime', prefixed_name)

    def test_should_return_correct_prefix_name_for_date_timestamp(self):
        prefixed_name = OWL2Datatype.XSD_DATE_TIME_STAMP.prefixed_name

        self.assertEqual('xsd:dateTimeStamp', prefixed_name)
