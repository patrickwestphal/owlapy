import os
import unittest

from owlapy.io import FileDocumentSource
from owlapy.model import IRI


dummy_file_name = os.path.sep.join(['foo', 'bar'])


class FileDummy(object):
    def __init__(self):
        self.name = dummy_file_name

    def read(self):
        return 'content'

    def close(self):
        pass


class TestFileDocumentSource(unittest.TestCase):

    def test___init__(self):
        file_dummy = FileDummy()
        doc_souce = FileDocumentSource(file_dummy)

        self.assertEqual(file_dummy, doc_souce.file)

    def test_get_document_iri(self):
        file_dummy = FileDummy()
        file_dummy_iri = IRI.create(file_dummy)
        doc_source = FileDocumentSource(file_dummy)

        self.assertEqual(file_dummy_iri, doc_source.get_document_iri())

    def test_is_input_stream_available(self):
        file_dummy = FileDummy()
        doc_souce = FileDocumentSource(file_dummy)

        self.assertTrue(doc_souce.is_input_stream_available())

    def test_get_input_stream(self):
        file_dummy = FileDummy()
        doc_source = FileDocumentSource(file_dummy)

        self.assertEqual(file_dummy, doc_source.get_input_stream())

    def test_is_reader_available(self):
        file_dummy = FileDummy()
        doc_souce = FileDocumentSource(file_dummy)

        self.assertTrue(doc_souce.is_reader_available())

    def test_get_reader(self):
        file_dummy = FileDummy()
        doc_source = FileDocumentSource(file_dummy)

        self.assertEqual(file_dummy, doc_source.get_reader())
