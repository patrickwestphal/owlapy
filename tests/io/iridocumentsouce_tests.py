import unittest

from owlapy.io import IRIDocumentSource
from owlapy.io import OWLOntologyInputSourceException
from owlapy.model import IRI


class TestIRIDocumentSource(unittest.TestCase):

    def test___init__(self):
        doc_iri = IRI('http://example.com/docXYZ')
        doc_source = IRIDocumentSource(doc_iri)

        self.assertEqual(doc_iri, doc_source.document_iri)

    def test___str__(self):
        doc_iri = IRI('http://example.com/docXYZ')
        doc_source = IRIDocumentSource(doc_iri)

        self.assertEqual(str(doc_iri), str(doc_source))

    def test___repr__(self):
        doc_iri = IRI('http://example.com/docXYZ')
        doc_source = IRIDocumentSource(doc_iri)

        self.assertEqual(str(doc_iri), doc_source.__repr__())

    def test_get_document_iri(self):
        doc_iri = IRI('http://example.com/docXYZ')
        doc_source = IRIDocumentSource(doc_iri)

        self.assertEqual(doc_iri, doc_source.get_document_iri())

    def test_is_input_stream_available(self):
        doc_iri = IRI('http://example.com/docXYZ')
        doc_source = IRIDocumentSource(doc_iri)
        self.assertFalse(doc_source.is_input_stream_available())

    def test_get_input_stream(self):
        doc_iri = IRI('http://example.com/docXYZ')
        doc_source = IRIDocumentSource(doc_iri)

        self.assertRaises(OWLOntologyInputSourceException,
                          doc_source.get_input_stream)

    def test_is_reader_available(self):
        doc_iri = IRI('http://example.com/docXYZ')
        doc_source = IRIDocumentSource(doc_iri)

        self.assertFalse(doc_source.is_reader_available())

    def test_get_reader(self):
        doc_iri = IRI('http://example.com/docXYZ')
        doc_source = IRIDocumentSource(doc_iri)

        self.assertRaises(OWLOntologyInputSourceException,
                          doc_source.get_reader)
