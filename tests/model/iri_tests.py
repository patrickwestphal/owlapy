import os
import unittest
import tempfile

from urllib import parse as p

import rdflib

from owlapy.model import IRI
from owlapy.model.iri import IRIException
from owlapy.model import OWLVisitorEx

class TestIRI(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # <__init__ tests> --------------------------------------------------------
    # whole (slash) IRI without fragment as input
    def test___init___01(self):
        prefix = 'http://example.org/foo/'
        suffix = 'bar'
        whole_iri = prefix + suffix
        iri = IRI(whole_iri)
        self.assertEqual(prefix, iri.prefix)
        self.assertEqual(prefix, iri.namespace)
        self.assertEqual(suffix, iri.remainder)

    # whole (hash) IRI without fragment as input
    def test___init___02(self):
        prefix = 'http://example.org/foo#'
        suffix = 'bar'
        whole_iri = prefix + suffix
        iri = IRI(whole_iri)
        self.assertEqual(prefix, iri.prefix)
        self.assertEqual(prefix, iri.namespace)
        self.assertEqual(suffix, iri.remainder)

    # prefix + suffix as input
    def test___init___03(self):
        prefix = 'http://example.org/foo/'
        suffix = 'bar'
        iri = IRI(prefix, suffix)
        self.assertEqual(prefix, iri.prefix)
        self.assertEqual(prefix, iri.namespace)
        self.assertEqual(suffix, iri.remainder)

    # rdflib.URIRef object as input
    def test___init___04(self):
        prefix = 'http://example.org/foo/'
        suffix = 'bar'
        uri = rdflib.URIRef(prefix + suffix)
        iri = IRI(uri)
        self.assertEqual(prefix, iri.prefix)
        self.assertEqual(prefix, iri.namespace)
        self.assertEqual(suffix, iri.remainder)
    # </__init__ tests> -------------------------------------------------------

    # <__len__ tests> ---------------------------------------------------------
    # whole IRI initialization
    def test___len___01(self):
        whole_iri_str = 'http://example.org/foo/bar'
        length = len(whole_iri_str)
        iri = IRI(whole_iri_str)
        self.assertEqual(length, len(iri))

    # prefix-suffix initialization
    def test___len___02(self):
        prefix = 'http://example.org/fooo/'
        prefix_len = len(prefix)
        suffix = 'baar'
        suffix_len = len(suffix)
        length = prefix_len + suffix_len
        iri = IRI(prefix, suffix)
        self.assertEqual(length, len(iri))

    # prefix-suffix initialization with empty prefix
    def test___len___03(self):
        prefix = ''
        prefix_len = len(prefix)
        suffix = 'baaar'
        suffix_len = len(suffix)
        length = prefix_len + suffix_len
        iri = IRI(prefix, suffix)
        self.assertEqual(length, len(iri))

    # prefix-suffix initialization with empty suffix
    def test___len___04(self):
        prefix = 'http://example.org/foooo/'
        prefix_len = len(prefix)
        suffix = ''
        suffix_len = len(suffix)
        length = prefix_len + suffix_len
        iri = IRI(prefix, suffix)
        self.assertEqual(length, len(iri))
    # </__len__ tests> --------------------------------------------------------

    # <__getitem__ tests> -----------------------------------------------------
    # get first
    def test___getitem___01(self):
        iri_str = 'http://exampe.org/foo#bar'
        iri = IRI(iri_str)
        self.assertEqual(iri_str[0], iri[0])

    # get last (-1)
    def test___getitem___02(self):
        iri_str = 'http://exampe.org/foo#bar'
        iri = IRI(iri_str)
        self.assertEqual(iri_str[-1], iri[-1])

    # get sub range (in prefix)
    def test___getitem___03(self):
        prefix = 'http://exampe.org/foo#'
        suffix = 'bar'
        iri_str = prefix + suffix
        iri = IRI(iri_str)
        start = len(prefix) - 6
        stop = len(prefix) - 2
        self.assertEqual(iri_str[start:stop], iri[start:stop])

    # get sub range (in prefix and suffix)
    def test___getitem___04(self):
        prefix = 'http://exampe.org/foo#'
        suffix = 'bar'
        iri_str = prefix + suffix
        iri = IRI(iri_str)
        start = len(prefix) - 2
        stop = len(prefix) + 2
        self.assertEqual(iri_str[start:stop], iri[start:stop])

    # get sub range (in suffix)
    def test___getitem___05(self):
        prefix = 'http://exampe.org/foo#'
        suffix = 'bar1234'
        iri_str = prefix + suffix
        iri = IRI(iri_str)
        start = len(prefix) + 1
        stop = len(prefix) + 5
        self.assertEqual(iri_str[start:stop], iri[start:stop])
    # </__getitem__ tests> ----------------------------------------------------

    # <__eq__ tests> ----------------------------------------------------------
    # 2 iris initialized with same iri string
    def test___eq___01(self):
        iri_str = 'http://example.org/foo#bar'
        iri1 = IRI(iri_str)
        iri2 = IRI(iri_str)
        self.assertEqual(iri1, iri2)

    # 2 iris initialized with different iri strings
    def test___eq___02(self):
        iri_str1 = 'http://example.org/foo#bar'
        iri_str2 = 'http://example.org/foo#baz'
        iri1 = IRI(iri_str1)
        iri2 = IRI(iri_str2)
        self.assertNotEqual(iri1, iri2)

    # 2 iris initialized with same prefixes and suffixes
    def test___eq___03(self):
        prefix = 'http://example.org/foo#'
        suffix = 'bar'
        iri1 = IRI(prefix, suffix)
        iri2 = IRI(prefix, suffix)
        self.assertEqual(iri1, iri2)

    # 2 iris initialized with different prefixes and suffixes
    def test___eq___04(self):
        prefix1 = 'http://example.org/foo#'
        suffix1 = 'bar'
        prefix2 = 'http://example.org/foo/'
        suffix2 = 'baz'
        iri1 = IRI(prefix1, suffix1)
        iri2 = IRI(prefix2, suffix2)
        self.assertNotEqual(iri1, iri2)

    # 2 iris initialized with different prefixes and suffixes, but
    # prefix1 + suffix1 == prefix2 + suffix2
    def test___eq___05(self):
        # ...since this is how owlapi.model.IRI behaves
        prefix1 = 'http://example.org/foo/bar#'
        suffix1 = 'baz'
        prefix2 = 'http://example.org/foo/'
        suffix2 = 'bar#baz'
        iri1 = IRI(prefix1, suffix1)
        iri2 = IRI(prefix2, suffix2)
        self.assertEqual(iri1, iri2)

    # 1st iri initialized with iri string and 2nd initialized with prefix and
    # suffix where iri string != prefix + suffix
    def test___eq___06(self):
        iri_str = 'http://example.org/foo/bar'
        iri1 = IRI(iri_str)
        prefix = 'http://example.org/bar#'
        suffix = 'baz'
        iri2 = IRI(prefix, suffix)
        self.assertNotEqual(iri1, iri2)

    # 1st iri initialized with iri string and 2nd initialized with prefix and
    # suffix where iri string == prefix + suffix
    def test___eq___07(self):
        prefix = 'http://example.org/foo#'
        suffix = 'bar'
        iri_str = prefix + suffix
        iri1 = IRI(iri_str)
        iri2 = IRI(prefix, suffix)
        self.assertEquals(iri1, iri2)

    # 1st iri initialized with iri string and 2nd initialized with
    # rdflib.URIRef where iri string == rdflib.URIRef identifier
    def test___eq___08(self):
        iri_str = 'http://example.org/foo#bar'
        iri1 = IRI(iri_str)
        uri = rdflib.URIRef(iri_str)
        iri2 = IRI(uri)
        self.assertEqual(iri1, iri2)

    # 1st iri initialized with iri string and 2nd initialized with
    # rdflib.URIRef where iri string != rdflib.URIRef identifier
    def test___eq___09(self):
        iri_str = 'http://example.org/foo#bar'
        iri1 = IRI(iri_str)
        uri_str = 'http://example.org/baz/bar'
        uri = rdflib.URIRef(uri_str)
        iri2 = IRI(uri)
        self.assertNotEqual(iri1, iri2)

    # 1st iri initialized with rdflib.URIRef and 2nd initialized with prefix
    # and suffix where rdflib.URIRef identifier != prefix + suffix
    def test___eq___10(self):
        uri = rdflib.URIRef('http://example.org/bar/baz')
        iri1 = IRI(uri)
        prefix = 'http://example.org/foo/'
        suffix = 'bar'
        iri2 = IRI(prefix, suffix)
        self.assertNotEqual(iri1, iri2)

    # 1st iri initialized with rdflib.URIRef and 2nd initialized with prefix
    # and suffix where rdflib.URIRef identifier == prefix + suffix
    def test___eq___11(self):
        prefix = 'http://example.org/foo/'
        suffix = 'bar'
        uri = rdflib.URIRef(prefix + suffix)
        iri1 = IRI(uri)
        iri2 = IRI(prefix, suffix)
        self.assertEqual(iri1, iri2)

    # 2 iris initialized with different rdflib.URIRefs
    def test___eq___12(self):
        uri1 = rdflib.URIRef('http://example.org/foo#bar')
        iri1 = IRI(uri1)
        uri2 = rdflib.URIRef('http://example.org/bar/baz')
        iri2 = IRI(uri2)
        self.assertNotEqual(iri1, iri2)

    # 2 iris initialized with same rdflib.URIRefs
    def test___eq___13(self):
        uri_str = 'http://example.org/foo#bar'
        uri1 = rdflib.URIRef(uri_str)
        uri2 = rdflib.URIRef(uri_str)
        iri1 = IRI(uri1)
        iri2 = IRI(uri2)
        self.assertEqual(iri1, iri2)

    # 1st is IRI, 2nd is not IRI
    def test___eq___14(self):
        iri = IRI('http://example.org/foo#bar')
        not_iri = 23
        self.assertNotEqual(iri, not_iri)
    # </__eq__ tests> ---------------------------------------------------------

    # <__hash__ tests> --------------------------------------------------------
        # 2 iris initialized with same iri string
    def test___hash___01(self):
        iri_str = 'http://example.org/foo#bar'
        iri1 = IRI(iri_str)
        iri2 = IRI(iri_str)
        self.assertEqual(hash(iri1), hash(iri2))

    # 2 iris initialized with different iri strings
    def test___hash___02(self):
        iri_str1 = 'http://example.org/foo#bar'
        iri_str2 = 'http://example.org/foo#baz'
        iri1 = IRI(iri_str1)
        iri2 = IRI(iri_str2)
        self.assertNotEqual(hash(iri1), hash(iri2))

    # 2 iris initialized with same prefixes and suffixes
    def test___hash___03(self):
        prefix = 'http://example.org/foo#'
        suffix = 'bar'
        iri1 = IRI(prefix, suffix)
        iri2 = IRI(prefix, suffix)
        self.assertEqual(hash(iri1), hash(iri2))

    # 2 iris initialized with different prefixes and suffixes
    def test___hash___04(self):
        prefix1 = 'http://example.org/foo#'
        suffix1 = 'bar'
        prefix2 = 'http://example.org/foo/'
        suffix2 = 'baz'
        iri1 = IRI(prefix1, suffix1)
        iri2 = IRI(prefix2, suffix2)
        self.assertNotEqual(hash(iri1), hash(iri2))

    # 2 iris initialized with different prefixes and suffixes, but
    # prefix1 + suffix1 == prefix2 + suffix2
    def test___hash___05(self):
        # ...since this is how owlapi.model.IRI behaves
        prefix1 = 'http://example.org/foo/bar#'
        suffix1 = 'baz'
        prefix2 = 'http://example.org/foo/'
        suffix2 = 'bar#baz'
        iri1 = IRI(prefix1, suffix1)
        iri2 = IRI(prefix2, suffix2)
        self.assertEqual(hash(iri1), hash(iri2))

    # 1st iri initialized with iri string and 2nd initialized with prefix and
    # suffix where iri string != prefix + suffix
    def test___hash___06(self):
        iri_str = 'http://example.org/foo/bar'
        iri1 = IRI(iri_str)
        prefix = 'http://example.org/bar#'
        suffix = 'baz'
        iri2 = IRI(prefix, suffix)
        self.assertNotEqual(hash(iri1), hash(iri2))

    # 1st iri initialized with iri string and 2nd initialized with prefix and
    # suffix where iri string == prefix + suffix
    def test___hash___07(self):
        prefix = 'http://example.org/foo#'
        suffix = 'bar'
        iri_str = prefix + suffix
        iri1 = IRI(iri_str)
        iri2 = IRI(prefix, suffix)
        self.assertEquals(hash(iri1), hash(iri2))

    # 1st iri initialized with iri string and 2nd initialized with
    # rdflib.URIRef where iri string == rdflib.URIRef identifier
    def test___hash___08(self):
        iri_str = 'http://example.org/foo#bar'
        iri1 = IRI(iri_str)
        uri = rdflib.URIRef(iri_str)
        iri2 = IRI(uri)
        self.assertEqual(hash(iri1), hash(iri2))

    # 1st iri initialized with iri string and 2nd initialized with
    # rdflib.URIRef where iri string != rdflib.URIRef identifier
    def test___hash___09(self):
        iri_str = 'http://example.org/foo#bar'
        iri1 = IRI(iri_str)
        uri_str = 'http://example.org/baz/bar'
        uri = rdflib.URIRef(uri_str)
        iri2 = IRI(uri)
        self.assertNotEqual(hash(iri1), hash(iri2))

    # 1st iri initialized with rdflib.URIRef and 2nd initialized with prefix
    # and suffix where rdflib.URIRef identifier != prefix + suffix
    def test___hash___10(self):
        uri = rdflib.URIRef('http://example.org/bar/baz')
        iri1 = IRI(uri)
        prefix = 'http://example.org/foo/'
        suffix = 'bar'
        iri2 = IRI(prefix, suffix)
        self.assertNotEqual(hash(iri1), hash(iri2))

    # 1st iri initialized with rdflib.URIRef and 2nd initialized with prefix
    # and suffix where rdflib.URIRef identifier == prefix + suffix
    def test___hash___11(self):
        prefix = 'http://example.org/foo/'
        suffix = 'bar'
        uri = rdflib.URIRef(prefix + suffix)
        iri1 = IRI(uri)
        iri2 = IRI(prefix, suffix)
        self.assertEqual(hash(iri1), hash(iri2))

    # 2 iris initialized with different rdflib.URIRefs
    def test___hash___12(self):
        uri1 = rdflib.URIRef('http://example.org/foo#bar')
        iri1 = IRI(uri1)
        uri2 = rdflib.URIRef('http://example.org/bar/baz')
        iri2 = IRI(uri2)
        self.assertNotEqual(hash(iri1), hash(iri2))

    # 2 iris initialized with same rdflib.URIRefs
    def test___hash___13(self):
        uri_str = 'http://example.org/foo#bar'
        uri1 = rdflib.URIRef(uri_str)
        uri2 = rdflib.URIRef(uri_str)
        iri1 = IRI(uri1)
        iri2 = IRI(uri2)
        self.assertEqual(hash(iri1), hash(iri2))

    # 1st is IRI, 2nd is not IRI
    def test___hash___14(self):
        iri = IRI('http://example.org/foo#bar')
        not_iri = 23
        self.assertNotEqual(hash(iri), hash(not_iri))
    # </__hash__ tests> -------------------------------------------------------

    # <__str__ tests> ---------------------------------------------------------
    # prefix and suffix present --> = prefix + suffix
    def test___str___01(self):
        prefix = 'http://example.org/foo#'
        suffix = 'bar'
        iri = IRI(prefix, suffix)
        self.assertEqual(prefix+suffix, str(iri))

    # suffix is None --> = prefix
    def test___str___02(self):
        prefix = 'http://example.org/foo#bar'
        suffix = None
        iri = IRI(prefix, suffix)
        self.assertEqual(prefix, str(iri))

    # suffix is empty string --> = prefix
    def test___str___03(self):
        prefix = 'http://example.org/foo#bar'
        suffix = ''
        iri = IRI(prefix, suffix)
        self.assertEqual(prefix, str(iri))
    # </__str__ tests> --------------------------------------------------------

    # <to_uri tests> ----------------------------------------------------------
    # initialised with whole iri string
    def test_to_uri_01(self):
        iri_str = 'http://example.org/foo#bar'
        iri = IRI(iri_str)
        uri = rdflib.URIRef(iri_str)
        self.assertEqual(uri, iri.to_uri())

    # initialised with prefix and suffix
    def test_to_uri_03(self):
        prefix = 'http://example.org/foo#'
        suffix = 'bar'
        iri = IRI(prefix, suffix)
        uri = rdflib.URIRef(prefix + suffix)
        self.assertEqual(uri, iri.to_uri())

    # initialised with rdflib.URIRef
    def test_to_uri_04(self):
        uri = rdflib.URIRef('http://example.org/foo#bar')
        iri = IRI(uri)
        self.assertEqual(uri, iri.to_uri())
    # </to_uri tests> ---------------------------------------------------------

    # <is_absolute tests> -----------------------------------------------------
    # test examples taken from https://tools.ietf.org/html/rfc1808

    # should not fail but would also fail in OWL API
    # def test_is_absolute_01(self):
    #     iri = IRI('g:h')
    #     self.assertFalse(iri.is_absolute())

    def test_is_absolute_02(self):
        iri = IRI('g')
        self.assertFalse(iri.is_absolute())

    def test_is_absolute_03(self):
        iri = IRI('./g')
        self.assertFalse(iri.is_absolute())

    def test_is_absolute_04(self):
        iri = IRI('g/')
        self.assertFalse(iri.is_absolute())

    def test_is_absolute_05(self):
        iri = IRI('/g')
        self.assertFalse(iri.is_absolute())

    def test_is_absolute_06(self):
        iri = IRI('//g')
        self.assertFalse(iri.is_absolute())

    def test_is_absolute_07(self):
        iri = IRI('?y')
        self.assertFalse(iri.is_absolute())

    def test_is_absolute_08(self):
        iri = IRI('g?y')
        self.assertFalse(iri.is_absolute())

    def test_is_absolute_09(self):
        iri = IRI('g?y/./x')
        self.assertFalse(iri.is_absolute())

    def test_is_absolute_10(self):
        iri = IRI('#s')
        self.assertFalse(iri.is_absolute())

    def test_is_absolute_11(self):
        iri = IRI('g#s')
        self.assertFalse(iri.is_absolute())

    def test_is_absolute_12(self):
        iri = IRI('g#s/./x')
        self.assertFalse(iri.is_absolute())

    def test_is_absolute_13(self):
        iri = IRI('g?y#s')
        self.assertFalse(iri.is_absolute())

    def test_is_absolute_14(self):
        iri = IRI(';x')
        self.assertFalse(iri.is_absolute())

    def test_is_absolute_15(self):
        iri = IRI('g;x')
        self.assertFalse(iri.is_absolute())

    def test_is_absolute_16(self):
        iri = IRI('g;x?y#s')
        self.assertFalse(iri.is_absolute())

    def test_is_absolute_17(self):
        iri = IRI('.')
        self.assertFalse(iri.is_absolute())

    def test_is_absolute_18(self):
        iri = IRI('./')
        self.assertFalse(iri.is_absolute())

    def test_is_absolute_19(self):
        iri = IRI('..')
        self.assertFalse(iri.is_absolute())

    def test_is_absolute_20(self):
        iri = IRI('../')
        self.assertFalse(iri.is_absolute())

    def test_is_absolute_21(self):
        iri = IRI('../g')
        self.assertFalse(iri.is_absolute())

    def test_is_absolute_22(self):
        iri = IRI('../..')
        self.assertFalse(iri.is_absolute())

    def test_is_absolute_23(self):
        iri = IRI('../../')
        self.assertFalse(iri.is_absolute())

    def test_is_absolute_24(self):
        iri = IRI('../../g')
        self.assertFalse(iri.is_absolute())

    def test_is_absolute_25(self):
        iri = IRI('http://example.org/foo#bar')
        self.assertTrue(iri.is_absolute())
    # </is_absolute tests> ----------------------------------------------------

    # <get_scheme tests> ------------------------------------------------------
    def test_get_scheme_01(self):
        iri = IRI('http://example.org/foo#bar')
        self.assertEqual('http', iri.get_scheme())

    def test_get_scheme_02(self):
        iri = IRI('https://example.org/foo#bar')
        self.assertEqual('https', iri.get_scheme())

    def test_get_scheme_03(self):
        iri = IRI('urn:nbn:de')
        self.assertEqual('urn', iri.get_scheme())
    # </get_scheme tests> -----------------------------------------------------

    # <_parse_iri_str tests> --------------------------------------------------
    def test__parse_iri_str_01(self):
        iri_str = 'http://example.org/foo?bar#baz'
        parts = IRI._parse_iri_str(iri_str)

        self.assertEqual('http', parts['scheme'])
        self.assertEqual('//example.org/foo?bar', parts['scheme_specific'])
        self.assertEqual('example.org', parts['auth'])
        self.assertEqual('/foo', parts['path'])
        self.assertEqual('bar', parts['query'])
        self.assertEqual('baz', parts['fragment'])

    def test__parse_iri_str_02(self):
        iri_str = 'http://example.org/foo?bar'
        parts = IRI._parse_iri_str(iri_str)

        self.assertEqual('http', parts['scheme'])
        self.assertEqual('//example.org/foo?bar', parts['scheme_specific'])
        self.assertEqual('example.org', parts['auth'])
        self.assertEqual('/foo', parts['path'])
        self.assertEqual('bar', parts['query'])
        self.assertEqual(None, parts['fragment'])

    def test__parse_iri_str_03(self):
        iri_str = 'http://example.org/foo#baz'
        parts = IRI._parse_iri_str(iri_str)

        self.assertEqual('http', parts['scheme'])
        self.assertEqual('//example.org/foo', parts['scheme_specific'])
        self.assertEqual('example.org', parts['auth'])
        self.assertEqual('/foo', parts['path'])
        self.assertEqual(None, parts['query'])
        self.assertEqual('baz', parts['fragment'])

    def test__parse_iri_str_04(self):
        iri_str = 'http://example.org/foo/bar'
        parts = IRI._parse_iri_str(iri_str)

        self.assertEqual('http', parts['scheme'])
        self.assertEqual('//example.org/foo/bar', parts['scheme_specific'])
        self.assertEqual('example.org', parts['auth'])
        self.assertEqual('/foo/bar', parts['path'])
        self.assertEqual(None, parts['query'])
        self.assertEqual(None, parts['fragment'])

    def test__parse_iri_str_05(self):
        iri_str = 'http://example.org/foo?bar=23&blah=42#baz'
        parts = IRI._parse_iri_str(iri_str)

        self.assertEqual('http', parts['scheme'])
        self.assertEqual('//example.org/foo?bar=23&blah=42',
                         parts['scheme_specific'])
        self.assertEqual('example.org', parts['auth'])
        self.assertEqual('/foo', parts['path'])
        self.assertEqual('bar=23&blah=42', parts['query'])
        self.assertEqual('baz', parts['fragment'])

    def test__parse_iri_str_06(self):
        iri_str = 'http://example.org/foo?bar&blah#baz'
        parts = IRI._parse_iri_str(iri_str)

        self.assertEqual('http', parts['scheme'])
        self.assertEqual('//example.org/foo?bar&blah', parts['scheme_specific'])
        self.assertEqual('example.org', parts['auth'])
        self.assertEqual('/foo', parts['path'])
        self.assertEqual('bar&blah', parts['query'])
        self.assertEqual('baz', parts['fragment'])

    def test__parse_iri_str_07(self):
        iri_str = 'http://userid:password@example.org:8080'
        parts = IRI._parse_iri_str(iri_str)

        self.assertEqual('http', parts['scheme'])
        self.assertEqual('//userid:password@example.org:8080',
                         parts['scheme_specific'])
        self.assertEqual('userid:password@example.org:8080', parts['auth'])
        self.assertEqual('', parts['path'])
        self.assertEqual(None, parts['query'])
        self.assertEqual(None, parts['fragment'])

    def test__parse_iri_str_08(self):
        iri_str = 'http://userid:password@example.org:8080/'
        parts = IRI._parse_iri_str(iri_str)

        self.assertEqual('http', parts['scheme'])
        self.assertEqual('//userid:password@example.org:8080/',
                         parts['scheme_specific'])
        self.assertEqual('userid:password@example.org:8080', parts['auth'])
        self.assertEqual('/', parts['path'])
        self.assertEqual(None, parts['query'])
        self.assertEqual(None, parts['fragment'])

    def test__parse_iri_str_09(self):
        iri_str = 'http://userid@example.org'
        parts = IRI._parse_iri_str(iri_str)

        self.assertEqual('http', parts['scheme'])
        self.assertEqual('//userid@example.org', parts['scheme_specific'])
        self.assertEqual('userid@example.org', parts['auth'])
        self.assertEqual('', parts['path'])
        self.assertEqual(None, parts['query'])
        self.assertEqual(None, parts['fragment'])

    def test__parse_iri_str_10(self):
        iri_str = 'http://userid@example.org/'
        parts = IRI._parse_iri_str(iri_str)

        self.assertEqual('http', parts['scheme'])
        self.assertEqual('//userid@example.org/', parts['scheme_specific'])
        self.assertEqual('userid@example.org', parts['auth'])
        self.assertEqual('/', parts['path'])
        self.assertEqual(None, parts['query'])
        self.assertEqual(None, parts['fragment'])

    def test__parse_iri_str_11(self):
        iri_str = 'http://userid@example.org:8080'
        parts = IRI._parse_iri_str(iri_str)

        self.assertEqual('http', parts['scheme'])
        self.assertEqual('//userid@example.org:8080', parts['scheme_specific'])
        self.assertEqual('userid@example.org:8080', parts['auth'])
        self.assertEqual('', parts['path'])
        self.assertEqual(None, parts['query'])
        self.assertEqual(None, parts['fragment'])

    def test__parse_iri_str_12(self):
        iri_str = 'http://userid@example.org:8080/'
        parts = IRI._parse_iri_str(iri_str)

        self.assertEqual('http', parts['scheme'])
        self.assertEqual('//userid@example.org:8080/', parts['scheme_specific'])
        self.assertEqual('userid@example.org:8080', parts['auth'])
        self.assertEqual('/', parts['path'])
        self.assertEqual(None, parts['query'])
        self.assertEqual(None, parts['fragment'])

    def test__parse_iri_str_13(self):
        iri_str = 'http://userid:password@example.org'
        parts = IRI._parse_iri_str(iri_str)

        self.assertEqual('http', parts['scheme'])
        self.assertEqual('//userid:password@example.org',
                         parts['scheme_specific'])
        self.assertEqual('userid:password@example.org', parts['auth'])
        self.assertEqual('', parts['path'])
        self.assertEqual(None, parts['query'])
        self.assertEqual(None, parts['fragment'])

    def test__parse_iri_str_14(self):
        iri_str = 'http://userid:password@example.org/'
        parts = IRI._parse_iri_str(iri_str)

        self.assertEqual('http', parts['scheme'])
        self.assertEqual('//userid:password@example.org/',
                         parts['scheme_specific'])
        self.assertEqual('userid:password@example.org', parts['auth'])
        self.assertEqual('/', parts['path'])
        self.assertEqual(None, parts['query'])
        self.assertEqual(None, parts['fragment'])

    def test__parse_iri_str_15(self):
        iri_str = 'http://foo.com/blah_(wikipedia)_blah#cite-1'
        parts = IRI._parse_iri_str(iri_str)

        self.assertEqual('http', parts['scheme'])
        self.assertEqual('//foo.com/blah_(wikipedia)_blah',
                         parts['scheme_specific'])
        self.assertEqual('foo.com', parts['auth'])
        self.assertEqual('/blah_(wikipedia)_blah', parts['path'])
        self.assertEqual(None, parts['query'])
        self.assertEqual('cite-1', parts['fragment'])

    def test__parse_iri_str_16(self):
        iri_str = 'http://code.google.com/events/#&product=browser'
        parts = IRI._parse_iri_str(iri_str)

        self.assertEqual('http', parts['scheme'])
        self.assertEqual('//code.google.com/events/', parts['scheme_specific'])
        self.assertEqual('code.google.com', parts['auth'])
        self.assertEqual('/events/', parts['path'])
        self.assertEqual(None, parts['query'])
        self.assertEqual('&product=browser', parts['fragment'])

    def test__parse_iri_str_17(self):
        iri_str = 'http://j.mp'
        parts = IRI._parse_iri_str(iri_str)

        self.assertEqual('http', parts['scheme'])
        self.assertEqual('//j.mp', parts['scheme_specific'])
        self.assertEqual('j.mp', parts['auth'])
        self.assertEqual('', parts['path'])
        self.assertEqual(None, parts['query'])
        self.assertEqual(None, parts['fragment'])

    def test__parse_iri_str_18(self):
        iri_str = 'http://foo.bar/?q=Test%20URL-encoded%20stuff'
        parts = IRI._parse_iri_str(iri_str)

        self.assertEqual('http', parts['scheme'])
        self.assertEqual('//foo.bar/?q=Test%20URL-encoded%20stuff',
                         parts['scheme_specific'])
        self.assertEqual('foo.bar', parts['auth'])
        self.assertEqual('/', parts['path'])
        self.assertEqual('q=Test%20URL-encoded%20stuff', parts['query'])
        self.assertEqual(None, parts['fragment'])

    def test__parse_iri_str_19(self):
        iri_str = 'http://-.~_!$&\'()*+,;=:%40:80%2f::::::@example.com'
        parts = IRI._parse_iri_str(iri_str)

        self.assertEqual('http', parts['scheme'])
        self.assertEqual('//-.~_!$&\'()*+,;=:%40:80%2f::::::@example.com',
                         parts['scheme_specific'])
        self.assertEqual('-.~_!$&\'()*+,;=:%40:80%2f::::::@example.com',
                         parts['auth'])
        self.assertEqual('', parts['path'])
        self.assertEqual(None, parts['query'])
        self.assertEqual(None, parts['fragment'])

    def test__parse_iri_str_20(self):
        iri_str = 'http://1337.net'
        parts = IRI._parse_iri_str(iri_str)

        self.assertEqual('http', parts['scheme'])
        self.assertEqual('//1337.net', parts['scheme_specific'])
        self.assertEqual('1337.net', parts['auth'])
        self.assertEqual('', parts['path'])
        self.assertEqual(None, parts['query'])
        self.assertEqual(None, parts['fragment'])
    # </_parse_iri_str tests> -------------------------------------------------

    # <resolve tests> ---------------------------------------------------------
    # tests taken from
    # https://android.googlesource.com/platform/libcore2/+/master/luni/src/test/java/libcore/java/net/URITest.java
    def test_resolve_01(self):
        base_iri = IRI('http://host/file?query/x')
        s = 'another'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://host/another')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_02(self):
        base_iri = IRI('http://host/file?query/x#fragment')
        s = '#another'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://host/file?query/x#another')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_03(self):
        base_iri = IRI('http://host/file')
        s = 'another#fragment'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://host/another#fragment')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_04(self):
        base_iri = IRI('http://host/a/b/c')
        s = '../d'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://host/a/d')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_05(self):
        base_iri = IRI('http://host/a/b/c')
        s = 'd/e'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://host/a/b/d/e')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_06(self):
        base_iri = IRI('http://host/a/b/c')
        s = '/d'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://host/d')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_07(self):
        base_iri = IRI('http://host/a/b/c')
        s = 'http://host2/d/e'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://host2/d/e')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_08(self):
        base_iri = IRI('http://host/a/b/c')
        s = 'https://host2/d/e'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('https://host2/d/e')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_09(self):
        base_iri = IRI('http://host/a/b/c')
        s = 'https://host2/d/e'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('https://host2/d/e')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_10(self):
        base_iri = IRI('http://host/a/b/c')
        s = '//another/d/e'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://another/d/e')
        self.assertEqual(expctd_iri, res_iri)

    # FIXME: this should raise an error, but IRIs are not validated, yet
    # def test_resolve_11(self):
    #     base_iri = IRI('http://host/a/b/c')
    #     s = 'http:'
    #     res_iri = base_iri.resolve(s)
    #     expctd_iri = IRI('fail')
    #     self.assertEqual(expctd_iri, res_iri)

    def test_resolve_12(self):
        base_iri = IRI('http://host/a/b/c')
        s = 'http:/'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http:/')
        self.assertEqual(expctd_iri, res_iri)

    # FIXME: this should raise an error, but IRIs are not validated, yet
    # def test_resolve_13(self):
    #     base_iri = IRI('http://host/a/b/c"')
    #     s = 'http://'
    #     res_iri = base_iri.resolve(s)
    #     expctd_iri = IRI('fail')
    #     self.assertEqual(expctd_iri, res_iri)

    # FIXME: this should raise an error, but IRIs are not validated, yet
    # def test_resolve_14(self):
    #     base_iri = IRI('http://host/a/b/c')
    #     s = '//'
    #     res_iri = base_iri.resolve(s)
    #     expctd_iri = IRI('fail')
    #     self.assertEqual(expctd_iri, res_iri)

    # FIXME: this should raise an error, but IRIs are not validated, yet
    # def test_resolve_15(self):
    #     base_iri = IRI('http://host/a/b/c')
    #     s = 'https:'
    #     res_iri = base_iri.resolve(s)
    #     expctd_iri = IRI('fail')
    #     self.assertEqual(expctd_iri, res_iri)

    def test_resolve_16(self):
        base_iri = IRI('http://host/a/b/c')
        s = 'https:/'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('https:/')
        self.assertEqual(expctd_iri, res_iri)

    # FIXME: this should raise an error, but IRIs are not validated, yet
    # def test_resolve_17(self):
    #     base_iri = IRI('http://host/a/b/c')
    #     s = 'https://'
    #     res_iri = base_iri.resolve(s)
    #     expctd_iri = IRI('fail')
    #     self.assertEqual(expctd_iri, res_iri)

    def test_resolve_18(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = 'https:h'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('https:h')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_19(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = 'g'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/c/g')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_20(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = './g'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/c/g')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_21(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = 'g/'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/c/g/')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_22(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = '/g'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/g')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_23(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = '//g'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://g')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_24(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = '?y'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/c/d;p?y')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_25(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = 'g?y'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/c/g?y')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_26(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = '#s'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/c/d;p?q#s')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_27(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = 'g#s'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/c/g#s')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_28(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = 'g?y#s'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/c/g?y#s')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_29(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = ';x'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/c/;x')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_30(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = 'g;x'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/c/g;x')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_31(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = 'g;x?y#s'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/c/g;x?y#s')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_32(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = ''
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/c/d;p?q')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_33(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = '.'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/c/')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_34(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = './'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/c/')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_35(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = '..'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_36(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = '../'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_37(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = '../g'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/g')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_38(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = '../..'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_39(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = '../../'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_40(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = '../../g'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/g')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_41(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = '../../../g'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/g')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_42(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = '../../../../g'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/g')
        self.assertEqual(expctd_iri, res_iri)

    # FIXME: fails since path normalization isn't implemented, yet
    # def test_resolve_43(self):
    #     base_iri = IRI('http://a/b/c/d;p?q')
    #     s = '/./g'
    #     res_iri = base_iri.resolve(s)
    #     expctd_iri = IRI('http://a/g')
    #     self.assertEqual(expctd_iri, res_iri)

    # FIXME: fails since path normalization isn't implemented, yet
    # def test_resolve_44(self):
    #     base_iri = IRI('http://a/b/c/d;p?q')
    #     s = '/../g'
    #     res_iri = base_iri.resolve(s)
    #     expctd_iri = IRI('http://a/g')
    #     self.assertEqual(expctd_iri, res_iri)

    def test_resolve_45(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = 'g.'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/c/g.')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_46(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = '.g'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/c/.g')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_47(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = 'g..'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/c/g..')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_48(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = '..g'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/c/..g')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_49(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = './../g'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/g')
        self.assertEqual(expctd_iri, res_iri)

    # FIXME: fails since path normalization isn't implemented, yet
    # def test_resolve_50(self):
    #     base_iri = IRI('http://a/b/c/d;p?q')
    #     s = './g/.'
    #     res_iri = base_iri.resolve(s)
    #     expctd_iri = IRI('http://a/b/c/g/')
    #     self.assertEqual(expctd_iri, res_iri)

    # FIXME: fails since path normalization isn't implemented, yet
    # def test_resolve_51(self):
    #     base_iri = IRI('http://a/b/c/d;p?q')
    #     s = 'g/./h'
    #     res_iri = base_iri.resolve(s)
    #     expctd_iri = IRI('http://a/b/c/g/h')
    #     self.assertEqual(expctd_iri, res_iri)

    # FIXME: fails since path normalization isn't implemented, yet
    # def test_resolve_52(self):
    #     base_iri = IRI('http://a/b/c/d;p?q')
    #     s = 'g/../h'
    #     res_iri = base_iri.resolve(s)
    #     expctd_iri = IRI('http://a/b/c/h')
    #     self.assertEqual(expctd_iri, res_iri)

    # FIXME: fails since path normalization isn't implemented, yet
    # def test_resolve_53(self):
    #     base_iri = IRI('http://a/b/c/d;p?q')
    #     s = 'g;x=1/./y'
    #     res_iri = base_iri.resolve(s)
    #     expctd_iri = IRI('http://a/b/c/g;x=1/y')
    #     self.assertEqual(expctd_iri, res_iri)

    def test_resolve_54(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = 'http:g'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http:g')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_55(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = 'g?y/./x'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/c/g?y/./x')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_56(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = 'g?y/../x'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/c/g?y/../x')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_57(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = 'g#s/./x'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/c/g#s/./x')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_58(self):
        base_iri = IRI('http://a/b/c/d;p?q')
        s = 'g#s/../x'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://a/b/c/g#s/../x')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_59(self):
        base_iri = IRI('file://a/b/c')
        s = 'd'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('file://a/b/d')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_60(self):
        base_iri = IRI('http://android.com/')
        s = 'http://android.com/'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://android.com/')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_61(self):
        base_iri = IRI('http://android.com/')
        s = 'robots.txt'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://android.com/robots.txt')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_62(self):
        base_iri = IRI('robots.txt')
        s = 'http://android.com/'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('http://android.com/')
        self.assertEqual(expctd_iri, res_iri)

    def test_resolve_63(self):
        base_iri = IRI('robots.txt')
        s = 'robots.txt'
        res_iri = base_iri.resolve(s)
        expctd_iri = IRI('robots.txt')
        self.assertEqual(expctd_iri, res_iri)
    # </resolve tests> --------------------------------------------------------

    # <is_reserved_vocabulary tests> ------------------------------------------
    def test_is_reserved_vocabulary_01(self):
        iri = IRI('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')
        self.assertTrue(iri.is_reserved_vocabulary())

    def test_is_reserved_vocabulary_02(self):
        iri = IRI('http://www.w3.org/2000/01/rdf-schema#subClassOf')
        self.assertTrue(iri.is_reserved_vocabulary())

    def test_is_reserved_vocabulary_03(self):
        iri = IRI('http://www.w3.org/2002/07/owl#Class')
        self.assertTrue(iri.is_reserved_vocabulary())

    def test_is_reserved_vocabulary_04(self):
        iri = IRI('http://www.w3.org/2001/XMLSchema#int')
        self.assertTrue(iri.is_reserved_vocabulary())

    def test_is_reserved_vocabulary_05(self):
        iri = IRI('http://example.org/foo#bar')
        self.assertFalse(iri.is_reserved_vocabulary())
    # </is_reserved_vocabulary tests> -----------------------------------------

    # <is_thing tests> --------------------------------------------------------
    def test_is_thing_01(self):
        iri = IRI('http://example.org/foo#bar')
        self.assertFalse(iri.is_thing())

    def test_is_thing_02(self):
        iri = IRI('http://www.w3.org/2002/07/owl#', 'SthElse')
        self.assertFalse(iri.is_thing())

    def test_is_thing_03(self):
        iri = IRI('http://www.w3.org/2002/07/owl#Thing')
        self.assertTrue(iri.is_thing())

    def test_is_thing_04(self):
        iri = IRI('http://www.w3.org/2002/07/owl#', 'Thing')
        self.assertTrue(iri.is_thing())

    def test_is_thing_05(self):
        uri = rdflib.URIRef('http://www.w3.org/2002/07/owl#Thing')
        iri = IRI(uri)
        self.assertTrue(iri.is_thing())
    # </is_thing tests> -------------------------------------------------------

    # <is_nothing tests> ------------------------------------------------------
    def test_is_nothing_01(self):
        iri = IRI('http://example.org/foo#bar')
        self.assertFalse(iri.is_nothing())

    def test_is_nothing_02(self):
        iri = IRI('http://www.w3.org/2002/07/owl#', 'SthElse')
        self.assertFalse(iri.is_nothing())

    def test_is_nothing_03(self):
        iri = IRI('http://www.w3.org/2002/07/owl#Nothing')
        self.assertTrue(iri.is_nothing())

    def test_is_nothing_04(self):
        iri = IRI('http://www.w3.org/2002/07/owl#', 'Nothing')
        self.assertTrue(iri.is_nothing())

    def test_is_nothing_05(self):
        uri = rdflib.URIRef('http://www.w3.org/2002/07/owl#Nothing')
        iri = IRI(uri)
        self.assertTrue(iri.is_nothing())
    # </is_nothing tests> -----------------------------------------------------

    # <is_plain_literal tests> ------------------------------------------------
    def test_is_plain_literal_01(self):
        iri = IRI('http://example.org/foo#bar')
        self.assertFalse(iri.is_plain_literal())

    def test_is_plain_literal_02(self):
        iri = IRI('http://www.w3.org/1999/02/22-rdf-syntax-ns#', 'SthElse')
        self.assertFalse(iri.is_plain_literal())

    def test_is_plain_literal_03(self):
        iri = IRI('http://www.w3.org/1999/02/22-rdf-syntax-ns#', 'PlainLiteral')
        self.assertTrue(iri.is_plain_literal())

    def test_is_plain_literal_04(self):
        iri = IRI('http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral')
        self.assertTrue(iri.is_plain_literal())

    def test_is_plain_literal_05(self):
        uri = rdflib.URIRef(
            'http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral')
        iri = IRI(uri)
        self.assertTrue(iri.is_plain_literal())
    # </is_plain_literal tests> -----------------------------------------------

    # <to_quoted_string tests> ------------------------------------------------
    def test_to_quoted_string(self):
        iri_str = 'http://example.org/foo#bar'
        iri = IRI(iri_str)
        self.assertEqual('<%s>' % iri_str, iri.to_quoted_string())
    # </to_quoted_string tests> -----------------------------------------------

    # <create tests> ----------------------------------------------------------
    def test_create_01(self):
        prefix = 'http://example.org/foo#'
        suffix = 'bar'
        iri = IRI.create(prefix, suffix)
        self.assertEqual(prefix, iri.prefix)
        self.assertEqual(suffix, iri.remainder)

    def test_create_02(self):
        iri_str = 'http://example.org/foo#bar'
        iri = IRI.create(iri_str)
        self.assertEqual(iri_str, str(iri))

    def test_create_03(self):
        with tempfile.TemporaryDirectory() as directory:
            file_name = 'deleteme.txt'
            file_path = os.path.join(directory, file_name)
            file = open(file_path, 'w')

            iri = IRI.create(file)
            self.assertEqual('file://%s' % file_path, str(iri))

    def test_create_04(self):
        with tempfile.TemporaryDirectory() as directory:
            file_name = 'deleteme.txt'
            file_path = os.path.join(directory, file_name)
            file = open(file_path, 'w')

            iri = IRI.create(file, 'should/be/ignored')
            self.assertEqual('file://%s' % file_path, str(iri))

    def test_create_05(self):
        with tempfile.TemporaryDirectory() as directory:
            file_name = 'delete me.txt'
            file_path = os.path.join(directory, file_name)
            file = open(file_path, 'w')

            quoted_file_name = 'delete+me.txt'
            file_iri = 'file://' + directory + os.path.sep + quoted_file_name
            iri = IRI.create(file)
            self.assertEqual(file_iri, str(iri))

    def test_create_06(self):
        with tempfile.TemporaryDirectory() as directory:
            file_name = 'delete me.txt'
            file_path = os.path.join(directory, file_name)
            file = open(file_path, 'w')

            quoted_file_name = 'delete+me.txt'
            file_iri = 'file://' + directory + os.path.sep + quoted_file_name
            iri = IRI.create(file, 'should/be/ignored')
            self.assertEqual(file_iri, str(iri))

    def test_create_07(self):
        iri_str = 'http://example.org/foo#bar'
        uri = rdflib.URIRef(iri_str)
        iri = IRI.create(uri)
        self.assertEqual(iri_str, str(iri))

    def test_create_08(self):
        iri_str = 'http://example.org/foo#bar'
        uri = rdflib.URIRef(iri_str)
        iri = IRI.create(uri, 'should/be/ignored')
        self.assertEqual(iri_str, str(iri))
    # </create tests> ---------------------------------------------------------

    # <generate_document_iri tests> -------------------------------------------
    def test_generate_document_iri(self):
        ont_iri = IRI.generate_document_iri()
        self.assertTrue(isinstance(ont_iri, IRI))
        self.assertTrue(str(ont_iri).startswith('owlapi:ontology'))
    # </generate_document_iri tests> ------------------------------------------

    # <prefixed_by tests> -----------------------------------------------------
    # prefix is None
    def test_prefixed_by_01(self):
        prefix = None
        iri = IRI('http://example.org/foo#', 'bar')
        try:
            prefixed_iri = iri.prefixed_by(prefix)
            self.fail('prefixing with None should raise an error')
        except IRIException as e:
            pass

    # remainder is None
    def test_prefixed_by_02(self):
        prefix = 'http://example.com/foo#'
        iri = IRI('http://example.org/bar#')
        prefixed_iri = iri.prefixed_by(prefix)
        self.assertEqual(prefix, prefixed_iri)

    # prefix and remainder are not None
    def test_prefixed_by_03(self):
        prefix = 'http://example.com/foo#'
        iri = IRI('http://example.org/foo#bar')
        prefixed_iri = iri.prefixed_by(prefix)
        self.assertEqual('http://example.com/foo#bar', str(prefixed_iri))
    # </prefixed_by tests> ----------------------------------------------------

    # <get_short_form tests> --------------------------------------------------
    def test_get_short_form_01(self):
        iri = IRI('http://example.org/foo#', 'bar')
        self.assertEqual('bar', iri.get_short_form())

    def test_get_short_form_02(self):
        iri = IRI('http://example.org/')
        self.assertEqual(iri.to_quoted_string(), iri.get_short_form())

    def test_get_short_form_03(self):
        iri = IRI('http://example.org/foo/bar#')
        self.assertEqual('bar#', iri.get_short_form())
    # </get_short_form tests> -------------------------------------------------

    # <accept tests> ----------------------------------------------------------
    def test_accept_01(self):
        class TestVisitor1(OWLVisitorEx):
            def visit(self, iri):
                return 'TEST'

        iri = IRI('http://example.org/foo#bar')
        visitor = TestVisitor1()
        self.assertEqual('TEST', iri.accept(visitor))

    def test_accept_02(self):
        class TestPrefixVisitor(OWLVisitorEx):
            def visit(self, iri):
                return iri.prefix

        visitor = TestPrefixVisitor()
        prefix = 'http://example.org/foo/bar#'
        suffix = 'baz'
        iri = IRI(prefix, suffix)
        self.assertEqual(prefix, iri.accept(visitor))
    # </accept tests> ---------------------------------------------------------

    # <get_classes_in_signature tests> ----------------------------------------
    def test_get_classes_in_signature(self):
        iri = IRI('http://example.org/foo#bar')
        self.assertEqual([], iri.get_classes_in_signature())
    # </get_classes_in_signature tests> ---------------------------------------

    # <get_data_properties_in_signature tests> --------------------------------
    def test_get_data_properties_in_signature(self):
        iri = IRI('http://example.org/foo#bar')
        self.assertEqual([], iri.get_data_properties_in_signature())
    # </get_data_properties_in_signature tests> -------------------------------

    # <get_individuals_in_signature tests> ------------------------------------
    def test_get_individuals_in_signature(self):
        iri = IRI('http://example.org/foo#bar')
        self.assertEqual([], iri.get_individuals_in_signature())
    # </get_individuals_in_signature tests> -----------------------------------

    # <get_object_properties_in_signature tests> ------------------------------
    def test_get_object_properties_in_signature(self):
        iri = IRI('http://example.org/foo#bar')
        self.assertEqual([], iri.get_object_properties_in_signature())
    # </get_object_properties_in_signature tests> -----------------------------

    # <get_signature tests> ---------------------------------------------------
    def test_get_signature(self):
        iri = IRI('http://example.org/foo#bar')
        self.assertEqual([], iri.get_signature())
    # </get_signature tests> --------------------------------------------------

    # <contains_entity_in_signature tests> ------------------------------------
    def test_contains_entity_in_signature(self):
        iri1 = IRI('http://example.org/foo#bar')
        iri2 = IRI('http://example.org/foo#baz')
        # should return False no matter what iri2 looks like
        self.assertFalse(iri1.contains_entity_in_signature(iri2))
    # </contains_entity_in_signature tests> -----------------------------------

    # <get_anonymous_individuals tests> ---------------------------------------
    def test_get_anonymous_individuals(self):
        iri = IRI('http://example.org/foo#bar')
        self.assertEqual([], iri.get_anonymous_individuals())
    # </get_anonymous_individuals tests> --------------------------------------

    # <get_datatypes_in_signature tests> --------------------------------------
    def test_get_datatypes_in_signature(self):
        iri = IRI('http://example.org/foo#bar')
        self.assertEqual([], iri.get_datatypes_in_signature())
    # </get_datatypes_in_signature tests> -------------------------------------

    # <get_nested_class_expressions tests> ------------------------------------
    def test_get_nested_class_expressions(self):
        iri = IRI('http://example.org/foo#bar')
        self.assertEqual([], iri.get_nested_class_expressions())
    # </get_nested_class_expressions tests> -----------------------------------

    # <is_top_entity tests> ---------------------------------------------------
    def test_is_top_entity(self):
        iri = IRI('http://example.org/foo#bar')
        self.assertFalse(iri.is_top_entity())
    # </is_top_entity tests> --------------------------------------------------

    # <is_bottom_entity tests> ------------------------------------------------
    def test_is_bottom_entity(self):
        iri = IRI('http://example.org/foo#bar')
        self.assertFalse(iri.is_bottom_entity())
    # </is_bottom_entity tests> -----------------------------------------------

    # <compare_to tests> ------------------------------------------------------
    def test_compare_to_01(self):
        """same object --> 0"""
        iri = IRI('http://ex.org/sth')
        self.assertEqual(0, iri.compare_to(iri))

    def test_compare_to_02(self):
        """IRI vs. arbitrary object --> -1"""
        iri = IRI('http://ex.org/sth')
        self.assertEqual(-1, iri.compare_to(23))

    def test_compare_to_03(self):
        """IRI vs. IRI (differing prefix lengths) --> -4"""
        iri1 = IRI('http://ex.org/sth')  # len(iri1.prefix) == 14
        iri2 = IRI('http://ex.org/foo/sth')  # len(iri2.prefix) == 18
        self.assertEqual(-4, iri1.compare_to(iri2))  # == 14 - 18

    def test_compare_to_04(self):
        """IRI vs. IRI (differing prefix lengths) --> 4"""
        iri1 = IRI('http://ex.org/foo/sth')  # len(iri1.prefix) == 18
        iri2 = IRI('http://ex.org/sth')  # len(iri2.prefix) == 14
        self.assertEqual(4, iri1.compare_to(iri2))  # == 18 - 14

    def test_compare_to_05(self):
        """IRI vs. IRI (differing chars in prefix) --> -25"""
        iri1 = IRI('http://ex.org/a/sth')  # ord('a') == 97
        iri2 = IRI('http://ex.org/z/sth')  # ord('z') == 122
        self.assertEqual(-25, iri1.compare_to(iri2))  # == 97 - 122

    def test_compare_to_06(self):
        """IRI vs. IRI (differing chars in prefix) --> 25"""
        iri1 = IRI('http://ex.org/z/sth')  # ord('z') == 122
        iri2 = IRI('http://ex.org/a/sth')  # ord('a') == 97
        self.assertEqual(25, iri1.compare_to(iri2))  # == 122 - 97

    def test_compare_to_07(self):
        """IRI vs. IRI (same prefixes; remainder w/ differing lengths) --> -4"""
        iri1 = IRI('http://ex.org/sth')  # len(iri1.remainder) == 3
        iri2 = IRI('http://ex.org/sthElse')  # len(iri2.remainder) == 7
        self.assertEqual(-4, iri1.compare_to(iri2))  # == 3 - 7

    def test_compare_to_08(self):
        """IRI vs. IRI (same prefixes; remainder w/ differing lengths) --> 4"""
        iri1 = IRI('http://ex.org/sthElse')  # len(iri1.remainder) == 7
        iri2 = IRI('http://ex.org/sth')  # len(iri1.remainder) == 3
        self.assertEqual(4, iri1.compare_to(iri2))  # == 7 - 3

    def test_compare_to_09(self):
        """IRI vs. IRI (same prefixes; differing chars in remainder) --> -25"""
        iri1 = IRI('http://ex.org/stha')  # ord('a') == 97
        iri2 = IRI('http://ex.org/sthz')  # ord('z') == 122
        self.assertEqual(-25, iri1.compare_to(iri2))  # == 97 - 122

    def test_compare_to_10(self):
        """IRI vs. IRI (same prefixes; differing chars in remainder) --> 25"""
        iri1 = IRI('http://ex.org/sthz')  # ord('z') == 122
        iri2 = IRI('http://ex.org/stha')  # ord('a') == 97
        self.assertEqual(25, iri1.compare_to(iri2))  # == 122 - 97

    def test_compare_to_11(self):
        """IRI vs. IRI (same prefixes; one remainder None) --> 4"""
        iri1 = IRI('http://ex.org/')  # remainder is None
        iri2 = IRI('http://ex.org/sth')
        self.assertEqual(-3, iri1.compare_to(iri2))

    def test_compare_to_12(self):
        """IRI vs. IRI (same prefixes; one remainder None) --> 4"""
        iri1 = IRI('http://ex.org/sth')
        iri2 = IRI('http://ex.org/')  # remainder is None
        self.assertEqual(3, iri1.compare_to(iri2))

    def test_compare_to_13(self):
        """IRI vs. IRI (same prefixes; both remainders None) --> 0"""
        iri1 = IRI('http://ex.org/')
        iri2 = IRI('http://ex.org/')
        self.assertEqual(0, iri1.compare_to(iri2))
    # </compare_to tests> -----------------------------------------------------