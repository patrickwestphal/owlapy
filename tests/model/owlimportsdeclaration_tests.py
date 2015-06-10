import unittest

from rdflib import URIRef

from owlapy.model import IRI
from owlapy.model import OWLImportsDeclaration
from owlapy.model import OWLObjectProperty


class TestOWLImportsDeclaration(unittest.TestCase):

    def test___init__(self):
        iri = IRI('http://ex.org/someOnt')
        oid = OWLImportsDeclaration(iri)
        self.assertEqual(iri, oid.iri)

    def test___ge__01(self):
        """equal"""
        iri1 = IRI('http://ex.org/someOnt')
        oid1 = OWLImportsDeclaration(iri1)

        iri2 = IRI('http://ex.org/someOnt')
        oid2 = OWLImportsDeclaration(iri2)
        self.assertTrue(oid1 >= oid2)
        self.assertFalse(oid1 < oid2)

    def test___ge__02(self):
        """greater"""
        iri1 = IRI('http://ex.org/zzzSomeOnt')
        oid1 = OWLImportsDeclaration(iri1)

        iri2 = IRI('http://ex.org/someOnt')
        oid2 = OWLImportsDeclaration(iri2)
        self.assertTrue(oid1 > oid2)
        self.assertFalse(oid1 <= oid2)

    def test___ge__03(self):
        """less"""
        iri1 = IRI('http://ex.org/someOnt')
        oid1 = OWLImportsDeclaration(iri1)

        iri2 = IRI('http://ex.org/zzzSomeOnt')
        oid2 = OWLImportsDeclaration(iri2)
        self.assertTrue(oid1 < oid2)
        self.assertFalse(oid1 >= oid2)

    def test___eq__01(self):
        """same object"""
        iri1 = IRI('http://ex.org/someOnt')
        oid1 = OWLImportsDeclaration(iri1)

        self.assertTrue(oid1 == oid1)

    def test___eq__02(self):
        """same IRI"""
        iri1 = IRI('http://ex.org/someOnt')
        oid1 = OWLImportsDeclaration(iri1)
        oid2 = OWLImportsDeclaration(iri1)

        self.assertTrue(oid1 == oid2)

    def test___eq__03(self):
        """same IRI; different class"""
        iri1 = IRI('http://ex.org/foo')
        oid1 = OWLImportsDeclaration(iri1)
        oid2 = OWLObjectProperty(iri1)

        self.assertFalse(oid1 == oid2)

    def test___eq__04(self):
        """completely different object"""
        iri1 = IRI('http://ex.org/someOnt')
        oid1 = OWLImportsDeclaration(iri1)

        self.assertFalse(oid1 == 23)

    def test___hash___(self):
        iri1 = IRI('http://ex.org/someOnt')
        oid1 = OWLImportsDeclaration(iri1)

        self.assertEqual(hash(iri1), hash(oid1))

    def test___str___(self):
        iri1 = IRI('http://ex.org/someOnt')
        oid1 = OWLImportsDeclaration(iri1)

        self.assertEqual('Import(%s)' % iri1.to_quoted_string(), str(oid1))

    def test___repr__(self):
        iri1 = IRI('http://ex.org/someOnt')
        oid1 = OWLImportsDeclaration(iri1)

        self.assertEqual(str(oid1), oid1.__repr__())

    def test_get_uri(self):
        uri = URIRef('http://ex.org/foo')
        iri = IRI(uri)
        oid = OWLImportsDeclaration(iri)

        self.assertEqual(uri, oid.get_uri())

    def test_compare_to_01(self):
        """same"""
        iri1 = IRI('http://ex.org/someOnt')
        oid1 = OWLImportsDeclaration(iri1)

        iri2 = IRI('http://ex.org/someOnt')
        oid2 = OWLImportsDeclaration(iri2)

        self.assertEqual(0, oid1.compare_to(oid2))
        self.assertEqual(0, oid2.compare_to(oid1))

    def test_compare_to_02(self):
        """positive"""
        iri1 = IRI('http://ex.org/someOntABC')
        oid1 = OWLImportsDeclaration(iri1)

        iri2 = IRI('http://ex.org/someOnt')
        oid2 = OWLImportsDeclaration(iri2)

        self.assertTrue(oid1.compare_to(oid2) > 0)

    def test_compare_to_03(self):
        """negative"""
        iri1 = IRI('http://ex.org/someOnt')
        oid1 = OWLImportsDeclaration(iri1)

        iri2 = IRI('http://ex.org/someOntABC')
        oid2 = OWLImportsDeclaration(iri2)

        self.assertTrue(oid1.compare_to(oid2) < 0)
